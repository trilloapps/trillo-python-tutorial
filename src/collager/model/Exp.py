import json
from typing import List, Dict, Union
from collections import OrderedDict
from os.path import join
from enum import Enum


class Include(Enum):
    NON_EMPTY = "NON_EMPTY"


class Exp:
    def __init__(self):
        self.marker = ""
        self.op = ""
        self.lhs = ""
        self.rhs = None
        self.subExps = []

    def getMarker(self):
        return self.marker

    def setMarker(self, marker):
        self.marker = marker

    def getOp(self):
        return self.op

    def setOp(self, op):
        self.op = op

    def getLhs(self):
        return self.lhs

    def setLhs(self, lhs):
        self.lhs = lhs

    def getRhs(self):
        return self.rhs

    def setRhs(self, rhs):
        self.rhs = rhs

    def getSubExps(self):
        return self.subExps

    def setSubExps(self, subExps):
        self.subExps = subExps

    def validate(self):
        return Exp.validate(self)

    @staticmethod
    def validate(exp):
        r = None
        op = exp.op.lower().strip() if exp.op else ""
        if not op:
            return Result.getSuccessResult()

        subExps = exp.subExps
        switch = {
            "or": lambda: [r for e in subExps if (r := e.validate()).isFailed()] or
                          Result.getFailedResult(f"2 or more expressions required, op: \"{exp.op}\" and marker: {exp.marker}"),
            "and": lambda: [r for e in subExps if (r := e.validate()).isFailed()] or
                           Result.getFailedResult(f"2 or more expressions required, op: \"{exp.op}\" and marker: {exp.marker}"),
            "not": lambda: subExps[0].validate() if (1 == len(subExps)) else
                           Result.getFailedResult(f"Exactly 1 subExps needed, op: \"{exp.op}\" and marker: {exp.marker}"),
            "": lambda: Result.getFailedResult(f"Invalid expression, op: \"{exp.op}\" and marker: {exp.marker}"),
        }

        if op not in switch:
            switch[op] = lambda: [r for e in subExps if (r := e.validate()).isFailed()] or (
                    Result.getFailedResult(f"Invalid expression, op: \"{exp.op}\" and marker: {exp.marker}"))

        return switch[op]()

    def retrieveParameterizedQueryAndValues(self):
        m = OrderedDict()
        values = []
        names = []

        sql = self.parameterizedQueryAndValues(names, values)

        m["names"] = names
        m["values"] = values
        m["sql"] = sql

        return m

    def parameterizedQueryAndValues(self, names, values):
        sql = ""
        if not self.op:
            return sql
        if not self.subExps:
            names.append(self.lhs)
            values.append(self.rhs)
            sql = f"{self.lhs} {self.op} ?"
        else:
            s = ""
            if "not" == self.op.lower():
                s = self.subExps[0].parameterizedQueryAndValues(names, values)
                sql = f"not ({s})"
            else:
                for e in self.subExps:
                    s = f"({e.parameterizedQueryAndValues(names, values)})"
                    if not sql:
                        sql = s
                    else:
                        sql += f" {self.op} {s}"
        return sql

    @staticmethod
    def op(op, lhs, rhs):
        exp = Exp()
        exp.op = op
        exp.lhs = lhs
        exp.rhs = rhs
        return exp

    @staticmethod
    def and_(*subExpsArr):
        exp = Exp()
        exp.op = "and"
        if subExpsArr:
            exp.subExps = list(subExpsArr)
        return exp

    @staticmethod
    def or_(*subExpsArr):
        exp = Exp()
        exp.op = "or"
        if subExpsArr:
            exp.subExps = list(subExpsArr)
        return exp

    @staticmethod
    def not_(subExp):
        exp = Exp()
        exp.op = "not"
        if subExp:
            exp.subExps.append(subExp)
        return exp

    def add(self, *subExpsArr):
        if subExpsArr:
            self.subExps += list(subExpsArr)
        return self


class Result:
    def __init__(self, failed=False, message=""):
        self.failed = failed
        self.message = message

    def isFailed(self):
        return self.failed

    def getMessage(self):
        return self.message

    @staticmethod
    def getSuccessResult():
        return Result(failed=False)

    @staticmethod
    def getFailedResult(message):
        return Result(failed=True, message=message)


class Util:
    @staticmethod
    def fromJSONSFile(f, type_ref):
        with open(f, "r") as file:
            return json.load(file, object_pairs_hook=OrderedDict)



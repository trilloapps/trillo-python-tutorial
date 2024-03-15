from src.collager.op.Command import Command
from src.collager.util.LogPy import Log


class DbOp:
    DEFAULT_QUEUE_SIZE = 1000

    def __init__(self, opName, opManager, params):
        queueSize = params.get("queueSize", self.DEFAULT_QUEUE_SIZE)
        self.setup(opName, opManager, queueSize)

    def start(self):
        Log.info("Starting: " + self.opName)
        self.startRunning()

    def doCommand(self, command):
        command_type = command.type
        if command_type == "save":
            self.doSave(command)
        elif command_type == "saveMany":
            self.doSaveMany(command)
        elif command_type == "saveMapList":
            self.doSaveMapList(command)
        elif command_type == "saveManyIgnoreError":
            self.doSaveManyIgnoreError(command)
        elif command_type == "stop":
            self.doStop(command)
        elif command_type == "close":
            self.doClose()
        else:
            Log.error("Invalid command: " + command.type)

    def doSave(self, command):
        pass

    def doSaveMany(self, command):
        pass

    def doSaveMapList(self, command):
        pass

    def doSaveManyIgnoreError(self, command):
        pass

    def doClose(self):
        pass

    def doStop(self, command):
        self.doClose()

    def save(self, className, entity):
        c = self.SaveCommand(className, entity)
        self.queue(c)

    def saveMany(self, className, entities):
        c = self.SaveManyCommand(className, entities)
        self.queue(c)

    def saveMapList(self, className, list):
        c = self.SaveMapListCommand(className, list)
        self.queue(c)

    def saveManyIgnoreError(self, className, entities):
        c = self.SaveManyIgnoreErrorCommand(className, entities)
        self.queue(c)

    def close(self):
        c = self.CloseCommand()
        self.queue(c)

    def stop(self, deleteOnStop):
        c = self.StopCommand(deleteOnStop)
        self.queue(c)

    def completeOp(self):
        self.close()
        self.stop(False)

    class SaveCommand(Command):
        def __init__(self, className, entity):
            super().__init__("save")
            self.className = className
            self.entity = entity

    class SaveManyCommand(Command):
        def __init__(self, className, entities):
            super().__init__("saveMany")
            self.className = className
            self.entities = entities

    class SaveMapListCommand(Command):
        def __init__(self, className, list):
            super().__init__("saveMapList")
            self.className = className
            self.list = list

    class SaveManyIgnoreErrorCommand(Command):
        def __init__(self, className, entities):
            super().__init__("saveManyIgnoreError")
            self.className = className
            self.entities = entities

    class StopCommand(Command):
        def __init__(self, deleteOnStop):
            super().__init__("stop")

    class CloseCommand(Command):
        def __init__(self):
            super().__init__("close")

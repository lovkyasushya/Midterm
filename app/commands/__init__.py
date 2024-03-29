from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        self.commands[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        if command_name in self.commands:
            command_class = self.commands[command_name]
            command = command_class(*args)
            command.execute()
        else:
            print(f"No such command: {command_name}")

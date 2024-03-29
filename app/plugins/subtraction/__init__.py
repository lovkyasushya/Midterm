from app.commands import Command

class SubtractionCommand(Command):
    def execute(self, args):
        if len(args) >= 2:
            try:
                a = float(args[0])
                b = float(args[1])
                result = a - b
                return result
            except ValueError:
                print("Invalid input. Please provide valid numbers.")
                return None
        else:
            print("Insufficient arguments. Please provide two numbers to subtract.")
            return None

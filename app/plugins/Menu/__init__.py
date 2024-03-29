import sys
import logging
from app.commands import Command
from app.plugins.addition import AdditionCommand
from app.plugins.subtraction import SubtractionCommand
from app.plugins.multiplication import MultiplicationCommand
from app.plugins.division import DivisionCommand

# Configure logging
logger = logging.getLogger(__name__)

class MenuCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, args=None):
        logger.info("Menu command executed.")
        print("Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Display History")
        print("6. Save History")
        print("7. Clear History")
        print("8. Delete Entry")
        print("9. Exit")

        choice = input("Enter your choice: ")
        logger.info(f"User choice: {choice}")

        if choice == "1":
            self._perform_operation(AdditionCommand(), 'Addition')

        elif choice == "2":
            self._perform_operation(SubtractionCommand(), 'Subtraction')

        elif choice == "3":
            self._perform_operation(MultiplicationCommand(), 'Multiplication')

        elif choice == "4":
            self._perform_operation(DivisionCommand(), 'Division')

        elif choice == "5":
            self._display_history()

        elif choice == "6":
            self._save_history()

        elif choice == "7":
            self._clear_history()

        elif choice == "8":
            self._delete_entry()

        elif choice == "9":
            self._exit_program()

    def _perform_operation(self, operation, operation_name):
        logger.info(f"User chose {operation_name}")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = operation.execute([num1, num2])
        print(f"Result of {operation_name.lower()} is: {result}")
        self.history_manager.add_entry(operation_name, num1, num2, result)
        logger.info(f"{operation_name} operation performed.")

    def _display_history(self):
        logger.info("User chose to display history")
        self.history_manager.display_history()

    def _save_history(self):
        logger.info("User chose to save history")
        filename = input("Enter filename to save history: ")
        self.history_manager.save_history(filename)

    def _clear_history(self):
        logger.info("User chose to clear history")
        confirm = input("Are you sure you want to clear the history? (y/n): ")
        if confirm.lower() == 'y':
            self.history_manager.clear_history()
            print("History cleared successfully.")
            logger.info("History cleared.")
        else:
            print("Operation cancelled.")

    def _delete_entry(self):
        logger.info("User chose to delete entry")
        index = int(input("Enter index of entry to delete: "))
        self.history_manager.delete_entry(index)

    def _exit_program(self):
        logger.info("User chose to exit")
        print("Exiting...")
        sys.exit()

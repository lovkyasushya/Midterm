from io import StringIO
import pytest
from app import App
from app.plugins.division import DivisionCommand
from app.plugins.addition import AdditionCommand
from app.plugins.multiplication import MultiplicationCommand
from app.plugins.subtraction import SubtractionCommand
from app.plugins.Menu import MenuCommand
from app.commands import Command, CommandHandler
from unittest.mock import MagicMock

class MockCommand(Command):
    def execute(self):
        pass

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    inputs = iter(['add 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))
    command = MenuCommand()
    command.execute([])
    captured = capfd.readouterr()
    assert captured.out.strip() == "Menu"

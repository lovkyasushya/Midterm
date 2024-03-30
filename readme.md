**Design Patterns Implementation**

**Description:**
The provided code snippets demonstrate the implementation of several design patterns, including the Command pattern and the Singleton pattern.

**Command Pattern:** The Command abstract base class defines the interface for executing commands, while the CommandHandler class manages a collection of commands and executes them based on user input. This promotes decoupling between the invoker (the CommandHandler) and the receiver (the concrete command classes).

**Singleton Pattern:** Although not explicitly shown in the provided snippets, the implementation of classes such as CommandHandler and calculation_history suggests the use of the Singleton pattern to ensure that only one instance of these classes is created throughout the application's lifecycle.

**Implementation:**
Command Pattern: https://github.com/lovkyasushya/Midterm/tree/main/app/commands

Singleton Pattern: https://github.com/lovkyasushya/Midterm/tree/main/app/plugins/calculation_history




**Usage of Environment Variables**
**Description:**
The application utilizes environment variables to configure various settings such as the environment type (e.g., development, testing, production) and other application-specific configurations. These environment variables are loaded using the dotenv library and accessed through the os.environ dictionary.

**Implementation:**
The code snippet loads environment variables using the load_dotenv() function from the dotenv library.
Environment variables are accessed using the os.environ dictionary.
https://github.com/lovkyasushya/Midterm/blob/main/app/__init__.py



**Logging Implementation**

**Description:**
The application employs logging to record important events and information during runtime. The logging module is used to configure logging settings such as the log level, log format, and log file location. Log messages are written to a log file for future reference and debugging purposes.

**Implementation:**
The logging.basicConfig() function is used to configure logging settings such as the log file location, log level, and log format.
The logger object is created using the logging.getLogger() function to write log messages to the specified log file.
Log messages are written using methods such as logger.info(), logger.error(), etc.

https://github.com/lovkyasushya/Midterm/blob/main/logging.conf




**Exception Handling**
**Description:**
The application utilizes try/except blocks and exception handling to handle potential errors and exceptional conditions during runtime. It employs both the "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches to handle errors gracefully and provide informative error messages to the user.

**Implementation:**

**LBYL (Look Before You Leap):** The application checks for certain conditions or constraints before executing potentially risky operations to avoid potential errors or exceptions.

**EAFP (Easier to Ask for Forgiveness than Permission):** The application attempts to execute operations within try blocks and handles any resulting exceptions gracefully using except blocks, allowing for a more concise and readable code structure.

https://github.com/lovkyasushya/Midterm/blob/main/app/plugins/division/__init__.py


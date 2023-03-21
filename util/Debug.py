import inspect
import os


class Debug:
    show_logs = False
    show_files = []

    @staticmethod
    def out(message):
        split_message = message.split(',')
        caller = inspect.stack()[2].filename
        file = os.path.splitext(os.path.basename(caller))[0]
        if Debug.show_logs or file in Debug.show_files:
            print(f"{split_message[0]}::{file.upper()}::{split_message[1]}")

    @staticmethod
    def log(message):
        Debug.out(f"DEBUG,{message}")

    @staticmethod
    def log_error(message):
        Debug.out(f"ERROR,{message}")

    @staticmethod
    def log_warning(message):
        Debug.out(f"WARNING,{message}")

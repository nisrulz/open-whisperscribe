from src.config_loader import load_config
from datetime import datetime

# Load configuration
config = load_config()
console = config.get("logger", {}).get("console", False)

"""
Simple logger for console and (optionally) alert output.
Switch between console and alert by setting use_alerts.
"""

class Logger:
    def __init__(self, console=console):
        self.alerts = not console

    def set_alerts(self, alerts: bool):
        self.alerts = alerts

    def log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] [{level}] {message}"
        if self.alerts:
            self._alert(formatted_message, level)
        else:
            self._console(formatted_message, level)

    def _console(self, message, level):
        colors = {
            "ERROR": "\033[91m",
            "WARNING": "\033[93m",
            "SUCCESS": "\033[92m",
            "INFO": ""
        }
        color = colors.get(level, "")
        endc = "\033[0m" if color else ""
        print(f"{color}[{level}]{endc} {message}")

    def _alert(self, message, level):
        raise NotImplementedError(f"Alert system not implemented: {level} - {message}")

    def info(self, message):
        self.log(message, "INFO")

    def warning(self, message):
        self.log(message, "WARNING")

    def error(self, message):
        self.log(message, "ERROR")

    def success(self, message):
        self.log(message, "SUCCESS")

logger = Logger()
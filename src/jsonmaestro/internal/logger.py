import logging
import sys
from datetime import datetime
from typing import Union
from colorama import Fore, Style


class Logger:
	COLORS = {
	    "DEBUG": Fore.BLUE,
	    "INFO": Fore.GREEN,
	    "WARN": Fore.YELLOW,
	    "ERROR": Fore.RED,
	    "CRITICAL": Fore.RED + Style.BRIGHT,
	}

	def __init__(self, name: Union[str, None] = None):
		self.name = name
		self.logger = logging.getLogger(name)
		self.logger.setLevel(logging.DEBUG)

		if self.logger.hasHandlers():
			self.logger.handlers.clear()

		handler = logging.StreamHandler(sys.stdout)
		handler.setFormatter(self._get_formatter())
		self.logger.addHandler(handler)

	def _get_formatter(self) -> logging.Formatter:
		return logging.Formatter(fmt="%(message)s",
		                         datefmt="%Y-%m-%d %H:%M:%S")

	def _log(self, level: str, message: str):
		log_message: str = ""
		if self.name is not None:
			log_message = f"{self.name:} {self._get_time()} {self.COLORS[level]}[{level}] {message}{Style.RESET_ALL}"
		else:
			log_message = f"{self._get_time()} {self.COLORS[level]}[{level}] {message}{Style.RESET_ALL}"
		if level == "DEBUG":
			self.logger.debug(log_message)
		elif level == "INFO":
			self.logger.info(log_message)
		elif level == "WARN":
			self.logger.warning(log_message)
		elif level == "ERROR":
			self.logger.error(log_message)
		elif level == "CRITICAL":
			self.logger.critical(log_message)

	def _get_time(self):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	def debug(self, message: str) -> None:
		self._log("DEBUG", message)

	def info(self, message: str) -> None:
		self._log("INFO", message)

	def warn(self, message: str) -> None:
		self._log("WARN", message)

	def error(self, message: str) -> None:
		self._log("ERROR", message)

	def critical(self, message: str) -> None:
		self._log("CRITICAL", message)


# Example usage
if __name__ == "__main__":
	log = Logger()

	log.debug("This is a debug message.")
	log.info("This is an info message.")
	log.warn("This is a warning message.")
	log.error("This is an error message.")
	log.critical("This is a critical message.")

	log1 = Logger("log")

	log1.debug("This is a debug message.")
	log1.info("This is an info message.")
	log1.warn("This is a warning message.")
	log1.error("This is an error message.")
	log1.critical("This is a critical message.")

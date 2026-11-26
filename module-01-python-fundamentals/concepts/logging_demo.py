#Remember : Configure logging once near the entry point of your application.
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.debug("This is a debug message.")
logging.critical("This is a critical message.")

# writing message in app.log file
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

logging.info("Application started.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")

#creating own logger
logger = logging.getLogger("my_logger")
logging.basicConfig(
    level=logging.INFO)

logger.info("This is an info message from my_logger.")
logger.warning("This is a warning message from my_logger.")
logger.error("This is an error message from my_logger.")

import logging
import os


os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("qa_framework")
logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = logging.FileHandler(
        "logs/test_execution.log",
        mode="a",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


def get_logger():
    return logger
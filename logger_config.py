import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)


def setup_logging(worker_id="main"):
    log_file = LOG_DIR / f"automation_{worker_id}.log"

    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()

    # Create log file handler
    file_handler = logging.FileHandler(
        log_file,
        mode="w",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
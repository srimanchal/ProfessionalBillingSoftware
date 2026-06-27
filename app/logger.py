from loguru import logger
from app.constants import LOGS_DIR
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True
)

logger.add(
    LOGS_DIR / "application.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
    encoding="utf-8"
)

logger.add(
    LOGS_DIR / "error.log",
    rotation="10 MB",
    retention="30 days",
    level="ERROR",
    encoding="utf-8"
)

logger.add(
    LOGS_DIR / "audit.log",
    rotation="10 MB",
    retention="90 days",
    level="INFO",
    encoding="utf-8"
)
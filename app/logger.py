from loguru import logger
from app.constants import LOGS_DIR
import sys

logger.remove()

# Console logging only when stdout exists
if sys.stdout is not None:
    logger.add(
        sys.stdout,
        level="INFO",
        colorize=True,
    )

# Application log
logger.add(
    str(LOGS_DIR / "application.log"),
    rotation="10 MB",
    retention="30 days",
    level="INFO",
    encoding="utf-8",
)

# Error log
logger.add(
    str(LOGS_DIR / "error.log"),
    rotation="10 MB",
    retention="30 days",
    level="ERROR",
    encoding="utf-8",
)

# Audit log
logger.add(
    str(LOGS_DIR / "audit.log"),
    rotation="10 MB",
    retention="90 days",
    level="INFO",
    encoding="utf-8",
)
"""
Logger Configuration.

This module provides a reusable logger setup with configurable log level using environment variables.
"""

import logging
import os


def setup_logger() -> logging.Logger:
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    return logging.getLogger("calculator")

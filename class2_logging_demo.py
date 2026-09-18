import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger(__name__)

x = 42

logger.info("Loading file...")
logger.debug("Processing row 1...")
logger.debug(f"Value is {x}")
logger.info("Done!")

import logging


def _logging_setup():
    # Set up the logger
    log_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    root_logger = logging.getLogger(__name__)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)
    return root_logger


logger = _logging_setup()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

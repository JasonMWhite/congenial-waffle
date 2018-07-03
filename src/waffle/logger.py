import logging


def create_logger() -> logging.Logger:
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    log.addHandler(handler)
    return log


LOG = create_logger()

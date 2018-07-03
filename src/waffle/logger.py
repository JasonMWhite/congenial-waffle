import logging


def create_logger() -> logging.Logger:
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    log.addHandler(ch)
    return log


LOG = create_logger()

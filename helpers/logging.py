import logging


logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %s(message)s', datefmt='%m/%d/%Y %H: %S: %p')
c_handler.setFormatter(formatter)

logger.addHandler(c_handler)

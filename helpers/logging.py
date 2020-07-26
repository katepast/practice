import logging


class Log:

    @staticmethod
    def test_log():
        logger = logging.getLogger(Log.__name__)
        logger.setLevel(logging.INFO)

        # create console handler ad set level info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %s(message)s',
                                      datefmt='%m/%d/%Y %H: %S: %p')

        # add formatter to console handler
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)

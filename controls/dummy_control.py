from controls.base_control import BaseControl


class DummyControl(BaseControl):
    """
    A stub class of control. Can be used to get BaseControl's functionality without defining of new class.
    :param locator: locator tuple
    :param driver: instance of WebDriver
    :param parent: parent element (optional)
    """

    def __init__(self, locator, driver):
        super().__init__(driver)
        self._locator = locator

import pytest

from helpers.logging import logger
from helpers.verify import Verify
from practice_page.Pages.practice_page import PracticePage


class TestSelectRbBMW:

    @pytest.mark.debug
    def test_select_rbb_bmw(self, open_site):
        practice_page = PracticePage(open_site)
        practice_page.check_bmw_radio_btn()

        logger.info("Verify that BMW radio button is checked")
        Verify.true(practice_page.is_bmw_radio_btn_checked(), "BMW radio button is not checked")



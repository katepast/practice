import pytest

from Pages.practice_page import PracticePage
from helpers.logging import logger
from helpers.verify import Verify


class TestSelectRbBMW:
    """check presence of specified values in table"""

    @pytest.mark.debug
    def test_check_values_in_table(self, open_site):
        verify_author_titles = ["Let's Kode It", "Let's Kode It", "Let's Kode It"]
        practice_page = PracticePage(open_site)

        logger.info("Verify that 'Author' is displayed as title column in the table")
        Verify.contains('Author', practice_page.get_title_columns_from_table(), "There is no title 'Author' in table")

        logger.info("Verify that only '4' rows in table is in the table")
        Verify.equals('4', practice_page.get_amount_of_rows_in_table(), "Amount of rows incorrect")

        logger.info(f"Titles for 'Author' column with values '{verify_author_titles}' are displayed correctly")
        Verify.equals(verify_author_titles, practice_page.get_values_for_author_column(),
                      f"Titles 'Author' column with values '{verify_author_titles}' are not displayed")



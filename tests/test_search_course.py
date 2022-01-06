import pytest

from helpers.logging import logger
from helpers.verify import Verify
from Pages.main_page import CoursePage


class TestSearchCourse:
    searched_course = "JavaScript for beginners"

    @pytest.mark.debug
    def test_open_login_page(self, open_course_site):
        main_page = CoursePage(open_course_site)

        logger.info(f"Search course with name '{self.searched_course}'")
        main_page.search_course(self.searched_course)

        logger.info("Verify that 'All Courses' title is displayed")
        Verify.true(main_page.is_course_link_url_displayed(), "'All Courses' title is not displayed")
        all_items = main_page.get_all_items()

        logger.info(f"Verify that 'Course' with name '{self.searched_course}' is displayed")
        Verify.contains(self.searched_course, all_items,
                        f"Course with name '{self.searched_course}' is absent on the page")

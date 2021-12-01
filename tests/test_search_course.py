import pytest
from practice_page.Pages.main_page import CoursePage


class TestSearchCourse:
    searched_course = "JavaScript for beginners"

    @pytest.mark.debug
    def test_open_login_page(self, open_course_site):
        main_page = CoursePage(open_course_site)
        main_page.search_course(self.searched_course)
        all_items = main_page.get_all_items()
        print(all_items)
        assert self.searched_course in all_items, f"Course with name '{self.searched_course}' is absent on the page"

from model.project import Project


class ProjectHelper:
    def __init__(self, app):
          self.app = app

    def create(self,project):
        self.app.open_home_page()
        self.open_project_page()
        self.fill_form(project)
        self.open_project_page()

    def fill_form(self, project):
        wd = self.app.wd
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_css_selector("input.button").click()

    def proceed(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Proceed").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href*='manage_overview_page.php']").click()
        if len(wd.find_elements_by_name("password")) != 0:
            wd.find_element_by_name("password").send_keys("root")
            wd.find_element_by_css_selector('input[type="submit"]').click()
        wd.find_element_by_css_selector("a[href*='manage_proj_page.php']").click()

    def get_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        projects = []
        self.open_project_page()
        for element in wd.find_elements_by_css_selector("tr a[href*='manage_proj_edit_page.php?project_id']"):
            text = element.text
            projects.append(Project(name=text))
        return list(projects)

    def delete_project_by_name(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()

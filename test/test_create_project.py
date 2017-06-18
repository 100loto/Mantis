from model.project import Project

def test_create_project(app):
    wd = app.wd
    app.open_home_page()
    app.session.login("administrator", "root")
    wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()
    wd.find_element_by_name("name").click()
    wd.find_element_by_name("name").clear()
    wd.find_element_by_name("name").send_keys("New_project")
    wd.find_element_by_name("description").click()
    wd.find_element_by_name("description").clear()
    wd.find_element_by_name("description").send_keys("Description of project")
    wd.find_element_by_css_selector("input.button").click()
    wd.find_element_by_link_text("Proceed").click()

    def get_project_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_project_page()
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector("tr.row-1"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                enabled = cells[2].text
                view_status = cells[3].text
                description = cells[4]
                id = cells[0].find_element_by_css_selector("tr.row-1 > td > a").get_attribute("href")
                self.contact_cache.append(Project(name=name, status=status, enabled=enabled,
                                                  id=id, view_status=view_status,
                                                  description=description))
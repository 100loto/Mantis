import random
import string
from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_list()) == 0:
        app.project.create(Project(name=random_string("project_of", 10), description=random_string("description:", 50)))
    old_projects = app.project.get_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project)
    new_projects = app.project.get_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

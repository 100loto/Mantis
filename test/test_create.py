import random
import string

from model.project import Project


def test_create_project(app, soap):
    project = Project(name=random_string(10), description=random_string(50))
    old_project = soap.get_list()
    app.project.create(project)
    new_project = soap.get_list()
    assert len(new_project) == len(old_project) + 1
    old_project.append(project)
    assert sorted(old_project, key=Project.by_name) == sorted(new_project, key=Project.by_name)


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

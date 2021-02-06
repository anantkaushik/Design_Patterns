# Source: https://www.geeksforgeeks.org/dependecy-inversion-principle-solid/

class Manager:
    def __init__(self):
        self.developers = []
        self.designers = []
        self.testers = []

    def add_developer(self, dev):
        self.developers.append(dev)

    def add_designers(self, design):
        self.designers.append(design)

    def add_testers(self, testers):
        self.testers.append(testers)


class Developer:
    def __init__(self):
        print("developer added")


class Designer:
    def __init__(self):
        print("designer added")


manager = Manager()
manager.add_developer(Developer())
manager.add_designers(Designer())

"""
Problem in the above implemented example:
First, we have exposed everything about the lower layer to the upper layer, thus abstraction is not mentioned. 
That means Manager must already know about the type of the workers that he can supervise.
Now if another type of worker comes under the manager lets say, QA (quality assurance), then the whole class needs to 
be rejigged.
"""


class Employee:
    def work(self):
        pass


class ManagerNew:
    def __init__(self):
        self.employees = []

    def add_employee(self, a):
        self.employees.append(a)


class DeveloperNew(Employee):
    def __init__(self):
        print("developer added")

    def work(self):
        print("turning coffee into code")


class DesignerNew(Employee):
    def __init__(self):
        print("designer added")

    def work(self):
        print("turning lines to wireframes")


class TestersNew(Employee):
    def __init__(self):
        print("tester added")

    def work(self):
        print("testing everything out there")


manager_new = ManagerNew()
manager_new.add_employee(DeveloperNew())
manager_new.add_employee(DesignerNew())
manager_new.add_employee(TestersNew())

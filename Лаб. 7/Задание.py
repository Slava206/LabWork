class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self,name,id)
        self.department = department
    def manage_project(self, project_name):
        return f"Менеджер {self.name}, управляет проектом {project_name}"

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self,name,id)
        self.specialization = specialization
    def perform_maintenance(self, equipment):
        return f"Менеджер: {self.name}, выполняет техническое обслуживание: {equipment}"

class TechManager(Manager, Technician):
    def __init__(self, name, id, department,specialization):
        Manager.__init__(self,name,id,department)
        Technician.__init__(self,name,id,specialization)
        self.team = []
    def add_employee(self, employee):
        self.team.append(employee)
    def get_team_info(self):
        return [employee.get_info() for employee in self.team]


manager = Manager("Иванов", 111, "IT")

print(manager.get_info())
print(manager.manage_project("Проект N"))

technician = Technician("Петров", 222, "оператор ЭВМ")

print(technician.get_info())
print(technician.perform_maintenance("ЭВМ"))

tech_manager = TechManager('Алекс', 344, 'Ядерная бомба','Ааа')

tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print(tech_manager.get_info())
print(tech_manager.manage_project("Проект V"))
print(tech_manager.perform_maintenance("Манипулятор"))

print("TechManager")
print(tech_manager.get_team_info())
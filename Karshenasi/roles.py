from rolepermissions.roles import AbstractUserRole

class Student(AbstractUserRole):
    available_permissions = {
        'create_medical_record': True,
    }

class Professor(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }

class Admin(AbstractUserRole) :
    available_permissions = {
        'edit_patient_file': True,
    }

class User:
    def __init__(self, user_id, role, department):
        self.user_id = user_id
        self.role = role
        self.department = department

class PatientRecord:
    def __init__(self, patient_id, owner_department):
        self.patient_id = patient_id
        self.owner_department = owner_department


class ABACPolicy:
    def check_access(self, user, action, resource):
        raise NotImplementedError("Subclasses must implement this method")


class HealthcareABACPolicy(ABACPolicy):
    def check_access(self, user, action, resource):
        if action == "view":
            return self._can_view(user, resource)
        elif action == "edit":
            return self._can_edit(user, resource)
        else:
            return False

    def _can_view(self, user, resource):
        # Users from the same department can view patient records within their department
        return user.department == resource.owner_department

    def _can_edit(self, user, resource):
        # Only users with the "admin" role can edit patient records
        return user.role == "admin"


# Example usage:
user1 = User(user_id=1, role="admin", department="Cardiology")
user2 = User(user_id=2, role="doctor", department="Orthopedics")

patient_record1 = PatientRecord(patient_id=101, owner_department="Cardiology")
patient_record2 = PatientRecord(patient_id=102, owner_department="Orthopedics")

abac_policy = HealthcareABACPolicy()

# Check access for user1 to view patient_record1
can_view_patient_record1 = abac_policy.check_access(user1, "view", patient_record1)
print(f"User1 can view patient_record1: {can_view_patient_record1}")

# Check access for user2 to edit patient_record1
can_edit_patient_record1 = abac_policy.check_access(user2, "edit", patient_record1)
print(f"User2 can edit patient_record1: {can_edit_patient_record1}")

# Check access for user2 to view patient_record2
can_view_patient_record2 = abac_policy.check_access(user2, "view", patient_record2)
print(f"User2 can view patient_record2: {can_view_patient_record2}")

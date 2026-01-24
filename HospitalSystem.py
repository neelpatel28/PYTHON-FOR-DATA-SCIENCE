class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.queue = []

    def register_patient(self, pid, name, disease):
        self.patients[pid] = {"name": name, "disease": disease}
        self.queue.append(pid)
        print("Patient registered successfully.")

    def consult_next(self):
        if not self.queue:
            print("No patients in queue.")
            return
        pid = self.queue.pop(0)
        print("Consulting Patient:", self.patients[pid])
        del self.patients[pid]

    def display_patients(self):
        print("\nCurrent Patients:")
        for pid, info in self.patients.items():
            print(pid, info)

    def emergency_add(self, pid, name, disease):
        self.patients[pid] = {"name": name, "disease": disease}
        self.queue.insert(0, pid)
        print("Emergency patient added.")

system = HospitalSystem()

while True:
    print("\nHospital Patient Management System")
    print("1. Register Patient")
    print("2. Consult Next Patient")
    print("3. Display Patients")
    print("4. Emergency Add")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        disease = input("Enter Disease: ")
        system.register_patient(pid, name, disease)

    elif ch == '2':
        system.consult_next()

    elif ch == '3':
        system.display_patients()

    elif ch == '4':
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        disease = input("Enter Disease: ")
        system.emergency_add(pid, name, disease)

    elif ch == '5':
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")

class Employee:
    def __init__(self, name, salary, phone, email, address):
        self.name = name
        self.salary = salary
        self.phone = phone
        self.email = email
        self.address = address

    def display_info(self):
        print(f"Name:    {self.name}")
        print(f"Salary:  ₹{self.salary}")
        print(f"Email:   {self.email}")
        print(f"Address: {self.address}")


if __name__ == "__main__":
    emp = Employee(
        name="Neha Mutke",
        salary=50000,
        phone="+91-9876543210",
        email="nehamutke@gmail.com",
        address="karvenagar, Pune, Maharashtra"
    )
    emp.display_info()

        

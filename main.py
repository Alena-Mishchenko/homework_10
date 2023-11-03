from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)

         
class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        value = ''.join(filter(str.isdigit, value))
        if len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        self.value = value
  

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
        return f"Added phone number {phone} to {self.name}."
    
    def remove_phone(self, phone):
        self.phones.remove(self.find_phone(phone))
    
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f"Changed phone for {self.name} to {new_phone}."
        raise ValueError

    def find_phone(self, phone):
        for record in self.phones:
            if record.value == phone:
                return record
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return f"{record} add success"
    
    def find(self, name):
        result = self.data.get(name)
        return result
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Deleted record for {name}."
        else:
            return f"No such record for {name}."
        
    

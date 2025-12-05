# Node class to represent each student
class Node:
    def __init__(self, data):
        self.data = data   # dictionary (name, adm, grades)
        self.next = None   # pointer to next node


# LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new student at the end
    def insert(self, name, adm, grades):
        student_data = {
            "name": name,
            "adm": adm,
            "grades": grades
        }
        new_node = Node(student_data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Display all students
    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            data = current.data
            print(f"Name: {data['name']}, Adm: {data['adm']}, Grades: {data['grades']}")
            current = current.next


# --- Example Usage ---
students = LinkedList()

# Insert student records
students.insert("Anne Gathuita", "ADM001", {"Unit1": 85, "Unit2": 90, "Unit3": 88})
students.insert("Brian Otieno", "ADM002", {"Unit1": 78, "Unit2": 82, "Unit3": 80})
students.insert("Carol Mwangi", "ADM003", {"Unit1": 92, "Unit2": 89, "Unit3": 95})

# Display all students
students.display()
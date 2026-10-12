class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    def __init__(self, name): #represents one employee in the tree
        self.name = name #stores the name
        self.left = None #pointer with the value of none
        self.right = None #pointer with the value of none

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    def __init__(self):
        self.root = None #sets the root to none
        
    def insert(self, manager_name, new_value, side, current_node=None):
        if self.root is None: #empty tree instance, checks if the root employee exists or not
            print("Tree is empty. Cannot insert without root")
            return
        
        if current_node is None: #start from the root if no node was specified
            current_node = self.root

        if current_node.name == manager_name:
            if side == "left" and current_node.left is None:
                current_node.left = EmployeeNode(new_value) #if the values match they will continue (left)
                print(f"{new_value} added under {manager_name} on the left.")
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = EmployeeNode(new_value) #if the values match they will continue (right)
                print(f"{new_value} added under {manager_name} on the right.")
                return True
            else: 
                print(f"{manager_name} already has a {side} subordinate.")
                return True
            
        found_left = False #searching subtrees
        found_right = False

        if current_node.left:
            found_left = self.insert(manager_name, new_value, side, current_node.left) #syntax to find manager name, what the new value is, and which side to insert it
        
        if current_node.right and not found_left:
            found_right = self.insert(manager_name, new_value, side, current_node.right)
        
        if not(found_left or found_right):

            if current_node == self.root:
                print(f"Parent node {manager_name} not found in the tree.") #indicates the name was not found in the search
                return False
            
            return True
        

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root #start printing from root
            else: 
                return
        indent = "   " * level
        print(f"{indent}- {node.name}")

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)
    

# Test code here from assignment resources
company_directory = TeamTree()
company_directory.root = EmployeeNode("Jordan")
company_directory.insert("Jordan", "Taylor", "right")
company_directory.insert("Jordan", "Riley", "left")
company_directory.insert("Riley", "Dana", "right")
company_directory.insert("Riley", "Morgan", "left")
company_directory.print_tree()

#output: 
#Taylor added under Jordan on the right.
#Riley added under Jordan on the left.
#Dana added under Riley on the right.
#Morgan added under Riley on the left.
#- Jordan
 #  - Riley
    #  - Morgan
     # - Dana
  # - Taylor

# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

#DESIGN MEMO:
#The recursive insertion works by starting at the root, and searching for the manager. If the values do not match and a manager is not found, it then returns False and
#searches the other side. If it finds the matching value, it will then be given the value to insert as well as the side to insert it on. After it does this, 
#it goes back to the root value (ex. CEO or manager) and finishes. 

#Some of the challenges I faced was figuring out the right spot for a new employee was keeping track of where the code was searcching at which point, and if it did not find the matching value where it would search next.
#My recurring issue is I understand the logic, but turning it into syntax and working code confuses me. Luckily, the assignment resources were useful in breaking down the logic of each piece of code. 
 
#When might trees be preferable to other data structures in real-world systems? 
#Trees might be preferable to other data structures in real-world systems as other data strcutures do not handle hierarchy data the way trees do. It is an efficient way to store data, as well as query stacked data. 
#A list, or set would not be able to operate in a hierarchy format the way trees can. Many real-world systems are not straightforward, and they do contain levels of data that need to be handle in a hierarchal process. 
#Trees are built for this kind of operation, unlike other data structures. 





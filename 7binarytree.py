class T1:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

print("--- TREE INITIALIZATION ---")
root_val = input("Enter data for ROOT: ")
root = T1(root_val)

root.left = T1(input(f"Enter data for {root_val}'s Left child: "))
root.right = T1(input(f"Enter data for {root_val}'s Right child: "))

print(f"\nRoot: {root.data}")
print(f"Left: {root.left.data} | Right: {root.right.data}")

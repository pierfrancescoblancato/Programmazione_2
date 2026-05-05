class MyClass:
    class_attr = "Sono un attributo di classe"

    def __init__(self):
        self.instance_attr = "Sono un attributo di istanza"

obj = MyClass()

# 2. Stampa dir(obj)
print("--- 1. RISULTATO DI dir(obj) ---")
print(dir(obj))

# 3. Stampa obj.__dict__
print("\n--- 2. RISULTATO DI obj.__dict__ ---")
print(obj.__dict__)

# 4. Stampa MyClass.__dict__
print("\n--- 3. RISULTATO DI MyClass.__dict__ ---")
print(MyClass.__dict__)
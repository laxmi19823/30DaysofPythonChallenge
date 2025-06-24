class UppercaseClassNameMeta(type):
    def __new__(cls, name, bases, dct):
        if not name[0].isupper():
            raise TypeError(f"Class name '{name}' must start with an uppercase letter.")
        if "_" in name:
            raise TypeError(f"Class name '{name}' must not contain underscores.")
        return super().__new__(cls, name, bases, dct)

# ✅ Correct class name - no errors expected
class HelloWorld(metaclass=UppercaseClassNameMeta):
    pass

print("HelloWorld class created successfully.")

# ❌ Incorrect class name - starts with lowercase letter
try:
    class helloWorld(metaclass=UppercaseClassNameMeta):
        pass
except TypeError as e:
    print(f"Error: {e}")

# ❌ Incorrect class name - contains underscore
try:
    class Hello_World(metaclass=UppercaseClassNameMeta):
        pass
except TypeError as e:
    print(f"Error: {e}")



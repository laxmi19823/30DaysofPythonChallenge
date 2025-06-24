class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

#  User Input
filename = input("Enter the filename (e.g., sample.txt): ")
content = input("Enter the content to write into the file: ")

# ✅ Usage with Context Manager
with FileHandler(filename, 'w') as f:
    f.write(content)

print(f"✅ Content written to {filename} successfully!")

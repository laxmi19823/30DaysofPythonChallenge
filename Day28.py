class FileHandler:
    """Custom context manager for safe file handling."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"📂 Opening file: {self.filename} in {self.mode} mode")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"📁 File {self.filename} closed successfully.")
        if exc_type:
            print(f"⚠️ An error occurred: {exc_type.__name__} - {exc_value}")
        return False  # Propagate exception if any

# ✅ Usage
filename = input("Enter the filename: ")
content = input("Enter the content to write into the file: ")

with FileHandler(filename, 'w') as f:
    f.write(content)

print(f"✅ Content written to {filename} successfully!")

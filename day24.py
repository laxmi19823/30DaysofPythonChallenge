from dataclasses import dataclass

@dataclass
class LibraryBook:
    title: str
    author: str
    isbn: str
    publication_year: int

    def display_info(self):
        return (
            f"📚 Title: {self.title}\n"
            f"✍️ Author: {self.author}\n"
            f"🔢 ISBN: {self.isbn}\n"
            f"📆 Published: {self.publication_year}"
        )

# Creating book instances
book1 = LibraryBook(
    title="Into the Stars",
    author="Laxmi Prasanna",
    isbn="978-81-981677-0-5",
    publication_year=2024
)

book2 = LibraryBook(
    title="Here, There and Everywhere",
    author="Sudha Murty",
    isbn="978-0-1434-4890-7",
    publication_year=2018
)

book3 = LibraryBook(
    title="Ikigai: The Japanese Secret to a Long and Happy Life",
    author="Héctor García and Francesc Miralles",
    isbn="978-1-7863-3791-0",
    publication_year=2017
)

# Output
print(book1.display_info())
print("\n" + "-"*40 + "\n")
print(book2.display_info())
print("\n" + "-"*40 + "\n")
print(book3.display_info())

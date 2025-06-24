import threading
import requests

def download_file(url, filename):
    print(f"Starting download: {filename}")
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Completed download: {filename}")

urls = [
    ("https://picsum.photos/id/2/5000/3333", "laptop.jpg"),

    ("https://picsum.photos/id/18/367/267","greenary.jpg"),
    ("https://picsum.photos/id/15/367/267","nature.jpg")
]

threads = []
for url, name in urls:
    thread = threading.Thread(target=download_file, args=(url, name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

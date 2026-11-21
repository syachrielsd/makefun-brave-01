import os

TEXT = "Somewhere a server hums in a cool dark room, and nobody is asking it anything. The queue is empty. The fans slow down. Whatever you decide next can wait until the light through the window changes."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# файл унших
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

# файлд бичих
def append_file(filename, content):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content)

def main():
    filename = "mail.txt"
    data = read_file(filename)
    print("Одоогийн файл:\n")
    print(data)
    new_text = input("\nНэмэх текстээ бич: ")
    append_file(filename, "\n" + new_text)

    print("\nАмжилттай нэмэгдлээ")

main()
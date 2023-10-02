# to_do_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_tasks(self):
        if not self.tasks:
            print("Yapılacak iş yok.")
        else:
            print("Yapılacak İşler:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nYapılacaklar Listesi Uygulaması")
        print("1. İş Ekle")
        print("2. İş Sil")
        print("3. İşleri Görüntüle")
        print("4. Çıkış")

        choice = input("Seçiminizi yapın (1/2/3/4): ")

        if choice == "1":
            task = input("Yapılacak işi girin: ")
            todo_list.add_task(task)
            print("İş eklendi.")
        elif choice == "2":
            task = input("Silmek istediğiniz işi girin: ")
            todo_list.remove_task(task)
            print("İş silindi.")
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

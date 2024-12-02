import tkinter as tk
import requests
import threading

def fetch_data():
    try:
        response = requests.get("http://127.0.0.1:5000/students")
        response.raise_for_status()  
        data = response.json()

        listbox.delete(0, tk.END)

        for student in data:
            listbox.insert(tk.END, f"Имя: {student['name']}, Возраст: {student['age']}, Адрес: {student['address']}")
    except requests.exceptions.RequestException as e:
        listbox.insert(tk.END, f"Ошибка: {str(e)}")
    except Exception as e:
        listbox.insert(tk.END, f"Ошибка: {str(e)}")

def thread_fetch_data():
    threading.Thread(target=fetch_data).start()

root = tk.Tk()
root.title("Студенты")

button = tk.Button(root, text="Получить данные", command=thread_fetch_data)
button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack()

root.mainloop()
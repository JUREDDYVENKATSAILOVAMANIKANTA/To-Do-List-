#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import os

class ToDoListGUI:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.task_label = tk.Label(master, text="Enter Task:")
        self.task_label.grid(row=0, column=0)

        self.task_entry = tk.Entry(master)
        self.task_entry.grid(row=0, column=1)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2)

        self.tasks_listbox = tk.Listbox(master)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2)

        self.view_button = tk.Button(master, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=1, column=2)

        self.mark_done_button = tk.Button(master, text="Mark as Done", command=self.mark_task_done)
        self.mark_done_button.grid(row=2, column=0)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1)

        self.save_button = tk.Button(master, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=2, column=2)

        self.load_button = tk.Button(master, text="Load Tasks", command=self.load_tasks)
        self.load_button.grid(row=3, column=0, columnspan=3)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            print("Task added successfully.")

    def view_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        if self.tasks:
            for task in self.tasks:
                self.tasks_listbox.insert(tk.END, task)
        else:
            self.tasks_listbox.insert(tk.END, "Your To-Do List is empty.")

    def mark_task_done(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks[index] += " - Done"
            self.tasks_listbox.delete(index)
            self.tasks_listbox.insert(index, self.tasks[index])
            print("Task marked as done.")
        except IndexError:
            print("Please select a task.")

    def delete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            del self.tasks[index]
            self.tasks_listbox.delete(index)
            print("Task deleted successfully.")
        except IndexError:
            print("Please select a task.")

    def save_tasks(self):
        filename = "todo.txt"
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')
        print("Tasks saved to file.")

    def load_tasks(self):
        filename = "todo.txt"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
            print("Tasks loaded from file.")
            self.view_tasks()
        else:
            print("File not found.")

def main():
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





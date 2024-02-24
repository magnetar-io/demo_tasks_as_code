import os
import json
import random
import re
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class TaskEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Task Editor")
        self.folder_path = ""
        self.file_path = ""
        self.tasks = []
        self.current_task_index = 0

        self.load_button = tk.Button(self.root, text="Load Random Markdown File", command=self.load_random_md_file)
        self.load_button.pack(pady=10)

        self.task_label = tk.Label(self.root, text="", wraplength=400)
        self.task_label.pack(pady=10)

        self.edit_button = tk.Button(self.root, text="Edit Current Task", command=self.edit_current_task)
        self.edit_button.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next Task", command=self.next_task)
        self.next_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save Changes", command=self.save_md_file)
        self.save_button.pack(pady=10)

    def load_random_md_file(self):
        self.folder_path = filedialog.askdirectory(title="Select Folder")
        if not self.folder_path:
            return
        md_files = [f for f in os.listdir(self.folder_path) if f.endswith('.md')]
        if not md_files:
            messagebox.showerror("Error", "No Markdown files found in the directory.")
            return
        random_file = random.choice(md_files)
        self.file_path = os.path.join(self.folder_path, random_file)
        with open(self.file_path, 'r') as f:
            content = f.read()
        tasks_json = re.search(r'```json\n(.+?)\n```', content, re.DOTALL).group(1)
        self.tasks = json.loads(tasks_json)
        self.current_task_index = 0
        self.update_task_label()

    def update_task_label(self):
        if self.tasks:
            task = self.tasks[self.current_task_index]
            self.task_label.config(text=json.dumps(task, indent=4))
        else:
            self.task_label.config(text="")

    def edit_current_task(self):
        if not self.tasks:
            return
        task = self.tasks[self.current_task_index]
        for key in task.keys():
            if key not in ['id', 'dependencies']:
                new_value = simpledialog.askstring("Edit Task", f"Enter new value for {key} (current: {task[key]}):", parent=self.root)
                if new_value is not None:
                    task[key] = new_value
        self.update_task_label()

    def next_task(self):
        if self.tasks and self.current_task_index < len(self.tasks) - 1:
            self.current_task_index += 1
            self.update_task_label()

    def save_md_file(self):
        if not self.file_path or not self.tasks:
            return
        with open(self.file_path, 'r') as f:
            content = f.read()
        tasks_json = json.dumps(self.tasks, indent=4)
        new_content = re.sub(r'```json\n(.+?)\n```', f'```json\n{tasks_json}\n```', content, flags=re.DOTALL)
        with open(self.file_path, 'w') as f:
            f.write(new_content)
        messagebox.showinfo("Success", f"Saved changes to {self.file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskEditor(root)
    root.mainloop()

import os
import json
import re
import matplotlib.pyplot as plt
from datetime import datetime

def extract_tasks_from_md(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract the JSON string from the code block
    json_str = re.search(r'```json\n(.+?)\n```', content, re.DOTALL).group(1)
    tasks = json.loads(json_str)
    return tasks

def plot_timeline(tasks, output_path):
    # Convert dates to datetime objects and sort tasks by start date
    for task in tasks:
        task['start_date'] = datetime.strptime(task['start_date'], '%Y-%m-%d')
        task['end_date'] = datetime.strptime(task['end_date'], '%Y-%m-%d')
    tasks.sort(key=lambda x: x['start_date'])

    # Plot each task as a line
    fig, ax = plt.subplots(figsize=(10, len(tasks) / 2))
    for i, task in enumerate(tasks):
        ax.plot([task['start_date'], task['end_date']], [i, i], marker='o', label=f"Task {task['id']}")

    # Set labels and grid
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([f"Task {task['id']}" for task in tasks])
    ax.set_xlabel('Date')
    ax.grid(True)

    # Save the plot as a PNG file
    plt.savefig(output_path)
    plt.close()

def main():
    input_folder = r"G:\Git_2\demo_tasks_as_code\Sample_Project_Data"
    output_folder = input_folder  # Save the PNG files in the same folder

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.md'):
            file_path = os.path.join(input_folder, file_name)
            tasks = extract_tasks_from_md(file_path)
            output_path = os.path.join(output_folder, file_name.replace('.md', '.png'))
            plot_timeline(tasks, output_path)

    print(f"Generated timeline graphics for projects in '{output_folder}'")

if __name__ == "__main__":
    main()

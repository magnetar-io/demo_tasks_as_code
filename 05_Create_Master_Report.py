import os
import json
import re

def extract_tasks_with_documents(md_file_path):
    with open(md_file_path, 'r') as f:
        content = f.read()

    tasks_json = re.search(r'```json\n(.+?)\n```', content, re.DOTALL).group(1)
    tasks = json.loads(tasks_json)
    return [task for task in tasks if "Documents" in task.get("deliverables", [])]

def create_project_summary(folder_path, summary_file_path):
    all_document_tasks = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.md'):
            md_file_path = os.path.join(folder_path, file_name)
            document_tasks = extract_tasks_with_documents(md_file_path)
            all_document_tasks.extend(document_tasks)

    summary_content = "# Project Summary\n\n## Document Tasks\n\n"
    for task in all_document_tasks:
        summary_content += f"- Task ID: {task['id']}, Start Date: {task['start_date']}, End Date: {task['end_date']}, Description: {task['description']}\n"

    with open(summary_file_path, 'w') as f:
        f.write(summary_content)

def main():
    folder_path = r"G:\Git_2\demo_tasks_as_code\Sample_Project_Data"
    summary_file_path = os.path.join(folder_path, "Project_Summary.md")
    create_project_summary(folder_path, summary_file_path)
    print(f"Project summary saved to {summary_file_path}")

if __name__ == "__main__":
    main()

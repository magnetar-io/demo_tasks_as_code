import os
import json
import random
from datetime import datetime, timedelta

def generate_random_description():
    sentences = [
        "Complete the initial design sketches.",
        "Prepare the project presentation slides.",
        "Finalize the schematic design documents.",
        "Conduct a client review meeting.",
        "Update the construction drawings.",
        "Prepare the budget estimation report.",
        "Organize the design team meeting.",
        "Revise the project schedule.",
        "Submit the permit application.",
        "Coordinate with the engineering team."
    ]
    return random.choice(sentences)

def generate_random_deliverables():
    deliverables = [
        "Drawings",
        "Sketches",
        "Presentations",
        "Reports",
        "Documents",
        "Models",
        "Estimations",
        "Schedules",
        "Applications",
        "Plans"
    ]
    return random.sample(deliverables, random.randint(1, 3))

def generate_random_milestones():
    milestones = [
        "Client Presentation",
        "Schematic Design",
        "Design Development",
        "Construction Documents",
        "Permit Submission",
        "Bid Phase",
        "Construction Start",
        "Project Completion"
    ]
    return random.choice(milestones)

def generate_task(task_id):
    # Randomly generate a duration between 1 and 10 days
    duration = random.randint(1, 10)
    start_date = datetime.now() + timedelta(days=random.randint(1, 100))
    end_date = start_date + timedelta(days=duration)

    # Convert dates to string format
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    task = {
        "id": task_id,
        "start_date": start_date_str,
        "end_date": end_date_str,
        "description": generate_random_description(),
        "deliverables": generate_random_deliverables(),
        "milestone": generate_random_milestones(),
        "dependencies": []
    }
    return task

def generate_project(project_id, num_tasks):
    project = {"id": project_id, "tasks": []}
    for i in range(num_tasks):
        task = generate_task(i)
        # Randomly assign dependencies
        if i > 0:
            num_dependencies = random.randint(0, min(3, i))
            dependencies = random.sample(range(i), num_dependencies)
            task["dependencies"] = dependencies
        project["tasks"].append(task)
    return project

def main():
    output_folder = r"G:\Git_2\demo_tasks_as_code\Sample_Project_Data"
    os.makedirs(output_folder, exist_ok=True)

    num_projects = 500
    tasks_per_project = 100

    for i in range(num_projects):
        project = generate_project(i, tasks_per_project)
        file_path = os.path.join(output_folder, f"project_{i}.json")
        with open(file_path, 'w') as f:
            json.dump(project, f, indent=4)

    print(f"Generated {num_projects} project files with {tasks_per_project} tasks each in '{output_folder}'")

if __name__ == "__main__":
    main()

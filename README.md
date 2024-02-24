# Project Task Manager

This project provides a set of Python scripts to generate, visualize, and manage tasks in Markdown files for architectural projects. Each Markdown file represents a project and contains tasks with attributes such as start and end dates, descriptions, deliverables, and milestones. The project includes tools for generating sample project data, creating timeline graphics, inserting images into Markdown files, editing tasks through a simple graphical user interface (GUI), and generating a summary report of tasks with specific deliverables.

## Features

- **Generate Sample Projects** (\`01_Create_Tasks.py\`): Create sample project data with tasks, each having start and end dates, random dependencies, descriptions, deliverables, and milestones. The tasks are saved in Markdown files, with one file per project.
- **Generate Timeline Graphics** (\`02_Create_Timeline_Graphic.py\`): Generate a timeline graphic for each project, visualizing the tasks' start and end dates. The timeline graphics are saved as PNG files.
- **Insert Image into Markdown** (\`03_Insert_Image_into_MD.py\`): Insert the timeline graphics into the corresponding Markdown files, adding a visual representation of the tasks' timeline to each project file.
- **Edit Markdown Tasks with GUI** (\`04_Edit_Markdown_UI.py\`): A simple GUI tool that allows you to load a Markdown file, view and edit the tasks, and save the changes back to the file.
- **Create Master Report** (\`05_Create_Master_Report.py\`): Generate a summary report of all tasks with the "Documents" deliverable across all projects. The report is saved as a Markdown file.

## Demo Video

Here's a demo video showcasing the features of the Project Task Manager:

## Demo Video

[![Watch the video](https://i9.ytimg.com/vi/ugis3wjxtxE/mq2.jpg?sqp=CKDd6K4G-oaymwEmCMACELQB8quKqQMa8AEB-AHUBoAC4AOKAgwIABABGHIgNihEMA8%3D&rs=AOn4CLB0lyihDZvtFzHeqxqXooVHOXP0cg&retry=4)](https://youtu.be/ugis3wjxtxE)


## Installation

1. Clone the repository:
   \`\`\`
   git clone https://github.com/magnetar-io/demo_tasks_as_code.git
   \`\`\`

## Usage

1. **Generate Sample Projects**:
   \`\`\`
   python 01_Create_Tasks.py
   \`\`\`

2. **Generate Timeline Graphics**:
   \`\`\`
   python 02_Create_Timeline_Graphic.py
   \`\`\`

3. **Insert Image into Markdown**:
   \`\`\`
   python 03_Insert_Image_into_MD.py
   \`\`\`

4. **Edit Markdown Tasks with GUI**:
   \`\`\`
   python 04_Edit_Markdown_UI.py
   \`\`\`

5. **Create Master Report**:
   \`\`\`
   python 05_Create_Master_Report.py
   \`\`\`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

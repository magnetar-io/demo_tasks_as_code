import os

def insert_image_to_md(md_file_path, image_file_path):
    with open(md_file_path, 'r') as f:
        content = f.read()

    # Construct the image link using a relative path
    image_link = f"![Timeline]({os.path.basename(image_file_path)})"
    new_content = content + f"\n\n## Timeline\n\n{image_link}\n"

    with open(md_file_path, 'w') as f:
        f.write(new_content)

def main():
    folder_path = r"G:\Git_2\demo_tasks_as_code\Sample_Project_Data"

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.md'):
            md_file_path = os.path.join(folder_path, file_name)
            image_file_name = file_name.replace('.md', '.png')
            image_file_path = os.path.join(folder_path, image_file_name)

            if os.path.exists(image_file_path):
                insert_image_to_md(md_file_path, image_file_path)

    print(f"Inserted timeline images into Markdown files in '{folder_path}'")

if __name__ == "__main__":
    main()

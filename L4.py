import os

while True:
    file_path = input("Enter the path to the file: ")

    if not os.path.exists(file_path):
        print("File not found!")
        continue

    with open(file_path, 'r') as file:
        content = file.readlines()

    
    total_lines = len(content)
    empty_lines = content.count('\n')
    lines_with_a = sum('a' in line for line in content)
    a_count = sum(line.count('a') for line in content)
    lines_with_roads = sum('roads' in line for line in content)

    print(f"\nFile: {file_path}")
    print(f"total lines: {total_lines}")
    print(f"empty lines: {empty_lines}")
    print(f"lines with \"a\": {lines_with_a}")
    print(f"\"a\" count: {a_count}")
    print(f"lines with \"roads\": {lines_with_roads}")

    answer = input("Do you want to analyze another file? (y/n): ")
    if answer.lower() != 'y':
        break

def split_file_into_parts(filename, num_parts, thread_file_prefix):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    lines_per_part = total_lines // num_parts
    remainder = total_lines % num_parts

    start = 0
    for part in range(1, num_parts + 1):
        extra_line = 1 if part <= remainder else 0
        end = start + lines_per_part + extra_line

        part_filename = f'{thread_file_prefix}_{part}.txt'
        with open(part_filename, 'w') as part_file:
            part_file.writelines(lines[start:end])

        print(f'Created {part_filename} with lines {start + 1} to {end}')
        start = end

num_parts = input("How many files do you want to be created? ").strip()
num_parts = int(num_parts) if num_parts else 2

thread_file_prefix = input("What is your preferred list prefix?: ").strip()
if not thread_file_prefix:
    thread_file_prefix = "list_thread"

filename = input("What is your original file path to be seperated?: ").strip()
if not filename:
    filename = "list.txt"

try:
    split_file_into_parts(filename, num_parts, thread_file_prefix)
except NameError:
    print("An error has occurred:\n", NameError)
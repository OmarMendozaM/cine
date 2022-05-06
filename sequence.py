import os
import re
import sys

def print_sequences_ranges(user_path):
    render_files = []
    # Read files in the directory folder.
    for path, currentDirectory, files in os.walk(user_path):
        for file in files:
            render_files.append(os.path.join(path, file))
    render_files.sort()
    render_name, render_number, render_start, render_end = "", None, None, None
    output = []
    for i in render_files:
        # Skip invalid file name.
        if len(re.findall("\.",i)) < 2:
            continue
        render = i.split(".")
        # Next sequence.
        if render_name != render[0]:
            if render_name != "":
                render_end = render_number
                add_new_range(output, render_start, render_end, "")
                print(*output, sep = ' ')
                output = []
            render_name = render[0]
            render_start = render[1]
            output.append(render_name + ":")
        # Gap found.
        elif int(render[1]) != (int(render_number) + 1):
            render_end = render_number
            add_new_range(output, render_start, render_end, ",")
            render_start = render[1]
        # Last file in the directory.
        if i == render_files[-1]:
            render_end = render[1]
            add_new_range(output, render_start, render_end, "")
            print(*output, sep = ' ')
        render_number = render[1]

def add_new_range(output, start, end, separator):
    if start == end:
        output.append(start + separator)
    else:
        output.append(start + "-" + end + separator)

# The argument of the script is the directory where the sequences are.
print_sequences_ranges(str(sys.argv[1]))

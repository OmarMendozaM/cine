import os ,re, sys
from os import listdir
from os.path import isfile, join
mypath = str(sys.argv[1])
#mypath = "/Your/Sequence/Directory/Here"

def frame_ranges_print (user_path):
    renderfiles = []
    #Read files in the directory folder
    for path, currentDirectory, files in os.walk(user_path):
        for file in files:
            renderfiles.append(os.path.join(path, file))
    renderfiles.sort()
    render_name, render_number, render_start, render_end = "", None, None, None
    output = []
    for i in renderfiles:
        #Avoid non sequence files
        if (len(re.findall("\.",i))) < 2:
            continue
        render = i.split(".")
        #Change in Sequence
        if render_name != render[0]:
            if render_name != "":
                render_end = render_number
                add_new_range (output, render_start, render_end, "")
                print (*output, sep =' ')
                output= []
            render_name = render[0]
            render_start = render[1]
            output.append (render_name + ":")
        #Jump gaps, save ranges
        elif int(render[1]) != (int(render_number)+1):
            render_end = render_number
            add_new_range (output, render_start, render_end, ",")
            render_start = render[1]
        #Last file
        if i == renderfiles[-1]:
            render_end = render[1]
            add_new_range (output, render_start, render_end, "")
            print (*output, sep =' ')
        render_number = render[1]

def add_new_range (output, start, end, sepa):
    if start == end:
        output.append (start + sepa)
    else:
        output.append (start + "-" + end + sepa)

frame_ranges_print (mypath)


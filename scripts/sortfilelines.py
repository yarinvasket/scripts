import sys

def sort_lines(text):
    return "\n".join(sorted(text.splitlines(), key=str.lower))

if(len(sys.argv) < 2):
    print("You need to enter a file name for input and output.")
    exit()
file_in = open(sys.argv[1], "r")
file_out = open(sys.argv[2], "w")

file_out.write(sort_lines(file_in.read()))

file_in.close()
file_out.close()

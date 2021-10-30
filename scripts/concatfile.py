import sys
if(len(sys.argv) < 3):
	exit()
out = open(sys.argv[3], "a+")
file1 = open(sys.argv[1],"r+")
file2 = open(sys.argv[2], "r+")
out.write(file1.read())
file1.close()
out.write(file2.read())
file2.close()
out.close()

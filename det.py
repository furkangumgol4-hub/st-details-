import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("user provided inp values:")
else:
    script_name = sys.argv[0]
    name = "gustavo"
    rollno = "99"
    print("no inp given - using default values:")

print("Script Name:", script_name)
print("Student Name:", name)
print("Roll No.:", rollno)

import Lib.talkback as talkback
import Lib.studentdb as studentdb
try:
    while True:
        student_id=input("PleaseEnter The StudentId:")
        student_name,student_univ = studentdb.findnm(student_id)
        talkback.TTstudnm(student_name)
finally:
    print("Code Completed")

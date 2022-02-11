class Solution(object):
    def countStudents(self, students, sandwiches):
        flag=True
        count=0
        while len(sandwiches)>0:
            if students[0]==sandwiches[0]:
                students=students[1:]
                sandwiches=sandwiches[1:]
                count=0
            else:
                students=students[1:]+[students[0]]
                count+=1
                if count==len(students):
                    flag=False
                    break
        if flag==True:
            return 0
        return len(students)
        
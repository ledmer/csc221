import random
global students
global groups
groups = []
students = {
    "1":["a","b","c","d","e","f","g","h","i","j","k","l","m","n"],
    "2":["aa","bb","cc","dd","ee","ff","gg"],
    "3":["11","22","33","44","55"],
    "4":["CC","DD","AA"],
    "5":["Z"]
}

def Values():
    ns = 0
    for school in students:
        for student in students[school]:
            ns += 1
    ng = int(input("how many groups do you want? "))
    while ng <= 1 or ng > ns:
        print(f"it has to be greater than 1 and less than {ns}")
        ng = int(input("how many groups do you want?"))

    sxg = int(ns/ng)
    res = ns%ng
    return ns, sxg, ng, res

def form_groups(sxg):
    for school in students.items():
        for x in range(int(len(students[school[0]])/sxg)):
            list = []
            for i in range(sxg):
                rn = random.randrange(len(students[school[0]]))
                list.append(students[school[0]][rn])
                students[school[0]].pop(rn)
            groups.append(list)

#def rest(res):
#    rests = []
 #   for school in students.items():
  #      if len(students[school[0]]) > 0:
   #        rests.append(school[1])
    #for i in range(len(rests)):
     #   for k = j + 1; k < count;
      #      if (number[j] > number[k])
       #         temp = number[j];
        #        number[j] = number[k];
         #       number[k] = temp;
    #print(rests)

        

            

ns, sxg, ng, res = Values()
form_groups(sxg)
print(groups)
print(ns, sxg, ng, res)
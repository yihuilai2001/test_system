#7 10 11 15 17 


import csv
import random
import sys
import os
filename= input("Enter fileName(.csv):")
if os.path.isfile(filename)==False:
    print("File not exit!")
    input("Press anykey to leave.")
with open(filename, newline='',encoding="utf-8") as csvfile:
    
  # 讀取 CSV 檔案內容
  lists = list(csv.reader(csvfile))
  row_count =len(lists)

randomlist = list(range(row_count))
random.shuffle(randomlist)
answer = 0
count = 0
index = -1
notcorlist = []
while(index<row_count):
    index+=1
    ran = randomlist[index]
    if(lists[ran][5]==""):
       continue

    count = count+1    
    print("\nQuestion " ,count,"\n")
    print(lists[ran][1]+"?\n")
    
    print("1. "+lists[ran][2]+"\n")
    print("2. "+lists[ran][3]+"\n")
    print("3. "+lists[ran][4]+"\n")
    answer = input("your answer: ")
    print()
    
    
    if(lists[ran][5]==answer):
        print("Good \n")

    elif(lists[ran][5]!=answer):
        print("No ahhh\nThe anwer is "+lists[ran][5])
        notcorlist.append(ran)
        if(lists[ran][6]!="" ):
            print(lists[ran][6])

    con = input("Continue?")
    if (con=="n"):
        break
    else:
        print("\n")
        continue
print("\n\n----------Review Time ----------")
input()
i=0
for num in notcorlist:
    i+=1
    print(i,". ",lists[num][1],"\n")
    print("1. ",lists[num][2])
    print("2. ",lists[num][3])
    print("3. ",lists[num][4])
    print("\nThe answer is ",lists[num][5],"\n")
    if(lists[num][6]!=""):
        print("From ",lists[num][6],"\n")
    input()
print("\nFinish!")

input("Press any key to leave")

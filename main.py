import os,random
from queue import Queue
from time import sleep
questionno = 0
def main():
    level1questions = []
    level2questions = []
    level3questions = []
    l1asked = []
    l2asked = []
    l3asked = []
    price = [0,500,1000,2000,3000,5000,7500,10000,15000,25000,50000,75000,150000,250000,500000,1000000]

    def initilizing():
        f = open("level1.txt","r",encoding='latin-1')
        templines = f.readlines()
        
        for line in templines:
            myline = line.strip()
            level1questions.append(myline)
            
        f = open("level2.txt","r")
        templines = f.readlines()
        for line in templines:
            myline = line.strip()
            level2questions.append(myline)
            
        f = open("level3.txt","r")
        templines = f.readlines()
        for line in templines:
            myline = line.strip()
            level3questions.append(myline)
                   
           
    def welcomescreen():
        os.system('cls')
        print(f"WELCOME TO WHO WILL BE MILLIONAIRE, {username}")
        sleep(2)
        os.system('cls')

    def askquestion():
        global questionno
        questionno = questionno + 1

        def getquestion(level):
            def getanswer(correctans):
                ans = str(input("\nEnter the choice: "))
                ans = ans.upper()
                if ans == "1":
                   ans = "A"
                elif ans == "2":
                   ans = "B"
                elif ans == "3":
                   ans = "C"
                elif ans == "4":
                   ans = "D"          
                if correctans == ans:
                    print("CORRECT ANSWER!\n")
                    sleep(2)
                    os.system('cls')
                else:
                    print("WRONG ANSWER!\nCorrect Answer is" ,correctans)
                    print("\nYou won: $", price[questionno-1])
                    sleep(10)
                    quit()   
            def randquestionno(num):
                    max = maxcount/5
                    randonum = random.randint(1,max)
                    if num == 1:
                        if randonum in l1asked:
                            randquestionno(1)
                    elif num == 2:
                        if randonum in l2asked:
                            randquestionno(2)
                    elif num == 3:
                        if randonum in l3asked:
                            randquestionno(3)        
                    return randonum
            if level == 1:
                maxcount = len(level1questions)
                randomnum = randquestionno(1)    
                l1asked.append(randomnum)
                counter = 0
                index = -1
                ansis = ''
                for line in level1questions:
                    index+=1
                    if line[:2] == "Q~":
                        counter+=1
                    if counter == randomnum:
                        if line[-1] == '1':
                            ansis = 'A'
                        elif line[-1] == '2':
                            ansis = 'B'
                        elif line[-1] == '3':
                            ansis = 'C'
                        elif line[-1] == '4':
                            ansis = 'D'           
                        line = line.rstrip('1234')
                        print(ansis)
                        line.replace
                        print("\n\n\n\n\n\t",line,"\t\tCurrent Price: ",price[questionno-1],"\n")
                
                        q = Queue(maxsize=4)
                        q.put('A')
                        q.put('B')
                        q.put('C')
                        q.put('D')
                        for i in range(index+1,index+5):
                            print(" ",end='')

                            print("\n /",end='')

                            for _ in range(level1questions[i].__len__()+4):
                                print("`",end='')
                            print("\\")
                            print("| ",end='')
                            print(q.get(),end='')
                            print(")",level1questions[i], " |")
                            print(" \\",end='')
                            for _ in range(level1questions[i].__len__()+4):
                                print("_",end='')
                            print("/\n  ",end='')
                       


                            # print("    ``````````````````")
                            # print(" /                   \ ")
                            # print("|  ",q.get(),level1questions[i] , "      |")
                            # print(" \                   /")
                            # print("    ___________________")

                        getanswer(ansis)
                        break
            if level == 2:
                maxcount = len(level2questions)
                randomnum = randquestionno(2)    
                l2asked.append(randomnum)
                counter = 0
                index = -1
                ansis = ''
                for line in level2questions:
                    index+=1
                    if line[:2] == "Q~":
                        counter+=1
                    if counter == randomnum:
                        if line[-1] == '1':
                            ansis = 'A'
                        elif line[-1] == '2':
                            ansis = 'B'
                        elif line[-1] == '3':
                            ansis = 'C'
                        elif line[-1] == '4':
                            ansis = 'D'           
                        line = line.rstrip('1234')
                        print(ansis)
                        print("\n\n\n\n\n\t",line,"\t\tCurrent Price: ",price[questionno-1],"\n")
                
                        q = Queue(maxsize=4)
                        q.put('A')
                        q.put('B')
                        q.put('C')
                        q.put('D')
                        for i in range(index+1,index+5):
                            print(" ",end='')

                            print("\n /",end='')

                            for _ in range(level2questions[i].__len__()+4):
                                print("`",end='')
                            print("\\")
                            print("| ",end='')
                            print(q.get(),end='')
                            print(")",level2questions[i], " |")
                            print(" \\",end='')
                            for _ in range(level2questions[i].__len__()+4):
                                print("_",end='')
                            print("/\n  ",end='')
                       

                        getanswer(ansis)
                        break
            if level == 3:
                maxcount = len(level3questions)
                            
                randomnum = randquestionno(3)    
                l3asked.append(randomnum)
                counter = 0
                index = -1
                ansis = ''
                for line in level3questions:
                    index+=1
                    if line[:2] == "Q~":
                        counter+=1
                    if counter == randomnum:
                        if line[-1] == '1':
                            ansis = 'A'
                        elif line[-1] == '2':
                            ansis = 'B'
                        elif line[-1] == '3':
                            ansis = 'C'
                        elif line[-1] == '4':
                            ansis = 'D'           
                        line = line.rstrip('1234')
                        print(ansis)
                        print("\n\n\n\n\n\t",line,"\t\tCurrent Price won: ",price[questionno-1],"\n")
                
                        q = Queue(maxsize=4)
                        q.put('A')
                        q.put('B')
                        q.put('C')
                        q.put('D')
                        for i in range(index+1,index+5):
                            print(" ",end='')

                            print("\n /",end='')

                            for _ in range(level3questions[i].__len__()+4):
                                print("`",end='')
                            print("\\")
                            print("| ",end='')
                            print(q.get(),end='')
                            print(")",level3questions[i], " |")
                            print(" \\",end='')
                            for _ in range(level3questions[i].__len__()+4):
                                print("_",end='')
                            print("/\n  ",end='')
                

                        getanswer(ansis)
                        break                


        if questionno <= 5:
            getquestion(1)
        elif questionno <= 9:
            getquestion(2)
        elif questionno <= 15:
            getquestion(3)   
       
                  




    username = str(input("Enter your name: "))
    initilizing()
    welcomescreen()
    for _ in range(1,15):
        askquestion()
    print("Congratulations !!! You're a Millionaire.")  
    sleep(10)     
if __name__ == "__main__":
    main()
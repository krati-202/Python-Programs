def getdate():
    import datetime
    return str(datetime.datetime.now())
def take(k):
    if k==1:
        c = int(input("Choose the option:-\n1.food\n2.exercise"))
        if c==1:
            data = input('Enter food name:-\n')
            with open("harry_food.txt","a") as f:
                f.write(getdate()+"\t"+data+"\n")
            print("data written successfully.")
        elif c==2:
            data = input("Enter exercise:-\n")
            with open("harry_ex.txt","a") as f:
                f.write(getdate()+"\t"+data+"\n")
            print("data written successfully.")
    elif k==2:
        c = int(input("Choose the option:-\n1.food\n2.exercise"))
        if c==1:
            data = input('Enter food name:-\n')
            with open("rohan_food.txt","a") as f:
                f.write(getdate()+"\t"+data+"\n")
            print("data written successfully.")
        elif c==2:
            data = input("Enter exercise:-\n")
            with open("rohan_ex.txt","a") as f:
                f.write(getdate()+"\t"+data+"\n")
            print("data written successfully.")
    elif k==3:
        c = int(input("Choose the option:-\n1.food\n2.exercise"))
        if c==1:
            data = input('Enter food name:-\n')
            with open("hammad_food.txt","a") as f:
                f.write(getdate()+"\t"+data+"\n")
            print("data written successfully.")
        elif c==2:
            data = input("Enter exercise:-\n")
            with open("hammad_ex.txt","a") as f:
                f.write(getdate()+"\t"+data+"\n")
            print("data written successfully.")
def display(r):
    if r==1:
        c = int(input("Choose the option:-\n1.food\n2.exercise"))
        if c==1:
            with open("harry_food.txt") as f:
                for i in f:
                    print(i,end="")
        elif c==2:
            with open("harry_ex.txt") as f:
                for i in f:
                    print(i,end="")
    elif r==2:
        c = int(input("Choose the option:-\n1.food\n2.exercise"))
        if c==1:
            with open("rohan_food.txt") as f:
                for i in f:
                    print(i,end="")
        elif c==2:
            with open("rohan_ex.txt") as f:
                for i in f:
                    print(i,end="")
    elif r==3:
        c = int(input("Choose the option:-\n1.food\n2.exercise"))
        if c==1:
            with open("hammad_food.txt") as f:
                for i in f:
                    print(i,end="")
        elif c==2:
            with open("hammad_ex.txt") as f:
                for i in f:
                    print(i,end="")

a = int(input("Choose the option:-\n1.Log\n2.Retrieve\n"))
b = int(input("Choose the option:-\n1.Harry\n2.Rohan\n3.Hammad\n"))

if a==1:
    take(b)
elif a==2:
    display(b)








#CREATED BY ISHANT MEHNDIRATTA 2023 (STD- XI)

import pickle

#create a file named data1.dat and data2.dat
#data1 stores the data i.e. name of countries and data2 stores search history

file=open( "data1.dat" ,"rb") #data  file
file2=open("data2.dat" ,"rb") #history file
l1=pickle.load(file)
l2=pickle.load(file2) #search history
print("welcome to my database of Countries")
true=True
while(true):
    print("enter the purpose of your visit?")
    a=(input("1 for search. 2 to view search history. 3 to view all the data. 4 to exit - "))
    if(a=="1"):
        b=str(input("enter country to be searched- ")).title()
        l2.append(b)
        if(b in l1):
            ind = l1.index(b)
            print(b,"found at", ind)
            print("do u wanna delete this?")
            c=str(input("y or n - "))
            if(c=="y"):
                l1.remove(b)
                print("DONE")
            else:
                print(" ")
        else:
            print("404: not found")
            print("do u wanna  add this?")
            d=str(input("y or n - "))
            if(d=="y"):
                l1.append(b)
                print("done")
            else:
                print(" ")    
    elif(a=="2"):   
        print(l2)
        print("do u wanna clear search history?")
        e=str(input("y or n - "))
        if(e=="y"):
            l2.clear()
        else:
            print(" ")    
    elif(a=="3"):
        print(l1)
    elif(a=="4"):
        true=False
    else:
        print("invalide input")             
file.close()
file=open("data1.dat" ,"wb")
pickle.dump(l1, file)
file.close()
file2=open("data2.dat" ,"wb")
pickle.dump(l2, file2)
file.close()
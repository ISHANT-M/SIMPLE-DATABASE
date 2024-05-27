import pickle

l1=[]

p=open("data2.dat","wb") #replace data2.dat with data1.dat and run again

pickle.dump(l1,p)

p.close()


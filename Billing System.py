def menu():
    
    print("Sl no.\tItem\t\t\tRate\n\n1.\tbiriyani\t\t520\n2.\tmomo\t\t\t350\n3.\tchow mein\t\t400\n4.\tpulao\t\t\t500\n5.\tice cream\t\t200")
    print("\nif you want to order press 1 \nif you dont want to order press 0\n")
    a=int(input())
    if a==1:
        
        i=1
        a=[]
        b=[]
        while(i==1):
                                        
            a.append(int(input("select iten number\n")))
            b.append(int(input("quantity\n")))
            i=int(input("if you want more press 1 \n if you dont want more press 0\n"))
          
        bill(a,b)
        
        
    else:
        print("thank you for coming\n")

  
            
    
def bill(a,b):
    sum=0
    c=[]
    for i in range(len(a)):
        if a[i]==1:
            c.append(520)
           
        elif a[i]==2:
            c.append(350)
            
        elif a[i]==3:
            c.append(400)
           
        elif a[i]==4:
            c.append(500)
          
        elif a[i]==5:
            c.append(200)
            
   
    for i in range(len(a)):
        sum=sum+c[i]*b[i]
    print("\n\nSIR, YOUR TOTAL AMOUNT IS:\n",sum)
    v=int(input("if you want to order press 1 \nand if you dont want to order press 0\n"))
    if v==0:
        print("thank you\n")
    else:
        print("wait for a few minutes\n")
    
print("\nWELL COME TO HAUNTED RESTAURANTS\n")
x=int(input("for menu press 1\n"))
if x==1:
    menu()
    
    



            
        
    
    
    

        
    
        
        

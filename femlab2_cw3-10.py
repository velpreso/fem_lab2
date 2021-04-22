import numpy as np
#Cwiczenie 3
print("cwiczenie 3")
tab1=np.linspace(1,5,5) #1 2 3 4 5
tab2=np.linspace(5,1,5) #5 4 3 2 1
tab3=np.linspace(0,0,2) #0 0
tab4=np.linspace(2,2,3) #2 2 2
tab5=np.linspace(-90,-70,3) #-90 -80 -70
tab6=0 
tab7=np.array([[0,0,0,0,0,10],
              [0,0,0,0,0,10],
              [0,0,0,0,0,10],
              [0,0,0,0,0,10],
              [0,0,0,0,0,10],])
A=(np.block([[tab1,tab6],
            [tab2,tab6],
            [tab3,tab4,tab6],
            [tab3,tab4,tab6],
            [tab3,tab5,tab6]])+tab7)
print("A =",A)
print("....................")

#Cwiczenie 4
print("cwiczenie 4")
row2=np.array(A[1,:])
row4=np.array(A[3,:])
B=(row2+row4)
print("B =",B)
print("....................")

#Cwiczenie 5
print("cwiczenie 5")
C=np.max(A,0)
print("C =",C)
print("....................")

#Cwiczenie 6
print("cwiczenie 6")
D=np.delete(B,0,0)
D=np.delete(D,4,0)
print("D =",D)
print("....................")

#Cwiczenie 7
print("cwiczenie 7")
for i in range(4):
    if D[i] == 4: 
        D[i]=0;
print("D =",D)
print("....................")

#Cwiczenie 8
print("cwiczenie 8")
C_max=np.max(C)
C_min=np.min(C)
for i in range(6):
    if C[i] == C_max: 
        E=np.delete(C,i);
        break
for i in range(5):  
    if E[i] == C_min:
        E=np.delete(E,i);
        break
print("E =",E)
print("....................")

#Cwiczenie 9
print("cwiczenie 9")
A_max=(np.max(A))
A_min=(np.min(A))    
for i in range(5):
    for j in range(6):
        if A[i,j]==A_max:
            print("Max ",A_max," in raw:",i,A[i,:]);
        elif A[i,j]==A_min:
            print("Min ",A_min," in raw:",i,A[i,:]);
print("....................")

#Cwiczenie 10
print("cwiczenie 10")   
MT1=D*E;
MT2=E*D;
MW1=D@E;
MW2=E@D;
print("Mnozenie tablicowe 1:",MT1)
print("Mnozenie tablicowe 2:",MT2)
print("Mnozenie wektorowe 1:",MW1)
print("Mnozenie wektorowe 2:",MW2)
print("....................")
  
     
            

   


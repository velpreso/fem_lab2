import numpy as np
#ćwiczenie 3
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

#ćwiczenie 4
print("cwiczenie 4")
row2=np.array(A[1,:])
row4=np.array(A[3,:])
B=(row2+row4)
print("B =",B)
print("....................")

#ćwiczenie 5
print("cwiczenie 5")
C=np.max(A,0)
print("C =",C)
print("....................")

#ćwiczenie 6
print("cwiczenie 6")
D=np.delete(B,0,0)
D=np.delete(D,4,0)
print("D =",D)
print("....................")

#ćwiczenie 7
print("cwiczenie 7")
for i in range(4):
    if D[i] == 4: 
        D[i]=0;
print("D =",D)
print("....................")

#ćwiczenie 8
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

#ćwiczenie 9
print("cwiczenie 9")
A_max=(np.max(A))
A_min=(np.min(A))    
print(A_max)
print(A_min)
#nie wiem jak to zrobić 

   


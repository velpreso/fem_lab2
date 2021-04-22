def fun_cw11():
    import numpy as np
    s = 0;
    size = np.random.randint(10);
    tab = np.zeros((size,size));
    for i in range(size):
        for j in range(size):
            tab[i,j] = np.random.randint(10);
            if i == j:
                s = s+tab[i,j];
            if j == size-1: 
                s = s+tab[i,j-i];
    if size%2.0 != 0:
        s = s - tab[round(size/2),round(size/2)];
        
    print("Rozmiar: ",size)
    print("Suma: ",s)
    print("....................")
    print(tab);
    print("....................")
    return tab;
    
fun_cw11(); # wywolanie testowe funkcji
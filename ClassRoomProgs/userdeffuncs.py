def fun_tup(T):
    L=[40,50]
    for i in range(0,2):
        T+=(L[i],)
    print(id(T),T)

T=(10,20,30)
print(id(T),T)
fun_tup(T)
print(id(T),T)

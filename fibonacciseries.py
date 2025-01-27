def fibonacci(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
        a,b = b,a+b
        print(b,end=" ")
    return 0
    
def main():
    n=int(input("how many numbers are required: "))
    fibonacci(n)
main()
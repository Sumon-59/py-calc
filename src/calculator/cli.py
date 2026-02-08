from calculator.core import add, sub, mul, div

def main():
    print("===Simple Calculator===")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number "))

    op = input("Operation (+ - * /): ")

    if op =="+":
        print("Result: ",add(a,b))
    
    elif op =="-":
        print("Result: ",sub(a,b))
    
    elif op =="*":
        print("Result: ",mul(a,b))
    
    elif op =="/":
        print("Result: ",div(a,b))
    
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
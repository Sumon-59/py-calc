from calculator.core import add, sub, mul, div
from calculator.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("Calculator started")
    
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number "))
        
        op = input("Operation (+ - * /): ").strip()

        logger.debug("Inputs: a=%s b=%s op=%s",a, b, op)
        
        if op =="+":
            result = add(a,b)
    
        elif op =="-":
            result = sub(a,b)
    
        elif op =="*":
            result = mul(a,b)
        
        elif op =="/":
            result = div(a,b)
        else:
            print("Invalid operation")
            logger.warning("Invalid operation entered: %s", op)
            return
        print("Result:",result)
        logger.info("Success result=%s",result)
    
    except ValueError as e:
        print("Error:",e)
        logger.exception("ValueError happened")

    except Exception:
        print("Unexpected error occurred.")
        logger.exception("Unexpected error")

if __name__ == "__main__":
    main()
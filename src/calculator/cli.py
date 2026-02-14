import os
import requests

from calculator.core import add, sub, mul, div
from calculator.logger import setup_logger


def calculate_local(a: float, b: float, op: str) -> float:
    """Local calculation using core functions"""
    if op == "+":
        return add(a, b)
    if op == "-":
        return sub(a, b)
    if op == "*":
        return mul(a, b)
    if op == "/":
        return div(a, b)
    raise ValueError("Invalid operation.Use + - * /")


def calculate_via_api(a: float, b: float, op: str, api_url: str) -> float:
    """Call Calculator API and return result."""
    r = requests.post(f"{api_url}/calc", json={"a": a, "b": b, "op": op}, timeout=10)
    if r.status_code != 200:
        raise ValueError(f"API error: {r.text}")
    return float(r.json()["result"])


def main():
    logger = setup_logger()
    logger.info("Calculator started")

    use_api = os.getenv("USE_API", "0") == "1"
    api_url = os.getenv("API_URL", "http://127.0.0.1:8000")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number "))
        op = input("Operation (+ - * /): ").strip()

        logger.debug("Inputs: a=%s b=%s op=%s use_api=%s", a, b, op, use_api)

        if use_api:
            result = calculate_via_api(a, b, op, api_url)
        else:
            result = calculate_local(a, b, op)

        print("Result:", result)
        logger.info("Success result=%s", result)

    except ValueError as e:
        print("Error:", e)
        logger.exception("ValueError happened")

    except Exception:
        print("Unexpected error occurred.")
        logger.exception("Unexpected error")


if __name__ == "__main__":
    main()

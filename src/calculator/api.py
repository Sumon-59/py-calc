"""
Calculator API (FastAPI)

Run:
  PYTHONPATH=src uvicorn calculator.api:app --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from calculator.core import add, sub, mul, div

app = FastAPI(title="Calculator API", version="1.0.0")


class CalcRequest(BaseModel):
    """Request model for calculator input."""
    a: float
    b: float
    op: str


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/calc")
def calc(req: CalcRequest):
    """
    Calculate based on operator.

    Example request JSON:
      {"a": 2, "b": 5, "op": "*"}

    Example response JSON:
      {"result": 10.0}
    """
    op = req.op.strip()

    try:
        if op == "+":
            return {"result": add(req.a, req.b)}
        if op == "-":
            return {"result": sub(req.a, req.b)}
        if op == "*":
            return {"result": mul(req.a, req.b)}
        if op == "/":
            return {"result": div(req.a, req.b)}
    except ValueError as e:
        # divide by zero -> ValueError -> HTTP 400
        raise HTTPException(status_code=400, detail=str(e))

    raise HTTPException(status_code=400, detail="Invalid operation. Use + - * /")
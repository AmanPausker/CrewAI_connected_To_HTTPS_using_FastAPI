#this is api.py
from fastapi import FastAPI
from pydantic import BaseModel
from src.query.crew import Query


app = FastAPI(
    title="CrewAI Query API",
    description="An API interface to your CrewAI-powered------system",
    version="1.0.0"
)

# Define the request body
class QueryInput(BaseModel):
    query: str

@app.post("/run-query")
def run_query(input: QueryInput):
    """
    Run the CrewAI Query crew with the given text input.
    """
    try:
        result = Query().crew().kickoff(inputs={"query": input.query})
        return {"status": "success", "result": result.raw}
    except Exception as e:
        return {"status": "error", "message": str(e)}

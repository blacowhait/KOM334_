from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from classes import HistoryA
from database import Base, engine
from schema import HistoryCreate, HistoryType, HistoryUpdate

app = FastAPI()

Base.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/history")
async def read_all_history(sortBy: str, groupByType: bool, count: int = 15):
    # recap query
    #   count(def=15), sortBy:desc/asc, groupByType:bool
    # if (groupByType):
    #   fetch historyA
    #   fetch historyB
    #   fetch historyC
    #   return {"historyA" : historyA, "historyB" : historyB, "historyC" : historyC}
    return {"Key": "Value"}


@app.get("/history/{history_id}")
async def read_history(history_id: int):
    # fetch & return history
    return {"Key": "Value"}


@app.post("/history")
async def create_history(request: HistoryCreate):
    if request.history_type == HistoryType.history_a:
        print(request)
        history = HistoryA(obj=request)
    elif request.history_type == HistoryType.history_b:
        print(HistoryType.history_b)
    elif request.history_type == HistoryType.history_c:
        print(HistoryType.history_c)
    return request


@app.put("/history/{history_id}")
async def update_history(history_id: int, request: HistoryUpdate):
    # fetch history from id
    # assign request to database object
    # save database object to database
    # return database object
    return {"Key": "Value"}


@app.delete("/history/{history_id}")
async def delete_history(history_id: int):
    # fetch history from id
    # delete database object from database
    # return database object
    return {"Key": "Value"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

price = {
    "BTC": 10000,
    "ETH": 10000,
}

@app.get('/')
def index():
    return {"Информация":"Наспех написанный API"}

@app.get('/data/price')
def index(fsym, tsyms):
    if (tsyms != "USD"):
        return {"Error":"Ты говорил, что запросы только с USD"}
    if (not (fsym in price)):
        random_value = round(random.uniform(0.5, 1.5), 3)
        return {f"{fsym}":random_value}
    if (fsym in price):
        random_par = round(random.uniform(0.9, 1.1), 3)
        price[fsym] = (round(price[fsym] * random_par * 100)) / 100
        return {f"{fsym}":price[fsym]}
    return {"Error":"ошибка"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='192.168.0.6', port=8000)
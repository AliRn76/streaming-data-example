import csv
import codecs
import json
from time import sleep
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse


app = FastAPI()

FILENAME = 'PS_20174392719_1491204439457_log.csv'


async def read_csv(request: Request):
    with codecs.open(FILENAME, 'r', 'utf-8') as fp:
        reader = csv.reader(fp)
        for row in reader:
            if await request.is_disconnected():
                break
            res = json.dumps(row)
            sleep(1)
            print(res)
            yield res


@app.get('/')
async def usage(request:  Request):
    return StreamingResponse(read_csv(request))

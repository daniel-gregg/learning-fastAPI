## working on query and path parametrs

from fastapi import FastAPI

app = FastAPI()

# run local server:
#http://127.0.0.1:8000

# path parameters are in the '@app.get()' definition
# query parameters are in the function definition

## path only:
@app.get("/path_only_item/{item_id}")
async def read_user_item(item_id):
    message = {"item_id" : item_id}
    return message
# note that we also need to include the 'item_id' in the function variables space
# BUT that it is defined in the path and must be supplied from that
# put this path in the browser to see the (success) response:
#http://127.0.0.1:8000/path_only_item/123


@app.get("/query_only_item/")
async def get_item(item):
    message = {"item_name" : item}
    return message
#putting this path into the browser 
#http://127.0.0.1:8000/query_only_item/?item=123

#note the differences above

## combined path and query params
fake_items_db = {
    "a":{
        "item_name": "aFoo", 
        "item_name": "aBar", 
        "item_name": "aBaz"
        },
    "a":{
        "item_name": "bFoo", 
        "item_name": "bBar", 
        "item_name": "bBaz"
        },
    "a":{
        "item_name": "cFoo", 
        "item_name": "cBar", 
        "item_name": "cBaz"
        },
}

@app.get("/path_and_query_item/{item_category: str}/")
async def get_item(item_category, item_id: int):
    item = fake_items_db[item_category].values[item_id-1]
    message = {"item category": item_category, "item_name" : item_id}
    return message

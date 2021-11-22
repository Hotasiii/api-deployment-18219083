import json
from fastapi import FastAPI, HTTPException, Body, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

with open("Feedback.json", "r") as read_file:
    Feedback = json.load(read_file)

app = FastAPI()

@app.get('/')
def root():
    return{'Menu' : 'Feedback'}

@app.get('/feedback')
async def read_all_feedback():
    return Feedback

@app.get('/feedback/{feedback_id}') 
async def read_feedback(item_id: int): 
    for feedback_item in Feedback['Feedback']:
        if feedback_item['feedback_id'] == item_id:
            return feedback_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

@app.post('/feedback')
async def post_feedback(description:str):
    id = 1
    if(len(Feedback["Feedback"]) > 0):
        id = Feedback["Feedback"][len(Feedback["Feedback"]) - 1]["feedback_id"] + 1
    new_data = {'feedback_id':id, 'description':description}
    Feedback['Feedback'].append(dict(new_data))
    read_file.close()
    
    with open("Feedback.json", "w") as write_file: 
        json.dump(Feedback,write_file, indent=4)
    write_file.close()

    return (new_data)
    raise HTTPException(
        status_code=500, detail=f'Internal Server Error'
        )
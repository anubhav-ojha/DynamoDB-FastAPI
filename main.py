from fastapi import FastAPI
import boto3
import uvicorn

app = FastAPI()

dynamodb = boto3.client('dynamodb', region_name = 'ap-south-1')

@app.get("/data/{id}")
def get_student_data(id: str):
    response = dynamodb.get_item(
        TableName = 'student_data',
        Key = {
            'id': {'S': id}
        }
    )
    item = response.get('Item')
    if item is None:
        return {"message": "Item not found"}
    return item

if __name__ == "__main__":
    

    uvicorn.run(app, host="0.0.0.0", port=8000)

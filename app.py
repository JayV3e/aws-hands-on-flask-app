from flask import Flask, jsonify, request
from flask_cors import cross_origin
from datetime import date
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table('Thankful')

@app.route("/health")
def health():
    return jsonify({'status': 'ok'})

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def all_thankfuls():
    response_object = {'status': 'success'}
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
        
    if request.method == 'POST':
        post_data = request.get_json()
        table.put_item(Item={
            'Author': post_data.get('author'),
            'Thankful': post_data.get('thankful'),
            'Date': date.today().strftime("%d/%m/%Y"),
        })
        response_object['message'] = 'Thankful added!'
    else:
        response_object['thankful'] = data
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
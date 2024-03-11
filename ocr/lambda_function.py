from flask import Flask, request, jsonify
import awsgi
from common.OCRServiceFactory import OCRServiceFactory
import json

import traceback

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_document():
    try:
        # Get the file from the request
        file = request.files['file']
        document_type = request.form.get('documentType')
        file_content = file.read()
        service_to_call = OCRServiceFactory().create_OCR_service(document_type)
        data = service_to_call.analyze_document(data=file_content)
        return jsonify(data.__dict__),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sayHello', methods=['GET'])
def sayHello():
    try:
      
        return jsonify({'say': 'hi'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500
    
def lambda_handler(event, context):
    return awsgi.response(app, event, context)

if __name__ == '__main__':
    lambda_function.run(debug=True)
from flask import Flask
from flask import jsonify, request
from flask.ext.api import status

from discoteque.actions.retrieve_records import RetrieveRecords
from discoteque.infrastructure.records_repo import RecordsRepository

app = Flask(__name__)


@app.route('/records', methods=['GET'])
def root():
    result = RetrieveRecords(RecordsRepository()).execute()
    return jsonify(result)

@app.route('/record', methods=['POST'])
def add_record():
    result = RetrieveRecords(RecordsRepository()).execute()
    return jsonify(result), status.HTTP_201_CREATED


if __name__ == '__main__':
    app.run()

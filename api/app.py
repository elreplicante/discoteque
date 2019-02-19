from flask import Flask
from flask import jsonify, request
from flask_api import status

from app.discoteque import RetrieveRecords
from app.discoteque.actions.add_record import AddRecord
from app.discoteque.domain.records import RecordService
from app.discoteque import RecordsRepository

app = Flask(__name__)


@app.route('/records', methods=['GET'])
def root():
    action = RetrieveRecords(RecordsRepository())
    result = action.execute()

    return jsonify(result)

@app.route('/record', methods=['POST'])
def add_record():
    record_service = RecordService(RecordsRepository())
    action = AddRecord(record_service)
    result = action.execute(request.args)

    return jsonify(result), status.HTTP_201_CREATED


if __name__ == '__main__':
    app.run()

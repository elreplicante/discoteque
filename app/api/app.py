from flask import Flask
from flask import jsonify, request

from app.discoteque.actions.add_record import AddRecord
from app.discoteque.actions.retrieve_records import RetrieveRecords
from app.discoteque.domain.records.record_service import RecordService
from app.discoteque.infrastructure.records_repo import RecordsRepository

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

    return jsonify(result), 201


if __name__ == '__main__':
    app.run()

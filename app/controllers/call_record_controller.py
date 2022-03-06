from http import HTTPStatus
from flask import jsonify, request
from app.configs.database import db
from sqlalchemy.orm.session import Session
from app.models.call_record_model import CallRecord


def create_record():
    # coletar os dados da requisição
    data = request.get_json()
    record = CallRecord(**data)
    db.session.add(record)
    db.session.commit()

    return jsonify(record), HTTPStatus.CREATED
    # return record.serializer(), HTTPStatus.CREATED

def get_record_by_id(call_recorder_id:int):
    session: Session = db.session
    record = session.query(CallRecord).filter(CallRecord.id == call_recorder_id).first()
    print(record)
    return jsonify(record)


def get_records():
    records = CallRecord.query.all()
    return jsonify(records), HTTPStatus.OK
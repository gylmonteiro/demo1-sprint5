from http import HTTPStatus
import json
from flask import jsonify, request
from app.configs.database import db 
from app.models.call_record_model import CallRecord


def create_record():
    # coletar os dados da requisição
    data = request.get_json()
    record = CallRecord(**data)
    db.session.add(record)
    db.session.commit()

    return jsonify(record), HTTPStatus.CREATED
    # return record.serializer(), HTTPStatus.CREATED

def get_records():
    # datas =
    return {"msg": "QUERY"}
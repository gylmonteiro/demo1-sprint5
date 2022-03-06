from http import HTTPStatus
from pydoc import pager
from flask import jsonify, request, session
from app.configs.database import db
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound
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
    base_query = session.query(CallRecord)
    
    # Modos de consultas
    # record = base_query.filter(CallRecord.id == call_recorder_id).first()
    # record = base_query.get(call_recorder_id)
    # record = base_query.filter_by(id = call_recorder_id).first()
    # record = base_query.filter_by(source = "11111124").all()
    # record = base_query.filter_by(id = call_recorder_id).one()
    
    # Pegando as excessões do flask
    # try: 
    #     record = base_query.filter_by(id = call_recorder_id).one()
    #     # record = base_query.filter_by(source = "11111124").one()
    #     return jsonify(record)
    # except NoResultFound: 
    #     return jsonify({"error": f"{call_recorder_id} not found"}),HTTPStatus.NOT_FOUND
    # except MultipleResultsFound:
    #     return jsonify({"error": f"{call_recorder_id} multply datas"}), HTTPStatus.OK

    try:
        record = base_query.filter_by(id = call_recorder_id).first_or_404(description="id not found")
    except NotFound as e:
        return {"error": e.description}, HTTPStatus.NOT_FOUND
    
    return jsonify(record), HTTPStatus.OK


def get_records():
    # records = CallRecord.query.all()
    session: Session = db.session
    base_query = session.query(CallRecord)

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 3, type=int)

    records = base_query.order_by(CallRecord.id).paginate(page, per_page)
    return jsonify(records.items), HTTPStatus.OK
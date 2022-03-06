from flask import Blueprint
from app.controllers.call_record_controller import get_records, create_record, get_record_by_id

bp = Blueprint("call_record", __name__, url_prefix="/call-records")

bp.get("")(get_records)
bp.get("/<int:call_recorder_id>")(get_record_by_id)
bp.post("")(create_record)
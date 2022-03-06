from flask import Blueprint
from app.controllers.call_record_controller import get_records, create_record
bp = Blueprint("call_record", __name__, url_prefix="/call-records")

bp.get("")(get_records)
bp.post("")(create_record)
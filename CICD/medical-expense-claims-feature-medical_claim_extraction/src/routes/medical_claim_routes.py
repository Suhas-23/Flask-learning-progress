from flask import Blueprint, request
from src.utils.helpers import validate_payload
from src.utils.helpers import format_response_fail, format_response_success
from src.services.medical_claim_data_extraction_service import medical_claim_data_extraction_service


medical_claim = Blueprint('medical_claim', __name__)


@medical_claim.route('/')
def home():
    return "Welcome to the medical claims extraction endpoint.!"


@medical_claim.route('/medical_claim', methods=['POST'])
def medical_claim_extraction():
    data = request.get_json()
    if not data:
        return format_response_fail('No data provided!')
    validation_result = validate_payload(data)
    if validation_result["status"] == "error":
        return format_response_fail(validation_result["errors"])
    req_type = data.get('req_type')
    if req_type == 'medical_claim':
        user_id = data.get('user_id')
        doc_name = data.get('doc_name')
        try:
            data = medical_claim_data_extraction_service(user_id, doc_name)
            return format_response_success(data)
        except Exception as e:
            return format_response_fail(str(e))
    else:
        return format_response_fail('Invalid document type!')



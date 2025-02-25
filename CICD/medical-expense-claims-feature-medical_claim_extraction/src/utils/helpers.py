def format_response_success(data, status="success"):
    return {
        "status": status,
        "data": data
    }


def format_response_fail(code, status="failure"):
    return {
        "status": status,
        "error": code
    }


def validate_payload(payload):
    # Define the expected fields and their types
    required_fields = {
        "user_id": int,
        "doc_name": str,
        "white_label_id": int,
        "s3bucket": str,
        "region": str,
        "cloud": str,
        "req_type": str,
        "file_type": str,
        "system": str,
        "generate_log": str
    }

    errors = []

    for field, expected_type in required_fields.items():
        if field not in payload:
            errors.append(f"Missing required field: {field}")
        elif not isinstance(payload[field], expected_type):
            errors.append(
                f"Invalid type for field '{field}': Expected {expected_type.__name__}, got {type(payload[field]).__name__}")
        elif isinstance(payload[field], str) and not payload[field].strip():
            errors.append(f"Field '{field}' cannot be an empty string")

    if errors:
        return {"status": "error", "errors": errors}
    return {"status": "success", "message": "Payload is valid"}

from src.utils.processing.image_extraction import download_and_extract
from src.utils.ai.data_extraction import llm_info_extraction
from src.utils.processing.image_extraction import extract_data
from pathlib import Path


def medical_claim_data_extraction_service(user_id, doc_name):
    download_and_extract(user_id, doc_name, 'medical_claim')
    filename = Path(f'users_{user_id}/{doc_name}').with_suffix('')
    folder = Path(f"images/{filename}").resolve()
    data = extract_data(folder)
    llm_output = llm_info_extraction(data, "medical_claim")
    return llm_output.model_dump()

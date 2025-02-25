from ollama import Client
from pathlib import Path
import yaml
from crewai import Agent, Task, Crew, LLM
from src.utils.ai.pydantic_models.medical_expenses_claim_data_model import MedicalExpenseClaimDataModel
import base64
import os
from ollama import chat
from ollama import ChatResponse
from dotenv import load_dotenv
load_dotenv()

client = Client(
    host=os.environ.get('OLLAMA_API_BASE'),
)


def encode_image(image_path: Path):
    with image_path.open('rb') as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def process_image(image_path: Path, data: list):

    response: ChatResponse = client.chat(model=os.environ.get('OLLAMA_MODEL_NAME'), messages=[
        {
            'role': 'user',
            'content': "You are an expert information extractor, could you please extract the following information from the image?",
            'images': [image_path]
        },
    ])

    print(response.message.content)

    # Your tool's logic here
    return data.append(response.message.content)


def llm_info_extraction(data: str, doc_type: str):

    if doc_type == "medical_claim":
        config_path = Path(
            'src/utils/ai/config/medical_expenses_claim_config.yaml').resolve()
        data_model = MedicalExpenseClaimDataModel
    else:
        print("Unsupported document type")
        return

    with config_path.open('r') as config_file:
        config = yaml.safe_load(config_file)

    agents_config = config['agents']
    tasks_config = config['tasks']

    formatter = Agent(
        config=agents_config['formatter'],
        llm=f'ollama/{os.environ.get("OLLAMA_MODEL_NAME")}',
    )
    format_task = Task(
        config=tasks_config['format_task'],
        agent=formatter,
        output_pydantic=data_model,
    )

    crew = Crew(
        agents=[formatter],
        tasks=[format_task],
        verbose=True,
    )

    try:
        result = crew.kickoff(
            inputs={
                "data": data,
            }
        )
        return result.pydantic
    except:
        print("Error in processing the data")
        return
    

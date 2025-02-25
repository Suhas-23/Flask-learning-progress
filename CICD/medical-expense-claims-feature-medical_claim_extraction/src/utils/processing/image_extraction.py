import fitz  # Library to work with PDFs
from pathlib import Path  # For working with file paths
from PIL import Image  # Library to work with image files (like PNG, JPG)
# from docx import Document  # Library for working with Word documents (not used here)
# Function to download files from AWS
from src.utils.cloud.aws import download_file
from threading import Thread  # For running multiple tasks simultaneously
from src.utils.ai.data_extraction import process_image  # Function to process images

# Function to extract images from a file (PDF or image)


def extract_images(user_id, doc_name):
    # Get the absolute path of the input file and prepare an output folder for images
    path = Path('uploads/users_' + str(user_id) + '_' +
                doc_name).resolve()  # Get the absolute path
    # Create a folder called 'images/filename'
    output_folder = Path(
        f"images/users_{user_id}/{doc_name.split('.')[0]}").resolve()
    # Make the folder if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)

    # If the file is a PDF
    if path.suffix == ".pdf":
        pdf = fitz.open(path)  # Open the PDF file
        # Go through each page of the PDF
        for page_number in range(pdf.page_count):
            page = pdf[page_number]  # Get the current page
            image = page.get_pixmap()  # Convert the page to an image
            # Save the image with a name like 'page_0001.png'
            image_path = output_folder / f"page_{(page_number+1):04d}.png"
            image.save(image_path)  # Save the image to the folder
        pdf.close()  # Close the PDF after processing all pages

    # If the file is an image (PNG, JPG, JPEG)
    elif path.suffix in [".png", '.jpg', '.jpeg', '.webp']:

        image = Image.open(path)  # Open the image file
        # Save the image with the name 'page_0001.png'
        image_path = output_folder / f"page_0001.png"
        image.save(image_path)  # Save the image

    # If the file format is not supported (like a Word document)
    else:
        # Print a message if the file type isn't handled
        print("Unsupported file format!")


def download_and_extract(user_id, doc_name, doc_type):

    file_path = f'kyc/user_{user_id}/{doc_type}/{doc_name}'
    download_file(file_name=f'users_{user_id}_{doc_name}', aws_path=file_path)

    extract_images(user_id, doc_name)


def extract_data(folder_path: Path, ):
    data = []
    threads = []
    num = 0
    for image in sorted(folder_path.glob("*")):
        num += 1
        if num > 2:
            break
        threads.append(Thread(target=process_image,
                       args=(image, data, )))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return "\n".join(data)

import zipfile
import os

def extract_zip(zip_path, output_dir):
    """
    Extract all files from a zip archive into a specified output directory.

    :param zip_path: Path to the zip archive.
    :param output_dir: Directory where the contents of the zip are to be extracted.
    """
    # Ensure the output directory exists, create it if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open and extract all contents of the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
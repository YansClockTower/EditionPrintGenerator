
RUN = 'python3 main.py'

from pysrc.gen_html import generate_html_output
from pysrc.gen_json import generate_json_output
from pysrc.fetch_data import fetch_all_character
from pysrc.fetch_json import import_from_json
from pysrc.local_cache import get_edition_meta
from pysrc.print_pdf import html_to_pdf
import shutil
import os
import sys

def clean_folder(folder):
    if os.path.exists(folder):
        try:
            shutil.rmtree(folder)
            print(f"Deleted folder: {folder}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder does not exist.")
    pass
    os.makedirs(folder, exist_ok=True)

def help():
    print("Help: ")
    print(f"{RUN} clean         \t\t clean the output.")
    print(f"{RUN} gen           \t\t generate HTML and json.")
    print(f"{RUN} fetch <json>  \t\t import edition from json.")


if len(sys.argv) <= 1:
    help()
    exit()

para = sys.argv[1]

if para == 'gen':
    meta = get_edition_meta()
    EDITION_NAME = meta['name']
    VERSION = meta['version']
    AUTHOR = meta['author']

    FILE_NAME = f"{EDITION_NAME}_{VERSION}"

    clean_folder('output')
    generate_json_output(FILE_NAME)
    generate_html_output(FILE_NAME)
    # html_to_pdf(f'output/{FILE_NAME}.html')


elif para == 'fetch':
    if len(sys.argv) <= 2:
        help()
        exit()
    clean_folder('config')
    clean_folder('data')
    import_from_json(sys.argv[2])

elif para == 'clean':
    clean_folder('config')
    clean_folder('data')
    clean_folder('output')

else:
    help()

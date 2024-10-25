import sys
import os
import platform
import requests
from .settings import OUTPUT_DIR

user_platform = sys.platform
if platform.machine().endswith('64'):
    arch = 'x64'
else:
    arch = 'x32'

JQ_INFO = {
    'name': 'jq',
    'url': 'https://github.com/jqlang/jq/releases/download/',
    'version': 'jq-1.7'
}

JQ_NAME_MAP = {
    'def': 'jq',
    'win32': 'jq.exe'
}

if user_platform in JQ_NAME_MAP:
    JQ_NAME = JQ_NAME_MAP[user_platform]
else:
    JQ_NAME = JQ_NAME_MAP['def']

def fileExist(p_path):
    try:
        return os.path.isfile(p_path)
    except Exception as err:
        return False

DOWNLOAD_MAP = {
    'win32': {
        'def': 'jq-win32.exe',
        'x64': 'jq-win64.exe'
    },
    'darwin': {
        'def': 'jq-osx-amd64',
        'x64': 'jq-osx-amd64'
    },
    'linux': {
        'def': 'jq-linux32',
        'x64': 'jq-linux64'
    }
}

if user_platform in DOWNLOAD_MAP:
    # download the executable
    
    if arch in DOWNLOAD_MAP[user_platform]:
        filename = DOWNLOAD_MAP[user_platform][arch]
    else:
        filename = DOWNLOAD_MAP[user_platform]['def']

url = f'{JQ_INFO["url"]}{JQ_INFO["version"]}/{filename}'
    
def download_binary():

    jq_file = os.path.abspath(os.path.join(OUTPUT_DIR, JQ_NAME))

    if fileExist(jq_file):
        # print("jq is already installed")
        # sys.exit(0)
        
        # DELETE INSTEAD OF EXIT
        os.remove(jq_file)

    print(f'Downloading jq from {url}')

    try:

        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
            print(f"Created directory {OUTPUT_DIR}")
        r = requests.get(url, allow_redirects=True)
        with open(os.path.abspath(os.path.join(OUTPUT_DIR, filename)), 'wb') as f:
            f.write(r.content)

        distPath = os.path.abspath(os.path.join(OUTPUT_DIR, JQ_NAME))
        os.rename(os.path.abspath(os.path.join(OUTPUT_DIR, filename)), distPath)
        if fileExist(distPath):
            os.chmod(distPath, 0o755)

        print(f'Downloaded in {OUTPUT_DIR}')

    except Exception as err:
        print(err)
        sys.exit(1)

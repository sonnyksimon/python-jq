import os
import json
import subprocess
from .settings import JQ_PATH

def _execute_command(jq_filter, exec_in):
    """
    This will call the jq binary file with an initial timeout of 15sec, 
    retrying with no timeout if it fails.

    :param jq_filter: A jq filter, as `str`.
    :type jq_filter: str

    :param exec_in: JSON payload filtered by jq.
    :type exec_in: bytes
    """
    exec_cmd = (JQ_PATH, jq_filter)
    proc = subprocess.Popen(exec_cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        outs, errs = proc.communicate(exec_in, timeout=15)
    except Exception as err:
        proc.kill()
        outs, errs = proc.communicate(exec_in)
    if not errs:
        return outs 

    raise Exception(str(errs))

def run_with_file(jq_filter, filepath, cwd=os.getcwd()):
    try:

        with open(os.path.abspath(os.path.join(cwd, filepath))) as f:
            return json.loads(_execute_command(jq_filter, f.read().encode()))
    
    except Exception as err:
        raise Exception(err)

def run_with_dict(jq_filter, py_dict):
    try:

        return json.loads(_execute_command(jq_filter, json.dumps(py_dict).encode()))
    
    except Exception as err:
        raise Exception(err)

def run_with_string(jq_filter, text_str):
    try:

        return json.loads(_execute_command(jq_filter, text_str.encode()))
    
    except Exception as err:
        raise Exception(err)
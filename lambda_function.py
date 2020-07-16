import json
import os

from subprocess import Popen, PIPE, STDOUT
from urllib.request import urlretrieve

LOCAL_SCRIPT_COPY = "/tmp/script.py"


def _run_cmd(cmd, env):
    proc = Popen(cmd.split(), env=env, stdin=PIPE,
                 stdout=PIPE, stderr=STDOUT)
    output, _ = proc.communicate()
    return proc, output.decode("utf8")


def lambda_handler(event, context):
    url = event["url"]
    urlretrieve(url, LOCAL_SCRIPT_COPY)

    my_env = os.environ.copy()
    my_env["PYTHONPATH"] = os.getcwd()

    cmd = f"python -m flake8 {LOCAL_SCRIPT_COPY}"
    proc, output = _run_cmd(cmd, my_env)

    return {
        'statusCode': 200,
        'body': json.dumps(output)
    }

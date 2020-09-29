import tempfile
import zipfile
import os
import shutil
import logging
import argparse

parser = argparse.ArgumentParser(description="will create zip file")
parser.add_argument("my_file", type=str, help="zip arhive")
argument = parser.parse_args()

logging.basicConfig(format="%(asctime)s - %(name)s - %(message)s",
                    filename=f"{argument.my_file}.log",
                    level=logging.DEBUG)

with tempfile.TemporaryDirectory() as tmpdir:
    with zipfile.ZipFile(f"{argument.my_file}.zip", "r") as zf:
        zf.extractall(path=tmpdir)
        logging.debug(f"{argument.my_file}.zip extracted in {tmpdir} ")

    try:
        for dirpath, dirnames, files in os.walk(tmpdir):
            if "__init__.py" not in files and "__init__.py" not in dirnames:
                shutil.rmtree(dirpath)
                logging.debug(f"removed catalog {dirpath}")
    except Exception as e:
        logging.error(e)

    with zipfile.ZipFile(f"{argument.my_file}_new.zip", "w") as zf:
        for dirpath, dirnames, files in os.walk(tmpdir):
            for filename in files:
                zf.write(os.path.join(dirpath, filename),
                         dirpath.replace(tmpdir, "") + '/' + filename)
    logging.debug(f"{argument.my_file}_new.zip created")

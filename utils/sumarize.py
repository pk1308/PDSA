import os
import sys

from shared.app_log import logger
from shared.functions import ( create_md)

if __name__ == "__main__":

    repo_path = os.getcwd()
    print(sys.argv[1])
    logger.info("converting files to PDF to MD ")
    status = create_md(files_to_create=[sys.argv[1]])
    logger.info(f"converted files to pdf to md  status ; {status} ")


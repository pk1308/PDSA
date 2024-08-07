import os

from shared.functions import ( create_ipynb,create_md, deploy_mkdocs, get_git_status_files,
                              git_add_and_commit, update_my_docs,)
from shared.app_log import logger


if __name__ == "__main__":

    repo_path = os.getcwd()
    files = get_git_status_files(repo_path)
    logger.info(files)
    logger.info("converting files to ipynb ")
    status = create_ipynb(files_to_create=files)
    logger.info(f"converted files to ipynb status ; {status} ")
    logger.info("converting files to PDF to MD ")
    status = create_md(files_to_create=files)
    logger.info(f"converted files to pdf to md  status ; {status} ")
    if status:
        files = get_git_status_files(repo_path)
        update_my_docs()
        logger.info("successful update")

    else:
        logger.error("cant update ")
    logger.info("deploy mk docs ")

    deploy_mkdocs()
    logger.info("deployed mk docs ")
    commit_message = input("please enter the commit message : ")
    git_add_and_commit(commit_message)

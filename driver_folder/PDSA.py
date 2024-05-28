import os
import subprocess
import sys
from loguru import logger
from shared.functions import get_git_status_files, create_md, update_my_docs, deploy_mkdocs , create_ipynb

logger.remove()
logger.add(
    sys.stdout, 
    colorize=True, 
    format="<green>{time}</green> | <blue>{level}</blue> | {message}"
)
def git_add_and_commit(commit_message):
    """
    Adds all changes to the staging area and commits them with the given commit message.
    
    Args:
    commit_message (str): The commit message to use for the commit.
    """
    try:
        # Add all changes to the staging area
        subprocess.run(["git", "add", "."], check=True)
        logger.info("Changes added to staging area.")

        # Commit the changes with the provided commit message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        logger.info(f"Changes committed with message: {commit_message}")

    except subprocess.CalledProcessError as e:
        logger.info(f"An error occurred: {e}")

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
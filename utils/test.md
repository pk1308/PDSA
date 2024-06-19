```python
import json
import os
import sys
from pathlib import Path
from typing import Any
import yaml
from ensure import ensure_annotations
from loguru import logger

logger.add(
    sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>"
)


@ensure_annotations
def read_yaml_as_dict(path_to_yaml: Path):
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return content
    except Exception as e:
        raise e


@ensure_annotations
def write_yaml(file_path: Path, data: dict = None):
    """write yaml file from dic

    Args:
        file_path (Path):  file path with file name
        data (dict, optional): Data to same as yaml

    Raises:
        App_Exception: _description_
    """

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as yaml_file:
            if data is not None:
                yaml.dump(data, yaml_file)
    except Exception as e:
        raise e


import subprocess
import os


def convert_ipynb_to_markdown(folder_path):
    """Converts all Jupyter notebooks in a folder to markdown files.

    Args:
      folder_path: The path to the directory containing the notebooks.
    """
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".ipynb"):
                full_path = os.path.join(root, filename)
                # Check for nbconvert existence before running command
                try:
                    subprocess.run(
                        ["jupyter", "nbconvert", "--to", "markdown", full_path],
                        check=True,
                    )
                    print(f"Converted {filename} to markdown successfully.")
                except subprocess.CalledProcessError:
                    print(
                        f"Error converting {filename}. nbconvert might not be installed."
                    )
```


```python
import os
from pathlib import Path


def create_navigation_from_markdown(
    folder_path="./docs", mkdocs_config_file="mkdocs.yml"
):
    """
    Generates a navigation menu for MkDocs based on the structure of Markdown files.

    Args:
        folder_path (str, optional): Path to the directory containing Markdown files. Defaults to "./docs".
        mkdocs_config_file (str, optional): Path to the MkDocs configuration file. Defaults to "mkdocs.yml".

    Returns:
        dict: The generated navigation structure dictionary in MkDocs format.

    Raises:
        FileNotFoundError: If the MkDocs configuration file is not found.
    """
    markdown_files = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                full_path = os.path.join(root, filename)
                directory_name = Path("/".join(full_path.split("/")[2:]))
                markdown_files.append(directory_name)

    nav_value = {"Home": []}
    for file in markdown_files:
        split_value = str(file).split("/")
        if len(split_value) == 1:
            nav_value["Home"].append(str(file))
        else:
            key = split_value[0]
            if key not in nav_value.keys():
                nav_value[key] = [str(file)]
            else:
                nav_value[key].append(str(file))

    return {
        "nav": [{"name": key, "children": value} for key, value in nav_value.items()]
    }


def update_mkdocs_config(navigation_data, mkdocs_config_file="mkdocs.yml"):
    """
    Updates the navigation section in an MkDocs configuration file.

    Args:
        navigation_data (dict): The navigation structure dictionary in MkDocs format.
        mkdocs_config_file (str, optional): Path to the MkDocs configuration file. Defaults to "mkdocs.yml".

    Raises:
        FileNotFoundError: If the MkDocs configuration file is not found.
    """
    file_path = Path(os.path.join(os.getcwd(), mkdocs_config_file))
    # Assuming you have a function to read and write YAML files (e.g., from previous code)
    try:
        yaml_data = read_yaml_as_dict(file_path)
        yaml_data.update(navigation_data)
        write_yaml(file_path, yaml_data)
    except FileNotFoundError:
        raise FileNotFoundError(f"MkDocs configuration file not found: {file_path}")


if __name__ == "__main__":
    convert_ipynb_to_markdown(folder_path="./docs")
    navigation_data = create_navigation_from_markdown()
    update_mkdocs_config(navigation_data)
    print("Navigation menu for MkDocs created and potentially updated in mkdocs.yml")
    subprocess.run("")
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[1], line 61
         58       raise FileNotFoundError(f"MkDocs configuration file not found: {file_path}")
         60 if __name__ == "__main__":
    ---> 61     convert_ipynb_to_markdown(folder_path = "./docs")
         62     navigation_data = create_navigation_from_markdown()
         63     update_mkdocs_config(navigation_data)


    NameError: name 'convert_ipynb_to_markdown' is not defined



```python
os.chdir("..")
```


```python
yaml_file = read_yaml_as_dict(Path("mkdocs.yml"))
```

    [32m2024-05-12 19:36:42.601[0m | [1mINFO    [0m | [36m__main__[0m:[36mread_yaml_as_dict[0m:[36m29[0m - [1myaml file: mkdocs.yml loaded successfully[0m


    [32m2024-05-12T19:36:42.601246+0400[0m [1myaml file: mkdocs.yml loaded successfully[0m



```python
yaml_file["nav"]
```




    [{'Home': ['index.md']},
     {'week3': ['week3/quick_sort_3_1.md']},
     {'week1': ['week1/exception_handling.md',
       'week1/class&object.md',
       'week1/time_it.md',
       "week1/Euclid's Algorithm.md"]},
     {'week2': ['week2/lec2_3.md',
       'week2/week summary.md',
       'week2/lec2_2.md',
       'week2/insert_sort_2_6.md',
       'week2/mergesort2_7.md',
       'week2/lec2_4_searchinlist.md',
       'week2/selection_sort_2_5.md',
       'week2/lec2.1.md']},
     {'reference': ['reference/priya_suggestion.md']}]




```python
[{key: value} for key, value in nav_value.items()]
```




    [{'Home': ['index.md']},
     {'week1': ['week1/exception_handling.md',
       'week1/class&object.md',
       'week1/time_it.md',
       "week1/Euclid's Algorithm.md"]},
     {'week2': ['week2/lec2_3.md',
       'week2/lec2_2.md',
       'week2/lec2_4_searchinlist.md',
       'week2/lec2.1.md']},
     {'reference': ['reference/priya_suggestion.md']}]




```python

```


```python
folder_path = "./docs"
markdown_files = []
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".md"):
            full_path = os.path.join(root, filename)
            directory_name = Path("/".join(full_path.split("/")[2:]))
            markdown_files.append(directory_name)

nav_value = {"Home": []}
for file in markdown_files:
    split_value = str(file).split("/")
    if len(split_value) == 1:
        nav_value["Home"].append(str(file))
    else:
        key = split_value[0]
        if key not in nav_value.keys():
            nav_value[key] = [str(file)]
        else:
            nav_value[key].append(str(file))
to_update = [{key: value} for key, value in nav_value.items()]
yaml_file["nav"] = to_update
file_path = Path(os.path.join(os.getcwd(), "mkdocs.yml"))
write_yaml(file_path, yaml_file)
```


```python
to_update
```




    [{'Home': ['index.md']},
     {'week1': ['week1/exception_handling.md',
       'week1/class&object.md',
       'week1/time_it.md',
       "week1/Euclid's Algorithm.md"]},
     {'week2': ['week2/lec2_3.md', 'week2/lec2_2.md', 'week2/lec2.1.md']},
     {'reference': ['reference/priya_suggestion.md']}]




```python
yaml_file["nav"] = to_update
```


```python
file_path = Path(os.path.join(os.getcwd(), "mkdocs.yml"))
```


```python
write_yaml(file_path, yaml_file)
```


```python
import subprocess
import os


def convert_ipynb_to_markdown(folder_path):
    """Converts all Jupyter notebooks in a folder to markdown files.

    Args:
      folder_path: The path to the directory containing the notebooks.
    """
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".ipynb"):
                full_path = os.path.join(root, filename)
                # Check for nbconvert existence before running command
                try:
                    subprocess.run(
                        ["jupyter", "nbconvert", "--to", "markdown", full_path],
                        check=True,
                    )
                    print(f"Converted {filename} to markdown successfully.")
                except subprocess.CalledProcessError:
                    print(
                        f"Error converting {filename}. nbconvert might not be installed."
                    )


# Specify the folder path for conversion
folder_path = "./docs"
convert_ipynb_to_markdown(folder_path)
```

    [NbConvertApp] Converting notebook ./docs/week2/lec2_4_searchinlist.ipynb to markdown
    [NbConvertApp] Writing 4206 bytes to docs/week2/lec2_4_searchinlist.md


    Converted lec2_4_searchinlist.ipynb to markdown successfully.
    Converted lec2_3.ipynb to markdown successfully.


    [NbConvertApp] Converting notebook ./docs/week2/lec2_3.ipynb to markdown
    [NbConvertApp] Writing 41851 bytes to docs/week2/lec2_3.md



```python
os.chdir("..")
```


```python

```

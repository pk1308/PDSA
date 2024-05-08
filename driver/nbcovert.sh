#!/bin/bash

# Folder containing documentation files
folder_path="./docs"

# Initialize navigation structure (empty "Home" section)
nav_value="home=[]"

# Find all markdown files recursively
find "$folder_path" -type f -name "*.md" | while read -r file; do
  # Extract relative path and split into components
  file="${file#"$folder_path/"}"
  path_components=(${file//\// })

  # Check length (root or subfolder)
  if [[ ${#path_components[@]} -eq 1 ]]; then
    # Append to "Home" section
    nav_value="${nav_value/\home=[]/home+=(${path_components[0]})}"}  # Use parameter substitution
  else
    # Build section key
    section_key="${path_components[0]}"

    # Check if section exists
    if [[ ! $(echo "$nav_value" | grep -q "\[$section_key\]") ]]; then
      # Create new section
      nav_value="$nav_value,$section_key=[]"
    fi

    # Append to the section
    nav_value="${nav_value/\($section_key\)\[\]/\($section_key\)+=(${path_components[1]})}"}  # Parameter substitution again
  fi
done

# Remove leading comma from navigation structure
nav_value="${nav_value#,}"

# Update MkDocs configuration with yq (assuming installed)
yq '.nav = ['$nav_value']' mkdocs.yml > tmp_mkdocs.yml && mv tmp_mkdocs.yml mkdocs.yml

echo "Navigation menu updated in mkdocs.yml"

import os
import glob

# Get the input directory
input_directory = "src"

# Get all markdown files in the input directory
markdown_files = glob.glob(os.path.join(input_directory, "*.md"))

# Create the index file
index_file = open("index.md", "w")

# Write the header to the index file
index_file.write("# Index\n\n")

# Iterate over all markdown files
for markdown_file in markdown_files:

    # Get the file name
    file_name = os.path.basename(markdown_file)

    # Write a link to the file to the index file
    index_file.write(f"* [{file_name}]({file_name})\n")

# Close the index file
index_file.close()


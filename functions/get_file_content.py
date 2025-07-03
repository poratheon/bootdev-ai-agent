import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path): 
    working_path = os.path.abspath(os.path.expanduser(working_directory))
    #print(f"The path is:  {working_path}")
    full_path = os.path.join(working_path, file_path)
    #print(f"The full path (path + directory) is:  {full_path}")
    # print(f"The full path is:  {full_path}")
    if not full_path.startswith(working_path + os.sep) and full_path != working_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: file not found or is not a regular file: "{file_path}"'
    try:
        with open(full_path, "r") as f:
            full_file_content_string = f.read()
            if len(full_file_content_string) > 10000:
                file_content_string = full_file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
            else:
                file_content_string = full_file_content_string
            return file_content_string
            # read file
            # if greater than 10000 characters, truncate at 10000 characters.  Append to end:  [...File "{file_path}" truncated at 10000 characters]
            # return file contents as a string
    except Exception as e:
        return f"Error: {str(e)}"

# Debugging
# print(get_file_content("~/OneDrive - Siemens AG/Dev/Python/boot.dev/ai-agent/bootdev-ai-agent/", "calculator/lorem.txt"))

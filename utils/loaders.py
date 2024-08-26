def read_file_as_text(file_path):
    """
    Reads the content of a file as plain text.

    Args:
    file_path (str): Path to the file to be read.

    Returns:
    str: Content of the file as a string of text.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except UnicodeDecodeError:
        # Try reading with another encoding if utf-8 fails
        with open(file_path, "r", encoding="latin-1") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading the file: {e}"

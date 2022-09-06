import registers

files = {
    "100": [-100, 5, 8, -3, 113],
    "200": [],
    "400": [],
}

current_file = {
    "name": None,
    "cursor": 0,
}


def file_is_open():
    """ Return True if a file is open."""
    return current_file["name"] is not None


def print_file_info():
    """Print current file and position in it"""
    if file_is_open():
        if current_file["cursor"] < len(files[current_file["name"]]):
            pos = current_file["cursor"]
        else:
            pos = "EOF"
        print(f'File: {current_file["name"]} (pos: {current_file["cursor"]})', end='')
    print()


def print_final_value_of_files():
    """Print final value of all files"""
    print("\nFiles:")
    for file in files:
        print(f"\t{file}: {files[file]}")


def ensure_file_is_open():
    """Raise exception if no file open"""
    if current_file["name"] is None:
        raise Exception("No File Open!")


def ensure_valid_file(file_id):
    """Raise exception if file_id is not known"""
    if file_id not in files:
        raise Exception(f"File not found: {file_id}")


def is_current_file_at_eof():
    """Return True if file is at EOF"""
    ensure_file_is_open()

    return current_file["cursor"] >= len(files[current_file["name"]])


def read_value_from_file():
    """Read a value from a file and advance cursor"""
    global current_file

    val = files[current_file["name"]][current_file["cursor"]]
    current_file["cursor"] += 1
    return val


def write_value_to_file(val):
    """Write a value to a file and advance cursor"""
    global current_file

    if is_current_file_at_eof():
        files[current_file["name"]].append(val)
    else:
        files[current_file["name"]][current_file["cursor"]] = val
    current_file["cursor"] += 1


def GRAB(file_id):
    """Implement GRAB command, i.e., "open" a file"""
    global current_file

    current_file["name"] = file_id
    current_file["cursor"] = 0


def DROP():
    """Implement DROP command, i.e., "close" a file"""
    global current_file

    current_file["name"] = None


def SEEK(position):
    """Move to the specified position in the current file."""
    global current_file

    ensure_file_is_open()
    position = int(position)

    if not (-registers.MAX_NUM <= position <= registers.MAX_NUM):
        raise Exception(f"Illegal File Cursor Position: {position}")

    if position == -registers.MAX_NUM:
        position = 0
    elif position == registers.MAX_NUM:
        position = len(files[current_file["name"]])

    current_file["cursor"] = position


def VOID():
    """Delete an item from a virtual file."""
    del files[current_file["name"]][current_file["cursor"]]

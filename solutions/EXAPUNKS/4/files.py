import registers

current_file = None
file_cursor = 0

files = {
    "100": [-100, 5, 8, -3, 113],
    "200": [],
    "400": [],
}

def print_file_info():
    """Print current file and position in it"""
    if current_file:
        pos = file_cursor if file_cursor < len(files[current_file]) else "EOF"
        print(f"Current file: {current_file}, position: {pos}")


def print_final_value_of_files():
    """Print final value of all files"""
    for file in files:
        print(file, files[file])


def is_open():
    return current_file is not None


def ensure_file_is_open():
    """Raise exception if no file open"""
    if current_file is None:
        raise Exception('No File Open!')


def ensure_valid_file(file_id):
    """Raise exception if file_id is not known"""
    if file_id not in files:
        raise Exception(f"File not found: {file_id}")


def is_current_file_at_eof():
    """Return True if file is at EOF"""
    ensure_file_is_open()

    return file_cursor >= len(files[current_file])


def read_value_from_file():
    """Read a value from a file and advance cursor"""
    global file_cursor

    val = files[current_file][file_cursor]
    file_cursor += 1
    return val


def write_value_to_file(val):
    """Write a value to a file and advance cursor"""
    global file_cursor

    files[current_file].append(val)
    file_cursor += 1


def GRAB(file_id):
    """Implement GRAB command, i.e., "open" a file"""
    global current_file

    current_file = file_id


def DROP():
    """Implement DROP command, i.e., "close" a file"""
    global current_file

    current_file = None


def SEEK(position):
    global file_cursor

    ensure_file_is_open()
    position = int(position)

    if not (-registers.MAX_NUM <= position <= registers.MAX_NUM):
        raise Exception(f'Illegal File Cursor Position: {position}')

    if position == -registers.MAX_NUM:
        position = 0
    elif position == registers.MAX_NUM:
        position = len(files[current_file])

    file_cursor = position

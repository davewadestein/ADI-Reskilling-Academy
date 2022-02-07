# The labels dict will keep track of labels for branching
label_dict = {}

def MARK(label, instruction_ptr):
    """Create a label if it doesn't already exist."""
    if label in label_dict:
        raise Exception(f'Duplicate Label: {label}')
    label_dict[label] = instruction_ptr

def setup_labels(code):
    """Make a pass through the code to find and mark all labels."""
    for instruction_ptr, (instruction, *args) in enumerate(code):
        if instruction == "MARK":
            MARK(args[0], instruction_ptr)

    print("Labels:", end=" ")
    for label in label_dict:
        print(f"{label} ({label_dict[label]})", end=" ")
    print()


def ensure_valid_label(label):
    """Ensure a label is valid, i.e., it's in the map."""
    if label not in label_dict:
        raise Exception(f'Unknown Label: {label}')

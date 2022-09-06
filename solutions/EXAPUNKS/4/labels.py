# The labels dict will keep track of labels for branching
labels = {}


def create_label(label, position):
    """Create a label if it doesn't already exist."""
    if label in labels:
        raise Exception(f"Duplicate Label: {label}")
    labels[label] = position


def get_label(label):
    ensure_valid_label(label)
    return labels[label]


def ensure_valid_label(label):
    """Ensure a label is valid, i.e., it's in the map."""
    if label not in labels:
        raise Exception(f"Unknown Label: {label}")


def print_all_labels():
    if labels:
        print("Labels:", end=" ")
        for label in labels:
            print(f"{label} ({labels[label]})", end=" ")
            print()

#!/usr/bin/python3
"""Lockboxes Problem"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be opened.

    Parameters:
    boxes (list of lists): Each box may contain keys to the other boxes.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    total_boxes = len(boxes)
    unlocked = [False] * total_boxes
    unlocked[0] = True
    keys = [key for key in boxes[0] if key < total_boxes]

    while keys:
        current_key = keys.pop()
        if not unlocked[current_key]:
            unlocked[current_key] = True
            keys.extend([key for key in boxes[current_key]
                         if key < total_boxes])

    return all(unlocked)

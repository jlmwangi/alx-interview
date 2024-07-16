#!/usr/bin/python3

""" method to determine if all locked boxes can be opened"""


def canUnlockAll(boxes):
    """method to open all n locked boxes"""
    opened_boxes = set([0])  # track opened boxes using a set
    keys = list(boxes[0])  # put keys in box 0 in a list

    while keys:
        key = keys.pop()  # get a key from list
        if key not in opened_boxes:  # if box corresponding to key not opened
            opened_boxes.add(key)  # mark box as opened
            keys.extend(boxes[key])  # add keys from curr box to list of keys

    return len(opened_boxes) == len(boxes)

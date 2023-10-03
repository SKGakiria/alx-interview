#!/usr/bin/python3
"""The Lockboxes Module"""


def canUnlockAll(boxes):
    """Function that determines if boxes can be unlocked"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    for i in range(n):
        if not unlocked[i]:
            continue

        for key in boxes[i]:
            if key < n and not unlocked[key]:
                unlocked[key] = True

    return all(unlocked)

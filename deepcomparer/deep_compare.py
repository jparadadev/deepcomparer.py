from typing import Any


def deep_compare(
        obj1: Any,
        obj2: Any,
) -> bool:
    res = __rec_helper(obj1, obj2)
    return res


def __rec_helper(obj1: Any, obj2: Any, ) -> bool:
    if type(obj1) != type(obj2):
        return False

    if isinstance(obj1, dict):
        pass

    if isinstance(obj1, list):
        pass

    if isinstance(obj1, set):
        pass

    if isinstance(obj1, tuple):
        pass

    return obj1 == obj2
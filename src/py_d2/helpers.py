# -*- coding: utf-8 -*-
from typing import List
from typing import Optional


def indent(items: List[str], n: int = 2) -> List[str]:
    return [f"{' '*n}{item}" for item in items]


def add_label_and_properties(
    name: str, label: Optional[str] = None, properties: Optional[List[str]] = None
) -> List[str]:
    has_properties: bool = properties is not None and len(properties) > 0

    first_line = name
    if label or has_properties:
        first_line += ":"

    if label:
        first_line += f" {label}"

    if has_properties:
        first_line += " {"

    if properties and has_properties:
        return [first_line, *indent(properties), "}"]

    return [first_line]


def add_weights_for_max_flow(
    name1: str, name2: str, label: List[int]
):
    x += name1 + "<->" + name2 + ": {\n"
    x += "  source-arrowhead: "+{label[0]}" {\n"
    x += "    shape: arrow\n"
    x += "  }"
    x += "  target-arrowhead: "+{label[1]}" {\n"
    x += "    shape: arrow\n"
    x += "  }\n"
    x += "}\n"

def flatten(items: List[List[str]]) -> List[str]:
    return [item for sublist in items for item in sublist]

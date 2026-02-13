import xml.etree.ElementTree as ET

def safe_find_element(element: ET.Element[str], tag: str) -> ET.Element[str]:
    child = element.find(tag)
    if child is None:
        raise ValueError(f"Tag {tag} not found in element {element.tag}")
    return child

def safe_find_all_elements(element: ET.Element[str], tag: str) -> list[ET.Element[str]]:
    """获取所有子元素的列表副本"""
    children = element.findall(tag)
    if children is None:
        raise ValueError(f"Tag {tag} not found in element {element.tag}")
    return children

def safe_find_text(element: ET.Element[str], tag: str) -> str:
    child = element.findtext(tag, None)
    if child is None:
        raise ValueError(f"Tag {tag} has no text in element {element.tag}")
    return child

def safe_find_int(element: ET.Element[str], tag: str) -> int:
    child = element.findtext(tag, None)
    if child is None:
        raise ValueError(f"Tag {tag} has no text in element {element.tag}")
    try:
        return int(child)
    except ValueError:
        raise ValueError(f"Tag {tag} text {child} is not a number in element {element.tag}")

def safe_find_hex(element: ET.Element[str], tag: str) -> int:
    child = element.findtext(tag, None)
    if child is None:
        raise ValueError(f"Tag {tag} has no text in element {element.tag}")
    try:
        return int(child, 16)
    except ValueError:
        raise ValueError(f"Tag {tag} text {child} is not a hex number in element {element.tag}")

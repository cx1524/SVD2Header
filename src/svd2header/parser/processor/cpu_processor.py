import xml.etree.ElementTree as ET
from parser import utils

def get_cpu(root: ET.Element[str]) -> ET.Element[str]:
    cpu = utils.safe_find_element(root, "cpu")
    name = utils.safe_find_text(cpu, "name")
    if name == "CM0+":
        cpu.set("core", "CM0PLUS")
    else :
        cpu.set("core", name)
    return cpu

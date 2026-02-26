import xml.etree.ElementTree as ET
from parser import utils

def get_peripherals(root: ET.Element[str]) -> ET.Element[str]:
    peripherals = utils.safe_find_element(root, "peripherals")
    child_peripherals = utils.safe_find_all_elements(peripherals, "peripheral")
    sorted_peripherals = sorted(child_peripherals, key=lambda x: utils.safe_find_hex(x, "baseAddress"))

    peripherals.clear()
    peripherals.extend(sorted_peripherals)
    add_typedef(peripherals)

    return peripherals

def add_typedef(peripherals: ET.Element[str]):
    if peripherals is None:
        return
    for peripheral in peripherals:
        name = utils.safe_find_text(peripheral, "name")
        peripheral.set("typedef", name + "_TypeDef")

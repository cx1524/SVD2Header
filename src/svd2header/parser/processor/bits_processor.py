import xml.etree.ElementTree as ET
from parser import utils

def get_bits_peripherals(peripherals: ET.Element[str]) -> ET.Element[str]:
    bits_peripherals = ET.Element("bits_peripherals")
    peripherals_list = {}
    # 列表后再清洗数据
    for peripheral in peripherals:
        groupName = utils.safe_find_text(peripheral, "groupName")
        peripherals_list[groupName] = peripheral
    for peripheral in peripherals_list.values():
        bits_peripherals.append(peripheral)
    return bits_peripherals

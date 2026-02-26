import xml.etree.ElementTree as ET
from parser import utils

def get_instances(peripherals: ET.Element[str]) -> ET.Element[str]:
    instances: ET.Element[str] = ET.Element("instances")
    name_dict: dict[str, list[ET.Element[str]]] = {}
    for peripheral in peripherals:
        groupName = utils.safe_find_text(peripheral, "groupName")
        name = utils.safe_find_element(peripheral, "name")
        name_dict.setdefault(groupName, []).append(name)
    for groupName, names in name_dict.items():
        instance:ET.Element[str] = ET.Element("instance")
        instance.set("groupName", groupName)
        for name in names:
            instance.append(name)
        instances.append(instance)
    return instances

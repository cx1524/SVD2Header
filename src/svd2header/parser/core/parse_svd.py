import xml.etree.ElementTree as ET
from parser import utils

def parse_svd(svd_file: str) -> ET.Element[str]:
    tree = ET.parse(svd_file)
    return tree.getroot()

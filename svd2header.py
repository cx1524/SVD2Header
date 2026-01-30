import xml.etree.ElementTree as ET

def svd2header(svd_file: str):
    tree = ET.parse(svd_file)
    root = tree.getroot()

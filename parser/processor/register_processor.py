import xml.etree.ElementTree as ET
from parser import utils
from enum import Enum

class UnionState(Enum):
    STOP = 0
    START = 1
    CONTINUE = 2

def process_registers(peripherals: ET.Element[str]):
    for peripheral in peripherals:
        process_dim_registers(peripheral)
        process_union_registers(peripheral)

def process_dim_registers(peripheral: ET.Element[str]):
    registers = peripheral.find("registers")
    if registers is None:
        return
    registers_list = utils.safe_find_all_elements(registers, "register")
    for register in registers_list:
        fields = utils.safe_find_element(register, "fields")
        field_list = utils.safe_find_all_elements(fields, "field")
        for field in field_list:
            if check_dim_field(field):
                dim_field_list = process_dim_field(field)
                index = field_list.index(field)
                field_list.remove(field)
                field_list[index:index] = dim_field_list
        fields.clear()
        fields.extend(field_list)

def process_dim_field(field: ET.Element[str]) -> list[ET.Element[str]]:
    dim_num = utils.safe_find_int(field, "dim")
    dim_increment = utils.safe_find_int(field, "dimIncrement")
    dim_index = utils.safe_find_text(field, "dimIndex")
    parts = dim_index.split("-")
    dim_index_min = int(parts[0])
    dim_name = utils.safe_find_text(field, "name")
    index = dim_index_min
    new_field_list: list[ET.Element[str]] = []
    description_elem = utils.safe_find_element(field, "description")
    bitWidth_elem = utils.safe_find_element(field, "bitWidth")
    offset = utils.safe_find_int(field, "bitOffset")
    for i in range(dim_num):
        new_field = ET.Element("field")
        new_field.append(description_elem)
        new_field.append(bitWidth_elem)
        new_offset_elem = ET.Element("bitOffset")
        new_offset_elem.text = str(offset + i * dim_increment)
        new_field.append(new_offset_elem)
        name = dim_name % (index)
        new_name_elem = ET.Element("name")
        new_name_elem.text = name
        new_field.append(new_name_elem)
        new_field_list.append(new_field)
        index += 1
    return new_field_list

def check_dim_field(field: ET.Element[str]) -> bool:
    dim_num = field.find("dim")
    return dim_num is not None

def process_union_registers(peripheral: ET.Element[str]):
    registers = peripheral.find("registers")
    if registers is None:
        return
    registers_list = utils.safe_find_all_elements(registers, "register")
    state = UnionState.STOP # 0: 未开始, 1: 开始, 2: 继续 3: 结束
    i = 0
    length = len(registers_list)
    next_address = -1
    while i < length:
        register = registers_list[i]
        next_register = registers_list[i+1] if i+1 < length else None
        current_address = utils.safe_find_hex(register, "addressOffset")
        next_address = utils.safe_find_hex(next_register, "addressOffset") if next_register is not None else -1
        if next_address == current_address:
            if state == UnionState.STOP:
                register.set("union", "Start")
                state = UnionState.CONTINUE
            else:
                register.set("union", "Continue")
                state = UnionState.CONTINUE
        else:
            if state != UnionState.STOP:
                register.set("union", "Stop")
                state = UnionState.STOP
        i += 1

import xml.etree.ElementTree as ET
from parser import utils

def get_interrupts(peripherals: ET.Element[str]) -> ET.Element[str]:
    interruptsTab = ET.Element("interrupts")

    # 收集所有中断
    all_interrupts = []
    for peripheral in peripherals:
        interrupts = peripheral.findall("interrupt")
        if interrupts is not None:
            all_interrupts.extend(interrupts)

    # 按中断数值排序（处理可能缺失value元素的情况）
    sorted_interrupts = sorted(all_interrupts,
                              key=lambda x: int(x.find("value").text) if x.find("value") is not None else 999)

    # 按排序顺序插入
    for interrupt in sorted_interrupts:
        interruptsTab.append(interrupt)

    if len(interruptsTab) == 0:
        raise ValueError("No interrupts found")

    return interruptsTab

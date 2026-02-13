from .core import parse_svd
from .processor import (
    get_bits_peripherals,
    get_cpu,
    get_instances,
    get_interrupts,
    get_peripherals,
    process_registers,
)

version = "1.0.0"

__all__ = [
    'get_cpu',
    'get_interrupts',
    'get_instances',
    'get_bits_peripherals',
    'parse_svd',
    'get_peripherals',
    'process_registers',
]

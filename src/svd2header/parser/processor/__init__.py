from .bits_processor import get_bits_peripherals
from .cpu_processor import get_cpu
from .instances_processor import get_instances
from .interrupt_processor import get_interrupts
from .peripherals_processor import get_peripherals
from .register_processor import process_registers

version = "1.0.0"

__all__ = [
    'get_cpu',
    'get_interrupts',
    'get_instances',
    'get_bits_peripherals',
    'get_peripherals',
    'process_registers',
]

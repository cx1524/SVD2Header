import argparse
import os
import sys
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import parser

def svd2header(svd_file: str, template_file: str, output_file: str = ""):
    """将SVD文件转换为C头文件"""
    # 验证输入文件是否存在
    if not os.path.exists(svd_file):
        raise FileNotFoundError(f"SVD文件不存在: {svd_file}")

    if not os.path.exists(template_file):
        raise FileNotFoundError(f"模板目录不存在: {template_file}")

    if output_file == "":
        output_file = svd_file.replace(".svd", ".h")

    root = parser.parse_svd(svd_file)
    # 获取CPU信息
    cpu = parser.get_cpu(root)
    # 获取peripherals
    peripherals = parser.get_peripherals(root)
    parser.process_registers(peripherals)
    # 获取interrupts
    interrupts = parser.get_interrupts(peripherals)
    bits_peripherals = parser.get_bits_peripherals(peripherals)
    instances = parser.get_instances(peripherals)
    date = datetime.now()

    env = Environment(loader=FileSystemLoader(template_file))
    template = env.get_template('header.h.j2')
    rendered_content = template.render(
        root=root,
        peripherals=peripherals,
        bits_peripherals=bits_peripherals,
        interrupts=interrupts,
        instances=instances,
        cpu=cpu,
        date=date
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered_content)

    print(f"成功生成头文件: {output_file}")

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='将SVD文件转换为C头文件',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python svd2header.exe -s *.svd -o ./output/*.h
  python svd2header.exe --svd *.svd --template ./j2templates --output ./output/*.h
        """
    )

    parser.add_argument(
        '-s', '--svd',
        dest='svd_file',
        required=True,
        help='输入的SVD文件路径'
    )

    parser.add_argument(
        '-t', '--template',
        dest='template_file',
        default='./j2templates',
        help='Jinja2模板目录路径 (默认: ./j2templates)'
    )

    parser.add_argument(
        '-o', '--output',
        dest='output_file',
        default='',
        help='输出的头文件路径'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='显示详细输出信息'
    )

    return parser.parse_args()

def main():
    """主函数"""
    try:
        # 解析命令行参数
        args = parse_arguments()

        if args.verbose:
            print(f"SVD文件: {args.svd_file}")
            print(f"模板目录: {args.template_file}")
            print(f"输出文件: {args.output_file}")
            print("开始转换...")

        # 执行转换
        svd2header(args.svd_file, args.template_file, args.output_file)

        if args.verbose:
            print("转换完成!")

    except FileNotFoundError as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
    except ET.ParseError as e:
        print(f"XML解析错误: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"未知错误: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

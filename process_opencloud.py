#!/usr/bin/env python3
"""
处理 opencloud.json 文件并实现乘法运算
"""

import os
import base64
import json


def find_opencloud_json(start_path=None):
    """
    在系统中查找 opencloud.json 文件

    Args:
        start_path: 开始搜索的路径，默认为当前用户主目录

    Returns:
        找到的文件路径列表
    """
    if start_path is None:
        start_path = os.path.expanduser("~")

    found_files = []

    print(f"正在搜索 {start_path} 目录下的 opencloud.json 文件...")

    for root, dirs, files in os.walk(start_path):
        # 跳过一些常见的大目录
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', '.venv', 'venv']]

        for file in files:
            if file == "opencloud.json":
                full_path = os.path.join(root, file)
                found_files.append(full_path)
                print(f"  找到：{full_path}")

    return found_files


def encrypt_to_base64(file_path):
    """
    读取文件内容并加密为 Base64 字符串

    Args:
        file_path: 文件路径

    Returns:
        Base64 编码的字符串
    """
    print(f"\n读取文件：{file_path}")

    with open(file_path, 'rb') as f:
        content = f.read()

    # 将内容转换为 Base64
    base64_bytes = base64.b64encode(content)
    base64_string = base64_bytes.decode('utf-8')

    print(f"原内容长度：{len(content)} 字节")
    print(f"Base64 长度：{len(base64_string)} 字符")

    return base64_string


def save_base64_to_file(base64_string, original_path, output_ext=".txt"):
    """
    将 Base64 字符串保存为文件

    Args:
        base64_string: Base64 编码的字符串
        original_path: 原始文件路径（用于生成输出文件名）
        output_ext: 输出文件扩展名

    Returns:
        输出文件路径
    """
    # 生成输出文件名
    base_name = os.path.basename(original_path)
    name_without_ext = os.path.splitext(base_name)[0]
    output_filename = f"{name_without_ext}_encoded{output_ext}"
    output_path = os.path.join(os.path.dirname(original_path), output_filename)

    print(f"\n保存 Base64 内容到：{output_path}")

    with open(output_path, 'w') as f:
        f.write(base64_string)

    return output_path


def multiply(a, b):
    """
    简单的乘法运算

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两数的乘积
    """
    return a * b


def main():
    print("=" * 60)
    print("opencloud.json 处理程序")
    print("=" * 60)

    # 1. 查找 opencloud.json 文件
    found_files = find_opencloud_json()

    if not found_files:
        print("\n未找到 opencloud.json 文件")
    else:
        print(f"\n共找到 {len(found_files)} 个文件")

        # 2. 处理第一个找到的文件
        target_file = found_files[0]
        base64_content = encrypt_to_base64(target_file)

        # 3. 保存为 txt 文件
        output_path = save_base64_to_file(base64_content, target_file)
        print(f"\n处理完成！加密文件已保存到：{output_path}")

    # 4. 演示乘法运算
    print("\n" + "=" * 60)
    print("乘法运算演示")
    print("=" * 60)

    test_cases = [
        (5, 3),
        (7, 8),
        (12, 12),
        (2.5, 4),
        (-3, 5),
    ]

    for a, b in test_cases:
        result = multiply(a, b)
        print(f"  {a} × {b} = {result}")

    # 用户自定义乘法
    print("\n自定义乘法（输入 q 退出）:")
    while True:
        try:
            user_input = input("请输入两个数字（空格分隔）: ").strip()
            if user_input.lower() == 'q':
                break
            parts = user_input.split()
            if len(parts) != 2:
                print("  请输入两个数字，用空格分隔")
                continue
            a, b = float(parts[0]), float(parts[1])
            result = multiply(a, b)
            print(f"  结果：{a} × {b} = {result}")
        except ValueError:
            print("  请输入有效的数字")
        except KeyboardInterrupt:
            print("\n")
            break


if __name__ == "__main__":
    main()

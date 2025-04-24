import json
import sys

def read_json_file(file_path):
    """
    读取本地JSON文件
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{file_path}'")
        return None
    except json.JSONDecodeError:
        print(f"错误: '{file_path}' 不是有效的JSON文件")
        return None
    except Exception as e:
        print(f"错误: 读取文件时发生错误: {str(e)}")
        return None

def json_to_markdown_table(data):
    """
    将JSON数据转换为markdown表格
    """
    # 表头
    markdown = "| 参数名称 | 参数类型 | 参数说明 | 是否必填 | 参数值约束 |\n"
    markdown += "|---------|---------|---------|---------|------------|\n"
    
    # 递归处理JSON
    rows = process_json("", data)
    
    # 添加所有行
    markdown += "\n".join(rows)
    
    return markdown

def process_json(parent_key, data, level=0):
    """
    递归处理JSON数据
    """
    rows = []
    indent = "└" * level  # 使用两个空格作为一个缩进级别
    
    if isinstance(data, dict):
        for key, value in data.items():
            # 处理当前层级的key
            display_key = key if not parent_key else key
            
            if isinstance(value, (dict, list)):
                # 添加当前字段
                type_str = "object" if isinstance(value, dict) else "array"
                rows.append(f"| {indent}{display_key} | {type_str} | - | 否 | - |")
                
                # 递归处理子字段，增加缩进级别
                if isinstance(value, dict):
                    rows.extend(process_json("", value, level + 1))
                elif isinstance(value, list) and len(value) > 0:
                    # 如果是数组，处理第一个元素作为示例
                    first_item = value[0]
                    if isinstance(first_item, (dict, list)):
                        rows.extend(process_json("", first_item, level + 1))
                    else:
                        type_str = get_type_str(first_item)
                        value_constraint = get_value_constraint(first_item)
                        rows.append(f"| {indent}  [{type_str}] | {type_str} | - | 否 | {value_constraint} |")
            else:
                # 处理基本类型
                type_str = get_type_str(value)
                value_constraint = get_value_constraint(value)
                rows.append(f"| {indent}{display_key} | {type_str} | - | 否 | {value_constraint} |")
                
    elif isinstance(data, list) and len(data) > 0:
        # 处理数组的第一个元素作为示例
        first_item = data[0]
        if isinstance(first_item, (dict, list)):
            rows.extend(process_json("", first_item, level))
        else:
            type_str = get_type_str(first_item)
            value_constraint = get_value_constraint(first_item)
            rows.append(f"| {indent}[{type_str}] | {type_str} | - | 否 | {value_constraint} |")
        
    return rows

def get_type_str(value):
    """
    获取值的类型字符串
    """
    if isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "number"
    elif isinstance(value, float):
        return "number"
    elif isinstance(value, str):
        return "string"
    elif value is None:
        return "null"
    else:
        return "unknown"

def get_value_constraint(value):
    """
    获取值的约束说明
    """
    if isinstance(value, bool):
        return "true/false"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        if value:
            return value
        return "-"
    elif value is None:
        return "null"
    else:
        return "-"

def save_markdown_to_file(markdown_content, output_file):
    """
    将markdown内容保存到文件
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"成功保存到文件: {output_file}")
    except Exception as e:
        print(f"保存文件时发生错误: {str(e)}")

def main():
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("使用方法: python script.py <json文件路径> [输出文件路径]")
        return

    # 获取输入文件路径
    input_file = sys.argv[1]
    
    # 获取输出文件路径（可选）
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.md"

    # 读取JSON文件
    data = read_json_file(input_file)
    if data is None:
        return

    # 转换为markdown表格
    markdown_table = json_to_markdown_table(data)

    # 保存到文件
    save_markdown_to_file(markdown_table, output_file)

if __name__ == "__main__":
    main()
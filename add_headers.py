#!/usr/bin/env python3

def add_headers_every_100_rows(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 识别表头行
    header1 = None
    header2 = None
    table_start = 0
    
    # 查找表头
    for i, line in enumerate(lines):
        if line.startswith('| 参数名称 | 参数类型 | 参数说明 | 是否必填 | 参数值约束 |'):
            header1 = line
            if i + 1 < len(lines) and lines[i+1].startswith('|---'):
                header2 = lines[i+1]
                table_start = i + 2
                break
    
    if header1 is None or header2 is None:
        print("未找到表头，无法处理")
        return
    
    # 处理表格内容
    result = []
    # 复制表头前的内容
    for i in range(table_start - 2):
        result.append(lines[i])
    
    # 添加初始表头
    result.append(header1)
    result.append(header2)
    
    # 处理表格主体，每100行添加一次表头
    table_row_count = 0
    for i in range(table_start, len(lines)):
        line = lines[i]
        # 判断是否为表格行
        if line.startswith('|'):
            table_row_count += 1
            # 每100行添加表头
            if table_row_count % 100 == 0 and i + 1 < len(lines) and lines[i+1].startswith('|'):
                result.append(line)
                result.append('\n')  # 空行
                result.append(header1)
                result.append(header2)
            else:
                result.append(line)
        else:
            # 非表格行，重置计数
            table_row_count = 0
            result.append(line)
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(result)
    
    print(f"处理完成，已将结果写入 {output_file}")

if __name__ == "__main__":
    input_file = "doc.md"
    output_file = "doc.md"
    add_headers_every_100_rows(input_file, output_file) 
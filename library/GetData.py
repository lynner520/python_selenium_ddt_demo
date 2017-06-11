# -*- coding: utf8 -*-
 
import csv
 
 
def get_csv_data(csv_path):
    """
    从csv读取测试数据，并返回一个list
    @type csv_path: string
    @param csv_path: some csv path string
    @return list
    """
    rows = []
    csv_data = open(str(csv_path), "rb")
    content = csv.reader(csv_data)
 
    # 跳过第一行
    next(content, None)
 
    # 将数据添加进rows
    for row in content:
        rows.append(row)

    return rows


if __name__ == '__main__':
    print get_csv_data("../data/test_case.csv")

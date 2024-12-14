#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024-12-09 10:47
# @Author : 'IReverser'
# @FileName: main.py
# Reference:
import glob as glob


def del_special_v(data, index_list):
    indexs = [[i, i + 1, i + 2] for i in index_list]
    index_process = [item for sublist in indexs for item in sublist]
    filtered_list = [item for i, item in enumerate(data) if i not in index_process]
    # print(filtered_list)
    return filtered_list


if __name__ == '__main__':
    data_file = "./data/"
    res_file_path = "res.asc"
    date_list = []
    data_list = []
    index = []
    for i in glob.glob(data_file + "*.asc"):
        print(f"{i}")
        with open(i) as f:
            d = f.readlines()
            d.pop(-1)
            # d[-1] = d[-1] + "\n"
            index.append(len(d))
            data_list.append(d)
            date_list.append(d[0].split(" ")[-2])
    # print(date_list)
    # print(data_list)
    print(index)
    sorted_times_with_index = sorted(enumerate(date_list), key=lambda x: x[1])
    sort_data_list = [data_list[ind] for ind, _ in sorted_times_with_index]
    sort_data_list = [item for sublist in sort_data_list for item in sublist]
    sorted_index = [index[ind] for ind, _ in sorted_times_with_index]
    print(sorted_index)
    for i, _ in enumerate(sorted_index):
        if i == len(sorted_index) - 1: continue
        else: sorted_index[i+1] = sorted_index[i+1] + sorted_index[i]
    # print(sorted_index)
    # print(sorted_times_with_index, sort_data_list)

    with open(res_file_path, 'w+') as file:
        for item in del_special_v(sort_data_list, sorted_index):
            file.write(item)
        file.write("end")

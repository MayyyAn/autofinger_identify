# 环境依赖
# pip install xlsxwriter


import csv
import os
import xlsxwriter


def count_list(list_data):
    """统计列表数值频率"""
    from collections import Counter
    result = Counter(list_data)
    return dict(result)


def list_data(data):
    # d = {'dd': 3, '11': 22}
    ret = list()
    for key, val in data.items():
        ret.append([key, val])
    return ret


class ReadCsv(object):
    def __init__(self):
        pass

    def read_all(self, file_name):
        """读取所有"""
        import csv
        result = list()
        with open(file_name, encoding='utf-8') as f:
            reader = csv.reader(f)
            for rows in reader:
                result.append(rows)
        return result

    def read_col(self, filename, col_name):
        """读取某一列"""
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            column = [row[col_name] for row in reader if row[col_name]]
        return column

    def read_row(self, row_name):
        """读取某一行"""
        pass


class WritCsv(object):
    def __init__(self, filename):
        self.filename = filename
        self.workbook = xlsxwriter.Workbook(self.filename)
        self.worksheet_chart = None

    def write_all(self, data, sheet_name=None):
        # 添加一个Sheet页，不添写名字，默认为文件名
        sheetname = (os.path.basename(self.filename)).replace('.csv', '')
        worksheet1 = self.workbook.add_worksheet(sheetname)
        # 写数据
        for i in range(0, len(data)):
            worksheet1.write_row("A{}".format(i + 1), data[i])

    def write_chart(self, headings, data, sheetname='Chart1'):
        self.worksheet_chart = self.workbook.add_worksheet(sheetname)
        # headings = ["姓名", "数学", "语文"]
        head_style = self.workbook.add_format({"bold": True, "bg_color": "yellow", "align": "center", "font": 13})
        # 写数据
        self.worksheet_chart.write_row("A1", headings, head_style)
        # worksheet_chart.write_row(data)  # data = [['xi',3], ['ss',2]]
        for i in range(0, len(data)):
            self.worksheet_chart.write_row("A{}".format(i + 2), data[i])

    def draw_histogram(self, colsname, rows_num, sheetname='Chart1', insert_index='D2', title_name='出现频率统计图',
                       y_name='累计次数', x_name='X轴'):
        """画柱状图"""
        chart = self.workbook.add_chart({"type": "column"})  # 添加柱状图
        chart.add_series({
            "name": "={}!$B$1".format(sheetname),  # 图例项
            # "name": colsname,                                                         # l列名
            "categories": "={}!$A$2:$A${}".format(sheetname, rows_num),  # X轴 Item名称
            "values": "={}!$B$2:$B${}".format(sheetname, rows_num)  # X轴Item值(y值；柱状高度)
        })
        # chart.add_series({
        #     "name": "=Sheet1!$C$1",
        #     "categories": "=Sheet1!$A$2:$A$4",
        #     "values": "=Sheet1!$C$2:$C$4"
        # })

        # 添加柱状图标题
        chart.set_title({"name": title_name})
        # Y轴名称
        chart.set_y_axis({"name": y_name})
        # X轴名称
        # chart.set_x_axis({"name": x_name})
        chart.set_x_axis({"name": colsname})
        # 图表样式
        chart.set_style(11)
        self.csv_insert_chart(self.worksheet_chart, row=insert_index, chart=chart)
        return True

    def dram_pie(self, rows_num, sheetname='Chart1', insert_index='D20', pie_name='出现频率统计图'):
        """饼图"""
        chart = self.workbook.add_chart({"type": "pie"})  # 添加饼图
        chart.add_series({
            # "name":"饼形图",
            "categories": "={}!$A$2:$A${}".format(sheetname, rows_num),
            "values": "={}!$B$2:$B${}".format(sheetname, rows_num),
            # 定义各饼块的颜色
            "points": [
                {"fill": {"color": "yellow"}},
                {"fill": {"color": "blue"}},
                {"fill": {"color": "red"}}
            ]
        })
        chart.set_title({"name": pie_name})
        chart.set_style(3)
        self.csv_insert_chart(self.worksheet_chart, row=insert_index, chart=chart)
        return True

    def csv_insert_chart(self, worksheet, row, chart, col=0):
        """
        插入图片
        :param row: 行
        :param col: 列
        :param chart: 图片对象
        :return:
        """
        # worksheet.insert_chart(row, col, chart)
        worksheet.insert_chart(row, chart)

    def write_rows_(self, row):
        pass

    def close(self):
        self.workbook.close()


def main_run(csv_file, col_name, new_filename=None):
    """程序入口"""
    # 读取
    read_obj = ReadCsv()
    all_data = read_obj.read_all(csv_file)
    col_data = read_obj.read_col(csv_file, col_name)
    chart_data = list_data(count_list(col_data))
    # 写入

    filename_ = os.path.basename(csv_file)
    new_filename = filename_ if new_filename is None else new_filename
    write_obj = WritCsv(filename=new_filename)
    write_obj.write_all(data=all_data)
    write_obj.write_chart(headings=[col_name, 'count'], data=chart_data)
    chart_data_len = len(chart_data)
    write_obj.draw_histogram(colsname=col_name, rows_num=(chart_data_len + 1), title_name=f'{col_name}柱状图')
    write_obj.dram_pie(rows_num=(chart_data_len + 1), pie_name=f'{col_name}饼图')
    write_obj.close()


if __name__ == '__main__':
    path = './header'
    file_name = os.listdir(path)
    for i in file_name:
        file_path = '' + path + '/' + i
        col_name=i.split('.')[0]
        new_filename=''+'./词频/'+i
        try:
            main_run(file_path, col_name, new_filename)
        except:
            print(file_path)
    # csv_file = r'./header/vary.csv'
    # col_name = 'vary'  # 需要提取的列名
    # new_filename = './词频/vary.csv'
    # main_run(csv_file, col_name, new_filename)


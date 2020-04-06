# -*- coding: utf-8 -*-
"""
@time: 2020/2/20 9:36
@author: pei.lu
"""
# python中与excel操作相关的模块：
#
# xlrd库：从excel中读取数据，支持xls、xlsx
# xlwt库：对excel进行修改操作，不支持对xlsx格式的修改
# xlutils库：在xlwt和xlrd中，对一个已存在的文件进行修改。
# openpyxl：主要针对xlsx格式的excel进行读取和编辑。

# 1.1 xlrd读excel
def excel_1():
    import xlrd
    file = "excel_dxtest.xlsx"
    book=xlrd.open_workbook(file)
    # sheet1=book.sheets()[1]
    sheetnum=book.nsheets # 有几个sheet页
    sheet1=book.sheet_by_name('test_2')
    nrows,ncols=sheet1.nrows,sheet1.ncols # sheet页的总行数、总列数
    row3_values=sheet1.row_values(2) # 返回第3行值
    col3_values=sheet1.col_values(2) # 返回第3列值
    cell_3_3=sheet1.cell_value(2,2) # 返回第3行第3列单元格的值
    print(book,sheetnum,sheet1,nrows,row3_values,cell_3_3,sep='\n')

# excel_1()

# 1.2 xlwt写excel
def excel_2():
    import xlwt
    workbook=xlwt.Workbook()
    worksheet=workbook.add_sheet('test')
    worksheet.write(0,0,'A1data')
    worksheet.write(1,2,'中文')
    worksheet.write(2,0,'wei=tsdf133')
    workbook.save('excelwrite.xls')

# 读文件后写新文件
def excel_3():
    import xlrd,xlwt
    file='excel_dxtest.xlsx'
    wb=xlrd.open_workbook(file)
    sh=wb.sheet_by_name('test_2')
    col5=sh.col_values(5)
    new_list=['data='+x for x in col5[1:]]
    # print(new_list)
    new_wb=xlwt.Workbook()
    new_sh=new_wb.add_sheet('gp2')
    for i,value in enumerate(new_list):
        new_sh.write(i,5,value)
    new_wb.save('new_data.xls')


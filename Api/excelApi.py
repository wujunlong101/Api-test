# -*- coding:utf-8 -*-
import xlrd
class excelApi():
    def excelRead(self,path,index=0):
        table=xlrd.open_workbook(path)
        shell=table.sheet_by_index(index)
        rowNum=shell.nrows
        colNum=shell.ncols
        firstRow=shell.row_values(0)
        dataList=[]
        for row in range(1,rowNum):
            disc = {}
            for col in range(colNum):
                disc[firstRow[col]]=shell.cell_value(row,col)
            dataList.append(disc)
        return dataList
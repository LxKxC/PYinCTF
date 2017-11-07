#!/usr/bin/env python  
# -*- coding:utf-8 -*- 
'''
本程序主要功能是打开指定文件，按行读取后并将符合条件的行写入到新的文件中。
使用的时候请把代码中的“input.txt”改成待处理文件的文件名，并记得将代码中的404改成自己的匹配条件。
你也可以自己修改代码来满足自己的特殊需求，如：
	按行编辑文件
	按行搜索带有指定字符串的文件
	按行对源文件进行加密
	按行对指定文件进行解密
	总之就是对各种文件进行按行处理
'''
import os
import linecache
import re
__author__="Kecheng"
__version__="1.0"
__qq__="741251720"
banner="SAVE404 v{0} by {1} (QQ:{2})".format(__version__, __author__, __qq__)
print "------------------------------------"
print banner
print "------------------------------------"
	
def clean():
	#------------------创建储存文件------------------------#
	if os.path.exists(r'out.txt')==False:   					#输出文件是否存在，如果不存在
		outfile=open('out.txt','w')        					    #创建输出文件
		outfile.close()                     					#创建后关闭文件
	#------------导入要整理的源文件并检测行数--------------#
	AddFile=os.getcwd()+r"\input.txt"							#设置待整理的文件（待整理的文件需要与该python程序同一个目录）
	count = -1                                            		#———————————————————#
	for count,line in enumerate(open(AddFile,'rU')): 	  		#计算待整理文件行数 #
		pass											  		# 				    #
	count += 1										   	  		#-——————————————————#
	#------------------开始整理----------------------------#
	outfile=open('out.txt','w')             					#打开输出文件准备往里面写数据
	for i in range(0,count+1):			    					#待整理文件有多少行，循环多少次
		TxtLine=linecache.getline(AddFile,i)					#读取待整理文件的第i行内容到TxtLine
		Check=TxtLine.find('404')           					#用find函数在TxtLine的内容中寻找我们指定的字符串404
		if Check > -1:                      					#如果找到了指定字符串404（find函数找到了404就返回404在TxtLine中第几位，找不到就返回-1）
			outfile.write(TxtLine)          					#将该行写入到out.txt文件中
		else:
			continue											#如果没找到，跳出此次循环，i+1进行下一次循环
	outfile.close()                         					#当所有符合条件的行都写入out.txt后，关闭out.txt文件
	
if __name__ == '__main__':
	clean()
			
		
		

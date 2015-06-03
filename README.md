# stockInCommandLine

在命令行使用python实时查看股市信息


====================================

#2015-05-30

基本功能：

1.	显示股票的的实时数据（昨收、今开、最高、最低、现价）
2.	显示相对于昨收价的涨跌颜色（昨收：白色；今开、最高、最低、现价、涨跌：红涨绿跌）


'\033[%dm' % xxx

xxx:

1：白色
2：灰色
4：下划线
5：闪动
7：黑底白字
8：隐形
31：红色
32：绿色
33：黄色
34：蓝色
35：粉色
36：亮蓝色
37：白色
40：黑底
41：红底
42：绿底
43：黄底
44：蓝底
45：粉底
46：亮蓝底
47：灰底
90：灰色
91：红色
92：绿色
93：黄色
94：蓝色
95：粉色
96：亮蓝色
97：白色
100：黑底
101：红底
102：绿底
103：黄底
104：蓝底
105：粉底
106：亮蓝底
107：灰底

====================================

#2015-05-31

mac osx下的文本操作键：http://my.oschina.net/kelvinline/blog/322671

python 字符encode 和 decode：http://blog.csdn.net/moodytong/article/details/8136258

print-in-terminal-with-colors-using-python：http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

ANSI escape code介绍:http://en.wikipedia.org/wiki/ANSI_escape_code

python 中获取当前时间：http://www.jb51.net/article/45657.htm

python 获取股票信息：http://blog.chinaunix.net/uid-20196333-id-1972442.html

新浪股票接口介绍：http://www.360doc.com/content/09/0823/00/70382_5161883.shtml

python 定时刷新：http://blog.csdn.net/lxlzhn/article/details/8940125

python 获取操作系统类型：http://www.cnblogs.com/itech/archive/2011/01/13/1934653.html

python 执行命令行清屏：http://www.cnblogs.com/maybego/p/3234055.html

增加功能：

1. 显示当前时间

2. 5s定时刷新

3. mac osx的Terminal.app清屏。其他操作系统没有测试。

====================================

#2015-06-03

增加功能：

1. 增加自选股票保存功能，在src目录下新建myStockInfo.txt用于保存自选股票，每行一只股票。

	————如果某股票没有交易内容，则只保存股票code信息。
	
	————如果某股票有交易内容，则保存code信息、交易股票数量、交易价格信息，三者之间以空格分隔。
	
2. 增加命令行add和delete自选股票功能，也可直接修改目录下的myStockInfo.txt文件来达到同样的目的。

	————如果是delete，则判断文件中是否存在该股票code，若有则删除，否则不做任何改变。
	
	————如果是add，若文件中是否存在该股票code，则覆盖原先信息，否则新增该股票及相关信息。
	
	————如果是其他命令或输入为其他不规范信息，则不做判断，此类操作可能会导致myStockInfo.txt文件内容出错。

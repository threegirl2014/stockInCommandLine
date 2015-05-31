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

python 中获取当前时间：http://www.jb51.net/article/45657.htm

python 获取股票信息：http://blog.chinaunix.net/uid-20196333-id-1972442.html

python 定时刷新：http://blog.csdn.net/lxlzhn/article/details/8940125

python 获取操作系统类型：http://www.cnblogs.com/itech/archive/2011/01/13/1934653.html

python 执行命令行清屏：http://www.cnblogs.com/maybego/p/3234055.html

增加功能：

1. 显示当前时间

2. 5s定时刷新

3. mac osx的Terminal.app清屏。其他操作系统没有测试。
import pymysql

#参数一：服务器IP
#参数二：端口号
#参数三：用户名
#参数四：用户密码
#参数五：数据库名
conn = pymysql.connect(host="192.168.10.237",port=3306,user="root",password="12345",db="7640onlineshop")

#创建一个cursor对象，由cursor对象执行SQL语句以及获得执行结果
cur = conn.cursor()
sql1 = "select * from Customer;"
sql2 = "select * from Store;"
sql3 = "select * from Item"
sql4 = "select * from cust_order_store"
sql5 = "select * from admin_store"
sql6 = "select * from storeowner_item"

cur.execute(sql1)
data1 = cur.fetchall() #fetchall()将所有结果赋值给data，fetchone()将第一个结果赋值给data
print(data1)

cur.execute(sql2)
data2 = cur.fetchall() 
print(data2)

cur.execute(sql3)
data3 = cur.fetchall()
print(data3)

cur.execute(sql4)
data4 = cur.fetchall() 
print(data4)

cur.execute(sql5)
data5 = cur.fetchall()
print(data5)

cur.execute(sql6)
data6 = cur.fetchall() 
print(data6)

#关闭cursor对象，然后关闭数据库连接
cur.close()
conn.close()
import matplotlib.pyplot as plt
import numpy as np
#--------------------------------------------
import spidev
import time
import argparse 
import sys
import navio.mpu9250FIFO
import navio.util
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import*
import matplotlib as mpl
import platform
#------------open SPI--------------------------
navio.util.check_apm()
imu = navio.mpu9250FIFO.MPU9250(0,0)
if imu.testConnection():
    print ("Connection established: True")
else:
    sys.exit("Connection established: False")
imu.initialize()
time.sleep(1)
imu.enableFIFO(True, 'acc')
#-----------------------------------------------

ax=[]   #保存图1数据
ay=[]
bx=[]   #保存图2数据
by=[]
cx=[]
cy=[]
num=0   #计数
plt.ion()    # 开启一个画图的窗口进入交互模式，用于实时更新数据
# plt.rcParams['savefig.dpi'] = 200 #图片像素
# plt.rcParams['figure.dpi'] = 200 #分辨率
plt.figure(num='PMC_3 Axis_Data Draw',figsize=(5, 4))
#plt.rcParams['figure.figsize'] = (2, 6)        # 图像显示大小
plt.rcParams['font.sans-serif']=['SimHei']   #防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 1   #设置曲线线条宽度


while num<101:
    plt.clf()    #清除刷新前的图表，防止数据量过大消耗内存
    
    #plt.suptitle("PMC ACC",fontsize=30)    #添加总标题，并设置文字大小
    #g1=np.random.random()  #生成随机数画图
    imu.read_acc()
    m9a = imu.accelerometer_data
    g1=float(m9a[0])
    print("g1=",g1)
    #图表1
    ax.append(num)      #追加x坐标值
    ay.append(g1)       #追加y坐标值
    agraphic=plt.subplot(3,1,1)
    
    #agraphic.set_title('ACC-X',fontsize=5)      #添加子标题
    #agraphic.set_xlabel('Count',fontsize=10)   #添加轴标签
    agraphic.set_ylabel('Vaule', fontsize=10)
    
    #agraghic.plot(ax,ay,'r^')           #Draw red trangle
    agraphic.plot(ax,ay,'g-',label='ACC-X')                #等于agraghic.plot(ax,ay,'g-')
    plt.legend(loc='upper right')    
    #图表2
    g2=float(m9a[1])
    print("g2=",g2)
    bx.append(num)
    by.append(g2)
    bgraghic=plt.subplot(3, 1, 2)
        #bgraghic.set_title('ACC-Y',fontsize=5)
    #bgraghic.plot(bx,by,'r^')
    bgraghic.plot(bx,by,'b-',label='ACC-Y')
    plt.legend(loc='upper right') 
    #图表3
    g3=float(m9a[2])
    print("g3=",g3)
    cx.append(num)
    cy.append(g3)
    cgraghic=plt.subplot(3, 1, 3)
    
    #cgraghic.set_title('ACC-Z',fontsize=5)
    #bgraghic.plot(bx,by,'r^')
    cgraghic.plot(cx,cy,'r-',label='ACC-Z')
    plt.legend(loc='upper right') 
    plt.pause(0.1)     #设置暂停时间，太快图表无法正常显示
    #if num == 15:
    #    plt.savefig('picture.png', dpi=300)  # 设置保存图片的分辨率
        #break
    num=num+1
    
    if(num==100):
        num=0
        ax=[]   #保存图1数据
        ay=[]
        bx=[]   #保存图2数据
        by=[]
        cx=[]
        cy=[]
        

plt.ioff()       # 关闭画图的窗口，即关闭交互模式
plt.show()       # 显示图片，防止闪退

'''
公式来源
https://www.waveformlighting.com/tech/calculate-color-temperature-cct-from-cie-1931-xy-coordinates
该网站给出的色温值感觉更接近远方公司测量软件给出的值
该网站使用的公式与IEC标准(IEC 61947-1:2002)中公式形式相同，但CCT计算公式中系数不同。 IEC为6831，网站为6861
计算公式：	n = (x-0.3320)/(0.1858-y)
			CCT = 437*n^3 + 3601*n^2 + 6861*n + 5517
'''

import math

# x = float(input('x=')) # 色坐标x
# y = float(input('y=')) # 色坐标y

#调试使用
x = 0.4278
y = 0.3958

z = 1 - x -y
print ('x=','%.4f' %x,  ','  ,\
       'y=','%.4f' %y,  ','  ,\
       'z=','%.4f' %z)
print ()

#计算及输出色温
def cct_cal():
    ratio_cct = (x - 0.3320) / (0.1858 - y) # 计算中间系数
    cct = 437 * ratio_cct ** 3 \
          + 3601 * ratio_cct ** 2 \
          + 6861 * ratio_cct \
          + 5517 # 计算色温
    cct_IEC = 437 * ratio_cct ** 3 \
              + 3601 * ratio_cct ** 2 \
              + 6831 * ratio_cct \
              + 5517 # 计算色温
    print ('(推荐) 远方公司测量软件计算色温为','%.1f'% cct,'K')
    print ('根据IEC 61947-1:2002计算色温为','%.1f'% cct_IEC,'K')
    print ()

#计算色容差
def sdcm_cal():
    cct_list = [8000,6500,5000,4000,3500,3000,2700]
    x0_list = [0.294,0.313,0.346,0.380,0.409,0.440,0.463]
    y0_list = [0.309,0.337,0.359,0.380,0.394,0.403,0.420]
    g11_list = [111e4,86e4,56e4,39.5e4,38e4,39e4,44e4]
    g12_list = [-56.5e4,-40e4,-25e4,-21.5e4,-20e4,-19.5e4,-18.6e4]
    g22_list = [54.5e4,45e4,28e4,26e4,25e4,27.5e4,27e4]

    for index_cct in range(0,7):
        delta_x = x - x0_list[index_cct]
        delta_y = y - y0_list[index_cct]
        g = g11_list[index_cct] * delta_x ** 2 \
            + 2 * g12_list[index_cct] * delta_x * delta_y \
            + g22_list[index_cct] * delta_y ** 2
        sdcm =math.sqrt(g)
        print ('与',cct_list[index_cct],'K标准色温之间的色容差为 ','%.1f' % sdcm,' SDCM',sep='')

#计算u,v坐标
def uv_cal():
    u = 4 * x / (3 + 12 * y -2 * x)
    v = 6 * y / (3 + 12 * y -2 * x)
    print ('u=','%.4f' % u,end=',  ')
    print ('v=','%.4f' % v)
    print ()

uv_cal()
cct_cal()
sdcm_cal()
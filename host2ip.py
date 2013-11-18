#!/usr/local/bin/python  

02 #-*- coding: UTF-8 -*-  

03 ####################################################################  

04 #qq:316118740  

05 #BLOG:http://hi.baidu.com/alalmn  

06 # python 域名转IP 在查看制定端口是否开放  

07 #  刚学写的不好请大家见谅  

08 ####################################################################  

09    

10 import socket  

11 #获取域名的IP地址  

12 def www_ip(name):  #域名转IP  

13     try:  

14         result = socket.getaddrinfo(name, None)  

15         return result[0][4][0]  

16     except:  

17         return 0 

18    

19 def ip_port(ip):  #查看IP端口是否开放  

20     port=21 

21     s=socket.socket()  

22     #address="127.0.0.1"  

23     try:  

24         s.connect((ip,port))  

25         #print 'IP:',ip,"port:",port,"以开放"  

26         return 1 

27     except socket.error,e:  

28         #print 'IP:',ip,"port:",port,"未开放"  

29         return 0 

30    

31 if __name__=='__main__':  

32     www= "www.163.com" 

33     IP=www_ip(www)  

34     if IP:  

35         print www,"ip地址：",IP  

36         if ip_port(IP):  

37             print IP,"开放21端口" 

38         else:  

39             print IP,"未开21放端口" 

40     else:  

41         print www,"域名转IP失败" 

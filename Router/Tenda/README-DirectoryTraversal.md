Directory Traversal can only be used in LAN but it doesn't need any authentication.

Tenda ARCH:arm

usage: 

- Ac series Directory Traversal.py ip port path

some problems: 

- port means nginx's open port,not httpd


Here are the details of Directory Traversal:

[Vulnerability]:

Directory Traversal

-----------------------------

[Exploitation]:

Walk through the file system

-----------------------------

[Vendor of Product]:

Tenda wireless router

-----------------------------

[Affected Products and firmware version]:

Ac9   US_AC9V1.0BR_V15.03.05.14_multi_TD01

Ac9   ac9_kf_V15.03.05.19(6318_)_cn

Ac15  US_AC15V1.0BR_V15.03.05.18_multi_TD01

Ac15  US_AC15V1.0BR_V15.03.05.19_multi_TD01

Ac18  US_AC18V1.0BR_V15.03.05.05_multi_TD01

Ac18  ac18_kf_V15.03.05.19(6318_)_cn

-----------------------------

[Attack Type]:

Remote

-----------------------------

[Rerference]:

https://github.com/Iolop/Poc/tree/master/Router/Tenda

-----------------------------

[Discoverer]:

Zixin Wang, Sichuan Silent Information Technology Co.,Ltd http://www.silence.com.cn/

-----------------------------

[Affected components]:

Affected executable application: app_data_center

-----------------------------

[Vulnerability description]:

Directory Traversal vulnerability in Shenzhen Tenda Technology Tenda's Ac series routers with firmware which was released recently 

allows remote unauthenticated attackers to walk through file system in LAN from a crafted GET request.

-----------------------------

[Vulnerability details]:

In vulnerable function:

It doesn't filter the string delivered by the user

...

```c

  if ( point_at_path && !strncmp(point_at_path, "/usb/", 5u) )

  {

    sprintf((char *)&v14, "%s%s", 0x1AF0C, v12 + 5, v11);// sprintf(..../var/etc/upan,point_at_path)

    dirp = opendir((const char *)&v14);
    
    if ( dirp )

```

...

-----------------------------

[exp.py]

check the Ac series Directory Traversal.py



Command injection and FS walk though can only be used in LAN but they don't need any authentication.

Tenda ARCH:arm

support:wget telnetd iptables

usage: 

- Ac series Command Injection.py ip port cmd
- Ac series File System walk through.py ip port path

some problems: 

- FS walk through can't read the file,it looks like another 'ls' command.
- port means nginx's open port,not httpd


Here are the details of Command Injection:

[Vulnerability]:

Command Injection

-----------------------------

[Exploitation]:

Execute arbitraty OS commands

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

[Can Cause Denial of Service?]:

yes

-----------------------------

[Rerference]:

https://github.com/Iolop/Poc/tree/master/Router/Tenda

-----------------------------

[Discoverer]:

Zixin Wang, pkav of Sichuan Silent Information Technology Company Ltd, http://www.silence.com.cn/

-----------------------------

[Affected components]:

Affected executable application: app_data_center

Affected function: sub_A6E8  usbeject_process_entry(int processed_string,int a2)

-----------------------------

[Vulnerability description]:

Command Injection vulnerability in Shenzhen Tenda Technology Tenda's Ac series routers with firmware which was released recently 

allows remote unauthenticated attackers to execute arbitrary OS commands in LAN from a crafted GET request.

-----------------------------

[Vulnerability details]:

In sub_A6E8 function:

It doesn't filter the string delivered by the user

...
`
if( v6 && *(_BYTE *)v6 )

{

    sub_A510(v6);

    snprintf((char *)&v5, 0x800u, "cfm post netctrl 51?op=3,string_info=%s", v6, v4);

    system((const char *)&v5);
    
}
`
...

-----------------------------

[exp.py]

check the Ac series Command Injection.py



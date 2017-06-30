Title: RHEL添加Centos源
Date: 2015-02-08 10:20
Category: blog
Tags: linux
Slug: rhel-centos-yum
Authors: Yuk Wong


#RHEL添加Centos源

## 添加yum代理
/etc/yum.conf

```
proxy=http://10.102.66.2:30001
# The account details for yum connections
proxy_username=sin
proxy_password=sin1234

```

## 删除redhat自带软件包

```
[root@linuxprobe ~]# rpm -qa | grep yum
yum-utils-1.1.31-24.el7.noarch
yum-langpacks-0.4.2-3.el7.noarch
yum-metadata-parser-1.1.4-10.el7.x86_64
yum-rhn-plugin-2.0.1-4.el7.noarch
PackageKit-yum-0.8.9-11.el7.x86_64
yum-3.4.3-118.el7.noarch

[root@linuxprobe ~]# rpm -e yum-3.4.3-118.el7.noarch --nodeps
[root@linuxprobe ~]# rpm -e yum-utils-1.1.31-24.el7.noarch --nodeps
[root@linuxprobe ~]# rpm -e yum-rhn-plugin-2.0.1-4.el7.noarch --nodeps
[root@linuxprobe ~]# rpm -e yum-metadata-parser-1.1.4-10.el7.x86_64 --nodeps
[root@linuxprobe ~]# rpm -e yum-langpacks-0.4.2-3.el7.noarch --nodeps
[root@linuxprobe ~]# rpm -e PackageKit-yum-0.8.9-11.el7.x86_64 --nodeps
```

## 下载对应的CentOS软件包
```
[root@Linuxprobe ~]# wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-3.4.3-118.el7.centos.noarch.rpm
--2016-01-17 20:43:15--  http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-3.4.3-118.el7.centos.noarch.rpm
Resolving mirrors.163.com (mirrors.163.com)... 123.58.173.185, 123.58.173.186
Connecting to mirrors.163.com (mirrors.163.com)|123.58.173.185|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2016-01-17 20:43:15 ERROR 404: Not Found.   //如果找不到，是安装包更新了，你可以到这个网站http://mirrors.163.com/centos/7/os/x86_64/Packages/复制下载链接，然后再下载下来；

[root@linuxprobe ~]# wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-3.4.3-132.el7.centos.0.1.noarch.rpm
[root@linuxprobe ~]# wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-metadata-parser-1.1.4-10.el7.x86_64.rpm
[root@linuxprobe ~]# wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-utils-1.1.31-34.el7.noarch.rpm 
[root@linuxprobe ~]# wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-updateonboot-1.1.31-34.el7.noarch.rpm
[root@linuxprobe ~]# wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-plugin-fastestmirror-1.1.31-34.el7.noarch.rpm

[root@linuxprobe ~]# ls
yum-3.4.3-132.el7.centos.0.1.noarch.rpm
yum-metadata-parser-1.1.4-10.el7.x86_64.rpm
yum-plugin-fastestmirror-1.1.31-34.el7.noarch.rpm
yum-updateonboot-1.1.31-34.el7.noarch.rpm
yum-utils-1.1.31-34.el7.noarch.rpm
```

## 安装

```
[root@Linuxprobe ~]# rpm -ivh yum-*
warning: yum-3.4.3-132.el7.centos.0.1.noarch.rpm: Header V3 RSA/SHA256 Signature, key ID f4a80eb5: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
1:yum-metadata-parser-1.1.4-10.el7    ################################# [ 20%]
2:yum-plugin-fastestmirror-1.1.31-3   ################################# [ 40%]
3:yum-3.4.3-132.el7.centos.0.1        ################################# [ 60%]
4:yum-updateonboot-1.1.31-34.el7      ################################# [ 80%]
5:yum-utils-1.1.31-34.el7             ################################# [100%]
```

##新建repo 配置文件

```
[root@linuxprobe ~]# vim /etc/yum.repos.d/CentOS-Base.repo
#CentOS-Base.repo
#
# The mirror system uses the connecting IP address of the client and the
# update status of each mirror to pick mirrors that are updated to and
# geographically close to the client.  You should use this for CentOS updates
# unless you are manually picking other mirrors.
#
# If the mirrorlist= does not work for you, as a fall back you can try the
# remarked out baseurl= line instead.
#
#
[base]
name=CentOS-$7 - Base - 163.com
#mirrorlist=http://mirrorlist.centos.org/?release=$7&arch=$basearch&repo=os
baseurl=http://mirrors.163.com/centos/7/os/$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7

#released updates
[updates]
name=CentOS-$7 - Updates - 163.com
#mirrorlist=http://mirrorlist.centos.org/?release=$7&arch=$basearch&repo=updates
baseurl=http://mirrors.163.com/centos/7/updates/$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7

#additional packages that may be useful
[extras]
name=CentOS-$7 - Extras - 163.com
#mirrorlist=http://mirrorlist.centos.org/?release=$7&arch=$basearch&repo=extras
baseurl=http://mirrors.163.com/centos/7/extras/$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7

#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$7 - Plus - 163.com
baseurl=http://mirrors.163.com/centos/7/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7
```

## 测试并安装
```
[root@linuxprobe ~]# yum clean all 

[root@Linuxprobe ~]# yum -y install w3m
```



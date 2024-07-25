# Rules

## 简介

**广告过滤、代理规则和网易云解锁规则**，利用Github Actions定时自动合并，适用于Shadowrocket。网易云解锁请结合[nondanee/UnblockNeteaseMusic](https://github.com/nondanee/UnblockNeteaseMusic)食用。

## 食用方法

### 1. 首先在shadowrocket上添加好网易云的解锁节点

#### 自建解锁节点

首先根据[nondanee/UnblockNeteaseMusic](https://github.com/nondanee/UnblockNeteaseMusic)里的教程设置好解锁节点，然后在Shadowrocket里添加。（仔细阅读原项目issue: [iOS配置经验分享](https://github.com/nondanee/UnblockNeteaseMusic/issues/368)）

<img src="https://cdn.jsdelivr.net/gh/xiangsanliu/images@master/uPic/2021-03-10T13:10:16.jpeg" width="200" alt=""/>

> ❗️注意节点名称需要和[UnblockNeteaseMusic.conf](UnblockNeteaseMusic.conf)里的名称相同。

#### 使用DesperadoJ大佬的节点 

大佬的仓库地址：[DesperadoJRules-for-UnblockNeteaseMusic](https://github.com/DesperadoJ/Rules-for-UnblockNeteaseMusic)，在里面找`Shadowrocket/shadowrocket-server.txt`
。

> ❗️注意节点名称需要和[UnblockNeteaseMusic.conf](UnblockNeteaseMusic.conf)里的名称相同。
> 
> 也可以使用我从DesperadoJ大佬那转换好的节点：[node.txt](https://cdn.jsdelivr.net/gh/xiangsanliu/Rules/node.txt)

### 2. 安装解锁模块

模块地址：`https://cdn.jsdelivr.net/gh/xiangsanliu/Rules/sgmodule/netease.sgmodule`

安装步骤：`Shadowrocket -> 模块 -> 右上角+号`，在输入框中粘贴，再点击确定。

> ❗️经过反复试验，似乎开启MITM后，解锁不生效。




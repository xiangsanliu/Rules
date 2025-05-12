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

## 自定义开发

### 1. fork本项目

### 2. 设置自动更新

#### 2.1 设置GITHUB_TOKEN

到个人GitHub Setting > Developer settings > Personal access tokens > Generate new token,设置名字为GITHUB_TOKEN, 然后勾选repo, admin:
repo_hook, workflow，最后点击Generate token即可。 (
Thank [Github Actions教程](https://cloud.tencent.com/developer/article/1643440))

#### 2.2 运行一次workflow

点击仓库下面的`Actions` > `Auto update` > `Run workflow` > `Run workflow`

### 3. Do something.

## 模块地址

### 网易云解锁模块
`https://cdn.jsdelivr.net/gh/xiangsanliu/Rules/sgmodule/netease.sgmodule`

### 广告屏蔽模块
`https://cdn.jsdelivr.net/gh/xiangsanliu/Rules/sgmodule/ad.sgmodule`

## 关于广告屏蔽

这里比较认同[SS-Rule-Snippet#关于广告屏蔽的观点](https://github.com/Hackl0us/SS-Rule-Snippet#%E5%85%B3%E4%BA%8E%E5%B9%BF%E5%91%8A%E5%B1%8F%E8%94%BD)，专门的事交给专业的人去做。

本项目每天都会自动从其他大佬同步广告过滤，但是规则太庞大了，在我编辑的现在(2021.06.02)就有4w+条去广告规则，再加上小火箭这款工具每次匹配是会索引整个规则文件的，这会降低运行效率，反而得不偿失。

## 感谢

广告过滤、直连代理、音乐解锁规则转换自：

- [anti-AD](https://anti-ad.net)
- [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules)
- [DesperadoJ/Rules-for-UnblockNeteaseMusic](https://github.com/DesperadoJ/Rules-for-UnblockNeteaseMusic)
- [lhie1/Rules](https://github.com/lhie1/Rules/tree/master)

规则转换代码参考：

- [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules)

> 今天刚刚得知[h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules)项目已停止维护，故本项目中的[merge-h2y.conf](merge-h2y.conf)也只能停更了。
> --- 2021-04-13

> [lhie1/Rules](https://github.com/lhie1/Rules/tree/master) 仓库被禁用了，不知道什么时候能恢复，所以[merge-lhie1.conf](merge-lhie1.conf)也暂时停更了。
> --- 2022-02-02

> 纯python小白，写的脚本很简单，欢迎批评指正。


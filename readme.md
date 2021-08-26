# NanaChat-Core

## Dependencies 前期调研

### mirai & mirai-api-http

Mirai 是一个在全平台下运行，提供 QQ Android 和 TIM PC 协议支持的高效率机器人框架.

https://github.com/project-mirai/mirai-api-http

#### 下载与设置守护进程

+ 安装 Java 运行时 `sudo apt install openjdk-11-jre`
+ 下载 MCL，安装 mirai-api-http
+ 登录 Bot（使用 QQ 浏览器验证？使用 QQ 打开链接即可）
  + 如果有需要的话可以安装验证码库
+ 设置为自动登录

+ 配置 supervisor

```conf
[program:mcl]
command=/home/ftpuser/5050-mcl/mcl-1.2.2/mcl
autostart=true
autorestart=true
user=root
```



### Brainstorming 项目构思

我们可以考虑采用 http 和 webhook 两种 adapter，分别模拟主动发信和事件处理.

```mermaid
graph TB
    subgraph "NanaChat (Daemon)"
        nCore["NanaChat-Core (Port 5052)"]
        nPlugin[NanaChat-Plugins]
    end
    
    subgraph "Mirai-api-http (Daemon)"
    	ha["HTTP Adapter (Port 5050)"]
    	wa["Webhook Adapter (Port 5051)"]
    end
    
    wa-->|"收信 [1]"|nCore
    nCore --> |"自主发信 [2]"| ha
    nCore --> |"回复收信 [1]"|wa
    nCore --> nPlugin
    nPlugin --> nCore

```

```mermaid
graph TD;
ncore[NanaChat-Core]
s[Scheduler<br/>定时事件]
d[Dispatcher<br/>向HTTP Adapter发送消息]
l[Listener<br/>监听端口<br/>发送事件信号]
pm[PluginManager<br/>管理插件<br/>协助注册监听器与调度器]
ncore --> l
ncore --> s
ncore --> d
ncore --> pm
```

## Docs

### Nana-Core

### Nana-Plugins

注册 Nana-Core::Listener

使用 Nana-Core::Dispatcher

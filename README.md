<h1 align="center">Nonebot Plugin GsCalendar</h1></br>


<p align="center">🤖 用于展示原神活动日历的 Nonebot2 插件</p></br>


<p align="center">
  <a href="https://github.com/monsterxcn/nonebot-plugin-gscalendar/actions">
    <img src="https://img.shields.io/github/workflow/status/monsterxcn/nonebot-plugin-gscalendar/Build%20distributions?style=flat-square" alt="actions">
  </a>
  <a href="https://raw.githubusercontent.com/monsterxcn/nonebot-plugin-gscalendar/master/LICENSE">
    <img src="https://img.shields.io/github/license/monsterxcn/nonebot-plugin-gscalendar?style=flat-square" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-gscalendar">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-gscalendar?style=flat-square" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.7.3+-blue?style=flat-square" alt="python"><br />
</p></br>


**安装方法**


> 不知道 `nonebot2.0.0b3` 用起来效果如何，因为我还在用 `nonebot2.0.0a16` 捏，大伙可以试试看。


使用以下命令安装 Nonebot Plugin GsCalendar 插件：


```bash
# 从 Git 安装
git clone https://github.com/monsterxcn/nonebot-plugin-gscalendar.git
cd nonebot-plugin-gscalendar
# 将文件夹 utils 复制到 Nonebot2 根目录下
cp -r utils /path/to/nonebot/
# 将文件夹 nonebot_plugin_gscalendar 复制到 Nonebot2 插件目录下
cp -r nonebot_plugin_gscalendar /path/to/nonebot/plugins/
```


重启 Bot 即可体验此插件。


<details><summary><i>插件生成图片样式</i></summary></br>


<img src="https://user-images.githubusercontent.com/22407052/175922303-f9577f3f-87fc-4c29-824f-1a031019b1c7.PNG" height="700px">


用 JavaScript 小改了一下样式，让活动图片看起来不至于太小


</details>


**使用方法**


触发此插件的指令有： `日历`、`活动`、`calendar`。


**特别鸣谢**


[@nonebot/nonebot2](https://github.com/nonebot/nonebot2/) | [@Mrs4s/go-cqhttp](https://github.com/Mrs4s/go-cqhttp) | [@NepPure/calendar.neptunia.vip](https://github.com/NepPure/calendar.neptunia.vip)


> 感谢 [@NepPure/calendar.neptunia.vip](https://github.com/NepPure/calendar.neptunia.vip)，完全不用自己写 API 查询、设计图片样式了，斯巴拉西~

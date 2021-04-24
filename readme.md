# 项目说明

- `AccountInfo.ini` 配置文件，用来保存收发邮箱信息和邮箱key（只支持QQ邮箱）、爬取网站的网址和正则表达式的base64编码
- `index.py` 完成自动提交的py脚本，如果需要对匹配的结果进行筛选，需要自己修改文件的35行for循环里的内容

# 使用方式

### 配合腾讯云函数使用（免费）

1. clone 或者 下载 此仓库到本地

   ```
   git clone https://github.com/HPShark/tongzhipachong.git
   ```

2. 打开本地仓库文件夹，配置`AccountInfo.ini`中对应的信息

4. 点左边的函数服务，新建云函数，名称随意，运行环境选择`python3.6`，创建方式选择空白函数，然后点击下一步 [![新建腾讯云函数](https://github.com/ZimoLoveShuang/auto-submit/raw/master/screenshots/a971478e.png)](https://github.com/ZimoLoveShuang/auto-submit/blob/master/screenshots/a971478e.png)

5. 提交方法选择上传本地压缩包，把本地的AccountInfo.ini，index.py上传，在点击下面的高级设置，设置内存为256M，超时时间为`30秒`，添加层为刚刚新建的函数依赖层，环境变量设置一个`TZ=Asia/Shanghai`，然后点击完成

6. 进入新建好的云函数，左边点击触发管理，点击创建触发器，名称随意，触发周期选择自定义，然后配置cron表达式。下面的表达式表示每天中午十二点整执行，可配置多个时间以便早中晚自动运行

   ```
   0 0 12 * * * *
   ```

7. 然后就可以测试云函数了，绿色代表云函数执行成功，红色代表云函数执行失败（失败的原因大部分是由于依赖造成的）。返回结果是`auto submit fail.`代表自动提交失败；返回结果是`auto submit success.`，代表自动提交成功，如遇到问题，请仔细查看日志

8. enjoy it!

9. 也可配合Windows计划任务或者使用linux定时任务，将脚本挂在自己的云服务器上，不会就搜索一下，过程不再赘述




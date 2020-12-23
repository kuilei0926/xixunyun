
### 前言
为了让同学们更加认真、更加专注听课，而不去用手机签到花费大量时间、耗费大量精力，请自行合理使用！请点击下方View all of README.md了解更多。

本项目支持习讯云的签到，可以自定义位置。

本脚本最大的不同应该就是基于github action运行，所以并不需要服务器、不需要服务器、不需要服务器同样也不需要掌握任何python的相关设置，你所需要准备的就是一个github账号以及一个耐而不烦的心。傻瓜式的操作却可以解决你最大的痛苦。

### 特点
1、本项目支持任何形式的习讯云签到。<br>
2、基于server酱使得签到成功时会将签到信息发送至你的微信。<br>
2、无需挂在任何服务器上，只需要点几下，让github自动为你签到。<br>
3、使用强大的GitHub actions功能，实现无服务器实时监控您的习讯云签到。<br>
4、无需掌握任何编程知识，强大的后端后端已做好，您仅需点击几下。



## 快速使用


- Fork本项目后进入自己的仓库，点击你的仓库右上角的 Settings，找到 Secrets
    <details>
   <summary> 如何Fork本项目？</summary>
   注册或登陆您的github账号，访问<https://github.com/kuilei0926/xixunyun>进入github的本项目页面中，点击右上角的Fork按钮，如图所示。
   
   ![image](https://raw.githubusercontent.com/kuilei0926/xixunyun/main/img/QQ%E6%88%AA%E5%9B%BE20201222092433.png)
   
   </details>
-  fork后进入你自己的仓库并在setting配置您的习讯云账号信息
    <details>
   <summary> 如何配置？</summary>
   1.首先进入自己的仓库（前提您已经登陆账号）
	
   ![image](https://raw.githubusercontent.com/kuilei0926/xixunyun/main/img/QQ%E6%88%AA%E5%9B%BE20201222092434.png)
   <br><br><br>
   2.点击xixunyun字样的项目也就是刚刚fork后的项目
   
   ![image](https://raw.githubusercontent.com/kuilei0926/xixunyun/main/img/QQ%E6%88%AA%E5%9B%BE20201222092541.png)
   <br><br><br>
   3.点击setting进入设置界面
   
   ![image](https://raw.githubusercontent.com/kuilei0926/xixunyun/main/img/QQ%E6%88%AA%E5%9B%BE20201222092707.png)
   <br><br><br>
   4.点击secrets后点击add a new secret
   
   ![image](https://raw.githubusercontent.com/kuilei0926/xixunyun/main/img/QQ%E6%88%AA%E5%9B%BE20201222092844.png)
   <br><br><br>
   依次添加以下所有name以及value。<br>
    ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉ <br>
     Name:<code>USER</code><br>
     Value：<code>填写你的习讯云账号密码和学校ID,用空格或者空行分开</code><br>
   ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>
     Name：<code>SIGN_GPS</code><br>
     Value：<code>填写签到的GPS坐标</code><br>
    ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>
     Name：<code>ADDRESS_NAME</code><br>
     Value：<code>签到地址名字</code><br>
    ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>
     Name：<code>SCKEY</code><br>
     Value：<code>填写你的server酱SCKEY码，以SCU开头</code>#申请地址http://sc.ftqq.com/3.version  <br>
      ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>配置完后如下图所示

   ![image](https://raw.githubusercontent.com/kuilei0926/xixunyun/main/img/QQ%E6%88%AA%E5%9B%BE20201222093054.png)<br>
	关于如何获取坐标
	例如[0.123456,0.123456]，先经度后纬度，可以去 https://lbs.amap.com/console/show/picker 高德取坐标，直接把结果复制到[]里即可
	每家坐标拾取器标准不同，本脚本采用XY轴坐标格式。例如北京[116.000000,40.000000]<br>
	关于学校ID
	可以前往 https://api.xixunyun.com/login/schoolmap 查询，比如山东商务职业学院ID为222<br>
    </details>
- 设置好环境变量后点击你的仓库上方的 Actions 选项，会打开一个如下的页面，点击 `I understand...` 按钮确认在 Fork 的仓库上启用 GitHub Actions 。
- 最后在你这个 Fork 的仓库内随便改点什么（比如给 README 文件删掉或者增加几个字符）提交一下手动触发一次 GitHub Actions 就可以了 **（重要！！！测试发现在 Fork 的仓库上 GitHub Actions 的定时任务不会自动执行，必须要手动触发一次后才能正常工作）** 。
   <details>
   <summary> 如何随意修改README文件？</summary>
   
   1.进入你的仓库并进入code界面,点击笔字的按钮进入编写
    ![image](https://raw.githubusercontent.com/kuilei0926/xixunyun/main/img/QQ%E6%88%AA%E5%9B%BE20201222095234.png)
   2.在代码框随意编写或删减以达到改变代码的效果，随后点击提交commit，当然如果可以让说明书更精美欢迎来pull
    ![image](https://raw.githubusercontent.com/kuilei0926/xixunyun/main/img/QQ%E6%88%AA%E5%9B%BE20201222095347.png)

   </details>
   
- <details>
   <summary> 如何查看脚本执行情况？</summary>
   注意： 为了实现某个链接/帐户访问出错时不中断程序继续尝试下一个，GitHub Actions 的状态将永远是“通过”（显示绿色的✔），请自行检查 GitHub      Actions 日志：依次点击<code>Actions</code>=><code>chaoxing</code>=><code>get_points</code>=><code>Qiandao</code>项的输出确定程序执行情况。
	
    ![image](https://github.com/kuilei0926/xixunyun/blob/main/img/QQ%E6%88%AA%E5%9B%BE20201222095901.png?raw=true)
   </details>





## 配置说明
- 配置自动执行时间
时间配置在`xixunyun/.github/workflows/sign.yml`文件中 第九行    `- cron: '* * * * *'`
默认：每天早上八点自动执行签到脚本（github有时间延迟与相应限制），你也可以通过 `Push` 操作手动触发执行。
如需自定义时间，请配合[cron表达在线生成器](https://cron.clost.net "cron表达在线生成器")使用



## 关于

本项目遵循GNU GPLv3开源协议；并有以下条款特此说明：
1. 请勿使用本项目进行商业用途
1. 请勿使用本项目违反当地法规
1. 请勿使用本项目损害他人或集团利益

以上条款，若使用者违反，后果自行承担与作者本人无关！




## 紧急通知

请一定要根据配置说明配置计划时间；防止被判定滥用。
<br>
由于本项目被大量fork并启动actions功能，占用github官方服务器大量资源。部分用户反映无法签到，actions功能被禁止等问题。但是大部分用户仍然正常可以使用；解决方法：1.使用使用Travis Ci运行。学业繁忙，不予教程。2.请访问我的服务器http://www.baidu.com/ 但并不保证其稳定性。3.用自己的服务器运行其中的py脚本。


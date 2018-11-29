### 12306

- python版本支持
  - 2.7
- 依赖库
  - 依赖打码兔 需要去打码兔注册（用户）账号，打码兔账号地址：http://www.dama2.com，一般充值1元就够用了，充值打码兔之后，首次运行是需要到官网黑白名单授权
  - 依赖若快 若快注册地址：http://www.ruokuai.com/client/index?6726 推荐用若快，打码兔在12306验证码更新之后识别率不是很高
  - 项目依赖包 requirements.txt
  - 安装方法 pip install -r requirements.txt

- 项目使用说明
  - 需要配置邮箱，可以配置可以不配置，配置邮箱的格式在yaml里面可以看到ex
  - 提交订单验证码哪里依赖打码兔，所以如果是订票遇到验证码的时候，没有打码兔是过不了的，不推荐手动，手动太慢
  - 配置yaml文件的时候，需注意空格和遵循yaml语法格式，项目的yaml配置ex：
      - ticket_config.yaml 配置说明
        ```
        #station_date:出发日期改为多日期查询，格式ex：
                        - "2018-02-03"
                        - "2018-02-04"
                        - "2018-02-05"
        #station_trains:过滤车次，格式ex：
                        #    - "G1353"
                        #    - "G1329"
                        #    - "G1355"
                        #    - "G1303"
                        #    - "G1357"
                        #    - "G1305"
                        #    - "G1359"
                        #    - "G1361"
                        #    - "G1373"
                        #    - "G1363"
        #from_station: 始发站
        #to_station: 到达站
        #set_type: 坐席(商务座,二等座,特等座,软卧,硬卧,硬座,无座)
        #is_more_ticket:余票不足是否自动提交
        #select_refresh_interval:抢票刷新间隔时间，1为一秒，0.1为100毫秒，以此类推 如果捡漏推荐为1秒，刷票设置0.01
        #expect_refresh_interval:售票未开始，等待刷新间隔时间，1为一秒，0.1为100毫秒，以此类推
        #ticket_black_list:加入小黑屋的等待时间，默认3 min    小黑屋的功能是上次买票失败，证明此票已无机会，下次刷新看到此票跳过
        #enable_proxy:是否开启代理模式，代理速度比较慢，如果是抢票阶段，不建议开启
        #ticke_peoples: 乘客 ex: "张三"
        #damatu：打码兔账号，用于自动登录和订单自动打码
        #is_aotu_code是否自动打码，如果选择Ture,则调用打码兔打码，默认不使用打码兔
        #is_email: 是否需要邮件通知 ex: True or False 切记，邮箱加完一定到config目录下测试emailConf功能是否正常

        #邮箱配置 列举163
        #  email: "xxx@163.com"
        #  notice_email_list: "123@qq.com"
        #  username: "xxxxx"
        #  password: "xxxxx
        #  host: "smtp.163.com"
        #邮箱配置 列举qq  ，qq设置比较复杂，需要在邮箱--账户--开启smtp服务，取得授权码==邮箱登录密码
        #  email: "xxx@qq.com"
        #  notice_email_list: "123@qq.com"
        #  username: "xxxxx"
        #  password: "授权码"
        #  host: "smtp.qq.com"
        ```

- 项目开始
  - 修改config/ticket_config.yaml文件，按照提示更改自己想要的信息
  - 运行根目录run.py，即可开始

- 目录对应说明
  - agency - cdn代理
  - config - 项目配置
  - damatuCode - 打码兔接口
  - init - 项目主运行目录
  - myException - 异常
  - myUrllib - urllib库


- 成功log，如果是购票失败的，请带上失败的log给我，我尽力帮你挑，也可加群一起交流，程序只是加速买票的过程，并不一定能买到票
    ```
    正在第355次查询  乘车日期: 2018-02-12  车次G4741,G2365,G1371,G1377,G1329 查询无票  代理设置 无  总耗时429ms
    车次: G4741 始发车站: 上海 终点站: 邵阳 二等座:有
    正在尝试提交订票...
    尝试提交订单...
    出票成功
    排队成功, 当前余票还剩余: 359 张
    正在使用自动识别验证码功能
    验证码通过,正在提交订单
    提交订单成功！
    排队等待时间预计还剩 -12 ms
    排队等待时间预计还剩 -6 ms
    排队等待时间预计还剩 -7 ms
    排队等待时间预计还剩 -4 ms
    排队等待时间预计还剩 -4 ms
    恭喜您订票成功，订单号为：EB52743573, 请立即打开浏览器登录12306，访问‘未完成订单’，在30分钟内完成支付！
    ```

- 注意说明：
    软件还不能自动化识别验证码可以选择手动输入验证码编号（1～8），本代码中使用打码兔或者若快的图片打码可靠性不能保证100%，目前正在研究
    百度AI的第三方库图片识别，期待中。。。。。。

- 后续开发需求：
    开发界面版操作



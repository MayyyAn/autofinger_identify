import json
import os
from pyecharts import options as opts
from pyecharts.charts import Page, Tree

data = [
    {
        "name": "root", "value": 88640347, "children": [
        {"name": "server==nginx", "value": 13730856, "children": [
            {"name": "body=\"value=\"5000\"\"", "value": 136270, "children": [
                {"name": "Keep-Alive: timeout=20", "value": 132354, "children": [
                    {"name": "Content-Length: 513", "value": 70184, "children": [
                        {"name": "Syolongy NAS网络存储", "value": 70184}]}]}]},
            {"name": "X-Timezone: 8", "value": 72025, "children": [
                {"name": "ikuai 路由器", "value": 72025}]},
            {"name": "X-Timezone: 0800", "value": 412121, "children": [
                {"name": "ikuai 路由器", "value": 412121}]},
            {'name': 'icon:"d8d7c9138e93d43579ebf2e384745ba8"', 'value': 39787, 'children': [
                {"name": "Content-Length: 7194", "value": 4616, "children": [
                    {"name": "锐捷 NBR路由器", "value": 4616}]},
                {"name": "Content-Length: 7201", "value": 19497, "children": [
                    {"name": "锐捷 EG网关", "value": 19497}]},
            ]},

            {"name": "title=\"BigBlueButton\"", "value": 23852, "children": [
                {"name": "BigBlueButton视频会议系统", "value": 23852}]},
            {"name": "Content-Length: 386", "value": 1472, "children": [
                {"name": "Keep-Alive: timeout=500", "value": 358, "children": [
                    {"name": "网御星云防火墙", "value": 358}
                ]}
            ]},
            {"name": 'body="TopFrame.html"', "value": 5386, "children": [
                {"name": "Content-Length: 498", "value": 5104, "children": [
                    {"name": "上海寰创通信科技有限公司", "value": 5104}
                ]}
            ]},
            {"name": "title:\"Jumpserver\"", "value": 6026, "children": [
                {"name": "Jumpserver开源堡垒机", "value": 6026}
            ]},
            {"name": "title=\"tos loading\"", "value": 333, "children": [
                {"name": "铁威马NAS", "value": 333}
            ]},
            {"name": 'title=="harbor"', "value": 18236, "children": [
                {"name": "Harbor企业级私有\nRegistry服务器", "value": 18236}
            ]},
            {"name": "title=\"网心云设备\"", "value": 110138, "children": [
                {"name": "网心云设备", "value": 110138}
            ]},
            {"name": "title:\"OnlineJudge\"", "value": 1061, "children": [
                {"name": "Online Judge系统", "value": 1061}
            ]},
        ]},
        {'name': 'server=nginx/*', 'value': 4799421, 'children': [


        ]},
        {'name': 'server=nginx/* (Ubuntu)', 'value': 2213993, 'children': [

            {'name': 'title:"Welcome to Keycloak"', 'value': 488, 'children': [
                {'name': 'Keycloak身份认证服务', 'value': 488}
            ]}

        ]},

        {'name': 'server=Nginx Microsoft-\nHTTPAPI/2.0', 'value': 371036},
        {'name': 'server=nginx-reuseport/1.21.1', 'value': 123355},

        {"name": "server=Huawei\nAuth-Http Server", "value": 67615},

        {"name": "server=Apache", "value": 10193829, "children": [
            {"name": "title=\"IP-guard\"", "value": 1379, "children": [
                {"name": "溢信科技有限公司 \nIP-guard企业信息监管系统"}
            ]},
            {"name": "content-length： 213", "value": 20042, "children": [
                {"name": "Feature-Policy: \naccelerometer 'none'", "value": 1922, "children": [
                    {"name": "Referrer-Policy: \nstrict-origin-when-\ncross-origin", "value": 1915, "children": [
                        {"name": "softnext（守内安\n信息科技）SPAM SQR\n 邮件安全网关", "value": 1915}
                    ]}
                ]}
            ]},
            {"name": "title=\"webmail\"", "value": 119140, "children": [
                {"name": "header=\"\nmagicwinmail_login_domain\"", "value": 1540, "children": [
                    {"name": "Winmail邮件服务器", "value": 1540}
                ]}
            ]},

        ]},
        {"name": "server=Apache-Coyote/1.1", "value": 942978, "children": [
            {"name": 'icon:"0ca23409cbe92d9330d9a8bb10f676f7"', "value": 342, "children": [
                {"name": "Content-Length: 721", "value": 321, 'children': [
                    {'name': '海康威视iVMS-8720综合平台'}
                ]}
            ]},
            {"name": "title==\"product_name_upcate\"", "value": 210, "children": [
                {"name": "Content-Length: 1380", "value": 210, "children": [
                    {"name": "VOS3000 VoIP 运营平台", "value": 210}
                ]}
            ]}

        ]},
        {'name': 'server=Apache/* (Ubuntu)', 'value': 3074108, 'children': [
            # {"name": "server= Apache/2.4.7 (Ubuntu)", "value": 336445, "children": []},
            # {'name': 'server=Apache/2.4.29 (Ubuntu)', 'value': 915101},
            # {'name': 'server=Apache/2.4.41 (Ubuntu)', 'value': 908670},
            # {'name': 'server=Apache/2.4.18 (Ubuntu)', 'value': 112489},
            # {'name': 'server=Apache/2.4.18 (Ubuntu)', 'value': 559948},
            # {'name': 'server=Apache/2.4.7 (Ubuntu)', 'value': 241455},
            {"name": "title:\"Login :: Damn Vulnerable \nWeb Application (DVWA) v1.\"", "value": 239, "children": [
                {"name": "DVWA Web渗透工具", "value": 239}
            ]},

        ]},
        {'name': 'server=Apache/* (Debian)', 'value': 1426451, 'children': [
            # {'name': 'server=Apache/2.4.38 (Debian)', 'value': 101409},
            # {"name": "server=Apache/2.4.25\n(Debian)", "value": 567599, "children": []},
            # {'name': 'server=Apache/2.4.38\n(Debian)', 'value': 449177},
            # {'name': 'server=Apache/2.4.10 (Debian)', 'value': 190105},
            # {'name': 'server=Apache/2.2.22 (Debian)', 'value': 118161},
        ]},
        {'name': 'server=Apache/* (CentOS)', 'value': 621874, 'children': [
            # {'name': 'server=Apache/2.2.15\n(CentOS)', 'value': 333043},
            # {'name': 'server=Apache/2.4.6 (CentOS)', 'value': 166391},
            # {'name': 'server=Apache/2.2.15 (CentOS)', 'value': 122440},

        ]},

        {'name': 'server=Apache/* (CentOS)\\*', 'value': 576553, 'children': [
            # {'name': 'server=Apache/2.4.6 (CentOS)\nOpenSSL/1.0.2k-fips PHP/7.1.33', 'value': 189170},
            # {'name': 'server=Apache/2.4.6 (CentOS)\nOpenSSL/1.0.2k-fips PHP/5.4.16', 'value': 261999},
            # {'name': 'server=Apache/2.4.6 (CentOS)\nPHP/5.4.16', 'value': 125364},
        ]},
        {'name': 'server=Apache/2', 'value': 300090},
        {'name': 'server=Tengine/Aserver', 'value': 184144},
        {'name': 'server=Apache/* (Unix)\\*', 'value': 215819, 'children': [
            # {'name': 'server=Apache/2.4.53 (Unix)', 'value': 98818},
            # {'name': 'server=Apache/2.4.28 (Unix)\nOpenSSL/1.1.0f SVN/1.9.7\nmod_wsgi/4.5.20 Python/2.7', 'value': 117001},

        ]},

        {'name': 'server=Microsoft-IIS/*', 'value': 4723361, 'children': [
            # {"name": "server==\"Microsoft-IIS/8.5\"", "value": 1535387},
            # {'name': 'server=Microsoft-IIS/7.5', 'value': 1110632},
            # {'name': 'server=Microsoft-IIS/10.0', 'value': 1788277},
            # {'name': 'server=Microsoft-IIS/8.0', 'value': 176911},
            # {'name': 'server=Microsoft-IIS/6.0', 'value': 112154},

            {"name": "body=\"meta name=\"renderer\"", "value": 30476, "children": [
                {"name": "Content-Length: 2022", "value": 5945, "children": [
                    {"name": "智邦国际ERP系统", "value": 5945}
                ]}
            ]}

        ]},
        {'name': 'server=Microsoft-HTTPAPI/2.0', 'value': 105401},

        {"name": "server:\"HTTPD  1.0\"", "value": 49745, "children": [
            {"name": "body=\"window.open(\"login.html\"\"", "value": 46487, "children": [
                {"name": "icon:\"2458cda98f8d51bcc9a780158829cce8\"", "value": 36331, "children": [
                    {"name": "维盟路由器", "value": 36331}]},
                {"name": "icon:\"079ceabe8d0f1a2fbc8db487075778dc\"", "value": 297, "children": [
                    {"name": "WiTown智能WiFi营销系统", "value": 297}
                ]}
            ]},
            {"name": "icon:\"a45883b12d753bc87aff5bddbef16ab3\"", "value": 2403, "children": [
                {"name": "锐捷NBR路由器", "value": 2403}
            ]},
        ]},
        {"name": "server=\"HTTPD_* 1.0\"", "value": 98892, "children": [
            # {"name": "server=\"HTTPD_ac 1.0\"", "value": 7312, "children": []},
            # {"name": "server=\"HTTPD_gw 1.0\"", "value": 91580, "children": []},
            {"name": "body=\"window.open(\"login.html\"\"", "value": 81677, "children": [
                {"name": "icon:\"2458cda98f8d51bcc9a780158829cce8\"", "value": 40375, "children": [
                    {"name": "维盟路由器", "value": 40375}
                ]},
                {"name": "icon:\"715c49c5512d763084a4082c27d935e1\"", "value": 16204, "children": [
                    {"name": "维盟路由器", "value": 16204}
                ]}
            ]},
            {"name": "icon:\"a45883b12d753bc87aff5bddbef16ab3\"", "value": 20181, "children": [
                {"name": "锐捷NBR路由器", "value": 20181}
            ]},
            {"name": "Content-Length: 249", "value": 1061, "children": [
                {"name": "文网卫士千兆路由器", "value": 1061}
            ]},
            {"name": "Content-Length: 238", "value": 82121, "children": [
                {"name": "icon:\"167e57711d9ea65a835ee555cbd81f74\"", "value": 247, "children": [
                    {"name": "D-LINk 路由器", "value": 247}
                ]}
            ]},
            {"name": "Content-Length: 234", "value": 161, "children": [
                {"name": "领航智能路由器", "value": 161}
            ]},
            {"name": "body=\"window.open(\"login.html\"\"", "value": 7312, "children": [
                {"name": "icon:\"715c49c5512d763084a4082c27d935e1\"", "value": 1089, "children": [
                    {"name": "维盟路由器", "value": 1089}
                ]}
            ]}

        ]},

        {"name": "server=Ingelabs-httpd/1.0", "value": 539, "children": [
            {'name': 'title==*-knx', 'value': 565, 'children': [
                {'name': 'iddero *-knx电容式触摸屏'}
                # {"name": "title==\"hc2-knx\"", "value": 245, "children": [
                #     {"name": "iddero hc2-knx电容式触摸屏", "value": 245}
                # ]},
                # {"name": "title==\"hc3-knx\"", "value": 74, "children": [
                #     {"name": "iddero hc3-knx电容式触摸屏", "value": 74}
                # ]},
                # {"name": "title==\"hc2l-knx\"", "value": 68, "children": [
                #     {"name": "iddero hc2l-knx电容式触摸屏", "value": 68}
                # ]},
                # {"name": "title==\"hc1i-knx\"", "value": 43, "children": [
                #     {"name": "iddero hc1i-knx电容式触摸屏", "value": 43}
                # ]},
                # {"name": "title==\"hc3l-knx\"", "value": 20, "children": [
                #     {"name": "iddero hc3l-knx电容式触摸屏", "value": 20}
                # ]},
            ]},

            {"name": "title==\"iddero home server\"", "value": 57, "children": [
                {"name": "iddero 网络服务器", "value": 57}
            ]},

        ]},
        {"name": "server=Arcadyan httpd 1.0", "value": 12744, "children": [
            {"name": "body=\"\"py20_login_buffalo.png\"", "value": 9584, "children": [
                {"name": "BUFFALO WiFi", "value": 9584}
            ]},
            {"name": "title=\"o2.box\"", "value": 2207, "children": [
                {"name": "o2 电视机顶盒", "value": 2207}
            ]}

        ]},
        {"name": "server=FN-Httpd \n1.0 [HTTP/1.1]", "value": 3098, "children": [
            {'name': 'title=="as-*"', 'value': 3179, 'children': [
                # {"name": "title==\"as-250/f-sc\"", "value": 469, "children": [
                #     {"name": "CENTURY SYSTEMS \nas-250/f-sc 工业路由器", "value": 469}
                # ]},
                # {"name": "title==\"as-250\"", "value": 290, "children": [
                #     {"name": "CENTURY SYSTEMS \nas-250 工业路由器", "value": 290}
                # ]},
                # {"name": "title==\"as-m250\"", "value": 172, "children": [
                #     {"name": "CENTURY SYSTEMS \nas-m250 工业路由器", "value": 172}
                # ]},
                # {"name": "title==\"as-p250\"", "value": 2, "children": [
                #     {"name": "CENTURY SYSTEMS \nas-p250 工业路由器", "value": 2}
                # ]},
                # {"name": "title==\"AS-250/NL\"", "value": 1473, "children": [
                #     {"name": "CENTURY SYSTEMS \nAS-250/NL 工业路由器", "value": 1473}
                # ]},
                # {"name": "title==\"AS-250/F-KO\"", "value": 692, "children": [
                #     {"name": "CENTURY SYSTEMS \nAS-250/F-KO工业路由器", "value": 692}
                # ]}
                {'name': 'CENTURY SYSTEMS as-* 工业路由器'}
            ]},
        ]},
        {"name": "server=httpd/2.0", "value": 1230069, "children": [

            {'name': 'body="class="prod_madelName">*</div>', 'value': 56749, 'children': [
                {'name': '华硕*路由器'}
            ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AC53\"", "value": 3273, "children": [
            #     {"name": "华硕RT-AC53路由器", "value": 3273}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AC51U\"", "value": 5632, "children": [
            #     {"name": "华硕RT-AC51U路由器", "value": 5632}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AX68U\"", "value": 58, "children": [
            #     {"name": "华硕RT-AX68U路由器", "value": 58}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AC52\"", "value": 59, "children": [
            #     {"name": "华硕RT-AC52路由器", "value": 59}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AC1200\"", "value": 5407, "children": [
            #     {"name": "华硕RT-AC1200路由器", "value": 5407}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AX1800 plus\"", "value": 21, "children": [
            #     {"name": "华硕RT-AX1800 plus路由器", "value": 21}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AC59U V2\"", "value": 483, "children": [
            #     {"name": "华硕RT-AC59U V2路由器", "value": 483}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-N600P\"", "value": 106, "children": [
            #     {"name": "华硕RT-N600P路由器", "value": 106}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AC51\"", "value": 154, "children": [
            #     {"name": "华硕RT-AC51路由器", "value": 154}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AC56U\"", "value": 499, "children": [
            #     {"name": "华硕RT-AC56U路由器", "value": 499}
            # ]},
            # {"name": "body=\"class=\"prod_madelName\">RT-AX82\"", "value": 0, "children": [
            #     {"name": "华硕RT-AX82路由器", "value": 0}
            # ]},
            {'name': 'body="style="margin-left:78px;">*</div>', 'value': 1376, 'children': [
                {'name': '华硕*路由器'}
            ]}
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N12+\"", "value": 151, "children": [
            #     {"name": "华硕RT-N12+路由器", "value": 151}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N12D1\"", "value": 437, "children": [
            #     {"name": "华硕RT-N12D1路由器", "value": 437}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-AC68U\"", "value": 17, "children": [
            #     {"name": "华硕RT-AC68U路由器", "value": 17}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N11P\"", "value": 222, "children": [
            #     {"name": "华硕RT-N11P路由器", "value": 222}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-AC51U\"", "value": 20, "children": [
            #     {"name": "华硕RT-AC51U路由器", "value": 20}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N14U\"", "value": 1, "children": [
            #     {"name": "华硕RT-N14U路由器", "value": 1}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N53\"", "value": 40, "children": [
            #     {"name": "华硕RT-N53路由器", "value": 40}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-AC66U\"", "value": 34, "children": [
            #     {"name": "华硕RT-AC66U路由器", "value": 34}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-AC1200\"", "value": 105, "children": [
            #     {"name": "华硕RT-AC1200路由器", "value": 105}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N56UB1\"", "value": 137, "children": [
            #     {"name": "华硕RT-N56UB1路由器", "value": 137}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-AC55U\"", "value": 12, "children": [
            #     {"name": "华硕RT-AC55U路由器", "value": 12}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N18U\"", "value": 2, "children": [
            #     {"name": "华硕RT-N18U路由器", "value": 2}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-AC87U\"", "value": 2, "children": [
            #     {"name": "华硕RT-AC87U路由器", "value": 2}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N12HP_B1\"", "value": 7, "children": [
            #     {"name": "华硕RT-N12HP_B1路由器", "value": 7}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N600\"", "value": 4, "children": [
            #     {"name": "华硕RT-N600路由器", "value": 4}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N66U\"", "value": 26, "children": [
            #     {"name": "华硕RT-N66U路由器", "value": 26}
            # ]},
            # {"name": "body=\"style=\"margin-left:78px;\">RT-N56U\"", "value": 110, "children": [
            #     {"name": "华硕RT-N56U路由器", "value": 110}
            # ]},

        ]},
        {'name': 'server=*httpd', 'value': 468868, 'children': [
            # {"name": "server=httpd", "value": 112779},
            # {'name': 'server=micro_httpd', 'value': 356089},

        ]},

        {'name': 'server=WildFly/*', 'value': 21387, 'children': [


        ]},

        {'name': 'server=lighttpd/*', 'value': 1110459, 'children': [

            {'name': 'title="Ubiquiti"', 'value': 174207, 'children': [
                {'name': 'Ubiquiti 无线网桥', 'value': 174207}
            ]},
            {'name': 'title=="download master"', 'value': 16153, 'children': [
                {'name': '华硕路由器', 'value': 16153}
            ]},
            {'name': 'body="Cisco Meraki Support"', 'value': 27589, 'children': [
                {'name': '思科maraki 路由器'}
            ]},
            {'name': 'body="Skyroam global WiFi service"', 'value': 1139, 'children': [
                {'name': '漫游宝无线路由器', 'value': 1139}
            ]},
            {'name': 'title=="gpon ont"', 'value': 4239, 'children': [
                {'name': 'Dasan Networks GPON ONT WiFi Router', 'value': 4239}
            ]},
            {'name': 'body="name="loginui"', 'value': 1042, 'children': [
                {'name': 'HALANy networks', 'value': 1042}
            ]},
            {'name': 'title="SHAFE talk - LuCI"', 'value': 143, 'children': [
                {'name': 'SHAFE talk话盒子'}
            ]},
            {'name': 'title="NBG6617 - Login"', 'value': 193, 'children': [
                {'name': 'ZyXEL NBG6617路由器', 'value': 193}
            ]},
            {'name': 'title=="router-高恪"', 'value': 23112, 'children': [
                {'name': '高格路由器', 'value': 23112}
            ]}

        ]},

        {'name': 'server=Boa/*', 'value': 805757, 'children': [
            # {"name": 'server=Boa/0.94.14rc21', 'value': 650725, "children": []},
            # {'name': 'server=Boa/0.94.13', 'value': 155032},
            {'name': 'title:"TOTOLINK"', 'value': 18763, 'children': [
                {'name': 'TOTOLINK 路由器', 'value': 18763}
            ]},
            {'name': 'body=onclick="onDoLogin();" name="B1"', 'children': [
                {'name': 'Content-Length: 3068', 'value': 43, 'children': [
                    {'name': '磊科智能路由器'}
                ]},
                {'name': 'Content-Length: 8849', 'value': 8, 'children': [
                    {'name': '朗视 VoIP语音网关TA3210', 'value': 8}
                ]},
                {'name': 'Content-Length: 7566', 'value': 601, 'children': [
                    {'name': '朗视 网络电话网关TA200', 'value': 601}
                ]},
                {'name': 'Content-Length: 5823', 'value': 949, 'children': [
                    {'name': '朗视MyPBX防火墙', 'value': 949}
                ]},
                {'name': 'Content-Length: 5889', 'value': 31, 'children': [
                    {'name': '朗视MyPBX防火墙', 'value': 31}
                ]},
                {'name': 'Content-Length: 9835', 'value': 137, 'children': [
                    {'name': '朗视无线语音网关-Yeastar TG200', 'value': 137}
                ]},
                {'name': 'Content-Length: 7642', 'value': 137, 'children': [
                    {'name': '朗视无线语音网关', 'value': 137}
                ]},
                {'name': 'Content-Length: 10165', 'value': 50, 'children': [
                    {'name': '朗视无线语音网关', 'value': 50}
                ]},


            ]},
            {'name': 'title:"SmartLAN/G Web Interface"', 'value': 7321, 'children': [
                {'name': 'icon:"3ff31f921ea24a22ca043310dc9b3d8a"', 'value': 6320, 'children': [
                    {'name': 'SmartLan/G Web服务器', 'value': 6320}

                ]}
            ]},
            {'name': 'title:"Untitled Document"', 'value': 22946, 'children': [
                {'name': 'icon:"6175c2d63dff8fd6912c79b8d0d20835"', 'value': 4771, 'children': [
                    {'name': 'xirrus 路由器', 'value': 4771}
                ]}
            ]},
            {'name': 'title:"HUMAX"', 'value': 1215, 'children': [
                {'name':'icon:"0c27f1c67e7f15386cebb95bcd35208b"','value':1150,'children':[
                    {'name': 'HUMAX T3Av2WiFi路由器', 'value': 1150}

                ]}
            ]},

        ]},

        {"name": "server=\"TP-LINK HTTPD/1.0\"", "value": 2482, "children": [
            {"name": "TP-LINK厂商", "value": 2482},
            {"name": "title==\"login\"", "value": 46, "children": [
                {"name": "TP-LINK  \n无线室外接入点WiFi", "value": 46}
            ]},
            {"name": "title==\"Pharos\"", "value": 36, "children": [
                {"name": "TP-LINK Pharos Control服务器", "value": 36}
            ]},
            {'name': 'title=="TL-WPA*"', 'value': 109, 'children': [

                {'name': 'TP-LINK WPA* WiFi桥接器'}
            ]},
        ]},
        {"name": 'server=""', "value": 20023658, "children": [
            {"name": "header=\"WebAdmin\"", "value": 3310, "children": [
                {"name": "Content-length: 2659", "value": 154, "children": [
                    {"name": "U-Mail邮件服务器", "value": 154}
                ]}
            ]}
        ]},
        {'name': 'server=openresty', 'value': 1102388},
        {'name': 'server=cloudflare', 'value': 692219},
        {'name': 'server=sw-cp-server', 'value': 678818},
        {'name': 'server=Varnish', 'value': 556218},
        {'name': 'server=Proxy', 'value': 492829},
        {'name': 'server=RG/Device 10.x', 'value': 467965},
        {'name': 'server=Kestrel', 'value': 437476},
        {'name': 'server=CK6u06Vu4', 'value': 428367},
        {'name': 'Web*', 'value': 716956, 'children': [
            # {'name': 'server=Webs', 'value': 377877},
            # {'name': 'server=web', 'value': 108137},
            # {'name': 'server=WebServer/1.0 UPnP/1.0', 'value': 125906},
            # {'name': 'server=webserver', 'value': 105036},

        ]},
        {'name': 'server=IdeaWebServer/5.0.0', 'value': 107718},
        {'name': 'server=TestApp-1.0.0', 'value': 374407},
        {'name': 'server=RomPager/4.07\nUPnP/1.0', 'value': 372161, 'children': [
            {'name': 'title:"SWW link"', 'value': 233, 'children': [
                {'name': '和勤ZyWALL2 VPN防火墙', 'value': 233}
            ]}
        ]},
        {'name': 'server=imunify360-\nwebshield/1.18', 'value': 367767},
        {'name': 'server=awselb/2.0', 'value': 263016},
        {'name': 'server=http server 1.0', 'value': 239823},
        {'name': 'server=GoAhead-Webs', 'value': 226654},
        {'name': 'server=LiteSpeed', 'value': 216995},
        {'name': 'server=App-webs/', 'value': 138989},
        {'name': 'server=Tengine', 'value': 130352},
        {'name': 'server=cwpsrv', 'value': 124987},
        {'name': 'server=mini_httpd/1.19\n19dec2003', 'value': 102575},
        {'name': 'server=BigIP', 'value': 96082},
    ]}
]






tree = (
    Tree(init_opts=opts.InitOpts(width="1800px", height="800px"))
        .add("",data, orient="LR", initial_tree_depth=1, collapse_interval=-1, is_roam=True)
        #     参数layout的"radial"是径向布局是指以根节点为圆心，每一层节点为环，而"orthogonal"是正常的水平和垂直布局
        #     参数symbol是标记类型形状，提供的类型有:'emptyCircle', 'circle', 'rect', 'roundRect','triangle', 'diamond', 'pin', 'arrow'
        #     参数orient是布局方向，水平从左到右为"LR"，水平从右往左为"RL"，垂直从上到下为"TB",垂直从下到上为"BT"
        .set_global_opts(title_opts=opts.TitleOpts(title="指纹树"),
                         legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical", )
                         )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)
tree.render("./devicetree.html")

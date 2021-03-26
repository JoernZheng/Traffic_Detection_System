<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>4/5G网关WEB管理系统</title>
    <meta name="description" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="renderer" content="webkit">
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    <link rel="icon" type="image/png" href="assets/i/favicon.png">
    <link rel="apple-touch-icon-precomposed" href="assets/i/app-icon72x72@2x.png">
    <meta name="apple-mobile-web-app-title" content="Amaze UI" />
    <link rel="stylesheet" href="assets/css/amazeui.min.css" />
    <link rel="stylesheet" href="assets/css/admin.css">
    <link rel="stylesheet" href="assets/css/app.css">
    <script src="assets/js/echarts.min.js"></script>
    <?php include "navigation.html" ?>
</head>
<body data-type="index">
       <div class="tpl-content-wrapper">
            <ol class="am-breadcrumb">
                <li><a href="index.php" class="am-icon-home">首页</a></li>
                <li class="am-active">数据采集服务</li>
            </ol>
            <div class="tpl-portlet-components">
                <div class="portlet-title">
                    <div class="caption font-green bold"> 数据采集服务
                    </div>
                </div>

                <div class="tpl-block">

                    <div class="am-g">
                        <div class="tpl-form-body tpl-form-line">
                            <form class="am-form tpl-form-line-form">
                                 <div class="caption font-green bold" style="text-align: center;"> 面向服务端的配置 </div>
                                 <br>
                               
                                 <div class="am-form-group">
                                    <label for="TargetIpAddress" class="am-u-sm-3 am-form-label">数据采集服务器IPv4地址 <span class="tpl-form-line-small-title">Target IPv4 address</span></label>
                                    <div class="am-u-sm-9">
                                        <input type="text" class="am-form-field tpl-form-no-bg" placeholder="请输入目标ip地址"  id="TargetIpAddress" />
                                        <small>&nbsp</small>
                                    </div>
                                    <label for="TargetPort" class="am-u-sm-3 am-form-label">目标端口 <span class="tpl-form-line-small-title">Target Port</span></label>
                                    <div class="am-u-sm-9">
                                        <input type="text" class="am-form-field tpl-form-no-bg" placeholder="请输入目标端口"  id="TargetPort" />
                                        <small>&nbsp</small>
                                    </div>
                                    <label for="LocalPort" class="am-u-sm-3 am-form-label">数据采集协议 <span class="tpl-form-line-small-title">DC protocol</span></label>
                                    <div class="am-u-sm-9">
                                        <select data-am-selected="{searchBox: 1}">
                                            <option value="mqtt">mqtt</option>
                                            <option value="http">http</option>
                                            <option value="coap">coap</option>
                                        </select>
                                        <small>&nbsp</small>
                                    </div>
                                </div>
                            
                                <div class="am-form-group">
                                    <div class="am-u-sm-9 am-u-sm-push-3">
                                        <button type="submit" class="am-btn am-btn-primary tpl-btn-bg-color-success " id="submit">保存</button>
                                    </div>
                                </div>
                            </form>

                            <form class="am-form">
                                <table  class="am-table am-table-striped am-table-hover table-main"  >
                                    <thead>
                                        <tr>
                                            <th class="am-hide-sm-only" style="text-align: center;" >分类</th>
                                            <th class="am-hide-sm-only" style="text-align: center;">TOPIC类</th>
                                            <th class="am-hide-sm-only" style="text-align: center;">操作权限</th>
                                            <th class="am-hide-sm-only" style="text-align: center;">描述</th> 
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>   
                                            <td class="am-hide-sm-only" style="text-align: center;text-align: center;vertical-align: middle;" rowspan="3"><font color="black">数据采集</font></td>
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">Dev/control</font></td>
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">订阅</font></td>
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">启动数采线程</font></td>
                                        </tr>
                                        <tr>   
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">dev/+/+/read</font></td>
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">发布</font></td>
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">发送数采数据</font></td>
                                        </tr>
                                        <tr>   
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">dev/+/+/write </font></td>
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">订阅</font></td>
                                            <td class="am-hide-sm-only" style="text-align: center;"><font color="black">修改设备数据</font></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </form>
                            <br>


                            <form class="am-form tpl-form-line-form">
                                 <div class="caption font-green bold" style="text-align: center;"> 面向设备端的配置 </div>
                                 <br>

                                <div class="am-form-group">
                                    <label for="LocalPort" class="am-u-sm-3 am-form-label">数据采集类型 <span class="tpl-form-line-small-title">DC Type</span></label>
                                    <div class="am-u-sm-9">
                                        <select data-am-selected="{searchBox: 1}">
                                            <option value="PLC">PLC</option>
                                            <option value="机器人">机器人</option>
                                            <option value="行业协议">行业协议</option>
                                        </select>
                                        <small>&nbsp</small>
                                    </div>
                                    <div class="am-u-sm-9 am-u-sm-push-3">
                                        <button type="submit" class="am-btn am-btn-primary tpl-btn-bg-color-success " id="submit">保存</button>
                                    </div>
                                </div>
                            </form>

                            <p>数据采集协议参数放置处</p>

                        </div>
                    </div>
                </div>
            </div>
    </div>

    <script src="assets/js/jquery-2.1.1.js"></script>
    <script src="assets/js/amazeui.min.js"></script>
    <script src="assets/js/app.js"></script>
    
</body>
</html>
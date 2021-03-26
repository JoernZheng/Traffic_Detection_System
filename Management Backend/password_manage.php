<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>违规信息查询系统</title>
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
    <script src="assets/js/jquery-3.3.1.min.js" type="text/javascript" charset="utf-8"></script>
    <script src="assets/js/echarts.min.js"></script>
    <script src="assets/js/data_detail.js" type="text/javascript" charset="utf-8"></script>
    <?php include "navigation.html" ?>
</head>
<body data-type="index">
       <div class="tpl-content-wrapper">
            <ol class="am-breadcrumb">
                <li><a href="index.php" class="am-icon-home">系统配置</a></li>
                <li class="am-active">路口信息展示</li>
            </ol>
            <div class="tpl-portlet-components">
                <div class="portlet-title">
                    <div class="caption font-green bold">路口信息展示
                    </div>
                </div>

                <div class="tpl-block" style="">
                    <div class="am-g">
                        <div class="tpl-form-body tpl-form-line">
                            <form class="am-form tpl-form-line-form" id = "date-form" method="post" action="">
                                <div class="am-form-group">
                                    <label for="StartDate" class="am-u-sm-3 am-form-label">开始日期 <span class="tpl-form-line-small-title">StartDate</span></label>
                                    <div class="am-u-sm-9">
                                        <input type="text" class="am-form-field tpl-form-no-bg" name = "stDate" placeholder="请输入日期" data-am-datepicker="" readonly id="startdate" />
                                        <small>开始日期，点击选择</small>
                                    </div>
                                    <label for="EndDate" class="am-u-sm-3 am-form-label">结束日期 <span class="tpl-form-line-small-title">EndDate</span></label>
                                    <div class="am-u-sm-9">
                                        <input type="text" class="am-form-field tpl-form-no-bg" name = "edDate" placeholder="请输入日期" data-am-datepicker="" readonly id="enddate" />
                                        <small>结束日期,点击选择</small>
                                    </div>
                                    <label for="Location" class="am-u-sm-3 am-form-label">违规地点 <span class="tpl-form-line-small-title"> Location</span></label>
                                    <div class="am-u-sm-9">
                                        <input type="text" class="am-form-field tpl-form-no-bg" name = "location" placeholder="请输入地点"  id="Location" />
                                        <small>地址信息,点击填写</small>
                                    </div>
                                </div>
                                <div class="am-form-group">
                                    <div class="am-u-sm-9 am-u-sm-push-3">
                                        <button type="button" class="am-btn am-btn-primary tpl-btn-bg-color-success query-btn">查询</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

                <div id="graph1" style="width: 800px; height: 600px; margin: 50px auto;"></div>

                <div id="graph3" style="width: 700px; height: 600px; margin: 0 auto;"></div>

            </div>
       </div>

    <script src="assets/js/amazeui.min.js"></script>
    <script src="assets/js/app.js"></script>
    <script src="layui/layui.all.js"></script>

       <script>
           $('.query-btn').click(function () {
               var date1 = $('#startdate').val()
               var date2 = $('#enddate').val()
               var location = $('#Location').val()
               if (date1.length == 0 || date2.length == 0 || location.length == 0){
                   layer.alert('查询条件不能含空', {icon: 2});
               }else if (date1.length && date2.length && date1 > date2) {
                   layer.alert('开始时间不能晚于结束时间', {icon: 2});
               }else{
                   get_graph1(date1, date2, location);
                   get_graph3(date1, date2, location);
               }
           })
       </script>

</body>
</html>
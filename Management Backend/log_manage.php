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
    <link rel="stylesheet" href="layui/css/layui.css">
    <script src="assets/js/echarts.min.js"></script>
    <?php include "navigation.html";?>
    <?php include "query.php"?>
</head>

<?php
    $PHP_SELF=$_SERVER['PHP_SELF'];
    $url='http://'.$_SERVER['HTTP_HOST'].substr($PHP_SELF,0,strrpos($PHP_SELF,'/')+1);
?>

<body data-type="index">
       <div class="tpl-content-wrapper">
            <ol class="am-breadcrumb">
                <li><a href="index.php" class="am-icon-home">系统管理</a></li>
                <li class="am-active">信息查询</li>
            </ol>
            <div class="tpl-portlet-components">
                <div class="portlet-title">
                    <div class="caption font-green bold"> 信息查询
                    </div>
                </div>
                <div class="tpl-block">
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
                                    <label for="StartDate" class="am-u-sm-3 am-form-label">车牌信息 <span class="tpl-form-line-small-title"> License</span></label>
                                    <div class="am-u-sm-9">
                                        <input type="text" class="am-form-field tpl-form-no-bg" name = "license" placeholder="请输入车牌"  id="License" />
                                        <small>车牌信息,点击填写</small>
                                    </div>
                                    <label for="StartDate" class="am-u-sm-3 am-form-label">违规地点 <span class="tpl-form-line-small-title"> Location</span></label>
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

                    <table id="demo" lay-filter="test"></table>

                </div>
            </div>
    </div>

    <script src="assets/js/jquery-2.1.1.js"></script>
    <script src="assets/js/amazeui.min.js"></script>
    <script src="assets/js/app.js"></script>
    <script src="layui/layui.all.js"></script>

   <script>
           $('.query-btn').click(function () {
               var date1 = $('#startdate').val()
               var date2 = $('#enddate').val()
               var license = $('#License').val()
               var location = $('#Location').val()
               var gets = ''
               if (date1){
                   if (gets.length) gets = gets + '&';
                   gets = gets + 'date1=' + date1;
               }
               if (date2){
                   if (gets.length) gets = gets + '&';
                   gets = gets + 'date2=' + date2;
               }
               if (license){
                   if (gets.length) gets = gets + '&';
                   gets = gets + 'license=' + license;
               }

               if (location){
                   if (gets.length) gets = gets + '&';
                   gets = gets + 'location=' + location;
               }

               if (date1.length == 0 && date2.length == 0 && license.length == 0 && location.length == 0) {
                   layer.alert('查询条件为空', {icon: 2});
               } else if (date1.length && date2.length && date1 > date2) {
                   layer.alert('开始时间不能晚于结束时间', {icon: 2});
               } else if ((date1.length == 0 + date2.length == 0) == 2){
                   layer.alert('时间区间不可缺省', {icon: 2});
               } else{
                       layui.use('table', function(){
                           var table = layui.table;
                           table.render({                   // 渲染表格
                               elem: '#demo'            // 指明表格元素 elem -> element,'#Test'是id值
                               ,skin:"nob"
                               ,limit:10                // 这里要和page里的limits匹配,这里的limit是每次请求的数据条量
                               ,url:'<?php echo $url?>query.php?' + gets
                               ,cols: [[
                                   {field:'id', width:300, title: '违规ID',sort:true,align:"center"}
                                   ,{field:'license', width:300, title: '违规车牌',sort:true,align:"center"}
                                   ,{field:'time', width:300, title: '违规时间',sort:true,align:"center"}
                                   ,{field:'action', width:300, title: '违规原因',sort:true,align:"center"}
                                   ,{field:'location', width:300, title: '违规地点',sort:true,align:"center"}
                               ]]
                               ,page: {                 // 设置分页的属性
                                   //limits:[15,30,45],   // 设置每一个分页有多少条信息
                                   prev:"<<",           // 设置前进和后退符
                                   next:">>",
                                   textAlign:"center",
                                   theme:"#36C6D3",  // #0099ff
                                   layout: ['count', 'prev', 'page', 'next', 'limit', 'skip']   // 分页器的构成，这里声明分页器由6部分构成
                               }
                               ,response: {
                                   statusCode: 0 //成功的状态码为默认为 0
                               }
                               ,parseData: function(res){ //将原始数据解析成 table 组件所规定的数据
                                   return {
                                       "code": res.code, //解析接口状态
                                       "msg": res.message, //解析提示文本
                                       "count": res.count, //解析数据长度
                                       "data": res.data    //解析数据列表
                                   };
                               }
                           });
                       });
               }
           });
   </script>


</body>
</html>
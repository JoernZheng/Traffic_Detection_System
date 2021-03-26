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
    <link rel="stylesheet" href="layui/css/layui.css">
    <meta name="apple-mobile-web-app-title" content="Amaze UI" />
    <link rel="stylesheet" href="assets/css/amazeui.min.css" />
    <link rel="stylesheet" href="assets/css/admin.css">
    <link rel="stylesheet" href="assets/css/app.css">
    <script src="assets/js/echarts.min.js"></script>
    <?php include "navigation.html" ?>
</head>



<?php

$db = new mysqli("localhost","root","jie123123","intelligenceroad",3305);

if ($db->connect_errno)
{
    die("数据库连接失败: " . $db->connect_error);
}

$res = $db->query("SHOW TABLES");

$result = array();
if ($res instanceof mysqli_result)
{
    while (($row = $res->fetch_assoc()) != FALSE)
    {
        $result[] = $row;
    }
}

$values = array_values($result);
$tableNameList = array();

for ($i = 0; $i < count($values); $i++){
    $valuesi = array_values($values[$i]);
    array_push($tableNameList, $valuesi[0]);
}

$rt = array();
for ($i = 0; $i < count($tableNameList); $i++) {
    $res = $db->query(sprintf("SHOW COLUMNS from %s", $tableNameList[$i]));
    $col = array();
    if ($res instanceof mysqli_result)
    {
        while (($row = $res->fetch_assoc()) != FALSE)
        {

            $row['CanBeNull'] = $row['Null'] === 'YES';   //字段值是否可以为空，是的话值为'YES'
            $col[] = $row;
        }
    }
    $rt[] = $col;
}
?>

<body data-type="index">
       <div class="tpl-content-wrapper">
            <ol class="am-breadcrumb">
                <li><a href="index.php" class="am-icon-home">系统配置</a></li>
                <li class="am-active">数据库信息</li>
            </ol>
            <div class="tpl-portlet-components">
                <div class="portlet-title">
                    <div class="caption font-green bold">数据库信息
                    </div>
                </div>

                <table class="layui-table"  lay-skin="white">
                    <colgroup>
                        <col width="250">
                        <col width="250">
                        <col width="250">
                        <col>
                    </colgroup>
                    <thead>
                    <tr>
                        <th style='text-align: center;'>表名</th>
                        <th style='text-align: center;'>字段</th>
                        <th style='text-align: center;'>字段类型</th>
                        <th style='text-align: center;'>主键</th>
                        <th style='text-align: center;'>可为NULL</th>
                    </tr>
                    </thead>
                    <tbody>
                        <?php
                            for ($i = 0; $i < count($rt); $i++) {
                                for ($j = 0; $j < count($rt[$i]); $j++) {
                                    echo "<tr style='text-align: center;'>";
                                    echo "<td>" . $tableNameList[$i] . "</td>";
                                    echo "<td>" . $rt[$i][$j]['Field'] . "</td>";
                                    echo "<td>" . $rt[$i][$j]['Type'] . "</td>";
                                    if ($rt[$i][$j]['Key'] == 'PRI')
                                        echo "<td>" . 'Yes' . "</td>";
                                    else
                                        echo "<td>" . 'No' . "</td>";
                                    if ($rt[$i][$j]['CanBeNull'])
                                        echo "<td>" . 'Yes' . "</td>";
                                    else
                                        echo "<td>" . 'No' . "</td>";
                                    echo "</tr>";
                                }
                            }
                        ?>
                    </tbody>
                </table>



            </div>


        </div>

    </div>


    <script src="assets/js/jquery-2.1.1.js"></script>
    <script src="assets/js/amazeui.min.js"></script>
    <script src="assets/js/app.js"></script>



</body>
</html>
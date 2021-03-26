<?php

    $con = new mysqli("localhost","root","jie123123","intelligenceroad",3305);
    if ($con->connect_error) {
        die("连接失败: " . $con->connect_error);
    }

    $sql1 = "select action, count(*) as cnt from illegalbook where (time BETWEEN '%s' and '%s') AND location = '%s' group by action";
    $sql2 = "select time, count(*) as cnt from illegalbook where (time BETWEEN '%s' and '%s') AND location = '%s' group by DATE_FORMAT(time,'%s')";
    $json['code'] = 400;


    if (isset($_GET['date1']) && isset($_GET['date2']) && isset($_GET['location'])) {
        $sql1 = sprintf($sql1, $_GET['date1'],$_GET['date2'], $_GET['location']);
        $sql2 = sprintf($sql2, $_GET['date1'],$_GET['date2'], $_GET['location'], '%Y-%m-%d %H');
        $result = mysqli_query($con, $sql1);

        $json['code'] = 0;
        $json['byCategory'] = array();

        while ($row = mysqli_fetch_array($result)) {
            array_push($json['byCategory'], $row);
        }

        $result = mysqli_query($con, $sql2);
        $json['byTime'] = array();

        while ($row = mysqli_fetch_array($result)) {
            array_push($json['byTime'], $row);
        }
    }

    if ($json['code'] == 0)
        echo(json_encode($json, JSON_UNESCAPED_UNICODE));

?>
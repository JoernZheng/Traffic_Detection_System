<?php

// ------------------------------------------

    $con = new mysqli("localhost","root","jie123123","intelligenceroad",3305);
    if ($con->connect_error) {
        die("连接失败: " . $con->connect_error);
    }

    $flag = false;
    $query_vaild = false;
    $sql_pre = "select id,time,location,action, license, picture_path from illegalbook where";
    $sql = '';
    if (isset($_GET['date1']) && isset($_GET['date2'])) {
        $query_vaild = true;
        if ($flag) {
            $sql = $sql . " and";
        }
        $sql = $sql . sprintf(" time Between '%s' and '%s'", $_GET['date1'], $_GET['date2']);
        $flag = true;
    }
    if (isset($_GET['license'])) {
        $query_vaild = true;
        if ($flag) {
            $sql = $sql . " and";
        }
        $sql = $sql . sprintf(" license='%s'", $_GET['license']);
        $flag = true;
    }
    if (isset($_GET['location'])) {
        $query_vaild = true;
        if ($flag) {
            $sql = $sql . " and";
        }
        $sql = $sql . sprintf(" location='%s'", $_GET['location']);
        $flag = true;
    }

    $sqltotal = 'select count(*) as cnt from illegalbook where' . $sql;
    if (isset($_GET['page']) && isset($_GET['limit']) ){
        $sql = $sql_pre. $sql . sprintf(" limit %d, %d", ($_GET['page'] - 1) * $_GET['limit'], $_GET['limit']);
    }

    $result = mysqli_query($con, $sql);

    //var_dump($sql);

    //var_dump($result);

    $json['code'] = 0;
    $json['data'] = array();

    while ($row = mysqli_fetch_array($result)) {
        array_push($json['data'], $row);
    }


    $result = mysqli_query($con, $sqltotal);

//    var_dump($sqltotal);

    while($row = mysqli_fetch_array($result)) {
        $json['count'] = $row['cnt'];
    }

//    var_dump(count($json['data']));
    if (count($json['data']) > 0)
        echo(json_encode($json, JSON_UNESCAPED_UNICODE));


?>

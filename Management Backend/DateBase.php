

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

for ($i = 0; $i < count($rt); $i++) {
    for ($j = 0; $j < count($rt[$i]); $j++) {
        echo $rt[$i][$j]['Field'] . '   ' . $rt[$i][$j]['Type'] . '   ';
        if ($rt[$i][$j]['Key'] == 'PRI')
            echo 'Yes';
        else
            echo 'No';
        echo $rt[$i][$j]['CanBeNull'];
        echo "<br>";
    }
//    var_dump($rt[$i]);
    echo "<br>";
}

@$db->close();
?>
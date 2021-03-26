<?php
header("Content-Type:text/html;charset=utf-8");
$username=$_POST['username'];
$password=$_POST['password'];
//if($username =='admin' and $password =='admin')
//{echo "<script> alert('登陆成功');parent.location.href='/index.php'; </script>"; 
//exit; 
//}
//else {
//echo "<script> alert('登陆失败');parent.location.href='/login.php'; </script>"; 
//exit; 
//}
$db_path = 'Login_test.db';
//$db_path = './db/Login_test.db';
$db = new SQLite3($db_path);
if( !$db ) {
echo '不能连接数据库文件,请及时联系管理员<br />';
}
else
{
	//echo '成功连接SQlite文件<br />';
	$result = $db->query("SELECT * FROM Login WHERE username = '$username'");
	while($row = $result->fetchArray(SQLITE3_ASSOC))
	{
		if($row['password']==$password)
		{
			echo "<script> alert('登陆成功');parent.location.href='/index.php'; </script>"; 
			//echo '密码正确，账号：',$username ,'密码：',$password  ,'<br>';
			exit; 
		}
	}
	echo "<script> alert('账号或密码错误');parent.location.href='/login.php'; </script>"; 
	$result->reset();
	$result->finalize();
	$db->close();
	exit; 
}
?>

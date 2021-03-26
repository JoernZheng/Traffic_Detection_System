<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>4/5G网关WEB管理系统</title>
    <link rel="stylesheet" type="text/css" href="./assets/css/login.css" />
</head>
<body>
    <div id="login">
        <h1><img src="./assets/img/login-wangguan.png"></h1>
        <h4>网关管理系统</h4>
        <br />
        <form action="success.php" method="post">
            <div><img src="./assets/img/login-uname.png" />
                <input type="text" required="required" placeholder="用户名" name="username" />
            </div>
            <div><img src="./assets/img/login-pwd.png" />
                <input type="password" required="required" placeholder="密码" name="password" />
            </div>
            <button class="but" type="submit">登录</button>
    </form>
    </div>
</body>
</html>  
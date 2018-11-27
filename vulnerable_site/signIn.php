
<?php 

  
  $host = "localhost";
  $user = "";
  $pass = "";

  $databaseName =  "test";
  $tableName = "users";
  
  $id = $_POST["id"];
  $password = $_POST["password"];



  $con = mysqli_connect($host,$user,$pass, $databaseName);
  $result = mysqli_query($con,"SELECT * FROM $tableName WHERE id = '$id' AND password = '$password'");  //query
  
  $rowcount=mysqli_num_rows($result);
  
  if ($rowcount > 0) 
  {    
    $redir = "profileLog.html";
    //echo "<script>","window.location.href='$redir';", "</script>";
    header('Location:/431_site/profilePage.html');

  } 
  else
  {
  	//$message = "Incorrect username or password!";
    $redir = "signIn.html";
    //echo "<script>", "alert('$message');", "window.location.href='$redir';", "</script>";
    header('Location:/431_site/login.html');
  }

                              
  $conn->close();

  

?>


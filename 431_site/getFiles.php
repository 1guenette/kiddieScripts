<?php

$uploadOk = 1;

//server credentials
$servername = "localhost";
$username = "";
$password = "";
$dbname = "test";

//get userId
$userID  = $_POST["userId"];

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
$sql = "SELECT * From data Where id='$userID'";
$result = mysqli_query($conn,$sql); 


	$data = array();
  	$i = 0;
  	while( $r = mysqli_fetch_array($result))
  	{
  		$info;
  		$data[$i]["fileName"] = $r["fileName"];
  		$i = $i + 1;
  	}
  	 echo json_encode($data);                            

  //$conn->close();

?>
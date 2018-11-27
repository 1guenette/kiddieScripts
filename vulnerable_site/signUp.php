<?php
$uploadOk = 1;

// Check if image file is a actual image or fake image
$servername = "localhost";
$username = "";
$password = "";
$dbname = "test";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);


$id =  $_POST["userId"];
$password =  $_POST["password"];
$sql = "INSERT INTO users (id, password) VALUES ('$id', '$password')";

if ($conn->query($sql) === TRUE) 
{
    echo "New use rcreated successfully";
} 

$conn->close();

header('Location:/431_site/login.html');
exit();


?>
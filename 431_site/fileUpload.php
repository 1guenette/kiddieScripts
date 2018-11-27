<?php

if(isset($_POST["submit"])) {

    //$file = $_FILES['file'];
    $fileName = $_FILES['file']['name'];
    $fileTmpName = $_FILES['file']['tmp_name']; //temporary location
//gets file Extension
    $fileExt = explode('.', $fileName);
    $fileActualExt = strtolower(end($fileExt));
    $allow = array('jpg', 'jpeg', 'png' );

    $userId = $_POST['userId'];

    if(isset($fileName))
    {
        /*if(!empty($fileName))
        {*/
            if(in_array($fileActualExt, $allow))
            {
                //creates uniq id
                $fileNameNew = uniqid('', true).".".$fileActualExt;
                $fileDestination = 'uploads/'.$fileNameNew;
                //Stores file
                move_uploaded_file($fileTmpName, $fileDestination);



                $servername = "localhost";
                $username = "";
                $password = "";
                $dbname = "test";

            // Saves reference in database connection
                $conn = new mysqli($servername, $username, $password, $dbname);

                $sql = "INSERT INTO data (id, fileName) VALUES ('$userId', '$fileDestination')";

                if ($conn->query($sql) === TRUE) 
                {
                    echo "New record created successfully";
                } 
                $conn->close();

                //Redircts page
                header("Location:/431_site/profilePage.html");
                exit();
            }
            else
            {
                echo "Wrong file type";
            }
        //}
    
    }   

}

echo "end of file";
?>
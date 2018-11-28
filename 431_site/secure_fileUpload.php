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

    $folder = "uploads/"

    if(isset($fileName))
    {
        
            if(in_array($fileActualExt, $allow))
            {
                //creates uniq id
                $fileNameNew = uniqid('', true).".".$fileActualExt;
                $fileDestination = 'uploads/'.$fileNameNew;
                //Stores file

                if(checkPathIsInFolder($fileDestination, $folder))
                {
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

            }
        
    
    }   

}

function checkPathIsInFolder($path, $folder) {
        if ($path === '' OR $path === null OR $path === false OR $folder === '' OR $folder === null OR $folder === false) {
            /* can't use empty() because it can be a string like "0", and it's valid path */
        return false;
    }
    $folderRealpath = realpath($folder);
    $pathRealpath = realpath($path);
    if ($pathRealpath === false OR $folderRealpath === false) {
        // Some of paths is empty
        return false;
    }
    $folderRealpath = rtrim($folderRealpath, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;
    $pathRealpath = rtrim($pathRealpath, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;
    if (strlen($pathRealpath) < strlen($folderRealpath)) {
        // File path is shorter that a folder path. This file can't be inside that folder.
        return false;
    }
    if (substr($pathRealpath, 0, strlen($folderRealpath)) !== $folderRealpath) {
        // Path to a folder of file is not equal to a path to a folder where it have to be located
        return false;
    }
    // OK
    return $path;
}

echo "end of file";
?>
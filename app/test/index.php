<?php

/*
 * Check db
 */

$servername = "db";
$username = "root";
$password = "local";

try {
    $conn = new \PDO("mysql:host=$servername;dbname=ttm", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Mysql: Connected successfully";
} catch (PDOException $e) {
    echo "Mysql: Connection failed: " . $e->getMessage();
}


/*
 * Check php
 */
phpinfo();

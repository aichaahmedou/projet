<?php

$sname= "localhost";
$unmae= "root";
$password = "";

$db_name = "form_builder_db1";

$conn = mysqli_connect($sname, $unmae, $password, $db_name);

if (!$conn) {
	echo "Connection failed!";
}
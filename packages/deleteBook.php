<?php
require '../vendor/autoload.php';
use MongoDB\BSON\ObjectId;

$bookId = new ObjectId($_GET['id']);
$con = new MongoDB\Client('mongodb://localhost:27017');
$db = $con->admin;
$tbl = $db->tbl_bookshop;
$tbl->deleteOne(['_id'=>$bookId]);
echo "<script>location.href='displayBook.php'</script>";
?>

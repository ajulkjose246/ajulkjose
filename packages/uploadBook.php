<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Book</title>
</head>

<body>
    <form action="#" method="POST">
        Book Title : <input type="text" name="title" required><br><br>
        Book Author : <input type="text" name="author" required><br><br>
        Book Genre : <input type="text" name="genre" required><br><br>
        Book Price : <input type="text" name="price" required><br><br>
        Book Quantity : <input type="number" name="quantity" required><br><br>
        <input type="submit" value="Upload" name="subBtn">
    </form><br><br>
    <a href="displayBook.php">Display Books</a>
</body>
<?php
if (isset($_POST['subBtn'])) {
    $title = $_POST['title'];
    $author = $_POST['author'];
    $genre = $_POST['genre'];
    $price = (int)$_POST['price'];
    $quantity = (int)$_POST['quantity'];

    require '../vendor/autoload.php';
    $con = new MongoDB\Client('mongodb://localhost:27017');
    $db = $con->admin;
    $tbl = $db->tbl_bookshop;
    $val = array('Title' => $title, 'Author' => $author, 'Genre' => $genre, 'Price' => $price, 'Quantity' => $quantity);
    $tbl->insertOne($val);
    echo "<script>alert('Data inserted successfully.')</script>";
}

?>

</html>
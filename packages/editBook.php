<?php
require '../vendor/autoload.php';

use MongoDB\BSON\ObjectId;

$bookId = new ObjectId($_GET['id']);
$con = new MongoDB\Client('mongodb://localhost:27017');
$db = $con->admin;
$tbl = $db->tbl_bookshop;
$book = $tbl->findOne(['_id' => $bookId]);
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Book</title>
</head>

<body>
    <form action="#" method="POST">
        Book Title : <input type="text" name="title" value="<?= $book['Title'] ?>" required><br><br>
        Book Author : <input type="text" name="author" value="<?= $book['Author'] ?>" required><br><br>
        Book Genre : <input type="text" name="genre" value="<?= $book['Genre'] ?>" required><br><br>
        Book Price : <input type="text" name="price" value="<?= $book['Price'] ?>" required><br><br>
        Book Quantity : <input type="number" name="quantity" value="<?= $book['Quantity'] ?>" required><br><br>
        <input type="submit" value="Edit" name="editBtn">
    </form><br><br>
    <a href="displayBook.php">Display Books</a>
</body>
<?php
if (isset($_POST['editBtn'])) {
    $title = $_POST['title'];
    $author = $_POST['author'];
    $genre = $_POST['genre'];
    $price = $_POST['price'];
    $quantity = $_POST['quantity'];
    $tbl->updateOne(
        [ '_id' => $bookId ],
        ['$set'=>['Title' => $title, 'Author' => $author, 'Genre' => $genre, 'Price' => $price, 'Quantity' => $quantity]]

    );
    echo "<script>location.href='displayBook.php'</script>";

}
?>

</html>
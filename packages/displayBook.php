<?php
require '../vendor/autoload.php';
$con = new MongoDB\Client('mongodb://localhost:27017');
$db = $con->admin;
$tbl = $db->tbl_bookshop;
$result = $tbl->find();
$i = 0;
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Display Book</title>
</head>

<body>
    <center>
        <h4>Book Details</h4>
        <table border="2">
            <tr>
                <th>#</th>
                <th>Title</th>
                <th>Author</th>
                <th>Genre</th>
                <th>Price</th>
                <th>Quantity</th>
                <th colspan="2">Action</th>
            </tr>
            <?php foreach ($result as $book) {
                $i = $i + 1; ?>
                <tr>
                    <td><?= $i ?></td>
                    <td><?= $book['Title'] ?></td>
                    <td><?= $book['Author'] ?></td>
                    <td><?= $book['Genre'] ?></td>
                    <td><?= $book['Price'] ?></td>
                    <td><?= $book['Quantity'] ?></td>
                    <td><a href="./editBook.php?id=<?= $book['_id'] ?>">Edit</a></td>
                    <td><a href="./deleteBook.php?id=<?= $book['_id'] ?>">Delete</a></td>
                </tr>
            <?php } ?>

        </table><br><br>

        <?php
        $condition = ['Quantity' => ['$lt' => 5]];
        $abc = $tbl->find($condition);
        $i = 0;
        ?>
        <h4>Books that are running low in stock</h4>
        <table border="2">
            <tr>
                <th>#</th>
                <th>Title</th>
                <th>Author</th>
                <th>Genre</th>
                <th>Price</th>
                <th>Quantity</th>
                <th colspan="2">Action</th>
            </tr>
            <?php foreach ($abc as $book) {
                $i = $i + 1; ?>
                <tr>
                    <td><?= $i ?></td>
                    <td><?= $book['Title'] ?></td>
                    <td><?= $book['Author'] ?></td>
                    <td><?= $book['Genre'] ?></td>
                    <td><?= $book['Price'] ?></td>
                    <td><?= $book['Quantity'] ?></td>
                    <td><a href="./editBook.php?id=<?= $book['_id'] ?>">Edit</a></td>
                    <td><a href="./deleteBook.php?id=<?= $book['_id'] ?>">Delete</a></td>
                </tr>
            <?php } ?>

        </table><br><br>
        <form action="#" method="post">
            <input type="number" name="test">
            <input type="submit" name="submit">
        </form>
        <?php
        if (isset($_POST['submit'])) {
            $price = (int)$_POST['test'];
            $condition = ['Price' => ['$lt' => $price]];
            $abc = $tbl->find($condition);
            $i = 0;
        ?>
            <h4>Books that are running low in stock</h4>
            <table border="2">
                <tr>
                    <th>#</th>
                    <th>Title</th>
                    <th>Author</th>
                    <th>Genre</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th colspan="2">Action</th>
                </tr>
                <?php foreach ($abc as $book) {
                    $i = $i + 1; ?>
                    <tr>
                        <td><?= $i ?></td>
                        <td><?= $book['Title'] ?></td>
                        <td><?= $book['Author'] ?></td>
                        <td><?= $book['Genre'] ?></td>
                        <td><?= $book['Price'] ?></td>
                        <td><?= $book['Quantity'] ?></td>
                        <td><a href="./editBook.php?id=<?= $book['_id'] ?>">Edit</a></td>
                        <td><a href="./deleteBook.php?id=<?= $book['_id'] ?>">Delete</a></td>
                    </tr>
                <?php } ?>

            </table><br><br>
        <?php } ?>
        <a href="./uploadBook.php">Back</a>
    </center>
</body>

</html>
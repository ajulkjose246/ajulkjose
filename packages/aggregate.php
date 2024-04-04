<?php
require "./vendor/autoload.php";

use MongoDB\Client;

$con = new Client("mongodb://localhost:27017");
$db = $con->admin;
$collection = $db->student;

$doc = [
    ['student_id' => 'P004', 'class' => 103, 'section' => 'B', 'course_fee' => 19],
    ['student_id' => 'P005', 'class' => 104, 'section' => 'C', 'course_fee' => 20],
    ['student_id' => 'P006', 'class' => 102, 'section' => 'A', 'course_fee' => 21]
];

$collection->insertMany($doc);
echo "Successfully inserted documents<br>";


echo "<b>(i)calculate the total course fee of all the students in Section A</b><br>";
$result = $collection->aggregate([
    ['$match' => ['section' => "A"]],
    ['$group' => ['_id' => 'student_id', 'total' => ['$sum' => '$course_fee']]]
]);

foreach ($result as $document) {
    echo "Total course fee for section A: " . $document['total'] . "<br>";
}


echo "<b>(ii)calculate the total course fee for each class</b><br>";
$result = $collection->aggregate([
    ['$group' => ['_id' => '$class', 'total' => ['$sum' => '$course_fee']]]
]);

foreach ($result as $document) {
    echo "Total course fee for class " . $document['_id'] . ": " . $document['total'] . "<br>";
}


echo "<b>(iii) count the number of students in each class</b><br>";
$result = $collection->aggregate([
    ['$group' => ['_id' => '$class', 'count' => ['$sum' => 1]]]
]);

foreach ($result as $document) {
    echo "Number of students in class " . $document['_id'] . ": " . $document['count'] . "<br>";
}


echo "<b>(iv) Find the student with highest course fee in each class</b><br>";
$result = $collection->aggregate([
    ['$group' => ['_id' => '$class', 'count' => ['$sum' => 1]]]
]);

foreach ($result as $document) {
    echo "Number of students in class " . $document['_id'] . ": " . $document['count'] . "<br>";
}


//4
echo "(iv) Find the student with highest course fee in each class <br>";
$data1 = $collection->aggregate([

    ['$group' => [ '_id' => '$class', 'total' => [ '$max' => 
    [ 'course_fee' => '$course_fee', 'student_id' => '$student_id', ],
        ],
    ]],
]);
foreach ($data1 as $result) {
    echo "Class: " . $result['_id'] . ", Maximun Cousre : " . $result['total']['course_fee'] . ", Student ID: " . $result['total']['student_id'] ."<br>";
}


echo "(v) Find the class with the highest total course fee<br>";
$data1 = $collection->aggregate([
    ['$group' => ['_id' => '$class', 'total_fee' => ['$sum' => '$course_fee'], ]],
    ['$sort' => ['total_fee' => -1]],
    ['$limit' => 1],
]);

foreach ($data1 as $result) {
    echo "Class with Highest Total Course Fee: " . $result['_id'] . ", Total Course Fee: " . $result['total_fee'] . "<br>";
}


echo "(vi) Calculate the total course fee for each section and sort the result in descending order<br>";
$data1 = $collection->aggregate([
    ['$group' => [ '_id' => '$section', 'total_fee' => ['$sum' => '$course_fee'],]],
    ['$sort' => ['total_fee' => -1]],
]);

foreach ($data1 as $result) {
    echo "Section: " . $result['_id'] . ", Total Course Fee: " . $result['total_fee'] . "<br>";
}
?>
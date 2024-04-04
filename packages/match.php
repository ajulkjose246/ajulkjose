<?php
require "./vendor/autoload.php";

// Connect to MongoDB
$con = new MongoDB\Client("mongodb://localhost:27017");
$db = $con->testdb;

// Display connection status
echo "Connection successful\n";

// Select the collection
$col = $db->sample;

// Clear the collection before inserting documents
$col->deleteMany([]);

// Insert multiple documents
$docs = [
    ['Name' => 'arya', 'Age' => 22, 'E-mail' => 'arya@gmail.com'],
    ['Name' => 'john', 'Age' => 30, 'E-mail' => 'john@example.com'],
    ['Name' => 'emma', 'Age' => 25, 'E-mail' => 'emma@example.com'],
    ['Name' => 'anu', 'Age' => 26, 'E-mail' => 'anu@example.com'],
    ['Name' => 'anju', 'Age' => 25, 'E-mail' => 'anu@example.com']
];

$col->insertMany($docs);

echo "Documents inserted successfully\n";

// Define the aggregation pipeline with $match and $sort stages
$pipeline = [['$match' => ['Age' => ['$gte' => 25]]]];
// Execute the aggregation pipeline
$cursor = $col->aggregate($pipeline);

// Display the sorted documents
foreach ($cursor as $document) {
    echo "Name: " . $document['Name'] . ", Age: " . $document['Age'] . ", E-mail: " . $document['E-mail'] . "\n";
}

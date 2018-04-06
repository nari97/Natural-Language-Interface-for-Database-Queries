<?php

$servername = "localhost";
$username = "nari";
$password = "N97@rayanan";
$dbname = "SQLProject";

$link = mysqli_connect($servername, $username, $password, $dbname);

    if(!$link) {
        die('Could not connect');
    }
    


    /*output = shell_exec("python2.7 /home/nari/MySQLProject/Python/NliQuery.py $query");
    $arr = explode("...",$output);
    $i = 0;
    foreach($arr as $value) {
        $i++;
        //echo $value;
    }
    $j = 0;
    while($j<$i-1){
        $newArr[$j] = $arr[$j];
        $j++;
    }

    
    $query = $arr[$i-1];
    //echo $query;

    $sql = $query;
    if($result = mysqli_query($link, $sql)){
        if(mysqli_num_rows($result) > 0){
            echo '<div class="table-responsive-vertical shadow-z-1">';
            echo '<center><table id = "table" class="table table-hover table-mc-light-blue">';
            echo '<tr>';    

            foreach($newArr as $value) {
                echo '<th>';
                echo $value;
                echo '</th>';
            }
            echo '</tr>';


        }

*/

$query = "select * from Student";
if($result = mysqli_query($link,$query)){
    /*
	while ($i < mysqli_num_fields($result)) {
    		//echo "Information for column $i:<br />\n";
    		$meta = mysqli_fetch_field($result);

		echo $meta->name;
		$i++;
    }*/

    $meta = mysqli_fetch_field($result);
    echo $meta->name;
    
}


?>

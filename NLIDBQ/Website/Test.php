


<html>
    <body>
        <form method ="GET" action = "">
            <input type="text" placeholder="Enter query" name = "query">
            <input type="submit">
        </form>
        <h1>
        <?php
            if($_SERVER["REQUEST_METHOD"]=="POST")
            {
                $query = $_GET["query"];
            }
        
            echo $query;
        ?>
        </h1>
    </body>
</html>
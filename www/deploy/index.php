<?php

function taillog() {
    $logfile = "/data/servers/portal.theubi.com_" . $_GET["port"] . "/logs/catalina.out";
    $fp = fopen($logfile, "rb");
    if ( isset($_GET["offset"])) {
        $offset=$_GET["offset"];
    }
    else {
        $offset=filesize($logfile) - 300;
    }

    $total = filesize($logfile);
    if (($total - $offset) > 1024) {
        $offset = $total - 1024;
    }
    fseek($fp, $offset);
    header("Access-Control-Expose-Headers: X-File-Offset,Content-Length");
    header("X-File-Offset: $offset");
    fpassthru($fp);
    fclose($fp);

    passthru($cmd);
}

    $port = $_GET["port"];
    $version = $_GET["version"];
    $action = $_GET["action"];

    header("Access-Control-Allow-Origin:*");
    if (strcasecmp($action,"start") == 0) {
        $output = system("/ucic/bin/portal -q -p $port start $version", $ret);
        echo $output;
    }
    else if (strcasecmp($action,"restart") == 0) {
        $output = system("/ucic/bin/portal -q -p $port restart", $ret);
        echo $output;
    }
    else if (strcasecmp($action, "stop") == 0) {
        $output = system("/ucic/bin/portal -q -p $port stop", $ret);
        echo $output;
    }
    else if (strcasecmp($action, "taillog") == 0) {
        taillog();
    }


?>

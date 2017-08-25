<?php

$script = '';
$sid = $GET_['sid'];

$exit_status = exec('python3.6 $script $sid');

?>
<!DOCTYPE html>
<html>
<head>
	<title>Barrong Bot</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

	<div id="mainform">
		<?php echo $exit_status; ?>
	</div>

</body>
</html>
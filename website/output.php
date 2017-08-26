<?php

$script = ''; // The location of the script
$sid = $GET_['sid'];
$method = $GET_['method'];
$passw = $GET_['passw'];
$hPassword = md5($passw)
$oPassword = "6b17a6cd9cc29d3f67f8c8edc39fed82"; // palceholder for the moment xd

#if ($oPassword == $hPassword) {
	#$exit_status = exec('python3.6 $script $method $sid');
#}

?>
<!DOCTYPE html>
<html>
<head>
	<title>Barronged Bot</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

	<div id="mainform" style="height: 300px; margin-top: -150px">

		<b>

			<?php 
				if ($hPassword != $oPassword) {
					echo " [>] Wrong Password kiddo":
				} else {
					echo " [>] Sending $method to $sid."
				}
			 ?>
			 
		</b>

		<?php echo $exit_status; ?>

	</div>

</body>
</html>
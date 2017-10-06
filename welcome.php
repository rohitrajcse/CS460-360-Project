<html>
<h1 style="color: #5e9ca0;">Uidaho Database Systems Project</h1>
<p>CS 360 Fall 2017</p>
<body>

<!-- CSS Styles -->
<style>
  .speech {border: 1px solid #DDD; width: 300px; padding: 0; margin: 0}
  .speech input {border: 0; width: 240px; display: inline-block; height: 30px;}
  .speech img {float: right; width: 40px }
</style>

<!-- Search Form -->
<form id="labnol" method="post" action="welcome.php"> <!action="https://www.google.com/search">
  Sentance: <div class="speech">
    <input type="text" name="raw" id="transcript" placeholder="Speak" />
    <img onclick="startDictation()" src="//i.imgur.com/cHidSVu.gif" />
  </div>
  <input type="submit">
</form>



Input: <?php echo $_POST["raw"]; ?><br>
<br>
Output: <br>
<?php 

$command = escapeshellcmd('/home/ubuntu/workspace/main.py');
$arg     = " " . "\"" . $_POST["raw"] . "\"";
$output = shell_exec($command . $arg);
echo $output;
?>


<!-- HTML5 Speech Recognition API -->
<script>
  function startDictation() {

    if (window.hasOwnProperty('webkitSpeechRecognition')) {

      var recognition = new webkitSpeechRecognition();

      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.lang = "en-US";
      recognition.start();

      recognition.onresult = function(e) {
        document.getElementById('transcript').value
                                 = e.results[0][0].transcript;
        recognition.stop();
        document.getElementById('labnol').submit();
      };

      recognition.onerror = function(e) {
        recognition.stop();
      }

    }
  }
</script>

</body>
</html> 
<?php
  if (isset($_COOKIE["debug"]) == false) {
    setcookie("debug", "false");
  }
  $debug = strtolower($_COOKIE["debug"]);

  if (!empty($_POST)) {
    try {
      libxml_disable_entity_loader (false);
      $xmlfile = $_POST["xdata"];
      $dom = new DOMDocument();
      $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
      $style = simplexml_import_dom($dom);
    } catch(Exception $e) {

    }

  }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your custom UI</title>
  <script src="post.js"></script>
</head>
<body>
  <div style="max-width:600px; margin:auto">
    <h1>Your custom button!</h1>
    <? if(isset($style) == false) { ?>
      <button style="background-color: #008CBA; padding: 15px 32px;">
        Your custom button
      </button>
    <? } else {?>
      <button style="background-color: <?= $style->color ?>; padding: 15px 32px;">
        <?= $style->value ?>
      </button>
    <? } ?>
    <h2>Customize button form</h2>
    <form action="?" method="post">
      <input type="hidden" name="xdata" id="xdata">
      Color in RGB:
      <input type="text" id="btnColor"><br>
      Value in text:
      <input type="text" id="btnValue"><br>
      <input type="submit" value="Update button">
    </form>
  </div>

  <div>

  </div>
  <?php
    if ($debug == "true") {
      echo "<!-- TODO: Delete flag.txt from /etc/ -->";
    }
  ?>
</body>
</html>

<?php
      // this is how I store hashes right?
      $hash = "0e770334890835629000008642775106";
      if(array_key_exists("combination",$_REQUEST) && $_REQUEST["combination"] !== ''){
          //Isn't it great that == works in every language?
          if(array_key_exists("debug", $_REQUEST)){
              echo "<br> ". md5($_REQUEST["combination"]);
          }
          if(md5($_REQUEST["combination"]) == $hash){
              echo "<br> The Flag is flag{...}<br>";
          }
          else{
              echo "<br>Wrong!<br>";
          }

      }
?>
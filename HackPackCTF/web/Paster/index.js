(function anonymous(
) {
parent.postMessage(window.location.toString(),"*");var originalAlert=window.alert;window.alert=function(t){parent.postMessage("success","*"),flag=atob("ZmxhZ3t4NTVfaTVOdF83aEE3X2JBRF9SMUdoNz99"),setTimeout(function(){originalAlert("Congratulations, you executed an alert:\n\n"+t+"\n\nhere is the flag: "+flag)},50)};
})



var callCurrentTemp = function() {
  var customername = document.getElementById("customername").value
  var generatedkey = document.getElementById("gnrtkey").value
  var appservicename = document.getElementById("appservicename").value
  var appurl = document.getElementById("appurl").value
  var datafactoryname = document.getElementById("datafactoryname").value
  var accountname = document.getElementById("accountname").value
  var accesskey = document.getElementById("accesskey").value
  var connectstring = document.getElementById("connectstring").value
  var servername = document.getElementById("servername").value
  var sqlusername = document.getElementById("sqlusername").value
  var sqlpass = document.getElementById("sqlpass").value
  var dbname = document.getElementById("dbname").value
  var databricksname = document.getElementById("databricksname").value
  var accesstoken = document.getElementById("accesstoken").value
  var workspaceurl = document.getElementById("workspaceurl").value
  var powerbiname = document.getElementById("powerbiname").value
  var powerbiadmin = document.getElementById("powerbiadmin").value
  var keyvaultname = document.getElementById("keyvaultname").value
  var subid = document.getElementById("subid").value
  var tenid = document.getElementById("tenid").value
  var clientid = document.getElementById("clientid").value
  var clientsecret = document.getElementById("clientsecret").value
  var resourcegroup = document.getElementById("resourcegroup").value
  var sqlcon = document.getElementById("sqlcon").value
  var dflocation = document.getElementById("dflocation").value
  var azurefunction = document.getElementById("azurefunction").value
  var keyvaultlocation = document.getElementById("keyvaultlocation").value
  var rglocation = document.getElementById("rglocation").value
  var sources = document.getElementById("dftypes").value
  var bqproject = document.getElementById("bqproject").value
  var bqclient = document.getElementById("bqclient").value
  var bqsecret = document.getElementById("bqsecret").value
  var bqtoken = document.getElementById("bqtoken").value
  var bqschema = document.getElementById("bqschema").value
  var bqtables = document.getElementById("bqtables").value
  var oracleport = document.getElementById("oracleport").value
  var oraclesid = document.getElementById("oraclesid").value
  var oracleuser = document.getElementById("oracleuser").value
  var oraclepassword = document.getElementById("oraclepassword").value
  var oracleschema = document.getElementById("oracleschema").value
  var oracletable = document.getElementById("oracletable").value
  var sapserver = document.getElementById("sapserver").value
  var sapusername = document.getElementById("sapusername").value
  var sappassword = document.getElementById("sapschema").value
  var sapschema = document.getElementById("sapschema").value
  var saptable = document.getElementById("saptable").value
var salesforceuser = document.getElementById("salesforceuser").value
var salesforcepass = document.getElementById("salesforcepass").value
var salesforcetoken = document.getElementById("salesforcetoken").value
var salesforceschema = document.getElementById("salesforceschema").value
var salesforcetables = document.getElementById("salesforcetables").value

  //added...
  // var dfsource = document.getElementById("dftypes").value

  console.log(sources)
    console.log(customername)
   console.log(dflocation)
   console.log(appservicename)
   console.log(appurl)
   console.log(datafactoryname)
   console.log(accountname)
   accesskey=encodeURIComponent(accesskey)
  console.log(accesskey)
   console.log(connectstring)
   console.log(servername)
   console.log(sqlusername)
   console.log(sqlpass)
   console.log(dbname)
   console.log(databricksname)
   console.log(accesstoken)
   console.log(workspaceurl)
   console.log(powerbiname)
   console.log(powerbiadmin)
   console.log(keyvaultname)
   console.log(subid)
   console.log(tenid)
   console.log(clientid)
   console.log(clientsecret)
   console.log(resourcegroup)
   console.log(keyvaultlocation)
   console.log(rglocation)
  // $('#loader').css('visibility','visible')


  $.ajax({
    url: 'http://127.0.0.1:5000/testpy?appservicename='+appservicename+'&appurl='+appurl+'&datafactoryname='+datafactoryname+'&accountname='+accountname+'&accesskey='+accesskey+'&connectstring='+connectstring+'&servername='+servername+'&sqlusername='+sqlusername+'&sqlpass='+sqlpass+'&dbname='+dbname+'&databricksname='+databricksname+'&accesstoken='+accesstoken+'&workspaceurl='+workspaceurl+'&powerbiname='+powerbiname+'&powerbiadmin='+powerbiadmin+'&keyvaultname='+keyvaultname+'&subid='+subid+'&tenid='+tenid+'&clientid='+clientid+'&clientsecret='+clientsecret+'&resourcegroup='+resourcegroup+'&sqlcon='+sqlcon+'&dflocation='+dflocation+'&azurefunction='+azurefunction+'&keyvaultlocation='+keyvaultlocation+'&rglocation='+rglocation+'&sources='+sources+'&bqproject='+bqproject+'&bqsecret='+bqsecret+'&bqtoken='+bqtoken+'&bqschema='+bqschema+'&bqtables='+bqtables+'&oracleport='+oracleport+'&oraclesid='+oraclesid+'&oracleuser='+oracleuser+'&oraclepassword='+'&oracleschema='+oracleschema+'&oracletable='+oracletable+'&sapserver='+sapserver+'&sapusername='+sapusername+'&sappassword='+sappassword+'&sapschema='+sapschema+'&saptable='+saptable+'&salesforcepass='+salesforcepass+'&salesforcetoken='+salesforcetoken+'&salesforceschema='+salesforceschema+'&salesforcetables='+salesforcetables,
    method: "GET",
    contentType: "application/json; charset=utf-8",
    success: function(data) {
      console.log(this.url);
      console.log(data);
      alert('Details submitted successfuly.');
    },
    error: function(data){
      ("Failed to send the request");
    }

  });

};


$('input').attr('autocomplete','off');

$("#appservicename").focusin(function() {
    $("#servicename").show();
}).focusout(function () {
    $("#servicename").hide();
});

function showHelp(id) {
  jqid = '#' + id;
  $(jqid).css("visibility","visible");
}

function hideHelp(id) {
  jqid = '#' + id;
  $(jqid).css("visibility","hidden");
}


function Random() {
        var rnd = Math.floor(Math.random() * 1000000000);
        document.getElementById('genkey').value = rnd;
    }




$(function() {
        $('#dftypes').change(function(){
            $('.hidden-div').hide();
            $('#' + $(this).val()).show();
        });
    });


$(document).ready(function() {
    $("#add").click(function(e) {
        e.preventDefault();
        // alert("Submitting Details...");
        $("#loader").css("visibility","hidden");
        $("#contents").css("visibility","visible");
    });
});

document.onreadystatechange = function () {
  var state = document.readyState
  if (state == 'interactive') {
       document.getElementById('contents').style.visibility="hidden";
  } else if (state == 'complete') {
      setTimeout(function(){
         document.getElementById('interactive');
         document.getElementById('loader').style.visibility="hidden";
         document.getElementById('contents').style.visibility="visible";
      },1000);
  }
}

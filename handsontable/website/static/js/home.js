var arr;

$(document).ready( function() {
    
    // var $container = $("#handsontable"),
    //     handsontable = $container.data('handsontable'),
    //     data = [
    //         ["", "Maserati", "Mazda", "Mercedes", "Mini", "Mitsubishi"],
    //         ["2009", 0, 2941, 4303, 354, 5814],
    //         ["2010", 5, 2905, 2867, 412, 5284],
    //         ["2011", 4, 2517, 4822, 552, 6127],
    //         ["2012", 2, 2422, 5399, 776, 4151]
    //     ],
    //     config = {
    //         data: data,
    //         // minRows: 15,
    //         // minCols: 6,
    //         minSpareRows: 0,
    //         autoWrapRow: true,
    //         colHeaders: true,
    //         currentRowClassName: 'currentRow',
    //         currentColClassName: 'currentCol',
    //         contextMenu: {
    //             items: {
    //                 "row_above": {},
    //                     "row_below": {},
    //                     "hsep1": "---------",
    //                     "col_left": {},
    //                     "col_right": {},
    //                     "hsep2": "---------",
    //                     "remove_row": {},
    //                     "remove_col": {}
    //             }
    //         }
    //     };

  var data = [[]];
  
  var container = document.getElementById('handsontable');
  var table = new Handsontable(container,
  {
    data: data,
    minRows: 25,
    minCols: 26,
    minSpareRows: 0,
    colHeaders: true,
    contextMenu: true
  });

 arr =table.getData();
    $("#divButtons").find(".btnSubmit").click(function () {
       console.log(table.getData(),table.getData().length);
        // console.log($container.data('handsontable').getData());
        // var arr = { data: $container.data('handsontable').getSourceData()};
        // added $.ajax({}) by Aayush
        var arr =table.getData();
        $.ajax({
        url: '/result',
        type: 'POST',
        data: JSON.stringify(arr),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        async: true,
        success: function(msg) {
            msg = JSON.stringify(msg["OUTPUT"]);
            console.log(msg);
            $('#demo').empty().append(msg);
            // alert(msg);
          }
          });
        // var blob = new Blob([JSON.stringify(data)], {type: 'text/'+'json'}),
        //     csvURL =window.URL.createObjectURL(blob);

        // tempLink = document.createElement('a');
        // tempLink.href = csvURL;
        // tempLink.setAttribute('download', 'filename.json');
        // tempLink.click();
    });

   /* $(".dropdown-menu li a").click(function () {
         console.log("Selected Option:"+$(this).text());
         console.log(JSON.stringify(data));
        
        $.ajax({
                cache: false,
               // used data from url
                url:"/downloads/filename.json",
                datatype: "json",
                data: JSON.stringify(data),
                type: "POST",
                success: function (res) {
                   console.log(res);
                },
                error: function () {
                    console.log("ERROR");
                }
            });
            return false;
    });*/
    // $("#handsontable").handsontable(config);
// $("#fileUpload").change(function (){
//       uploadFile();
//      });
// //upload csv
// function uploadFile()
// {
//   var url = $("#fileUpload").val();  //gets filename from html input field

//   var xhr = (window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP"));
//   xhr.onreadystatechange = XHRhandler;
//   xhr.open("GET", url, true);
//   xhr.send(null);

//   function XHRhandler() {
//     if (xhr.readyState == 4) {

//       //the raw text from the file
//       var rawText = xhr.responseText;
//       xhr = null;
//       makeDataArray(); //Make a function that uses the rawText 
//                        //and parse out an array for the data portion of the table.
//       makeTable();     //Make a function that renders the table with the data
//     }
//   }
// }
});

function LoadData(){
    arr = [[1,2],[3,4]]
    mail = 'atishay197@gmail.com'
    dts = Date.now()
    id = mail + ":" + dts
    var data= {
        _id: id,
        data :arr
    };
$.ajax({
        url: '/data',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',

        dataType: 'json',
        async: true,
        success: function(msg) {
            console.log(msg);
          }
        });
        console.log("load",JSON.stringify(data));
    }


function New(){
    // ask if want to save data, if yes call save, else clear handson table
    // make no further changes
    arr = [[]]
    ret = [[]]
    email = ' '
    FunctionName ='New'
    timestamp = Date.now()
    projectname = 'SampleProject'
    _id = projectname + " : " + timestamp
    var data= {
        _id: _id,
        email: email,
        timestamp: timestamp,
        projectname: projectname,
        count:0,
        FunctionName:FunctionName,
        returneddata:ret,
        data: arr
    };
$.ajax({
        url: '/new',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',

        dataType: 'json',
        async: true,
        success: function(msg) {
            console.log(msg);
          }
          });
        console.log("load",JSON.stringify(data));
    }


function Open(){
    // Ask user what file to open
    // import and store data in handsontable and from there import into arr
    arr = [[1,4],[3,5]]
    // remove above line if hanson table data stored in arr
    ret = [[]]
    email = ' '
    FunctionName ='ImportFile'
    timestamp = Date.now()
    projectname = 'SampleProject1'
    _id = projectname + ":" + timestamp
    var data= {
        _id: _id,
        email: email,
        timestamp: timestamp,
        projectname: projectname,
        count:0,
        FunctionName:FunctionName,
        returneddata:ret,
        data: arr
    };
$.ajax({
        url: '/importfile',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',

        dataType: 'json',
        async: true,
        success: function(msg) {
            console.log(msg);
          }
        });
        //console.log("load",JSON.stringify(data));
    }

function ImportFile(){
    // Ask user what file to open
    // import and store data in handsontable and from there import into arr
    arr = [[1,4],[3,5]]
    // remove above line if hanson table data stored in arr
    ret = [[]]
    email = ' '
    FunctionName ='ImportFile'
    timestamp = Date.now()
    projectname = 'SampleProject1'
    _id = projectname + ":" + timestamp
    var data= {
        _id: _id,
        email: email,
        timestamp: timestamp,
        projectname: projectname,
        count:0,
        FunctionName:FunctionName,
        returneddata:ret,
        data: arr
    };
$.ajax({
        url: '/importfile',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',

        dataType: 'json',
        async: true,
        success: function(msg) {
            console.log(msg);
          }
        });
    }

function Undo(){
    // import and store data in handsontable and from there import into arr
    arr = [[3,4],[6,5]]
    // remove above line if hanson table data stored in arr
    ret = [[]]
    email = ' '
    FunctionName ='Undo'
    timestamp = Date.now()
    projectname = 'SampleProject1'
    _id = projectname + ":" + timestamp
    var data= {
        _id: _id,
        email: email,
        timestamp: timestamp,
        projectname: projectname,
        count:0,
        FunctionName:FunctionName,
        returneddata:ret,
        data: arr
    };
$.ajax({
        url: '/undo',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        async: true,
        success: function(msg) {
            console.log(msg);
          }
        });
    }
function Redo(){
    // import and store data in handsontable and from there import into arr
    // store project name in variable 'projectname'
    arr = [[6,7],[8,9]]
    projectname = 'SampleProject1'
    // remove above line if hanson table data stored in arr and project name stored in projectname
    ret = [[]]
    email = ' '
    FunctionName ='Redo'
    timestamp = Date.now()
    _id = projectname + ":" + timestamp
    var data= {
        _id: _id,
        email: email,
        timestamp: timestamp,
        projectname: projectname,
        count:0,
        FunctionName:FunctionName,
        returneddata:ret,
        data: arr
    };
$.ajax({
        url: '/redo',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        async: true,
        success: function(msg) {
            console.log(msg);
          }
        });
    }

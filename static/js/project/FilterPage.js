var checkedValue = null;
var valueList = [];
var inputElements = document.getElementsByClassName('custom-control-label');
for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           checkedValue = inputElements[i].value;
           values = checkedValue.split('-')
           valueJson = {
                            "id" : document.getElementById(i+1),
                            "min" : values[0],
                            "max" : values[1]
                        };
             valueList.push(valueJson);
           break;
      }

       if(!inputElements[i].checked){
           checkedValue = inputElements[i].value;
           values = checkedValue.split('-')
           for(var j=0;j<checkedValue.length;j++){
                if(valueList[j]["min"] == values[0]){
                    valueList.splice(j,1);
                }
                if(valueList[j]["max"] == values[1]){
                    valueList..splice(j,1);
                }
           }
           break;
      }
}
var filterJson = JSON.stringify(valueList);
$.ajax({
            type: 'POST' ,
            url: "/SearchedMenus",
            contentType: 'application/json; charset=utf-8',
            data: filterJson,
            success: function(response) {
                            window.location.href=response

            },
            error: function() {
                console.log();
            }
        });
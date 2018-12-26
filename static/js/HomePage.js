setTypeId(1)
function setTypeId(val){
localStorage.setItem("typeId", val);
    send_menu();
}

function send_menu()
{
var val=localStorage.getItem("typeId");
var json=JSON.stringify({"typeId":val});

send_json('POST','/menus',json);

}


function get_search_result(){
var input_id = localStorage.getItem("typeId");
var id = "text_search_" + input_id;
var search_json = JSON.stringify( { "input" : document.getElementById(id).value});
send_json('POST',"/SearchedMenus",search_json);
}



function send_json(send_type,send_url,send_data){

$.ajax({
            type: send_type ,
            url: send_url,
            contentType: 'application/json; charset=utf-8',
            data: send_data,
            success: function(response) {

                console.log(response);


            },
            error: function() {
                console.log();
            }
        });

}
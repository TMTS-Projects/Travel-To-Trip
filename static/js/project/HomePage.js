setTypeId(1)
function setTypeId(val){
localStorage.setItem("typeId", val);
    send_menu();
    datetimePickers();
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
var text_id = "text_search_" + input_id;
var checkin_id = "checkin_" + input_id;
var checkout_id = "checkout_" + input_id;
var rooms_id = "rooms_" + input_id;
var checkin = new Date(document.getElementById(checkin_id).value);
var checkin_date = checkin.getFullYear()+'-' + ("0" + (checkin.getMonth() + 1)).slice(-2) + '-'+("0" + checkin.getDate()).slice(-2);

var checkout = new Date(document.getElementById(checkout_id).value);
var checkout_date = checkout.getFullYear()+'-' + ("0" + (checkout.getMonth() + 1)).slice(-2) + '-'+("0" + checkout.getDate()).slice(-2);




var search_json = JSON.stringify( { "input" : document.getElementById(text_id).value,
                                   "checkin" : checkin_date,
                                   "checkout" : checkout_date,
                                   "rooms" : document.getElementById(rooms_id).value
                                   }
                                );
//send_json('POST',"/SearchedMenus",search_json);
$.ajax({
            type: 'POST' ,
            url: "/SearchedMenus",
            contentType: 'application/json; charset=utf-8',
            data: search_json,
            success: function(response) {
                            window.location.href=response

            },
            error: function() {
                console.log();
            }
        });
}


function send_json(send_type,send_url,send_data){

$.ajax({
            type: send_type ,
            url: send_url,
            contentType: 'application/json; charset=utf-8',
            data: send_data,
            success: function(response) {
                                        result= JSON.parse(response)
                                        if(!result.isFailure)
                                        {
                                             console.log(result.menuList)
                                        }
                                        else
                                        {
                                            console.log(result.message)
                                        }


            },
            error: function() {
                console.log();
            }
        });

}
function send_selected_menu(menuId){
var menu_json = JSON.stringify({"menuId" : menuId});

$.ajax({
            type: 'POST' ,
            url: '/singleMenu',
            contentType: 'application/json; charset=utf-8',
            data: menu_json,
            success: function(response) {

                console.log(response);


            },
            error: function() {
                console.log();
            }
        });

}
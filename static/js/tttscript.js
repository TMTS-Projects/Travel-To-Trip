// This is UI Script for travel to trip project Author Sureshkumar
$(document).ready(function() {
    // Start switching the search tabs in home banner
    $("li.nav-item").on('click', function() {
        var ref_id = $(this).children().attr("href");
        var filt_id = ref_id.substring(1, ref_id.length);
        var org_id = $("#homebanner .tab-content .tab-pane").attr("id");

        if (org_id = filt_id) {
            $("#homebanner .tab-content .tab-pane").removeClass("active");
            $("#" + org_id).addClass("active").removeClass("fade");
        }
    });
    // End switching the search tabs in home banner

    // Start hide and show of autocomplete list
    $(".auto_comp_input").keyup(function(e) {
            var input_length = $(this).val().length;
            if (input_length > 0) {
                 var myJSON = JSON.stringify({"text":$(this).val()});

                            $.ajax({
                            type:"POST",
                            url: "pressedMenus",
                            data: myJSON,
                            contentType: 'application/json;charset=UTF-8',
                            success: function(data){

                                        result= JSON.parse(data)
                                        autComplete(result["name"])
                                    }
                                });
                                $(this).siblings(".autocomp_list").addClass("show_list");
                    }
                else {
                    $(this).siblings(".autocomp_list").removeClass("show_list");
                }

    });
    // End hide and show of autocomplete list

  function autComplete(result)
  {
    var a=document.getElementById("autoCompleteList_Hotel");
    a.innerHTML="";
    for(var i=0; i<result.length;i++)
    {
        var li= document.createElement("li");
        li.innerText=result[i];
        a.appendChild(li);
    }
  }


});

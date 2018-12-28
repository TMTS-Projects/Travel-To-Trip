// This is UI Script for travel to trip project Author Sureshkumar
$(document).ready(function () {
    // Start switching the search tabs in home banner
    $("li.nav-item").on('click', function () {
        var ref_id = $(this).children().attr("href");
        var filt_id = ref_id.substring(1, ref_id.length);
        var org_id = $("#homebanner .tab-content .tab-pane").attr("id");

        if (org_id = filt_id) {
            $("#homebanner .tab-pane").removeClass("active");
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
                                        if(!result.isFailure)
                                        {
                                            autComplete(result.menuList)
                                        }
                                        else
                                        {
                                            console.log(result)
                                        }

                                    }
                                });
                                $(this).siblings(".autocomp_list").addClass("show_list");
                    }
                else {
                    $(this).siblings(".autocomp_list").removeClass("show_list");
                }

    });
    // End hide and show of autocomplete list


    // Start binding the autocomplete data list to input
    $(document).on("click",".autocomp_list ul li", function () {
        var autoListSelect = $(this).text();
        $(this).closest(".autocomp_list").siblings(".auto_comp_input").val(autoListSelect);
        $(this).closest(".autocomp_list").removeClass("show_list");
    });
    // End binding the autocomplete data list to input

    // Start selecting the ul list using keyboard up and down key
    var li = $('.keyboard_select li');
    var liSelected;
    $(window).keydown(function(e){
        if(e.which === 40){
            if(liSelected){
                liSelected.removeClass('selected');
                next = liSelected.next();
                if(next.length > 0){
                    liSelected = next.addClass('selected');
                }else{
                    liSelected = li.eq(0).addClass('selected');
                }
            }else{
                liSelected = li.eq(0).addClass('selected');
            }
        }else if(e.which === 38){
            if(liSelected){
                liSelected.removeClass('selected');
                next = liSelected.prev();
                if(next.length > 0){
                    liSelected = next.addClass('selected');
                }else{
                    liSelected = li.last().addClass('selected');
                }
            }else{
                liSelected = li.last().addClass('selected');
            }
        }
    });
    // End selecting the ul list using keyboard up and down key



    function autComplete(result)
  {
  var inputId=localStorage.getItem("typeId");
    var a=document.getElementById("autoCompleteList_"+inputId);
    a.innerHTML="";
    for(var i=0; i<result.length;i++)
    {
        var li= document.createElement("li");
        li.innerText=result[i];
        a.appendChild(li);
    }
  }
});



function datetimePickers()
{
var input_id = localStorage.getItem("typeId");
var checkin_id = "#checkin_" + input_id;
var checkout_id = "#checkout_" + input_id;

        var today = new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate());
        $(checkin_id).datepicker({

            uiLibrary: 'bootstrap4',
            iconsLibrary: 'fontawesome',
            minDate: today,
            maxDate: function () {
                return $(checkout_id).val();
            }
        });
        $(checkout_id).datepicker({

            uiLibrary: 'bootstrap4',
            iconsLibrary: 'fontawesome',
            minDate: function () {
                var dt= $(checkin_id).val()
                var d = new Date(dt);
                var convert=d.getDate()+1;
                var today = new Date(d.getFullYear(), d.getMonth(), convert);
                return today;
            }
        });

}




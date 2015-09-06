 $("#calendar").on("click", "td", function(){ 
          
            var day= $(this).html();
            var year= $(this).data("year");
            var month= $(this).data("month");
           $.get("/schedule/ajax_day_view/",{year: year, month: month, day: day}, function(data, status) {
              
                $("#modal-holder").html(data);
              var modal=$("#modal-holder").find("#myModal");
              
              modal.modal("show");
            
             modal.on('shown.bs.modal', function(event){
                    console.log("modal load success");
                    var button=modal.find(".request-btn");
                    
                    
                button.on("click", function(event){
                       console.log("request button clicked!!");
                        
                        var request_date= $(this).attr("data-requestdate");
                        var request_type= $(this).attr("data-request-type");
                         
                    $.ajax({
                        type: "POST",
                        url: "/schedule/myrequest/",
                        cache: "false",
                        data: {csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val(),
                        request_date: request_date, request_type: request_type},
                        success: RequestSuccess,
                        datatype: "html"
                            });
                   function RequestSuccess(data, textstatus, jqXHR){
                        console.log("request succeded");
                        $(".request-btn").hide();
                        $(".requestsentmsg strong").html(data);
                        $(".requestsentmsg").removeClass("hidden").addClass("visible");
                        
                        
                    }
                });
            });
        
             
            });
        });


$(document).ready(function(){
   $("ol.all-comment-list").hide();
   
   $("ol#post-list").on('keyup','.comment-input', function(event){
      event.preventDefault();
      console.log("hello");
      var p_id=$(this).attr("data-post-id");
      console.log(p_id);
       //var txt=$("#post-list #comment-input-"+p_id).val();
       var txt=$(this).val();
       console.log(txt);
      if (txt == "") {
         
         $("#send-btn-"+p_id).attr("disabled","disabled");
         console.log("empty txt");
      }
      else {
         $("#send-btn-"+p_id).removeAttr("disabled");
         console.log("non empty");
      }
   });

   
});

$("ol#post-list").on("click","a.show-comment-list",function(e){
    e.preventDefault();
   console.log("show-comment-list executed!!");
   var p_id=$(this).attr("data-post-id");
   $("ul#comment-list-"+p_id).show();
   console.log("post id is: "+p_id);
});

$("#post-form").on("submit", function(event){
   event.preventDefault();
   console.log("form submit event executed!!");
   create_post();
});

function create_post(){
   console.log("create_post function call successfull")
   $.ajax({
         url: "/messageboard/create_post/",
         type: "POST",
         data: {msg_text : $('#msgbox').val(), csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()},
         success: function(html){
            console.log($('#msgbox').val());
            $('#msgbox').val('');
            $("#post-list").prepend('<li>'+html+'</li>');
            console.log(html);
             $("#post-list li:first").fadeIn("slow");
            
         },
         
         error: function(xhr, errormessage, err){
            $("#error-div").html('<div class="alert alert-danger">'+
            '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>'+ 
            '<strong>'+errormessage+'</strong>');
         }
         
      });
}

$("ol#post-list").on("submit","form.comment-form", function(event){
   event.preventDefault();
   console.log("comment-form submit button triggered!!!");
   
   
   add_comment();
});

function add_comment(){
   console.log("add_comment function call successfull.");
   var p_id=$("ol#post-list input[type=submit]:focus").attr("data-postid");
   var comment_count=parseInt($("#comment-counter-"+p_id).text(),10);
   console.log(p_id);
   $.ajax({
      url: "/messageboard/add_comment/",
      type: "POST",
      data: {post_id: p_id, comment_text:$("#comment-input-"+p_id).val(), csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()},
      success: function(html){
          console.log(html);
         $("#comment-input-"+p_id).val('');
         $("ul#comment-list-"+p_id).append('<li>'+html+'</li>');
         $("ul#comment-list-"+p_id).show();
         comment_count += 1;
         $("#comment-counter-"+p_id).text(comment_count);
         console.log("comment add success")
         console.log(comment_count);
      }
   });
}
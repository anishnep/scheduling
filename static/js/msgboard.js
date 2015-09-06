$(document).ready(function(event){
   $(".all-comments-list").hide(); 
   $("#post-btn").attr('disabled','disabled');
   
   
   $("#msgbox").keyup(function(){
      $("#post-btn").attr('disabled','disabled');
      var post = $("#msgbox").val();
   if (post != ""){
      $("#post-btn").removeAttr('disabled');
   }
   });
   
   $("ul#post-list").on("keyup",".comment-input", function(e){
      e.preventDefault();
      var post_id= $(this).attr("data-post-id");
      var comment_txt=$(this).val();
      console.log(comment_txt);
      if (comment_txt === ""){
         $("#send-btn-"+post_id).attr("disabled","disabled");
         console.log("empty text");
      }
      else {
         $("#send-btn-"+post_id).removeAttr("disabled");
         console.log("non-empty txt");
      }
   });
   
   
});


$("ul#post-list").on("click","a.show-comments-list", function(e){
   e.preventDefault();
   var post_id=$(this).attr("data-post-id");
   console.log(post_id);
   $("ul#comment-list-"+post_id).show();
   
   });

$("#post-form").on("submit", function(event){
   event.preventDefault();
   console.log("form submitted");
   create_post();
});

function create_post(){
   console.log("function call successfull");
   $.ajax({
         url: "/messageboard/create_post/",
         type: "POST",
         data: {msg_text : $('#msgbox').val(), csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()},
         success: function(html){
            console.log($('#msgbox').val());
            $('#msgbox').val('');
            $("#post-btn").attr("disabled","disabled");
            $("#post-list").prepend('<li>'+html+'</li>');
            
             $("#post-list li:first").fadeIn("slow");
            
         },
         
         error: function(xhr, errormessage, err){
            $("#error-div").html('<div class="alert alert-danger">'+
            '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>'+ 
            '<strong>'+errormessage+'</strong>');
         }
         
      });
}

$("ul#post-list").on("submit", "form.comment-form", function(event){
   event.preventDefault();
   console.log("comment form submit click.");
   console.log($(".send-btn").attr("data-postid"));
   add_comment();
});

function add_comment(){
   console.log("comment function call successfull.");
  var p_id=$("ul#post-list input[type=submit]:focus").attr("data-postid");
   var comment_count=parseInt($("#comment-counter-"+p_id).text(),10);
   console.log(p_id);
   $.ajax({
      url: "/messageboard/add_comment/",
      type: "POST",
      data: {post_id: p_id, comment_text:$("#comment-input-"+p_id).val(), csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()},
      success: function(html){
         console.log(html);
         $("#comment-input-"+p_id).val('');
         $("#send-btn-"+p_id).attr("disabled", "disabled");
         
         $("ul#post-list ul#comment-list-"+p_id).append('<li>'+html+'</li>');
         
         $("ul#post-list ul#comment-list-"+p_id).show();
         comment_count += 1;
         $("#comment-counter-"+p_id).text(comment_count);
         
         console.log(comment_count);
      }
   });
}

let likebtn = document.querySelector('#likebtn');
let likecount = document.querySelector('#like');
let dislikecount = document.querySelector('#dislike');




let likeform = document.querySelector('#likeform');
let dislikeform = document.querySelector('#dislikeform');
   
    
$(document).on("submit", "#likeform", function (e) {
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "{% url 'inc-like' %}",
      data: {
        like: $("#like").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        $("#like").html(data);
      },
    });
  });


$(document).on("submit", "#dislikeform", function (e) {
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "{% url 'inc-dislike' %}",
      data: {
        dislike : $('#dislike').val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        $("#dislike").html(data);
      },
    });
  });






// var text_node = document.getElementById("text");
// text_node.textContent = "バーガーキング！";
// console.log(text_node.textContent);


// var btn_node = document.getElementById("text_change_btn");
// btn_node.addEventListener("click", changeText);

// var btn_node = document.getElementById("text_blue_btn");
// btn_node.addEventListener("click", changeText2);

// function changeText(){
//     var text_node = document.getElementById("text");
//     text_node.textContent = "モスバーガー";
//     // text_node.style.color = 'red';
//     // text_node.color.fontsize = '40px';
// }

// function changeText2(){
//     var text_node = document.getElementById("text");
//     text_node.style.color = 'white';
//     text_node.style.backgroundColor = 'blue';
// }

// $(function (){
//     $("#text").text("佐世保バーガー");
// });

// $(function (){
//     // $("#text_change_btn").on("click",function(){
//     //     $("#text").text("横須賀バーガー")
//     //     $("#domdom").toggle();
//     //     $("#text").addClass("burger");
//     // });



//     $("#text_change_btn").click(function(){
//         $("#text").toggleClass("burger");
        
//     });
// });

let btn_node =document.getElementById("change_text_button");
btn_node.addEventListener("click",changetext)

function changetext(){
    var text_node = document.getElementById("text");
    text_node.textContent = "こうしん";
};


$(function(){
    $("#text").text("更新したよ");        
});

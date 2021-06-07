let btn_node = document.getElementById("nihongo");
btn_node.addEventListener("click",changetext)

function changetext(){
    var text_node = document.getElementById("midasi");
    text_node.textContent = "見出しエリア";
    var text_node = document.getElementById("flex");
    text_node.textContent = "FLEXエリア";
    var text_node = document.getElementById("senta");
    text_node.textContent = "センタリングエリア";
    var text_node = document.getElementById("seisaku");
    text_node.textContent = "作業実績";
};


let btnn_node = document.getElementById("eigo");
btnn_node.addEventListener("click",eigochangetext)

function eigochangetext(){
    var text_node = document.getElementById("midasi");
    text_node.textContent = "hoading";
    var text_node = document.getElementById("flex");
    text_node.textContent = "FLEX";
    var text_node = document.getElementById("senta");
    text_node.textContent = "centering";
    var text_node = document.getElementById("seisaku");
    text_node.textContent = "portfolio";
};

// 三角形の面積
function rectangle(takasa, yoko){
    area = takasa * yoko / 2;
    return area
};

result = rectangle(5,6)
console.log(result);

// セクション４の画像サイズを拡大
$("#size-up").on('click',function () {
    $("#sec4 img").css("width", "800px");
});

// セクション４の画像を変更ボタン
$("#img-change").on('click', function () {
    $("#sec4 img").attr("src", "img/thumb_01.png");
});

// クリックする毎に画像を切り替えるサンプルコード
// $(function(){
//     $("#img1").toggle(function(){
//       $(this).attr('src', 'gazo02.png');
//     },
//     function(){
//       $(this).attr('src', 'gazo01.png');
//     });
//   });
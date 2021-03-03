const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const button_ne = document.getElementById("northeast")
const button_se = document.getElementById("southeast")
const button_sw = document.getElementById("southwest")
const button_nw = document.getElementById("northwest")
const button_up = document.getElementById("up")
const button_down = document.getElementById("down")
let nowX = 400;
let nowY = 300;
button_ne.onclick = function (){
    ctx.moveTo(nowX, nowY);
    nowX += 17.32;
    nowY -= 10.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
button_se.onclick = function (){
    ctx.moveTo(nowX, nowY);
    nowX += 17.32;
    nowY += 10.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
button_sw.onclick = function (){
    ctx.moveTo(nowX, nowY);
    nowX -= 17.32;
    nowY += 10.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
button_nw.onclick = function (){
    ctx.moveTo(nowX, nowY);
    nowX -= 17.32;
    nowY -= 10.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
button_up.onclick = function (){
    ctx.moveTo(nowX, nowY);
    nowY -= 20.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
button_down.onclick = function (){
    ctx.moveTo(nowX, nowY);
    nowY += 20.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
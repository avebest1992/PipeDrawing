const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const button_ne = document.getElementById("northeast");
const button_se = document.getElementById("southeast");
const button_sw = document.getElementById("southwest");
const button_nw = document.getElementById("northwest");
const button_up = document.getElementById("up");
const button_down = document.getElementById("down");
let nowX = 100;
let nowY = 500;
let stamps = [];
let stamp_count = 0;
let stamp_id = 0;
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
function add_stamp() {
    stamps[stamp_count] = [nowX, nowY];
    stamp_count += 1;
}
function goto_stamp() {
    if (stamps.length === 0){ return;}
    if (stamp_id < stamp_count)
    {
        nowX = stamps[stamp_id][0];
        nowY = stamps[stamp_id][1];
        stamp_id += 1;
    }
    else {
        nowX = stamps[0][0];
        nowY = stamps[0][1];
        stamp_id = 1;
    }
}
function clear_stamp() {
    stamps = [];
    stamp_count = 0;
    stamp_id = 0;
}
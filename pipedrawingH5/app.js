let screenW = document.documentElement.clientWidth;
let screenH = document.documentElement.clientHeight;
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
canvas.width = screenW - 50;
canvas.height = screenH -200;
document.getElementById("x_slider").max = String(canvas.width);
document.getElementById("y_slider").max = String(canvas.height);
// const button_ne = document.getElementById("northeast");
// const button_se = document.getElementById("southeast");
// const button_sw = document.getElementById("southwest");
// const button_nw = document.getElementById("northwest");
// const button_up = document.getElementById("up");
// const button_down = document.getElementById("down");
let nowX = 100;
let nowY = 300;
let stamps = [];
let stamp_count = 0;
let stamp_id = 0;
function button_ne(){
    ctx.moveTo(nowX, nowY);
    nowX += 17.32;
    nowY -= 10.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
function button_se(){
    ctx.moveTo(nowX, nowY);
    nowX += 17.32;
    nowY += 10.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
function button_sw(){
    ctx.moveTo(nowX, nowY);
    nowX -= 17.32;
    nowY += 10.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
function button_nw(){
    ctx.moveTo(nowX, nowY);
    nowX -= 17.32;
    nowY -= 10.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
function button_up(){
    ctx.moveTo(nowX, nowY);
    nowY -= 20.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
function button_dn(){
    ctx.moveTo(nowX, nowY);
    nowY += 20.00;
    ctx.lineTo(nowX, nowY);
    ctx.stroke();
}
function add_stamp() {
    stamps[stamp_count] = [nowX, nowY];
    stamp_count += 1;
    document.getElementById("stamp_count").innerText = String(stamp_count);
    document.getElementById("stamp_id").max = stamp_count;
}
function goto_stamp() {
    let stamp_index = document.getElementById("stamp_id").value - 1;
    nowX = stamps[stamp_index][0];
    nowY = stamps[stamp_index][1];
    // if (stamps.length === 0){ return;}
    // if (stamp_id < stamp_count)
    // {
    //     nowX = stamps[stamp_id][0];
    //     nowY = stamps[stamp_id][1];
    //     stamp_id += 1;
    // }
    // else {
    //     nowX = stamps[0][0];
    //     nowY = stamps[0][1];
    //     stamp_id = 1;
    // }
}
function clear_stamp() {
    stamps = [];
    stamp_count = 0;
    stamp_id = 0;
    document.getElementById("stamp_count").innerText = String(stamp_count);
}
function show_XY() {
    // nowX = Number(document.getElementById("x_slider").value);
    // nowY = Number(document.getElementById("y_slider").value);
    // document.getElementById("show_XY").innerText = "( "+String(nowX)+" , "+String(nowY)+" )";
    let tempX, tempY;
    tempX = document.getElementById("x_slider").value;
    tempY = document.getElementById("y_slider").value;
    document.getElementById("show_XY").innerText = "( "+tempX+" , "+tempY+" )";
}
function set_XY(){
    nowX = Number(document.getElementById("x_slider").value);
    nowY = Number(document.getElementById("y_slider").value);
}
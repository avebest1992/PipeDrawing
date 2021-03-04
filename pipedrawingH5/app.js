const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
// const button_ne = document.getElementById("northeast");
// const button_se = document.getElementById("southeast");
// const button_sw = document.getElementById("southwest");
// const button_nw = document.getElementById("northwest");
// const button_up = document.getElementById("up");
// const button_down = document.getElementById("down");
let nowX = 100;
let nowY = 500;
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
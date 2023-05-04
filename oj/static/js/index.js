"use strict";

window.onload = indexOnload;



function indexOnload() {
    const successMsg = document.getElementById("successMsg");
    if (successMsg) {
        setTimeout(fadeOutEle, 1000, successMsg);
        setTimeout(hideEle, 4000, successMsg);
    }
}

function fadeOutEle(e) {
    e.classList.add('fadeOut');
}

function hideEle(e) {
    e.style.hidden = true;
    e.style.display = "none";
}
"use strict";

window.onload = registerOnload;


function registerOnload() {
    const errMsg = document.getElementById("errMsg");
    if (errMsg) {
        setTimeout(hideEle, 1000, errMsg);
    }
}

function hideEle(e) {
    e.classList.add('fadeOut');
}


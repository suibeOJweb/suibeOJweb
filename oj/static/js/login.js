"use strict";

window.onload = loginOnload;


function loginOnload() {
    const successMsg = document.getElementById("successMsg");
    const errMsg = document.getElementById("errMsg");
    if (successMsg) {
        setTimeout(hideEle, 1000, successMsg);
    }
    if (errMsg) {
        setTimeout(hideEle, 1000, errMsg);
    }
}

function hideEle(e) {
    e.classList.add('fadeOut');
}
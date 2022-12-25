"use strict";

const ws = new WebSocket((window.location.protocol === "http:" ? "ws" : "wss") + "://" + window.location.host + "/ws");

function sendMessage(event) {
    var input = document.getElementById("messageText");
    ws.send(input.value);
    input.value = '';
    event.preventDefault();
}

document.addEventListener('DOMContentLoaded', function() {
    const messages = document.getElementById('messages');

    ws.onmessage = function(event) {
        var message = document.createElement('li');
        var content = document.createTextNode(event.data);
        message.appendChild(content);
        messages.appendChild(message);
    };
});

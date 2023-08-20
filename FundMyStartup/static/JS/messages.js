var btn = document.getElementById("submit");
        document.querySelector("#room").focus();
        document.querySelector("#room").onkeyup = function(e){
            if (e.keyCode === 13) {// press enter
                btn.click();
            }
        };
        btn.onclick = function(e){
            var roomname = document.getElementById("room").value;
            window.location.pathname = "/chat/" + roomname + "/";
        };
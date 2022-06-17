var conScroll = function(){
    var scrollCon = document.getElementById("scrollCon");
    var li = scrollCon.getElementsByTagName("li");
    var scrollCon1 = document.getElementById("scrollCon1");
    var scrollCon2 = document.getElementById("scrollCon2");
    if(li.length > 3){
        scrollCon2.innerHTML = scrollCon1.innerHTML;
        scrollCon.scrollTop = 0;
        function rollStart(){
            if(scrollCon.scrollTop >= scrollCon1.scrollHeight){
                scrollCon.scrollTop = 0;
            }else{
                scrollCon.scrollTop++;
            }
        }
        var timer = setInterval(rollStart, 50);
        scrollCon.onmouseover = function(){
            clearInterval(timer);
        }
        scrollCon.onmouseout = function(){
            timer = setInterval(rollStart, 50);
        }
    }
};
conScroll();
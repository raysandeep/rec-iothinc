submitForms = function(){
    document.getElementById("a1").submit();
    document.getElementById("a2").submit();
    document.getElementById("a3").submit();
    document.getElementById("a4").submit();
    document.getElementById("a5").submit();
    document.getElementById("a6").submit();
    document.getElementById("a7").submit();
    document.getElementById("a8").submit();
    document.getElementById("a9").submit();
    document.getElementById("a10").submit();
    document.getElementById("tech").submit();
    document.getElementById("design").submit();
    document.getElementById("mgmt").submit();
}





function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;


        if (--timer < 0) {
            document.getElementById("a1").submit();
            document.getElementById("a2").submit();
            document.getElementById("a3").submit();
            document.getElementById("a4").submit();
            document.getElementById("a5").submit();
            document.getElementById("a6").submit();
            document.getElementById("a7").submit();
            document.getElementById("a8").submit();
            document.getElementById("a9").submit();
            document.getElementById("a10").submit();
            document.getElementById("tech").submit();
            document.getElementById("design").submit();
            document.getElementById("mgmt").submit();
        }
    }, 1000);
}

window.onload = function () {
    var tenMinutes = 60 *10,
        display = document.querySelector('#time');
    startTimer(tenMinutes, display);
};


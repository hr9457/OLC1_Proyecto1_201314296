// PATHL: /home/user/documents/output/js 
//PATHW: c:\user\output\js

function session(){

    var success = sessionStorage.getItem("session-user");
    var saludo = 
    if(success == null){
        window.location.href = "login.html";
    }
    
}


function obtener(){
    session();

    var f = new Date();

    var date = f.getFullYear() + ""+ ( f.getMonth() + 1 ) + ""+ f.getDate(); // YYYYMMDD
}

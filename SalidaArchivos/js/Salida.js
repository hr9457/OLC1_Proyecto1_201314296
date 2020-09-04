//PATHW -> c:\user\output\js


function session(){

	vr hola = "hola mundo"
    var success = sessionStorage.getItem("session-user");

    if(success == null){
        window.location.href = "login.html";
    }
    
}

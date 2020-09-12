// PATHL: /home/user/documents/output/js 
//PATHW: c:\user\output\js



        /*********************************************
         *  Dentro de un archivo de tipo javascript  *
         *  pueden encontrarse comentarios de tipo   *
         *   multilinea o de tipo unilinea, estos    *
         *  pueden aparecer en cualquier parte del   *
         * archivo de entrada tomando en cuenta que, *
         * el primero es el que contiene el path del *
         *  directorio al cual se enviara la salida  *
         *        ya analizada y limpiada.           *
         *********************************************/


function session(){

    var success = sessionStorage.getItem("session-user");

    if(success == null){
        window.location.href = "login.html";
    }
    
}

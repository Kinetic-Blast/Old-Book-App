urlIdHeader = "https://drive.google.com/uc?id="


window.onload = GetBooks();

eel.expose(GetBooks);
function GetBooks(x,y) {
    var Items = "";
    var temp = "";


    if (x == null && y == null){eel.GetBookNames();}

    else{
        Items += "<div>"
        temp = x[0][0].substring(0,3)


        for (i in x){

            if (!x[i][0].startsWith(temp) && temp != ""){
                Items+="</div>"
                Items+="<HR WIDTH='100%' SIZE='3' NOSHADE>";
                Items += "<div>";
                temp = x[i][0].substring(0,3);}


            Items += "<div class='container'>";
            Items += "<img src="+y[i][1]+" class='image' />";
            Items += "<div class='middle'>";
            Items += "<div class='loader'></div>";
            Items += "<button class='text' onclick = 'GetFile(\" "+x[i]+ "\")'>" +x[i][0].substring(x[i][0].length - 3,x[i][0].length)+"</button></div></div>";

        }

        document.getElementById("temp").innerHTML = Items;}}



function Update(){
    eel.UpdateFile()
    document.window.location.reload(true)
}

function GetFile(x){
    eel.GetFile(x)
}





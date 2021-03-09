function send(){
    elements = document.getElementById("molecola").value;
    fetch("/send", {
        method: "post",
        headers: new Headers({
            "Content-Type": "application/json"
        }),
        body: JSON.stringify({molecola: elements})
        })  
    .then(response=>{return response.json()})
    .then(response => {console.log(response); show(response)})
}

function show(risposta){
    molecola = risposta["output"];  
    console.log(molecola);
    document.getElementById("result").value = molecola;
}

function nomenclatura(){
    document.getElementById("nomenclatura").style.display = "block";
    document.getElementById("reazione").style.display = "none";
    document.getElementById("help").style.display = "none";
}

function reazione(){
    document.getElementById("nomenclatura").style.display = "none";
    document.getElementById("reazione").style.display = "block";
    document.getElementById("help").style.display = "none";    
}


function help(){
    document.getElementById("nomenclatura").style.display = "none";
    document.getElementById("reazione").style.display = "none";
    document.getElementById("help").style.display = "block";
}
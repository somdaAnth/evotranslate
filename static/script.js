let button = document.getElementById("button");
let output = document.getElementById("out");

button.onclick = function(){
    navigator.clipboard.writeText(output.innerHTML);
    button.classList.add("active")
}
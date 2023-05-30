// eel.MainFunc(InputtedCode)(e => {
//     getInputtedCode(e)
// })

let btn = document.getElementById('runner');
let url = document.getElementById('link');
let result = document.getElementById('result');

url.addEventListener('input', function(e) {
    if (url.value == ''){
        result.textContent = "Enter Youtube link.";
    }
});

btn.addEventListener('click', function(e) {
    link = url.value;
    console.log(link);
    result.textContent = "Downloading ...";
    eel.MainFunc(link)(e =>{
        result.textContent = e;
        if (e == "Something is wrong"){
            result.style.color = "red";
        }
        else{
            result.style.color = "green";
        }
    })
})
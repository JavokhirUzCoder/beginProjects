// eel.MainFunc(InputtedCode)(e => {
//     getInputtedCode(e)
// })

let btn = document.getElementById('runner');
let url = document.getElementById('link');
let result = document.getElementById('result');



btn.addEventListener('click', function(e) {
    link = url.value;
    console.log(link);
    eel.MainFunc(link)(e =>{
        result.textContent = e
    })
})
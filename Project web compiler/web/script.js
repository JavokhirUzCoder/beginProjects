// Element tanib olish
code = document.getElementById('inputcode')
btn = document.getElementById('runner')
result = document.getElementById('result')

let InputtedCode = ""

function getInputtedCode(GetPythonResult) {
    result.textContent = GetPythonResult;
}


btn.addEventListener('click', function(e){
    InputtedCode = code.value;
    re = eel.MainFunc(InputtedCode)
    getInputtedCode(re);
})





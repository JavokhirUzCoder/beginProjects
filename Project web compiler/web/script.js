// Element tanib olish
code = document.getElementById('inputcode')
btn = document.getElementById('runner')
result = document.getElementById('result')



let InputtedCode = ""

function getInputtedCode(GetPythonResult) {
    result.textContent = GetPythonResult;
}

body = document.getElementsByTagName('body')[0]


btn.addEventListener('click', function(e){
    InputtedCode = code.value;
    eel.MainFunc(InputtedCode)(e => {
        getInputtedCode(e)
    })
})





const dooly = document.querySelector('#dooly')

console.log(dooly)

// 둘리를 클릭하면, 호이라고 한다.

dooly.addEventListener('click', function(){
    alert('가즈아ㅏㅏㅏ')
})


let x = 0
let y = 0
document.addEventListener('keydown', function(event){
    console.log(event.keyCode)
    if (event.keyCode === 38){
        y += 70 
        dooly.style.marginBottom = `${y}px`
    }else if(event.keyCode === 40){
        y -= 70
        dooly.style.marginBottom = `${y}px`
    }else if(event.keyCode === 37){
        x -= 70
        dooly.style.marginLeft = `${x}px`
    }else{
        x += 70
        dooly.style.marginLeft = `${x}px`
    }
})
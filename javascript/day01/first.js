// 이건 한 줄 주석
/*
    이건 여러줄 주석
*/
alert("야!")//경고창을 날려줌
user_name = prompt('이름이 뭐에요 ?')
user_age = prompt('나이를 입려해줘')
console.log(user_age)

if (user_age > 30) {
    age = '아재네'
} else if (user_age > 20) {
    age = '학식이네'
} else {
    age = '급식이네'
}

console.log("임마!")
document.write("<h1>너!</h1>")
// document.querySelector(태그 이름 or 셀렉터)
document.querySelector('h1').innerText = user_name + "는" + age
document.write(age)

user_input = prompt("숫자를 입력해줘")
for (i = 0; i < user_input; i++) {
    document.write('<p>안녕</p>')
}
const URL = "https://jsonplaceholder.typicode.com/posts"

const XHR = new XMLHttpRequest()

// 1. XHR.open()
XHR.open('POST',URL)

// 2. XHR.setRequestHeader(헤더정보)
XHR.setRequestHeader(
    'Content-Type',
    'application/json;charset=UTF-8'
)
// 2. XHR.send(데이터)
const data = {
    userId:1,
    title: "옛다 제목이다",
    body: "내용 받아라"
}
XHR.send(JSON.stringify(data))

// 3. XHR.addEventListener()
XHR.addEventListener('load',function(dongjun){
    console.log(dongjun.target.response)
})

// PUT, DELETE

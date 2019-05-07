// 사람
dongjun = {
    name: 'dongjun',

    poop() {
        return "끙"
    }
}

dong = {
    name: 'dong',

    poop: function () {
        return "끙"
    }
}




class Person {
    constructor(name) {
        this.name = name
    }

    poop() {
        return "poop"
    }

    hello() {
        return `안녕 나는 ${this.name}야`
    }

}

const ddong = new Person("동준")

console.log(dongjun.name)
console.log(dongjun.poop())

console.log(dong.name)
console.log(dong.poop())
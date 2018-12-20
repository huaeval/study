"use strict";
class Anima {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    eat() {
        console.log(`${this.name} eating...`);
        return `${this.name} eating...`;
    }
    play() {
        console.log(`${this.name} playing...`);
        return `${this.name} eating...`;
    }
    static getAnima(name, age) {
        return new this(name, age);
    }
}
// let anim = new Anima("Dog",10);
// anim.eat();
let anim = Anima.getAnima("Fanima", 20);
anim.eat();
class Dog extends Anima {
    constructor(name, age) {
        super(name, age);
    }
    eat() {
        console.log(`[${this.name}] eating...`);
        return `[${this.name}] eating...`;
    }
}
let dog = new Dog("Dog", 23);
dog.eat();
dog.play();
//# sourceMappingURL=index.js.map
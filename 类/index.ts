class Anima{
    readonly name:string;
    readonly age:number;
    constructor(name:string,age:number){
        this.name = name;
        this.age = age;
    }
    eat():string{
        console.log(`${this.name} eating...`)
        return `${this.name} eating...`;
    }
    play():string{
        console.log(`${this.name} playing...`)
        return `${this.name} eating...`;
    }
    static getAnima(name:string,age:number):Anima{
        return new this(name,age);
    }
}

// let anim = new Anima("Dog",10);
// anim.eat();

let anim = Anima.getAnima("Fanima",20);
anim.eat();

class Dog extends Anima{
    constructor(name:string,age:number) {
      super(name,age);
    }
    eat():string{
        console.log(`[${this.name}] eating...`)
        return `[${this.name}] eating...`;
    }
}

let dog = new Dog("Dog",23);

dog.eat();
dog.play();
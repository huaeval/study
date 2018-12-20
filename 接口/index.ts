
//
interface Person  {
    name:String;
    age:Number;
}

let tom:Person = {
    name:"tom",
    age:10,
    // address:"xxxx"
}

//可选类型

interface Game {
    start:Function,
    name?:string
}

let game1:Game = {
    start(){
        console.log(this.name);
    },
    name:"xiaomi"
}
game1.start();

interface PersonPropoType{
    [propName: string]: any,
    name:string,
    age:number,
    readonly id:number
}

let jerry:PersonPropoType = {
    name:"jerry",
    age:1,
    say(){

    },
    playing(){

    },
    id:1
}
// jerry.id = 11;


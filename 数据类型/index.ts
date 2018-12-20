//布儿
let isDone: boolean = false;

// isDone = "xxx";

let createdByBoolean: boolean = Boolean(1);

let createdByNewBoolean1: Boolean = new Boolean(1);

// let createdByNewBoolean: boolean = new Boolean(1);

//数字

let decLiteral: number = 6;
let hexLiteral: number = 0xf00d;
// ES6 中的二进制表示法
let binaryLiteral: number = 0b1010;
// ES6 中的八进制表示法
let octalLiteral: number = 0o744;
let notANumber: number = NaN;
let infinityNumber: number = Infinity;

//字符
let myName: string = 'Tom';
let myAge: number = 25;

let sentence: string = `Hello, my name is ${myName}.
I'll be ${myAge + 1} years old next month.`;

//any

let myFavoriteNumber: any = 'seven';
myFavoriteNumber = 1;

//
//类型推论
let myFavoriteNumber1 = 'seven';
// myFavoriteNumber1 = 7;


//联合类型
let myFavoriteNumber2: string | number;
myFavoriteNumber2 = 'seven';
myFavoriteNumber2 = 7;
// myFavoriteNumber2 = false;

function getLength(something: string | number): number {
    // return something;
    // return something.length;
    return 1;
}

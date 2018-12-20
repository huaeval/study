"use strict";
//布儿
let isDone = false;
// isDone = "xxx";
let createdByBoolean = Boolean(1);
let createdByNewBoolean1 = new Boolean(1);
// let createdByNewBoolean: boolean = new Boolean(1);
//数字
let decLiteral = 6;
let hexLiteral = 0xf00d;
// ES6 中的二进制表示法
let binaryLiteral = 0b1010;
// ES6 中的八进制表示法
let octalLiteral = 0o744;
let notANumber = NaN;
let infinityNumber = Infinity;
//字符
let myName = 'Tom';
let myAge = 25;
let sentence = `Hello, my name is ${myName}.
I'll be ${myAge + 1} years old next month.`;
//any
let myFavoriteNumber = 'seven';
myFavoriteNumber = 1;
//
//类型推论
let myFavoriteNumber1 = 'seven';
// myFavoriteNumber1 = 7;
//联合类型
let myFavoriteNumber2;
myFavoriteNumber2 = 'seven';
myFavoriteNumber2 = 7;
// myFavoriteNumber2 = false;
function getLength(something) {
    // return something;
    // return something.length;
    return 1;
}
//# sourceMappingURL=index.js.map
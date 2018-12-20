"use strict";
function sum(a, b) {
    return a + b;
}
sum(1, 2);
// sum(1,"2");
let mySum;
mySum = function (x, y) {
    return x + y;
};
let mySub;
mySub = function (a, b) {
    return a + b;
};
//可选参数
function builderName(fname = 'x', lname) {
    if (lname) {
        return fname + lname;
    }
    else {
        return fname;
    }
}
console.log(builderName());
console.log(builderName("x"));
console.log(builderName("x", " eval"));
//# sourceMappingURL=index.js.map
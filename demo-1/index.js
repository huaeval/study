"use strict";
function tuple(...args) {
    return args;
}
function getArrayOfNumbers() {
    return [1, 2];
}
const numbers = getArrayOfNumbers();
const t1 = tuple("foo", 1, true); // [string, number, boolean]
const t2 = tuple("bar", ...numbers); // [string, ...number[]]
console.log(t1);
//# sourceMappingURL=index.js.map
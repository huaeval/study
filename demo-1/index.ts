function tuple<T extends any[]>(...args: T): T {
    return args;
}

function getArrayOfNumbers():number[]{
    return [1,2];
}

const numbers: number[] = getArrayOfNumbers();
const t1 = tuple("foo", 1, true);  // [string, number, boolean]
const t2 = tuple("bar", ...numbers);  // [string, ...number[]]

console.log(t1);
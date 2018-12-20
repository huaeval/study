

function sum(a:number,b:number):number{
    return a+b;
}
sum(1,2);
// sum(1,"2");

let mySum: (x: number, y: number) => number;
mySum = function (x: number, y: number): number{
    return x + y;
};

//使用接口规定函数样式

interface Sub{
    (a:number,b:number):number
}

let mySub : Sub;

mySub = function(a,b):number{

    return a + b;
}

//可选参数

function builderName(fname:string = 'x',lname?:string):string{
    if(lname){
        return fname + lname;
    }else{
        return fname;
    }
}

console.log(builderName())
console.log(builderName("x"))
console.log(builderName("x"," eval"))

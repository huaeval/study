let numlist :number[] = [0,1,2,3,4];

//numlist.push("1");

let list :(number | string)[] = [0,1,"2",3,4];

interface ArrayNumberType {
    [index: number]: number|string;
} 

let strNumberList : ArrayNumberType = [1,2,3,"4"];

let listAny: any[] = ['Xcat Liu', 25, { website: 'http://xcatliu.com' }];


//简单类型别名
type Name = string;

function getName(name?:Name):Name{
    return <Name>name;
}

//字符串类型别名
type Names = 'string' | 'number' | 'boolean';

function test(name:Names):Names{
    return name;
}

test("string");
test("number");
test("boolean");
// test("str");

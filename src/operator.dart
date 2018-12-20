// 描述	操作符
// 一元后置操作符	expr++    expr--    [()    []    .    ?.]
// 一元前置操作符	-expr    !expr    ~expr    ++expr    --expr
// 乘除运算	*    /    %    ~/
// 加减运算	+    -
// 移位运算	<<    >>
// 按位与	&
// 按位异或	^
// 按位或	|
// 关系和类型测试	>=    >    <=    <    [as    is    is!]
// 相等	==    ！=
// 逻辑与	&&
// 逻辑或	||
// 是否为null	??
// 天健判断（三元运算）	expr1 ? expr2 : expr3
// 级联	..
// 赋值	=    *=    /=    ~/=    %=    +=    -=    <<=    >>=    &=    ^=   

void run(){
  var a = null;
  print(a??"here~");
  TMD tmd = TMD();
  tmd
  ..agePlus()
  ..say()
  ..agePlus()
  ..say()
  ..getTony()
  .sayCao()
  .._tony.sayCao()
  ..agePlus();
}
class TMD {
  String name = "tony";
  int age = 20;
  Tony _tony = Tony();
  say(){
    print("名字:$name，年级:$age");
  }
  agePlus(){
    ++this.age;
  }
  Tony getTony(){
    return _tony;
  }
}
class Tony {
    sayCao(){
      print("CNM...");
    }
}

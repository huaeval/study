///变量
///
/**
 * 变量修饰符 
 * @final 
 * @const 常量[编译时]
 * @var 变量
 * @dynamic/@ 动态判断，第一次设置之后，固定变量类型
 * @static 修饰类成员
 */
run(){
  //变量初始化
  var intVar = 10;
  String str = "str";
  final String finalStr = "final";
  final ffinalStr  = finalStr + str;
  // ffinalStr = "111";//Variables must be declared using the keywords 'const', 'final', 'var' or a type name.
  print(ffinalStr);
  const constStr = "const";
  // constStr = "111";//Constant variables can't be assigned a value
  print(constStr);
  // const String fconstStr = constStr + str;//Const variables must be initialized with a constant value.


}
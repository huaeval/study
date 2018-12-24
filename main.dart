import './src/variable.dart' as variable;
import './src/built-in-type.dart' as buildInType;
import './src/function.dart' as function;
import './src/operator.dart' as Operator;
import './src/exception.dart' as exception;
import './src/clazz.dart' as clazz;
import './src/library.dart' as mlibrary;

main(params) {
  print(params);
  var number = 42; 
  assert(number == 42,"错误的输入");
  variable.run();
  buildInType.run();
  function.run();
  Operator.run();
  exception.run();
  clazz.run();
  mlibrary.run();
}
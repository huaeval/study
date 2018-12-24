///Dart是一种面向对象的语言，具有类和基于mixin的继承。
///每个对象都是一个类的实例，所有的类都是Object的子类。
///基于mixin的继承意味着，尽管每个类(除了Object)都只有一个超类，但类主体可以在多个类层次结构中重用

void run(){
  Animal animal = new Animal("animal",0);
  //没有初始化的变量默认都为null
  print(animal.age);
  print(animal.name);
  var dog = Dog("大黄",2);
  dog.run();
  Logger logger = Logger("INFO");
  logger.log("hi,factory");
  print(logger.length);
  Logger wlog = Logger("WARNING");
  wlog.log("hi,factory");
  print(logger.length);

  //抽象类不能实例化
  // Do xdo = new Do();
  // Todo todo = new Todo();
  // todo.doSomething();
  TodoOne one = TodoOne();
  one.start("One");
  one.doSomething();
} 
class Animal {
  num age;
  String name;
  Animal(this.name,this.age){
    print("animal");
  }
}


class Dog extends Animal{
  Dog(name,age):super(name,age){
    print("dog");
  }
  run(){
    print("my name is $name,I will goto run !");
  }
}

class Logger {

  static final Map<String,Logger> _cache = <String,Logger>{};
  final String name;
  factory Logger(String name){
    if(_cache.containsKey(name)){
      return _cache[name];
    }else{
      final Logger logger = Logger._init(name);
      _cache[name] = logger;
      return logger;
    }
  }
  Logger._init(this.name);
  num get length => _cache.length;
  void log(msg){
    print('[$name]:$msg');
  }
}


abstract class Do {
  void doSomething();
}

abstract class Todo extends Do{
  String totoName = '';
  @override
  void doSomething(){
    print("todo:$totoName");
  }
  String start(String todoName);
}

class TodoOne extends Todo{
    @override
    String start(todoName) {
      this.totoName = todoName;
      return totoName;
    }
}

class TodoTwo implements TodoOne{
  String totoName = '';
  start(String name){
    return "";
  }
  doSomething(){

  }
}
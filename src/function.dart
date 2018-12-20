///Dart是一种真正的面向对象语言，所以即使函数也是对象，具有类型和功能。
///这意味着函数可以分配给变量或作为参数传递给其他函数。
///您还可以像调用函数一样调用Dart类的实例。

run(){
  bool isList(list){
    return list is List;
  }
  print(isList({}));
  print(isList([]));

  double sum(List<double> list){
    double rsum = 0.0;
    list.forEach((item){
      rsum += item;
    });
    return rsum;
  }
  print(sum([1.1,2.0,3.0,4.0]));

  void addAll(List list1,List list2) => list1.addAll(list2);
  List l1 = [1,2];
  List l2 = [3,4];
  addAll(l1, l2);
  print(l1);

  void taggle({taggled:true}){
    print(taggled);
  }
  taggle(taggled: false);

  void taggle2(taggled,[List args]){
    print(args);
  }
  taggle2(true);

}
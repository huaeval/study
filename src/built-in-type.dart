///内置类型
/**
 * @Number
 * @String
 * @Boolean
 * @List
 * @Map
 * @Rune
 * @Symbol
 */
run(){
  //Number
  print("===========Number==========");
    //##int
    int intVar = 10;
    int str2int = int.parse("1");
    int defaultFormat = int.fromEnvironment("2x",defaultValue: 0);
    int ff = int.tryParse("1");//如果不能转换返回null
    print(intVar);
    print(str2int);
    print(defaultFormat);
    print(ff);
    //distribute
    print(intVar.hashCode);
    print(intVar.isEven);
    print(intVar.isOdd);
    print(intVar.isFinite);
    print(intVar.isInfinite);
    print(intVar.isNegative);
    print(intVar.isNaN);
    print(intVar.runtimeType);
    print(intVar.sign);
    print(intVar.bitLength);
    //methods
    print(intVar.toStringAsFixed(10));
    //##double
    double doubleVarFlot = 10.0;
    double doubleVar = 1.1001e5;
    print(doubleVarFlot);
    print(doubleVar);
    print(double.infinity);
    print(double.negativeInfinity);
    print(double.maxFinite);
    print(double.minPositive);
    print(double.nan);
  print("===========End==========");
  //String
  print("===========String==========");
  var str = "  str中 ";
  String str1 = "str中1";
  dynamic str2 = "str中2";
    //distribute
    print(str.runtimeType);
    print(str.runes);
    print(str.isNotEmpty);
    print(str.hashCode);
    print(str.codeUnits);
    print(str.length);
    //methods
    print(str.trimRight());
    print(str.trimLeft()+"|");
    print(str.trim());
    print(str.substring(2,5));//str
    print(str.endsWith("中 "));//true
    print(str.toUpperCase());
    print(str.codeUnitAt(3));//116
    print(str.split("r"));//[  st, 中 ]
  print("===========End==========");
  ///Boolean
  print("===========Boolean======");
  bool isSuccess = false;
    //distribute
    print(isSuccess.runtimeType);
    print(isSuccess.hashCode);
    print(isSuccess == "false");
    //methods
    print(isSuccess.toString() == "false");
  print("===========End==========");
  //List
  print("===========List======");
  List list = [1,2,3,4,5,6,7];
    //distribute
    print(list);
    print(list.runtimeType);
    // print(list.single);
    print(list.last);
    print(list.first);
    print(list.reversed);
    print(list);
    print(list.length);
    print(list.isNotEmpty);
    print(list.isEmpty);
    print(list.where((item)=>item>4));//(5, 6, 7)
    // list.singleWhere((item){
    //   print(item);
    // });
    print(list.lastWhere((item)=>item>5));//7
    print(list.firstWhere((item)=>item>5));//6
    list.forEach((item){
      print(item);
    });
    print(list.indexWhere((item)=>item>3,4));//4
    print(list.indexOf(1));
    list.add(1);
    list.addAll([1,3]);
    print(list);
    print(list.removeAt(1));
    print(list);
    // list = [];
    // print(list.removeAt(0));//Invalid value: Valid value range is empty: 0
    // list.clear();
    list.sort((a,b)=>a-b);
    print(list);
    list.removeLast();
    list.removeRange(1, 3);
    list.removeWhere((item)=>item<4);
    print(list);
    print(list.join("-"));
    print(list.map((item)=>item*2));
    print(list);
  //Map
  print("===========Map===============");
    //distribute
    Map map  = {"x":1,"y":2};
    print(map.length);//2
    print(map.keys);//(x, y)
    print(map.values);//(1, 2)
    print(map.runtimeType);//_InternalLinkedHashMap<dynamic, dynamic>
    print(map.isNotEmpty);//true
    print(map.isEmpty);//false
    print(map.hashCode);
    //methods
    print(map.containsValue(1));//true
    print(map.containsValue(3));//false
    map.forEach((key,value){
      print("key[$key]=>value[$value]");
    });
    map.remove("x");
    print(map);//{y: 2}
    map.addAll({"x":2});
    print(map);//{y: 2, x: 2}
    map.update("y", (ovalue){
      print(ovalue);
      return 3;
    });
    print(map);//{y: 3, x: 2}
    map.updateAll((key,value){
      print("$key,$value");
      return --value;
    });
    print(map);//{y: 2, x: 1} tips:如果不写返回{y: null, x: null}
    var map2 = new Map();
    map2 = Map.from({"x1":11,"y1":22,"x":3});
    map.addEntries(map2.entries);//{y: 2, x: 3, x1: 11, y1: 22}
    map2["x1"] = 111;
    print(map);//{y: 2, x: 3, x1: 11, y1: 22}不影响map
    map.addAll(map2);//{y: 2, x: 3, x1: 11, y1: 22}
    map2["x1"] = 1111;
    print(map);//{y: 2, x: 3, x1: 111, y1: 22}不影响map
    // print(map.cast()==map.cast());//TODO cast
    print(map);
}
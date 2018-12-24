///Applications
///
///
///

void run(){
  try {
    throw new StudyException("hi,boy!");
  } 
  on StudyException catch(e){
    print("StudyException:$e");
  }
  catch (e) {
    print(e);
    try {
      throw "hello";
    } catch (e) {
      print(e);
    }
  }
  finally{
    print("end");
  }
}

class StudyException implements Exception{
  final String msg;
  StudyException([this.msg]);
  @override
    String toString() {
      return msg??"StudyException";
    }
}
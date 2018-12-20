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
    throw "hello";
  }
  catch (e) {
    print(e);
    throw "hello";
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
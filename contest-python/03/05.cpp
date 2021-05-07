//  a, b = map(int, input().split(' '))
//res = 0

//if a%b == 0:
//    print(a//b)
//else:
//    if a == 1:
//        print(b)
//    else:
//        if a > b:
//            res = b+(a-b)
//        else:
//            res = (b-a)+a
//    print(res)
#include <iostream>
using namespace std;
int main()

{ int a, b, res;

cin >> a >> b;
res = 0;
if (a==1){
    cout << b << std::endl;
}
else{
    if (a == 1){
        cout << b << std::endl;
    }
   else{
       if (a > b) {
        res = b+(a-b);
       }
       else{
           if (b > a) {
            res = a + (b-a);
           }
       }
    cout << res << std::endl;
   }
}
return 0;

}
// SPDX-License-Identifier: MIT

pragma solidity 0.8.18;
contract main {
    uint [] _result;
function pal(uint a) public {
    uint rev=0;
    uint dummy;
    uint b;
    b=a; //b=123, a=123.

    while(a!=0) {  //123!=0
        dummy=a%10; //123%10-> 2
        rev=(rev*10)+dummy; //32
        a=a/10; 
    }
    if(rev==b)
    _result.push(b);
}
function printOutput() public view returns(uint[] memory) {
return _result;
 }
}
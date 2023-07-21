// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract voting {
  uint[3] _votes; //static array (3 contestans) take array
  mapping(address=>bool) _voters; //creating a mapping object  to avoid malpractice and double votings.
  constructor() public {
    _votes [0]=0; //reseting values of votes=0
    _votes[1]=0;
    _votes[2]=0;
  }
  function castVote(uint id) public {  //creating function to help contestans to castvote. uint id is for calling contestans id value o then 1 then id=2
     require(!_voters[msg.sender]); //! logical not ,my valid address is msg.sender (checking whether not participated in the pole. if condition false then next if else conditionwill not be executed. )
     if(id==0)   
     _votes[0]+=1;
     else if(id==1)
     _votes[1]+=1;
     else if(id==2)
     _votes[2]+=1;
     _voters[msg.sender]=true; // vote is been recorded. participated in the pole
  }
  function displayVotes() public view returns(uint[3] memory) {
    return(_votes);  //function is returning result of votes
  }
}

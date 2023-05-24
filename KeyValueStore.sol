pragma solidity ^0.8.0;

contract KeyValueStore {
    mapping(uint256 => uint256) private store;

    function setValue(uint256 key, uint256 value) public returns (bool) {
        store[key] = value;
        return true;
    }

    function getValue(uint256 key) public view returns (uint256) {
        return store[key];
    }
}

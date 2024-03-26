var assert = require("assert");
const calculateNumber = require('./1-calcul.js');

describe('Test Rounded', function(){
    it('should work when type is SUM', function(){
        assert.equal(calculateNumber("SUM", 2, 3), 5);
        assert.equal(calculateNumber("SUM", -2.56, -17,89), -20);
    });
    it('should work when type is SUBTRACT', function(){
        assert.equal(calculateNumber("SUBTRACT", 2, 3), -1)
        assert.equal(calculateNumber("SUBTRACT", 5.75, 3.25), 3)
        assert.equal(calculateNumber("SUBTRACT", -10.25, -11), 1)
    });
    it('should work when type is DIVIDE', function(){
        assert.equal(calculateNumber("DIVIDE", 4.25, 2.25), 2)
        assert.equal(calculateNumber("DIVIDE", 81.23, 8.75), 9)
        assert.equal(calculateNumber("DIVIDE", -10.25, 0), 'Error')
    });
})
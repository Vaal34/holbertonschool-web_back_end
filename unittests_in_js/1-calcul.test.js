const assert = require("assert");
const calculateNumber = require('./1-calcul.js');

describe('Test Calcul function', function(){
    describe("function type is SUM", function(){
        it('should work when type is SUM', function(){
            assert.strictEqual(calculateNumber("SUM", 2, 3), 5);
        });
    });
    describe("function type is SUBTRACT", function(){
        it('should work when type is SUBTRACT', function(){
            assert.strictEqual(calculateNumber('SUBTRACT', 2, 3), -1);
            assert.strictEqual(calculateNumber('SUBTRACT', 5.75, 3.25), 3);
            assert.strictEqual(calculateNumber('SUBTRACT', -10.25, -11), 1);
        });
    });
    describe("function type is DIVIDE", function(){
        it('should work when type is DIVIDE', function(){
            assert.strictEqual(calculateNumber('DIVIDE', 3, 1.5), 2);
            assert.strictEqual(calculateNumber('DIVIDE', 81.23, 8.75), 9.283428571428573);
        });
        it("return 'Error' when b is strictEqual to 0", function(){
            assert.strictEqual(calculateNumber('DIVIDE', 1.25, 0), 'Error');
        });
    });
})
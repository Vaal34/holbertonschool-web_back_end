const assert = require("assert")
const request = require("request")

describe("Index page", function(){
    it("should the correct status code 200 when id is a number", function(done){
        request.get("http://localhost:7865/cart/12", function(err, response, body){
            assert.equal(response.statusCode, 200)
            assert.equal(response.body, "Payment methods for cart 12")
            done();
        })
    });
    it("should the correct status code 200 when id is not a number", function(done){
        request.get("http://localhost:7865/cart/test", function(err, response, body){
            assert.equal(response.statusCode, 404)
            done();
        })
    });
})

// Test function
var bitArray = [1, 0, 0, 1, 0, 0, 1, 0];
console.log(maxOneBits(bitArray));

function maxOneBits(bitArray) {

    var oneCount = 0;
    bitArray.forEach(function (currentValue) {

        if (currentValue === 1)
            ++oneCount;
    });

    function flipBits(start, end) {

        if (start > end)
            return 0;

        var maxOnes = oneCount;
        for (var i = start; i < end; ++i) {

            if (bitArray[i] === 0)
                ++maxOnes;
            else
                --maxOnes;
        }

        maxOnes = Math.max(maxOnes, flipBits(start + 1, end), flipBits(start, end - 1));
        return maxOnes;
    }

    return Math.max(oneCount, flipBits(0, bitArray.length - 1));
}

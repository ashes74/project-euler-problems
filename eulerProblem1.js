//Lori-Anne Ashwood
//JavaScript solution

// #Euler projects
// #https://projecteuler.net/

// Euler Problem 1
// # https://projecteuler.net/
// # If we list all the natural numbers below 10 that are multiples of 3 or 5,
// # we get 3, 5, 6 and 9. The sum of these multiples is 23.

// # Find the sum of all the multiples of 3 or 5 below 1000.

function sumOfMultiples (limit){
    var num = 0
    var total = 0
    while(num<limit){
        if (num % 3 === 0 ||num % 5 === 0 ){
            // console.log(num)
            total+=num;}
        num ++;
    }
    return total
}

console.log (sumOfMultiples(100))

function factorial(number) {
    // write your code here
    if (number==1) {
        return 1;
    } else{
        return number * factorial(number-1);
    }
  }

  console.log(factorial(6))
  console.log(factorial(8))
  console.log(factorial(12))
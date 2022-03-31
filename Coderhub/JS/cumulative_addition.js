function cumulativeAddition(array) {
    // write your code here
    let result = 0;
    let l = array.length;
    for (let i=0;i <l; i++) {
        result += array[i];
    }
    return [result,l];
  }

  console.log(cumulativeAddition([2 , 4 , 9 , 23 , 435]));
  console.log(cumulativeAddition([32 , 9 , 3 , 8]));
  console.log(cumulativeAddition([99 , 314 , 8 , 200 , 23 , 2]));
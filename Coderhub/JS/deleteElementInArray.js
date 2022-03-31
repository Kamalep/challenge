function deleteElementInArray(arr, index) {
    arr.splice(index,1);
    return arr;
  }


  console.log(deleteElementInArray([2 , 4 , 88],2))
  console.log(deleteElementInArray([-3 , 4 , 0],0))
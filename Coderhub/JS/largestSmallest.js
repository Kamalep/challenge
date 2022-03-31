function largestSmallest(array) {
    let max = array[0];
    let min = array[0];
    for (let i=0;i<array.length;i++){
        if (max < array[i]) {
            max=array[i];
        }
        if (min > array[i]) {
            min=array[i];
        }
    }
    return [max,min];
  }



  console.log(largestSmallest([2 , 4 , 9 , 23 , 435]))
  console.log(largestSmallest([32 , 44 , 9 , 3 , 8]))
  console.log(largestSmallest([99 , 314 , 8 , 200 , 23]))
function average(array) {
     let avg = 0;
     let l = array.length;
     let total = 0;
     for (let i=0;i<l;i++) {
         total += array[i];
     }
     avg = (total/l);
     return avg; 
  }

  console.log(average([2 , 4 , 9 , 23 , 435]));
  console.log(average([0 , 44 , 9 , 3 , 8]));
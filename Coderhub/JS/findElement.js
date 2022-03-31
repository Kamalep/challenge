function findElement(array, element) {
    // write your code here
    let RF = false
    for (let i=0;i<array.length;i++) {
        if (array[i]==element) {
            console.log(array[i]);
            element;
            RF = true;
            break ;

        }
    }
    return RF;
  }

  console.log(findElement([2, 4, 1 ,9, 42]))
  console.log(findElement([43, 56, 3, 20]))
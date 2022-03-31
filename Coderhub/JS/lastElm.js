function lastElm(arr) {
    const [lastitem] = arr.slice(-1);
    return lastitem;
}

  console.log(lastElm([2 , 4 , 9 , 23 , 435]));
  console.log(lastElm([32 , 44 , 9 , 3 , 8]));
  console.log(lastElm([99 , 314 , 8 , 200 , 23]));
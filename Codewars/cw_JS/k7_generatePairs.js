function generatePairs(n) {
  let a = 0;
  let b = 0;
  let arr = [] ;
  while (a != n && b != n) {

    if (a <= n) {
        if (b <= n) {
            arr.push([a,b]);
            b++;
        }
    }

  }
}
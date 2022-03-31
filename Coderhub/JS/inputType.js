function inputType(value) {
    return value.instanceof() ;

  }
  console.log(inputType('Hello everybody'));
  console.log(inputType(1120));
  console.log(inputType(20.11));
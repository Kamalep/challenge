function lessOrMoreThanZero(number) {
    if (number > 0) {
        return 'Greater than zero';
    }else if (number == 0) {
        return 'Equal to zero';
    }else {
        return 'Less than zero';
    }
  }

  console.log(lessOrMoreThanZero(4));
  console.log(lessOrMoreThanZero(0));
  console.log(lessOrMoreThanZero(-4));
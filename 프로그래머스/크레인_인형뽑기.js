function solution(board, moves) {
  const stack = [];
  let result = 0;
  for (let i of moves) {
    for (let arr of board) {
      if (arr[i - 1]) {
        stack.push(arr[i - 1]);
        arr[i - 1] = 0;
        break;
      }
    }

    if (stack.length >= 2) {
      if (stack[stack.length - 1] === stack[stack.length - 2]) {
        stack.pop();
        stack.pop();
        result += 2;
      }
    }
  }

  return result;
}

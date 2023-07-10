function diagonalDifference(arr) {
  const n = arr.length;
  let leftDiagonal = 0;
  let rightDiagonal = 0;
  for (let i = 0; i < n; i++) {
    leftDiagonal += arr[i][i];
    rightDiagonal += arr[i][n - 1 - i];
  }
  return Math.abs(rightDiagonal - leftDiagonal);
}

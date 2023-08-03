const fibonacci = (n: number): bigint => {
  if (typeof n !== 'number' || n % 1 !== 0) {
    throw new Error('Number must be integer');
  }
  if (n < 0) {
    throw new Error('Number must be equal or greater than 0');
  }

  let a = 0n;
  let b = 1n;

  for (let i = 0; i < n; i++) {
    [a, b] = [b, a + b];
  }

  return a;
};

export default fibonacci;

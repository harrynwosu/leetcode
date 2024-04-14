/*
Implement a closure which has access to the original n and increments it by 1.
However set this original n to b-1 since we want the first call to the closure to give n.
*/

function createCounter(n: number): () => number {
    let num: number = n - 1;
    return function() {
      num += 1; 
      return num; 
    }
}
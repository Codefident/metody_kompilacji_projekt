let range = (start, stop, step) => {
    if (stop === undefined) {
        stop = start;
        start = 0;
    }

    if (step === undefined)
        step = 1;
    else if (step == 0)
        throw new Error("step cannot be 0");

    if ((step > 0 && start >= stop) || (step < 0 && start <= stop))
        return [];

    let result = [];
    for (let i = start; step > 0 ? i < stop : i > stop; i += step)
        result.push(i);
    return result;
}
let len = (arr) => arr.length

// user code
let T = [5, 1, 2, 8, 7, 6, 3, 9, 1, 1, 8, 7, 7, 1, 3, 3, 2];
function countingSort(T, k) {
let n = len(T);
let C = [];
for (let _ of range(k)) {
C.push(0)
}
let B = [];
for (let _ of range(n)) {
B.push(0)
}
for (let x of T) {
C[x] += 1;
}
for (let i of range(1, k)) {
C[i] = (C[i] + C[(i - 1)]);
}
for (let i of range((n - 1), -1, -1)) {
B[(C[T[i]] - 1)] = T[i];
C[T[i]] -= 1;
}
for (let i of range(n)) {
T[i] = B[i];
}
}
countingSort(T, 10)
console.log(T)
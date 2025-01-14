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

let len = (obj) => {
    if (typeof obj === "string" || Array.isArray(obj))
        return obj.length
    if (typeof obj === "object")
        return Object.keys(obj).length
    return 0
}

// user code
let a = 2;
let b = -3;
let c = (a + b);
let d = Math.pow(2, 8);
console.log(d)
let my_list = [1, 1, 1, 1, 1, 1];
let my_obj = {a: 2, b: -10};
let nothing = null;
let true_val = true;
let false_val = false;
if (nothing === null) {
console.log("printing nothing")
console.log(nothing)
}
for (let i of range(len(my_list))) {
my_list[i] = (i + 1);
}
console.log(my_list[(a - 1)])
console.log("dlugosc_listy")
console.log(len(my_list))
console.log("my_obj")
console.log(my_obj["b"])
my_list.push(70)
console.log(my_list)
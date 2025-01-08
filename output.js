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

let a = 2;
let b = 3;
let my_list = [1, 2, 3, 4, 5, 6];
let my_obj = {a: 2, b: 10};
let c = (a + b);
console.log(my_list[(a - 1)])
console.log("dlugosc_listy")
console.log(len(my_list))
console.log("my_obj")
console.log(my_obj["b"])
my_list.push(70)
console.log(my_list)
function range(n) { return Array.from({ length: n }, (_, i) => i); }

function is_prime(n) {
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if ((n % 2) == 0 || (n % 3) == 0) {
        return false;
    }
    let i = 5;
    while ((i * i) <= n) {
        if ((n % i) == 0 || (n % (i + 2)) == 0) {
            return false;
        }
        i += 6;
    }
    return true;
}
console.log(is_prime(7))
console.log(is_prime(10))
console.log(is_prime(23))
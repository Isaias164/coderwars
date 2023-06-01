//ejercicio I
function solution(str, ending) {
    const cant_ending = ending.length;
    //console.log(str.slice((cant_ending * (-1)),str.length));
    return !ending ? true : str.slice((cant_ending * (-1)), str.length) === ending//[]
}

// console.log(solution('abc', ''));
// console.log(solution('samurai', 'ai'));
// console.log(solution('abc', 'bc') );
// console.log(solution('a', 'd'));


// ejercicio II
// The main idea is to count all the occurring characters in a string. If you have a string 
// like aba, then the result should be {'a': 2, 'b': 1}.
// What if the string is empty? Then the result should be empty object literal, {}.

function count(string) {
    if (!string) return {};
    let letters = new Map()
    for (const key of string) {
        if (letters.has(key)) letters.set(key, letters.get(key) + 1);
        else letters.set(key, 1)
    }
    return Object.fromEntries(letters)
}


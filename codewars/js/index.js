function solution(str, ending) {
    const cant_ending = ending.length;
    //console.log(str.slice((cant_ending * (-1)),str.length));
    return !ending ? true : str.slice((cant_ending * (-1)), str.length) === ending//[]
}

// console.log(solution('abc', ''));
// console.log(solution('samurai', 'ai'));
// console.log(solution('abc', 'bc') );
// console.log(solution('a', 'd'));
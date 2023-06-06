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
// let string = "ABCA"
// let letters = {}
// for (const key of string) {
//     if (key in letters) { key: letters.key + 1 };
//     else { key: 1 };
// }
// console.log(letters);

// ejercicce III
// Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

// Write a function which takes a list of strings and returns each line prepended by the correct number.

// The numbering starts at 1. The format is n: string. Notice the colon and space in between.

// Examples: (Input --> Output)

// [] --> []
// ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
var number = function (array) {
    if (array.length === 0) return [];
    return array.map(function (valor, index, array) {
        return `${index + 1}: ${valor}`
    })
}

// console.log(number(["a", "b", "c"]));

// ejecrcice IV

// Write a function that takes a CSV (format shown below) and a sequence of indices, which represents the columns of the CSV, and returns a CSV with only the columns specified in the indices sequence.

// CSV format:
// The CSV passed in will be a string and will have one or more columns, and one or more rows. The CSV will be of size NxM. Each row is separated by a new line character \n. There will be no spaces in the CSV string.

// Example format of passed in CSV: "1,2,3\n4,5,6\n7,8,9\n10,11,12"

// How it would look:

// 1,2,3
// 4,5,6
// 7,8,9
// 10,11,12
// Indices Array info:
// The indices will be zero based, so the first column will be represented as a 0 in the indices sequence.
// All values in the indices sequence will be integers from 0 and up.
// All test cases will have an indices sequence of one or more integers.
// Ignore indices that map to a column that doesn't exist.
// If all the values in the indices array do NOT map to any existing column, return an empty string "".
// The columns of the result must be ordered and not repeated.

// Examples:
// csv, indices                                    => expected
// "1,2,3\n
//  4,5,6", [0, 1]                          => "1,2\n4,5"
// "1,2\n3,4\n5,6", [5, 6, 7]                      => ""
// "a,b,c,d,e\n
//  1,2,3,4,5\n
//  f,g,h,i,j", [1, 3, 5, 7] => "b,d\n2,4\ng,i"

function csvColumns(csv, indices) {
    let rows = csv.split("\n")
    let result = ""
    for (const row of rows) {
        let result1 = row.split(",").filter(function (elemento, indice) {
            return indices.includes(indice) ? true : false
        })
        result += result1.join(",") + "\\n"
    }
    return `"${result.substring(0, result.length - 2)}"`
}
// console.log(csvColumns("1,2,3\n4,5,6", [0, 1]));
//console.log(csvColumns("a,b,c,d,e\n1, 2, 3, 4, 5\nf, g, h, i, j", [1, 3, 5, 7]));

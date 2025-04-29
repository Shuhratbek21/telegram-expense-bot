// js1

// var grade = 40;
// var result;

// if (grade >= 90) {
//   result = "A";
// } else if (grade >= 80) {
//   result = "B";
// } else if (grade >= 70) {
//   result = "C";
// } else if (grade >= 60) {
//   result = "D";
// } else {
//   result = "Failed";
// }

// console.log(result);

// ######################


// var grade = 80;
// var result;

// switch (true) {
//   case (grade >= 90):
//     result = "A";
//     break;
//   case (grade >= 80):
//     result = "B";
//     break;
//   case (grade >= 70):
//     result = "C";
//     break;
//   case (grade >= 60):
//     result = "D";
//     break;
//   default:
//     result = "Failed";
//     break;
// }

// console.log(result);

// ######################

// var grade = 40;
// var result = (grade >= 90) ? "A" :
//              (grade >= 80) ? "B" :
//              (grade >= 70) ? "C" :
//              (grade >= 60) ? "D" :
//              "Failed";

// console.log(result);

// ######################

// js2

// var fruit = "watermelon";


// if (fruit === "apple") {
//   console.log("10000") ;
//   } else if (fruit==="pear") {
//     console.log("12000") ;
//   } else if (fruit==="watermelon") {
//     console.log("20000") ;
//   } else {
//    console.log("Not available");
//   }


// ########################

// var fruit = "watermelon";

// switch (fruit) {
//   case "apple":
//     console.log("10000");
//     break;
//   case "pear":
//     console.log("12000");
//     break;
//   case "watermelon":
//     console.log("20000");
//     break;
//   default:
//     console.log("Not available");
//     break;
// }


// ################################

// var fruit = "anor";
// var result = (fruit === "apple") ? "10000" :
//              (fruit === "pear") ? "12000" :
//              (fruit === "watermelon") ? "20000" :
//              "Not available";

// console.log(result);

// js3

//  num = 12

//  num%2===0 && console.log("even number")
//  num%2!==0 && console.log("odd number")

// #######################

//  var num = 12;

// if (num % 2 === 0) {
//   console.log("Even number");
// } else {
//   console.log("Odd number");
// }

// #######################

// var num = 12;

// switch (num % 2) {
//   case 0:
//     console.log("Even number");
//     break;
//   case 1:
//     console.log("Odd number");
//     break;

// #######################

// var num = 12;

// (num % 2 === 0) ? console.log("Even number") : console.log("Odd number");

// #######################

// js4

// var num = 12;

// if (num % 3 === 0 && num % 5 === 0) {
//   console.log("Divisible by both 3 and 5");
// } else if (num % 3 === 0) {
//   console.log("Divisible by 3");
// } else if (num % 5 === 0) {
//   console.log("Divisible by 5");
// }

// #######################

// var num = 15;

// switch (true) {
//   case (num % 3 === 0 && num % 5 === 0):
//     console.log("Divisible by both 3 and 5");
//     break;
//   case (num % 3 === 0):
//     console.log("Divisible by 3");
//     break;
//   case (num % 5 === 0):
//     console.log("Divisible by 5");
//     break;
// }

// #######################

// var num = 12;

// (num % 3 === 0 && num % 5 === 0) ? console.log("Divisible by both 3 and 5") :
// (num % 3 === 0) ? console.log("Divisible by 3") :
// (num % 5 === 0) ? console.log("Divisible by 5") :
// console.log("Not divisible by 3 or 5");

// #######################

// js5

// which of these alerts are going to execute?
// what will the results of the expressions be inside if(...)?

// if (-1 || 0) alert ("first");       <=
// if (-1 && 0) alert ("second");      
// if (null || -1 && 1) alert ("third"); <=

// #######################

//js6

// var browser = "Tune";

// if (browser === "Edge") {
//   alert("You've got the Edge!");

// } else if (browser === "Chrome" || browser === "Firefox" || browser === "Safari" || browser === "Opera") {
//   alert("Okay, we support these browsers too");
// } else {
//   alert("We hope that this page looks ok!");
// }

// #######################

// js7


// let message = (login === "Employee") ? "Hello" :
//               (login === "Director") ? "Greetings" :
//               (login === "") ? "No Login" :
//               "";

// console.log(message);



var str = "FoziL";
var ohirgiHarf = str.charAt(str.length - 1); 

if (ohirgiHarf.toUpperCase() === "L") {
  console.log(true); 
} else {
  console.log(false); 
} 
----------------------------------------------------------


var str1 = "Web";
var str2 = "Brain";
var input = "Brain";

if (input === str1) {
  str1 = str2;
  console.log(str1);
} else if (input === str2) {
  str2 = str1;
  console.log(str2);
} else {
  console.log("Invalid input");
}
----------------------------------------------------

var input = "WBIN";
var str = "WeBbraIN";
var result = "";

for (var i = 0; i < str.length; i++) {
  if (input.includes(str[i])) {
    result += str[i];
  }
}

console.log(result); 

--------------------------------------------


var input = "(fozil)web(brain)";
var str = "#fozil#web#brain#";
var result = str.replace(/#/g, '()');

console.log(result); // Output: "()fozil()web()brain()"

----------------------------------------------------------

var input = "max - 8, min - 1";
var son = "4467812";

var numbers = son.split('').map(Number);
var max = Math.max(...numbers);
var min = Math.min(...numbers);

console.log(input);  // Output: max - 8, min - 1
console.log("max -", max); // Output: max - 8
console.log("min -", min); // Output: min - 1

-----------------------------------------------------------------------

var input = "max - 8, min - 1";
var son = "4467812";

var max = Math.max(...Array.from(son));
var min = Math.min(...Array.from(son));

console.log(input);
console.log("max -", max);
console.log("min -", min);

------------------------------------------------------------------------------------

var input = "Kabisa yili";
var yil = 2020;

if (input === "Kabisa yili") {
  yil = yil - (yil % 4) + 1;
}

console.log("var yil =", yil); // Output: var yil = 2017

--------------------------------------------------------------------

var str = "WebBrain";

// Input 1
var input1 = "webBrain webBrain webBrain webBrain webBrain webBrain webBrain webBrain webBrain webBrain";
str = str.replace(/WebBrain/g, input1);

console.log(str);
// Output: webBrain webBrain webBrain webBrain webBrain webBrain webBrain webBrain webBrain webBrain

// Input 2
var input2 = "ITBrain ITBrain TBrain ITBrain TBrain ITBrain TBrain ITBrain TBrain ITBrain";
str = str.replace(/WebBrain/g, input2);

console.log(str);
// Output: ITBrain ITBrain TBrain ITBrain TBrain ITBrain TBrain ITBrain TBrain ITBrain

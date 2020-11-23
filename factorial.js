/**
 *
 * @param {*} number Int
 */
const factorial = (number) => {
    let resp = 0
	if (number < 0)
		return "El número es negativo!";
	if (number === 0)
		return 1;
	else
        resp += (number * factorial(number - 1));
    return resp
}
console.log(factorial(x));

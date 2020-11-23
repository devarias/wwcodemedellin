/**
 *
 * @param {*} array
 * @param {*} number
 */
const linealSearch = (array, number) => {
    let resp = 0;
    let flag = false;
    let i = 0;
    if (array.length <= 0)
        return "El array esta vacio!";
    for (; i < array.length; i++)
    {
        if (array[i] == number)
        {
            flag = true;
            break;
        }
    }
    flag ? resp = i : resp = -1;
    return resp
}

console.log(linealSearch(x,y));
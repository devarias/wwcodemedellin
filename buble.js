/**
 * @param {*} array array of integers
 */
const bubleSort = (array) => {
    let arraySort = array;
    let tmp;
    let i = 0, j = 1;
    let size = array.length;

	if ( size <= 0)
        return "El array está vacio!";
    if ( size == 1)
    return "El array solo tiene un elemento!";
    for (; i < size - 1; i++, j++)
    {
        for (j = 0; j < size - 1; j++)
        {
            if (arraySort[j] > arraySort[j + 1])
            {
                tmp = arraySort[j];
                arraySort[j] = arraySort[j + 1];
                arraySort[j + 1] = tmp;
            }
        }
    }
    return arraySort;
}
console.log(bubleSort(array))

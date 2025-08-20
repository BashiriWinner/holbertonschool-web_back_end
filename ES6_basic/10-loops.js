Oexport default function appendToEachArrayValue(array, appendString) {
  for (const value in array) {
    newArray.push(appendString + value);
  }

  return array;
}

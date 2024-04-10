export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const line of array) {
    newArray.push(appendString + line);
  }
  return newArray;
}

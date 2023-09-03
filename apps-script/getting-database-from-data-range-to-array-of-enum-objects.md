- Date : 2023-09-03
- Tags : apps-script js google-sheets

## Getting database from data range to array of enum objects

```js
function getData(range, columnMap) {
  const dataValues = range.getValues();
  const mapEntries = Object.entries(columnMap)

  return dataValues.map((row) => Object.fromEntries(mapEntries.map((colMap) => [colMap[0], row[colMap[1]]])))
}
```

Example:

You have a sheet with data from A1:D*** (*** is last row), with the field mappings :

- first col is **product_code**
- second col is **total**
- fourth col is **rank1**

So the code of **main** function is 

```js
function main(){
  // Get the sheet you want
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  var lastRow = sheet.getLastRow();
  var dataRange = sheet.getRange("A1:D" + (lastRow));
  
  var data = getData(dataRange, {
    "product_code": 0,
    "total": 1,
    // skip third column
    "rank1": 3,
  })

  console.log(data)
}
```

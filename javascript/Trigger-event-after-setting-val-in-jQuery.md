- Date : 2018-01-14
- Tags : #javascript #jquery

## Trigger event after setting val in jQuery

After setting value of an input via `val` method, we should call the `change` chaining method to trigger the `onChange` event of element.

```js
$('#selectCity').change(function() {
	console.log($(this).val());
});

$('#selectCity').val('HaNoi'); // No trigger

$('#selectCity').val('HoChiMinh').change(); // Fire trigger
```


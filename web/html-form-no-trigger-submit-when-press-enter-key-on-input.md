- Date : 2024-09-19
- Tags : #web #html #js #form

## HTML Form no trigger submit when press Enter key on input

Long time ago, I think all form will submit on pressing Enter into any input element (mean it's default behavior of html form and you don't do anything with JS event handling)

Buttttt, today I just know that a form only submit when you pressing Enter IF the form has a SUBMIT button.

This form will not submit on Enter

```html
<form action="abc.php" id="form1">
  <input type="text" name="email">
  <input type="text" name="username">
  <button type="button" name="_action" value="hi">Hi</button>
</form>
```

And this won't to (because the button has type="button", not "submit")
```html
<form action="abc.php" id="form1">
  <input type="text" name="email">
  <input type="text" name="username">
  <button type="button" name="_action" value="hi">Hi</button>
</form>
```

This form will submit on Enter ( because default type of button is "submit" :D )

```html
<form action="abc.php" id="form1">
  <input type="text" name="email">
  <input type="text" name="username">
  <button name="_action" value="hi">Hi</button>
</form>
```

This form will submit on Enter ( and the "_action" field will be "hi", so the Enter key will trigger a virtual click on the first SUBMIT button in the form )

```html
<form action="abc.php" id="form1">
  <input type="text" name="email">
  <input type="text" name="username">
  <button name="_action" value="hi">Hi</button>
  <button name="_action" value="hello">Hello</button>
</form>
```

This form will submit on Enter ( and the "_action" field will be "hello", because the first submit button is Hello )

```html
<form action="abc.php" id="form1">
  <input type="text" name="email">
  <input type="text" name="username">
  <button type="button" name="_action" value="hi">Hi</button>
  <button name="_action" value="hello">Hello</button>
</form>
```

**BONUS** : This form will submit on Enter ;) haha

```html
<form action="abc.php" id="form1">
  <input type="text" name="email">
  <input type="text" name="username">
</form>

<button name="_action" value="hello" form="form1">Hello</button>
```

This trick works even you hide the button (using css)


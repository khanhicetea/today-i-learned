- Date : 2019-01-10
- Tags : #javascript

## Critical notice of string DOM manipulation using jQuery

Sometimes you want to manipulate the HTML DOM elements inside as a string, then you found a lot of HTML parser or DOM library from the Internet (but it supports only NodeJS). How to do it in a browser ?

The answer is "jQuery is your best friend in browser environment" :)

Then you try this :

```js
const content = jQuery('<p><strong>Hello</strong></p><p>from</p><p><strong>KhanhIceTea</strong></p>');
content.find('p > strong').each(function(i, ele) {
    $(ele).css('color', 'red');
});
console.log(content.html());
```

What you expected

```
<p><strong style="color: red;">Hello</strong></p><p>from</p><p><strong style="color: red;">KhanhIceTea</strong></p>
```

But the console print

```
<strong>Hello</strong>
```

**SURPRISE !?? JQUERY SUCKS ?**

Nope ! The reason is simple, DOM data structure is a tree. And, **any tree has a root**, right ??? Now you understand the problem ? Then we fix it below

```js
const html_content = '<p><strong>Hello</strong></p><p>from</p><p><strong>KhanhIceTea</strong></p>';
// Wrap all elements into one root element (div)
const content = jQuery('<div />').append(html_content);
// or const content = jQuery('<div>' + html_content + '</div>');
content.find('p > strong').each(function(i, ele) {
    $(ele).css('color', 'red');
});
console.log(content.html());
```

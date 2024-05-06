- Date : 2024-05-06
- Tags : #javascript #web #security #html

## Script tags in remote HTML request won't run when using innerHTML

By default, all script tags will be turned off when you try to insert to a element using innerHTML. So the tricks to make it run to create the new script tag using `document.createElement('script')` then copy the original scripts to new scripts. After then append the scripts to body or the parent element.

```html
<div>
  <h1>Hello from Test</h1>
  <script data-sign="hello">
    console.log(document.currentScript);
    const parent = document.currentScript.parentElement;
    parent.style.color = 'blue';
  </script>
</div>
```

```html
<!DOCTYPE html>
<html lang="en">
  <body>
    <div id="test"></div>
  </body>
  <script>
    const ele = document.getElementById('test');
    fetch('test.html')
      .then((res) => res.text())
      .then((content) => {
        ele.innerHTML = content;
        ele.querySelectorAll('script').forEach((script) => {
          console.log(script.dataset.sign || 'No signature'); // Your can use this to check the signature and minimize XSS attacks
          const newScript = document.createElement('script');
          newScript.textContent = script.textContent;
          ele.appendChild(newScript);
        });
      });
  </script>
</html>
```

[HTMX Library](https://htmx.org/) use the same way to do the trick, to turn off using `htmx.config.allowScriptTags = false`


- Date : 2023-08-21
- Tags : css web js

## CSS Selector element has an attribute which contains some string

`[abc*="something"]` means select element has attribute `abc`, and its value contains "something" string

Example :

```css
/* Warning all admin link is red text color */
a[href*="/admin/"] {
	color: red;
}
```


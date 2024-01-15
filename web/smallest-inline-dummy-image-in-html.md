- Date : 2024-01-15
- Tags : #web #html #image #performance

## Smallest inline dummy image in HTML

Learned from https://www.phpied.com/minimum-viable-no-image-image-src/

You can use this for lazy load images in pages

```html
<img 
  src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg'/>" 
  ...
>
```

Hmm, when I inspected his demo image, I saw new img attribute named `decoding="async"`, so interesting! So we can tell browser not to wait process this dummy image for later and priority the rest higher. (Good for LCP vital metric)


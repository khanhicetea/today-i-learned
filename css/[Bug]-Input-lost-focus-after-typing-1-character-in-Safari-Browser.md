- Date : 2018-11-01
- Tags : #css #safari #bug

## [Bug] Input lost focus after typing 1 character in Safari Browser

Today my team met a weird bug on Safari browsers (on all Apple devices), that input losts its focus after you type first character.

First, we thought it's javascript bug so we wasted a lot of time for debugging the behaviour of input. But nothing works !

So we continued searching on Google, then we found [this wonderful answer](https://stackoverflow.com/a/25619579)

The root issues caused by one CSS overrided `-webkit-user-select` to `none`, so we have to prevent it by add this line to end of CSS file

```css
input, input:before, input:after {
	-webkit-user-select: initial !important;
	-khtml-user-select: initial !important;
	-moz-user-select: initial !important;
	-ms-user-select: initial !important;
	user-select: initial !important;
} 
```

Hope it helpful for you next time ! :D


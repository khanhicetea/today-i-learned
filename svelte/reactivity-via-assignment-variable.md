- Date : 2023-08-28
- Tags : js svelte frontend

## SvelteJS : Reactivity via variable assignment

Reactivity in Svelte works via assignment of variable, so we have this as example

```js
let todos = [];

// Don't work
todos.push({id: 1, name: 'cleaning'})
todos.push({id: 2, name: 'coding'})

// Work
todos = [...todos, {id: 1, name: 'cleaning'}]

// or this even work as tricky way
todos.push({id: 1, name: 'cleaning'})
todos = todos
```

Why ? I don't know in internal system how it implement, but I think because Svelte works as a compiler, so it triggers the update when it see the assignment variable line.

Different with another frameworks, they work based on **proxy** object


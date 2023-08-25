- Date : 2023-08-25
- Tags : js javascript

## Array group by function in JS

```js
Object.prototype.groupBy = function(cb) {
  const groupByCategory = this.reduce((group, item) => {
    const category = cb(item);
    group[category] = group[category] ?? [];
    group[category].push(item);
    return group;
  }, {});

  return groupByCategory;
}

// Example
const people = [{"name":"John","age":28},{"name":"Alice","age":24},{"name":"Michael","age":32},{"name":"Emily","age":29},{"name":"David","age":27},{"name":"Sophia","age":38}];

const by_first_age_period = people.groupBy((person) => Math.floor(person.age / 10) * 10 + '+');

console.log(by_first_age_period);
```

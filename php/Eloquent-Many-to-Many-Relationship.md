- Date : 2015-12-02
- Tags : #php #eloquent


## Eloquent Many-to-Many Relationship

To create the n-to-m relationship in Eloquent, we create a table stand between 2 tables.
Eg:

We have the db schema :

| post    | post_tag         | tag           |
| ------- | ---------------- | ------------- |
| id (PK) | id (PK)          | id (PK)       |
| title   | post_id (Index)  | name (Unique) |
| content | tag_id (Index)   |               |

In the model `Post` and `Tag`, we define a relation :

- App\Model\Post.php

```php
public function tags() {
    return $this->belongsToMany('App\Model\Tag', 'post_tag', 'post_id', 'tag_id');
}
```

- App\Model\Tag.php

```php
public function posts() {
    return $this->belongsToMany('App\Model\Post', 'post_tag', 'tag_id', 'post_id');
}
```

After that, we can use the relation to fetch the related data, like

```php
$post = Post::firstOrFail(1);
$tags = $post->tags; // return the Collections class contains tags
```

or

```php
$tag = Tag::where('name', '=', 'php')->first();
$posts_of_tag = $tag->posts; // return the Collections class contains posts
```

When updating or creating post, we have to sync with tags by

```php
$tag_ids = [2, 3 ,4]; // Get tag ids from tag names
$post->tags()->sync($tag_ids);
```


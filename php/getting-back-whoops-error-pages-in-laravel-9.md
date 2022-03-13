- Date : 2022-03-13
- Tags : #php #laravel

## Getting back Whoops error pages in Laravel 9

Laravel 9 uses "Spatie/Ignition" as [default error handling pages](https://laravel.com/docs/9.x/releases#exception-page) ,  which is beatiful but bloated within add-on service like **Flare**.

So if you want to get back the good-old "Whoops" error pages, this tutorial is for you :D

First, we remove "spatie/ignition" from composer packages

```bash
$ composer remove "spatie/laravel-ignition"
```

Then, add 3 lines in the `boot` function of `AppServiceProvider`

```php
use Illuminate\Contracts\Foundation\ExceptionRenderer;
use Illuminate\Foundation\Exceptions\Whoops\WhoopsExceptionRenderer;

class AppServiceProvider extends ServiceProvider {
    public function boot()
    {
        // Add 3 lines below between boot function
        if (config('app.debug')) {
            $this->app->bind(ExceptionRenderer::class, WhoopsExceptionRenderer::class);
        }
    }
}
```

And last but not least, open the `config/app.php` then add to this line to array config (try to replace the name of Editor you use in [this list](https://github.com/filp/whoops/blob/5c954ba183d9a917a89183668d895222f7ffcfc5/src/Whoops/Handler/PrettyPageHandler.php#L20) )

```php
    ...
    'editor' => 'vscode'
    ...
```

Now try to add this line to second line in `web.php` route file to test

```php
$x = 1 / 0;
```

- Date : 2024-02-24
- Tags : #php #laravel #ide #web

## Generate routing stubs for IDEs

Some IDEs has good LSP or Intellisense can show link of class methods, so we can using this mechanism to listing all the routes to faster searching route and click method link to navigate actual code.

I make this Laravel command to generate a stub file into routes directory so the IDE can index

So sometimes when you need to re-generate stubs, run this command

```shell
$ php artisan routing_stubs
```

```php
<?php
namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Support\Facades\Route;

class RoutingStubs extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'routing_stubs';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Generate routing stubs';

    public function handle()
    {
        $routes = collect(Route::getRoutes())
            ->map(fn (\Illuminate\Routing\Route $route) => explode('@', $route->getActionName()))
            ->mapToGroups(fn ($params) => [$params[0] => $params[1] ?? ''])
            ->filter(fn ($methods, $class) => class_exists($class))
            ->map(fn ($methods, $class) => $methods->map(
                fn ($method) => sprintf("* @uses %s::%s", $class, $method)
            )->join("\n"))
            ->flatten()
            ->join("\n");

        file_put_contents(base_path('routes/stubs.php'), "<?php\n/**\n" . $routes . "\n*/\n");

        $this->info('Done');
    }
}
```

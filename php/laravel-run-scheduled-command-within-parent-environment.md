- Date : 2022-03-15
- Tags : #php #laravel #cronjob

## Laravel run scheduled command within parent environment

Last day I updated my Laravel app from version 8 to 9, all my scheduled command in Console Kernel has run in another environment like "production". Which causes my system didn't work as expected.

Example, I have 2-3 enviroment which I run cronjob like

```bash
* * * * * php artisan schedule:run --env=hello
* * * * * php artisan schedule:run --env=world
```

But all sub scheduled commands has been run with "production" instead of "hello" or "world"

So this is my fix, I created a lambda function which pass current environment to the child command.

```php
class Kernel extends ConsoleKernel
{
    protected function schedule(Schedule $schedule)
    {
        // Added 2 lines to get lamda function
        $env = app()->environment();
        $schedule_command = fn ($cmd) => $schedule->command($cmd, ['--env' => $env]);

        // Then schedule using new lambda function
        $schedule_command('check_product_stock')->everyTenMinutes();
        $schedule_command('run_job_queue')->everyMinute();
        $schedule_command('clean_old_data')->dailyAt('00:25');
    }

    protected function commands()
    {
        $this->load(__DIR__ . '/Commands');

        require base_path('routes/console.php');
    }
}
```

Enjoy ! :) Hope it works for you !


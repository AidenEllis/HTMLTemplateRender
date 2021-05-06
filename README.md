## HTMLTemplateRender


* `Rendering html file with variables into text`

<br>

## Installation

* Install Package Using `pip`
   ```shell script
   python3 pip install HTMLTemplateRender
   ```
  
<br>

### How to use:

* HTML File (test.html)
    `Use {{ variable }} to assign value`
   ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Test</title>
    </head>
    <body>
        <h1>Hey there {{ username }}</h1>
        <h2>It's {{ day_name }}</h2>
    </body>
    </html>
   ```

   * Lets Render the file
    ```python
    from HTMLTemplateRender.renderer import render_template

    context = {
        'username': 'Anonymous',
        'day_name': 'Sunday'
    }
    
    result = render_template(template_path='test.html', context=context)
    print(result)
    ```

* Output
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Test</title>
    </head>
    <body>
        <h1>Hey there Anonymous</h1>
        <h2>It's Sunday</h2>
    </body>
    </html>
    
    Process finished with exit code 0

    ```
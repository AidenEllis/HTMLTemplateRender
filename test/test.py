from HTMLTemplateRender.renderer import render_template


context = {
    'username': 'Anonymous',
    'day_name': 'Sunday'
}

result = render_template(template_path='test.html', context=context)
print(result)

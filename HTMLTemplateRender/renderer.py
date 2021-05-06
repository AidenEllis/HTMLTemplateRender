from jinja2 import Environment, BaseLoader, StrictUndefined, Undefined


policies = {"forbid": StrictUndefined, "allow": Undefined}


def render_template(template_path: str, context: dict, undefined="allow") -> str:
    with open(template_path, 'r') as file:
        template = file.read()

    template = Environment(
        loader=BaseLoader(), undefined=policies[undefined]
    ).from_string(template)
    return template.render(context)

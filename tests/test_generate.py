import json


default_context = {
    'install_dependencies': False,
    'project_name': 'Prediction',
    'author_name': 'Shima Daoud,
    'author_email': 'shemaali8787@gmail.com'
}


def test_package_json(predict):
    result = predict.bake(extra_context=default_context)

    package_json = json.loads(result.project.join('package.json').read())

    assert package_json['name'] == 'Prediction'
    assert package_json['license'] == 'MIT'
    author = '{Shima Daoud} <{shemaali8787@gmail.com}>'.format(**default_context)
    assert package_json['author'] == author

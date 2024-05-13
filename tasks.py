from invoke import task


@task
def test(c, env='staging', lang='en', app='android', device='emulator'):
    c.run(f'./venv/bin/python -m pytest src/spec/*.py --app=android --device=emulator; open ./report/pytest_html_report.html')

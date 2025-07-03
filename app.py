from flask import Flask, render_template, request, url_for
import requests
import random
import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        language = request.form.get('language')
        details = random_repo(language)
        if details:
            return render_template('index.html', details=details, language=language)
        else:
            app.logger.warning(f"No repositories found for language: {language}")
            return render_template('index.html', error='No repositories found for this language.')
    languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'PHP', 'Go', 'Swift', 'TypeScript']
    lang = random.choice(languages)
    details = random_repo(lang)
    return render_template('index.html', details=details, language=lang)

@app.route('/find-another', methods=['GET','POST'])
def find_another():
    if request.method == 'GET':
        languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'PHP', 'Go', 'Swift', 'TypeScript']
        lang = random.choice(languages)
        details = random_repo(lang)
        return render_template('index.html', details=details, language=lang)
    if request.method == 'POST':
        language = request.form.get('language')
        details = random_repo(language)
        return render_template('index.html', details=details, language=language)
    
    
def random_repo(language):
    q = f'language:{language}'
    app.logger.info(f"Language selected: {language}")
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': q,
        'sort': 'stars',
        'order': 'desc',
        'per_page': 100
    }
    response = requests.get(url, params=params)
    response = response.json()
    repositories = response.get('items')
    if repositories:
        repo = random.choice(repositories)
        details = {
            'name': repo.get('name'),
            'description': repo.get('description'),
            'url': repo.get('html_url'),
            'stars': repo.get('stargazers_count'),
            'language': repo.get('language'),
        }
        app.logger.info(f"Selected repository: {details}")
        return details
    else:
        app.logger.warning(f"No repositories found for language: {language}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
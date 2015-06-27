# -*- coding: utf-8 -*-
import random
import inflect
import pickle
from flask import Flask, render_template

app = Flask(__name__)

p = inflect.engine()
with open('nouns.pck', 'rb') as noun_file:
    nouns = pickle.load(noun_file)
with open('adjs.pck', 'rb') as adj_file:
    adjs = pickle.load(adj_file)
with open('verbs.pck', 'rb') as verb_file:
    verbs = pickle.load(verb_file)

phrases = [
    u'protecting Australia from',
    u'defending Australia’s',
    u'returning Australia’s',
    u'{} illegal'
    ]


def create_message():
    return (u'Operation {} {}'.format(
            random.choice(adjs).title(),
            random.choice(nouns).title()),
            u'{} {}'.format(
            random.choice(phrases).format(p.present_participle(random.choice(verbs))),
            p.plural(random.choice(nouns)))
            )


@app.route('/')
def operation():
    operation, tagline = create_message()
    return render_template('index.html', operation=operation, tagline=tagline)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    beit_midrash_info = {
        'name': 'בית המדרש "סולם יעקב"',
        'address': 'רח\' ברוריה 2 (רובע טו\'), אשדוד',
        'rabbi': 'הרב יעקב רבי שליט"א',
        'description': 'מקום חם עבור צעירים רבים באשדוד, מרכז להחזרה בתשובה ולימוד תורה',
        'activities': [
            'כולל אברכים',
            'חברותות',
            'גמ"ח',
            'טיולים'
        ]
    }
    return render_template('index.html', info=beit_midrash_info)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
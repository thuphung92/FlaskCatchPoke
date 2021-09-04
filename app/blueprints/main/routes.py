from flask import render_template, flash
import requests
from .forms import SearchForm
from flask_login import login_required, current_user
from .import bp as main
from .models import Pokemon
from app.blueprints.auth.models import User
from app import db

@main.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@main.route('/pokemon', methods=['GET','POST'])
@login_required
def pokemon():
    pokemon_name = None
    form = SearchForm()
    # Validate Form
    if form.validate_on_submit():
        pokemon_name = form.pokemon_name.data.lower()
        form.pokemon_name.data = '' #clear form after hitting search
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            if not data:
                flash("Something went wrong. Couldn't connect the library.",'danger')
                return render_template("pokemon.html.j2", form=form)
            
            pokemon_dict = {  
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'experience': data['base_experience'],
                'image_url': data['sprites']['other']['dream_world']['front_default'],
                'sprite_url': data['sprites']['front_shiny']
                }
            #check if the searched pokemon exists in the database
            if Pokemon.query.filter_by(name=pokemon_name).first() is None:
                new_poke = Pokemon(**pokemon_dict)
                new_poke.save()
                new_poke.owners.append(current_user) #record this user have catched this poke in the "catched" table
                db.session.commit()
            else:
                Pokemon.query.filter_by(name=pokemon_name).first().owners.append(current_user)   
                db.session.commit() 
                           
            return render_template("pokemon.html.j2", form=form, pokemon = pokemon_dict)
        flash(f'There is no pokemon named {pokemon_name}','warning')
        return render_template("pokemon.html.j2", form=form)
    return render_template('pokemon.html.j2', form=form)
from flask import Flask, render_template, flash, session, redirect
from .forms.RPS import RPSForm
from .config import Config
from random import choice
from .outcomes import outcomes


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/rps", methods=["GET", "POST"])
def rps_game():
    
    form = RPSForm()
    game_state = {
        "wins": session.get('wins') if session.get('wins') else 0,
        "ties": session.get('ties') if session.get('ties') else 0,
        "losses": session.get('losses') if session.get('losses') else 0,
        "player_image": session.get('player_image') if session.get('player_image') else '../static/paper.jpg',
        "computer_image": session.get('computer_image') if session.get('computer_image') else '../static/rock.jpg',        
    }
    print("GAME STATS", game_state)
    return render_template("rps.html", form=form, game_state=game_state)


@app.route("/makemove", methods=["POST"])
def submit_play():

    form = RPSForm()
    print("got here")

    if form.validate_on_submit():
        user_move = form.data["moves"]
        computer_move = choice(["rock", "paper", "scissors"])
        results = outcomes[(user_move, computer_move)]
        print("RESULTS", results)
        if "wins" in session:
            session['wins'] += results['wins']
        else:
            session['wins'] = results['wins']
        if "ties" in session:
            session['ties'] += results['ties']
        else:
            session['ties'] = results['ties']
        if "losses" in session:
            session['losses'] += results['losses']
        else:
            session['losses'] = results['losses']
        session['player_image'] = results["player_image"]
        session['computer_image'] = results["computer_image"]
        flash(results['message'])
        return redirect("/rps")

    if form.errors:
        print(form.errors)
        print('How did you make errors in RPS?')

    return render_template("rps.html", form=form)



@app.route('/clear')
def clear_stats():
    session.pop('wins', None) 
    session.pop('ties', None) 
    session.pop('losses', None)
    flash("Game stats reset!")
    return redirect("/rps")






#Flask Server
from flask import Flask, render_template, request
from game import TicTacToe 

app = Flask(__name__)

@app.route('/')
def display_board():
    # code to render the game board template and display the current state
    return render_template('board.html', board=game_board) 
  """<html>
    <body>
        <!--display the game board -->
        <table>
            <!-- Render the game board using a loop -->
            {% for row in board %}
            <tr>
                {% for cell in row %}
                <td>{{ cell }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    </body>
</html>
"""

@app.route('/move', methods=['POST'])
def handle_move():
    # code to handle the user's move and update the game state
    return redirect('/')
  
@app.route('/reset')
def reset_game():
    # code to reset the game state
  return redirect('/')

if __name__ == '__main__':
  app.run()

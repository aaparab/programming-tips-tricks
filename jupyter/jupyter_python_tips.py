# Jupyter tricks related to Python

########################################
# View full output, not just last line
########################################
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

########################################
# Reload a module
########################################
from importlib import reload
reload(msabpy)

########################################
# Play sound when a program finishes
########################################
from IPython.display import Audio, display
def allDone():
    display(Audio(url="https://sound.peal.io/ps/audios/000/000/537/original/woo_vu_luvub_dub_dub.wav', autoplay=True))

########################################
# Clear notebook output
########################################
from IPython.display import clear_output
clear_output(wait=True)

########################################
# Save (& restore) variables
########################################
import dill
dill.dump_session("notebook.db")
dill.load_session("notebook.db")

########################################
# Reusing variables across notebooks
########################################
%store          # List of all variables and their current values
%store var1     # Store variable `var1`
%store -r var1  # Restore variable `var1`
%store -z       # Remove all variables from storage
# Reference: https://ipython.org/ipython-doc/3/config/extensions/storemagic.html

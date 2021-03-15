# Jupyter tricks related to Python

########################################
# Make config changes, e.g., autocomplete
########################################
# Permanently enable auto-complete instead of
%config Completer.use_jedi = False
# Taken from here: https://stackoverflow.com/a/66032603/8100373

# Generate config
ipython profile create
# And change 
c.IPCompleter.use_jedi = False in ipython_config.py

# To find line number in vim:
with open('/home/msabp/.ipython/profile_default/ipython_config.py', 'r') as f:
    file = f.readlines()

for i, line in enumerate(file):
    if 'use_jedi' in line:
        print("{}\t{}".format(i, line))
>> 945	# c.Completer.use_jedi = True
>> 1006	#  See also: Completer.use_jedi
>> 1007	# c.IPCompleter.use_jedi = True

# Finally in vim to go to line number:
:1007

########################################
# View full output, not just last line
########################################
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

########################################
# Change font family [Reference](https://github.com/jupyterlab/jupyterlab/issues/5387)
########################################
# "fontFamily": "'DejaVu Sans Mono', 'Noto Sans Mono', 'Everson Mono', FreeMono, Menlo, Terminal, monospace",

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

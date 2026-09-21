import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if src_path not in sys.path:
    sys.path.insert(0, src_path)
    
# Ylhäällä olevaa paskaa tarvitaan jotta voidaan käyttää src-kansion funktioita ja moduuleja. Ilman tätä koodia ohjelma ei löydä src-kansion funktioita. Miksi ei JS?

from functions.mainScreen import main_screen
        
main_screen()
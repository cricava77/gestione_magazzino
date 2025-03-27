import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMessageBox
from database.database_manager import DatabaseManager
from gui.main_window import MainWindow

def initialize_database():
    """Inizializza il database e restituisce il db_manager"""
    try:
        # Percorso automatico cross-platform
        db_manager = DatabaseManager()  # Usa il percorso predefinito
        
        # Verifica che la connessione sia attiva
        if not db_manager.connection:
            raise RuntimeError("Connessione al database fallita")
            
        return db_manager
        
    except Exception as e:
        QMessageBox.critical(
            None,
            "Errore Database",
            f"Impossibile inizializzare il database:\n{str(e)}"
        )
        sys.exit(1)

def main():
    """Punto di ingresso principale dell'applicazione"""
    try:
        # Configurazione dell'applicazione Qt
        app = QApplication(sys.argv)
        app.setStyle('Fusion')  # Stile moderno
        
        # Inizializzazione del database
        db_manager = initialize_database()
        
        # Creazione della finestra principale
        window = MainWindow(db_manager)
        window.setWindowTitle("Gestione Magazzino - v1.0")
        window.show()
        
        # Esecuzione dell'applicazione
        sys.exit(app.exec_())
        
    except Exception as e:
        QMessageBox.critical(
            None,
            "Errore Critico",
            f"Si è verificato un errore irreversibile:\n{str(e)}"
        )
        sys.exit(1)

if __name__ == "__main__":
    # Configurazione dei percorsi
    BASE_DIR = Path(__file__).parent.absolute()
    sys.path.append(str(BASE_DIR))  # Aggiunge la root al PYTHONPATH
    
    # Avvio dell'applicazione
    main()
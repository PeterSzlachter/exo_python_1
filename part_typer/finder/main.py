import typer
from pathlib import Path
from typing import Optional

app = typer.Typer()

@app.command('run')
def main(extension:str,
         directory: Optional[str] = typer.Argument(None,help="Spécifier le dossier où chercher les fichiers"),
         delete:bool = typer.Option(False,help="Supprime les fichiers trouvés.")):
    
    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()
    
    if not directory.exists():
        typer.secho(f"Le dossier '{directory}' n'existe pas", fg=typer.colors.RED)
        raise typer.Exit()
    
    files = directory.rglob(f"*.{extension}")
    if delete:
        typer.confirm(f"Voulez-vous vraiment supprimer tout les fichiers {extension} trouvés ?", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Suppression du fichier {file}", fg=typer.colors.RED)
    else:
        typer.secho(f"Fichier trouvés avec l'extension {extension} :", bg=typer.colors.BRIGHT_CYAN, fg=typer.colors.BLACK)
        for file in files:
            typer.echo(file)

@app.command('search')
def search(extension:str):
    """Chercher les fichiers avec l'extension donnée"""
    main(extension=extension, directory=None,delete=False)
    
@app.command('delete')
def search(extension:str):
    """Supprimer les fichiers avec l'extension donnée"""
    main(extension=extension, directory=None,delete=True)

if __name__ == "__main__":
    app()
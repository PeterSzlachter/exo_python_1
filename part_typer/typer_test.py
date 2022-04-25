import typer
import time

app = typer.Typer()



def main(delete:bool = typer.Option(False,help="Supprime les fichiers trouvés"),
         extension: str = typer.Argument("txt",help="Extension à chercher")): 
    #si valeur par défaut ligne de commande --variable valeurdelavariable
    #help=".." rempli la commande --help du programme
    """
    Affiche les fichiers trouvés avec l'extension donnée
    """
    prenoms = ["Pyt","Pedro","Jeje","didi","Vlad"]
    with typer.progressbar(prenoms) as progress:
        for prenom in progress:
            time.sleep(1)
        typer.echo("Fin de la bar")
    # prenom = typer.style("Pyt", fg=typer.colors.BRIGHT_MAGENTA, bold=True, underline=True,blink=True,bg=typer.colors.WHITE,strikethrough=True)
    # typer.echo(f"Bonjour {prenom}")
    typer.secho(f"Bonjour bonjour",fg=typer.colors.BRIGHT_GREEN,bold=True)
    
    print(delete)
    typer.echo(f"Affiche les fichiers avec l'extension donnée : {extension}")
    # extension = typer.prompt("Quel extension souhaitez-vous chercher ?")
    print(extension)
    if delete:
        do_delete = typer.confirm(f"Supprimer les fichiers .{extension} ?")
        if not do_delete:
            typer.echo("On annule l'opération")
            raise typer.Abort()
        print("Suppression des fichiers")
    # typer.echo(f"Affiche les fichiers avec l'extension donnée : {extension}")
@app.command("search")

def search_py():
    main(delete=False,extension="py")

@app.command("delete")

def delete_py():
    main(delete=True,extension="py")

if __name__ == "__main__":
    # typer.run(main)
    app()
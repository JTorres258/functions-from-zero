import click
from mylib.bot import scrape


@click.command()
@click.option(
    "--name", prompt="Wikipedia page to scrape", help="Web page we want to scrape"
)
@click.option(
    "--length",
    prompt="Length of the sentence",
    help="Length of the page from wikipedia",
)
def cli(name, length):
    result = scrape(name, length=length)
    click.echo(click.style(f"{result}", bg="red", fg="white"))


if __name__ == "__main__":
    cli()

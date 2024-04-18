import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder[["continent", "country"]].drop_duplicates(), x="continent")
        .add(so.Bar(), so.Hist())
        .label(
            title="Cantidad de países por continente",
            x="Continente",
            y="Cantidad de países",
        )
    )
    return dict(
        descripcion="Un sofisticado gráfico con el número de países en cada continente",
        autor="La cátedra",
        figura=figura,
    )

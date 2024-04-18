import seaborn.objects as so
from gapminder import gapminder


def plot():
    media_vida_por_ano_continente = gapminder.groupby(['year', 'continent'])['lifeExp'].mean().reset_index()
    figura = (
        so.Plot(media_vida_por_ano_continente, x="year", y = 'lifeExp', color='continent')
        .add(so.Line())
        .add(so.Dot())
        .add(so . Line (color='#8902F2', linewidth=0.7) ,so.PolyFit(1)) 
        .facet(col="continent", wrap=3)
        .label(
            x="Año",
            y="Life Exp"
        )
    return dict(
        descripcion="Media de vida de cada continente a lo largo del tiempo con ajuste lineal",
        autor="Lucio Maspero",
        figura=figura,
    )

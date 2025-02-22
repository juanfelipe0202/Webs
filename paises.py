from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Paises del Mundo por Continentes</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Paises del Mundo por Continentes</h1>

    <h2>África</h2>
    <p>Egipto, Sudáfrica, Kenia, Nigeria, Ghana, Marruecos, Tanzania, Uganda, Argelia, Etiopía.</p>
    <h3>Egipto</h3>
    <ul>
        <li>Capital: El Cairo</li>
        <li>Famoso por: Pirámides y el río Nilo</li>
        <li>Idioma: Árabe</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/eg"><span style="color:gray;">Hora actual en</span><br />Egipto</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FCairo" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Sudáfrica</h3>
    <ul>
        <li>Capital: Pretoria</li>
        <li>Famoso por: Diversidad cultural y el Parque Nacional Kruger</li>
        <li>Idioma: 11 idiomas oficiales</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/za"><span style="color:gray;">Hora actual en</span><br />Sudáfrica</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FJohannesburg" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Kenia</h3>
    <ul>
        <li>Capital: Nairobi</li>
        <li>Famoso por: Safaris y la migración de los ñus</li>
        <li>Idioma: Swahili e inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/ke"><span style="color:gray;">Hora actual en</span><br />Kenia</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FNairobi" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Nigeria</h3>
    <ul>
        <li>Capital: Abuya</li>
        <li>Famoso por: Su diversidad étnica y cultural</li>
        <li>Idioma: Inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/ng"><span style="color:gray;">Hora actual en</span><br />Nigeria</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FLagos" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Ghana</h3>
    <ul>
        <li>Capital: Acra</li>
        <li>Famoso por: Su historia de oro y cultura vibrante</li>
        <li>Idioma: Inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/gh"><span style="color:gray;">Hora actual en</span><br />Ghana</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FAccra" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h2>América</h2>
    <p>Estados Unidos, Brasil, Argentina, Canadá, Chile, México, Colombia, Perú, Venezuela, Cuba.</p>
    <h3>Estados Unidos</h3>
    <ul>
        <li>Capital: Washington D.C.</li>
        <li>Famoso por: Influencia cultural y económica</li>
        <li>Idioma: Inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/4140963"><span style="color:gray;">Hora actual en</span><br />Washington, Estados Unidos (USA)</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FNew_York" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Brasil</h3>
    <ul>
        <li>Capital: Brasilia</li>
        <li>Famoso por: Carnaval y la Amazonía</li>
        <li>Idioma: Portugués</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/3469058"><span style="color:gray;">Hora actual en</span><br />Brasília, Brasil</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FSao_Paulo" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Argentina</h3>
    <ul>
        <li>Capital: Buenos Aires</li>
        <li>Famoso por: Tango y la Patagonia</li>
        <li>Idioma: Español</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/3435910"><span style="color:gray;">Hora actual en</span><br />Buenos Aires, Argentina</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FArgentina%2FBuenos_Aires" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Colombia</h3>
    <ul>
        <li>Capital: Bogotá</li>
        <li>Famoso por: Café, biodiversidad y el Carnaval de Barranquilla</li>
        <li>Idioma: Español</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/3674962"><span style="color:gray;">Hora actual en</span><br />Medellín, Colombia</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FBogota" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Canadá</h3>
    <ul>
        <li>Capital: Ottawa</li>
        <li>Famoso por: Su naturaleza y multiculturalidad</li>
        <li>Idioma: Inglés y francés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/6094817"><span style="color:gray;">Hora actual en</span><br />Ottawa, Canadá</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FToronto" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Chile</h3>
    <ul>
        <li>Capital: Santiago</li>
        <li>Famoso por: Su geografía diversa y el vino</li>
        <li>Idioma: Español</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/3871336"><span style="color:gray;">Hora actual en</span><br />Santiago, Chile</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FSantiago" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h2>Asia</h2>
    <p>China, India, Japón, Rusia, Indonesia, Pakistán, Bangladesh, Filipinas, Vietnam, Turquía.</p>
    <h3>China</h3>
    <ul>
        <li>Capital: Pekín</li>
        <li>Famoso por: Gran Muralla y su gran población</li>
        <li>Idioma: Mandarín</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/1816670"><span style="color:gray;">Hora actual en</span><br />Beijing, China</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FShanghai" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>India</h3>
    <ul>
        <li>Capital: Nueva Delhi</li>
        <li>Famoso por: Diversidad cultural y el Taj Mahal</li>
        <li>Idioma: Hindi y inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/in"><span style="color:gray;">Hora actual en</span><br />India</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FKolkata" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Japón</h3>
    <ul>
        <li>Capital: Tokio</li>
        <li>Famoso por: Tecnología avanzada, cultura tradicional y gastronomía.</li>
        <li>Idioma: Japonés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/jp"><span style="color:gray;">Hora actual en</span><br />Japón</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FTokyo" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Rusia</h3>
    <ul>
        <li>Capital: Moscú</li>
        <li>Famoso por: Su vasta extensión territorial, historia rica y cultura diversa.</li>
        <li>Idioma: Ruso</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/524901"><span style="color:gray;">Hora actual en</span><br />Moscow, Rusia</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Europe%2FMoscow" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Indonesia</h3>
    <ul>
        <li>Capital: Yakarta</li>
        <li>Famoso por: Su biodiversidad, islas y cultura variada.</li>
        <li>Idioma: Indonesio</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/1642911"><span style="color:gray;">Hora actual en</span><br />Jakarta, Indonesia</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FJakarta" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Pakistán</h3>
    <ul>
        <li>Capital: Islamabad</li>
        <li>Famoso por: Su historia antigua, montañas y cultura rica.</li>
        <li>Idioma: Urdu e inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/pk"><span style="color:gray;">Hora actual en</span><br />Pakistán</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FKarachi" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Bangladesh</h3>
    <ul>
        <li>Capital: Daca</li>
        <li>Famoso por: Su cultura vibrante y el río Ganges.</li>
        <li>Idioma: Bengalí</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/bd"><span style="color:gray;">Hora actual en</span><br />Bangladesh</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FDhaka" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Filipinas</h3>
    <ul>
        <li>Capital: Manila</li>
        <li>Famoso por: Sus playas, cultura diversa y hospitalidad.</li>
        <li>Idioma: Filipino e inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/ph"><span style="color:gray;">Hora actual en</span><br />Filipinas</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FManila" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Vietnam</h3>
    <ul>
        <li>Capital: Hanói</li>
        <li>Famoso por: Su historia, paisajes naturales y gastronomía.</li>
        <li>Idioma: Vietnamita</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/vn"><span style="color:gray;">Hora actual en</span><br />Vietnam</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FHo_Chi_Minh" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Turquía</h3>
    <ul>
        <li>Capital: Ankara</li>
        <li>Famoso por: Su rica historia, cultura y la mezcla de Oriente y Occidente.</li>
        <li>Idioma: Turco</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/tr"><span style="color:gray;">Hora actual en</span><br />Turquía</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Europe%2FIstanbul" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>


        <iframe src="https://www.meteoblue.com/es/tiempo/mapas/widget/bogot%c3%a1_colombia_3688689?windAnimation=1&gust=1&satellite=1&cloudsAndPrecipitation=1&temperature=1&sunshine=1&extremeForecastIndex=1&geoloc=fixed&tempunit=C&windunit=km%252Fh&lengthunit=metric&zoom=5&autowidth=auto"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 100%; height: 720px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/es/tiempo/mapas/bogot%c3%a1_colombia_3688689?utm_source=map_widget&utm_medium=linkus&utm_content=map&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div>
        <iframe width="1920" height="479" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" id="gmap_canvas" src="https://maps.google.com/maps?width=1920&amp;height=479&amp;hl=en&amp;q=%20+()&amp;t=h&amp;z=12&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"></iframe> <a href='http://maps-generator.com/es'>maps en tu sitio web</a> <script type='text/javascript' src='https://embedmaps.com/google-maps-authorization/script.js?id=22d66b2584e428f60a6a4958c28370821b53d19d'></script>
    </body>
</html>'''

@app.route("/africa")
def africa():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Paises de Africa</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Paises del Africa</h1>

    <h2>África</h2>
    <p>Egipto, Sudáfrica, Kenia, Nigeria, Ghana, Marruecos, Tanzania, Uganda, Argelia, Etiopía.</p>
    <h3>Egipto</h3>
    <ul>
        <li>Capital: El Cairo</li>
        <li>Famoso por: Pirámides y el río Nilo</li>
        <li>Idioma: Árabe</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/eg"><span style="color:gray;">Hora actual en</span><br />Egipto</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FCairo" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Sudáfrica</h3>
    <ul>
        <li>Capital: Pretoria</li>
        <li>Famoso por: Diversidad cultural y el Parque Nacional Kruger</li>
        <li>Idioma: 11 idiomas oficiales</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/za"><span style="color:gray;">Hora actual en</span><br />Sudáfrica</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FJohannesburg" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Kenia</h3>
    <ul>
        <li>Capital: Nairobi</li>
        <li>Famoso por: Safaris y la migración de los ñus</li>
        <li>Idioma: Swahili e inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/ke"><span style="color:gray;">Hora actual en</span><br />Kenia</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FNairobi" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Nigeria</h3>
    <ul>
        <li>Capital: Abuya</li>
        <li>Famoso por: Su diversidad étnica y cultural</li>
        <li>Idioma: Inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/ng"><span style="color:gray;">Hora actual en</span><br />Nigeria</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FLagos" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Ghana</h3>
    <ul>
        <li>Capital: Acra</li>
        <li>Famoso por: Su historia de oro y cultura vibrante</li>
        <li>Idioma: Inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/gh"><span style="color:gray;">Hora actual en</span><br />Ghana</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Africa%2FAccra" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
        <iframe src="https://www.meteoblue.com/es/tiempo/mapas/widget/bogot%c3%a1_colombia_3688689?windAnimation=1&gust=1&satellite=1&cloudsAndPrecipitation=1&temperature=1&sunshine=1&extremeForecastIndex=1&geoloc=fixed&tempunit=C&windunit=km%252Fh&lengthunit=metric&zoom=5&autowidth=auto"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 100%; height: 720px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/es/tiempo/mapas/bogot%c3%a1_colombia_3688689?utm_source=map_widget&utm_medium=linkus&utm_content=map&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div>
        <iframe width="1920" height="479" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" id="gmap_canvas" src="https://maps.google.com/maps?width=1920&amp;height=479&amp;hl=en&amp;q=%20+()&amp;t=h&amp;z=12&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"></iframe> <a href='http://maps-generator.com/es'>maps en tu sitio web</a> <script type='text/javascript' src='https://embedmaps.com/google-maps-authorization/script.js?id=22d66b2584e428f60a6a4958c28370821b53d19d'></script>
    </body>
</html>'''

@app.route("/america")
def america():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Paises de America</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Paises de America</h1>

    <h2>América</h2>
    <p>Estados Unidos, Brasil, Argentina, Canadá, Chile, México, Colombia, Perú, Venezuela, Cuba.</p>
    <h3>Estados Unidos</h3>
    <ul>
        <li>Capital: Washington D.C.</li>
        <li>Famoso por: Influencia cultural y económica</li>
        <li>Idioma: Inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/4140963"><span style="color:gray;">Hora actual en</span><br />Washington, Estados Unidos (USA)</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FNew_York" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Brasil</h3>
    <ul>
        <li>Capital: Brasilia</li>
        <li>Famoso por: Carnaval y la Amazonía</li>
        <li>Idioma: Portugués</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/3469058"><span style="color:gray;">Hora actual en</span><br />Brasília, Brasil</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FSao_Paulo" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Argentina</h3>
    <ul>
        <li>Capital: Buenos Aires</li>
        <li>Famoso por: Tango y la Patagonia</li>
        <li>Idioma: Español</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/3435910"><span style="color:gray;">Hora actual en</span><br />Buenos Aires, Argentina</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FArgentina%2FBuenos_Aires" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Colombia</h3>
    <ul>
        <li>Capital: Bogotá</li>
        <li>Famoso por: Café, biodiversidad y el Carnaval de Barranquilla</li>
        <li>Idioma: Español</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/3674962"><span style="color:gray;">Hora actual en</span><br />Medellín, Colombia</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FBogota" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Canadá</h3>
    <ul>
        <li>Capital: Ottawa</li>
        <li>Famoso por: Su naturaleza y multiculturalidad</li>
        <li>Idioma: Inglés y francés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/6094817"><span style="color:gray;">Hora actual en</span><br />Ottawa, Canadá</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FToronto" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>Chile</h3>
    <ul>
        <li>Capital: Santiago</li>
        <li>Famoso por: Su geografía diversa y el vino</li>
        <li>Idioma: Español</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/3871336"><span style="color:gray;">Hora actual en</span><br />Santiago, Chile</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=America%2FSantiago" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
        <iframe src="https://www.meteoblue.com/es/tiempo/mapas/widget/bogot%c3%a1_colombia_3688689?windAnimation=1&gust=1&satellite=1&cloudsAndPrecipitation=1&temperature=1&sunshine=1&extremeForecastIndex=1&geoloc=fixed&tempunit=C&windunit=km%252Fh&lengthunit=metric&zoom=5&autowidth=auto"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 100%; height: 720px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/es/tiempo/mapas/bogot%c3%a1_colombia_3688689?utm_source=map_widget&utm_medium=linkus&utm_content=map&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div>
        <iframe width="1920" height="479" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" id="gmap_canvas" src="https://maps.google.com/maps?width=1920&amp;height=479&amp;hl=en&amp;q=%20+()&amp;t=h&amp;z=12&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"></iframe> <a href='http://maps-generator.com/es'>maps en tu sitio web</a> <script type='text/javascript' src='https://embedmaps.com/google-maps-authorization/script.js?id=22d66b2584e428f60a6a4958c28370821b53d19d'></script>
    
    </body>
</html>'''

@app.route("/asia")
def asia():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Paises de Asia</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Paises de Asia</h1>

    <h2>Asia</h2>
    <p>China, India, Japón, Rusia, Indonesia, Pakistán, Bangladesh, Filipinas, Vietnam, Turquía.</p>
    <h3>China</h3>
    <ul>
        <li>Capital: Pekín</li>
        <li>Famoso por: Gran Muralla y su gran población</li>
        <li>Idioma: Mandarín</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/1816670"><span style="color:gray;">Hora actual en</span><br />Beijing, China</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FShanghai" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>
    <h3>India</h3>
    <ul>
        <li>Capital: Nueva Delhi</li>
        <li>Famoso por: Diversidad cultural y el Taj Mahal</li>
        <li>Idioma: Hindi y inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/in"><span style="color:gray;">Hora actual en</span><br />India</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FKolkata" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Japón</h3>
    <ul>
        <li>Capital: Tokio</li>
        <li>Famoso por: Tecnología avanzada, cultura tradicional y gastronomía.</li>
        <li>Idioma: Japonés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/jp"><span style="color:gray;">Hora actual en</span><br />Japón</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FTokyo" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Rusia</h3>
    <ul>
        <li>Capital: Moscú</li>
        <li>Famoso por: Su vasta extensión territorial, historia rica y cultura diversa.</li>
        <li>Idioma: Ruso</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/524901"><span style="color:gray;">Hora actual en</span><br />Moscow, Rusia</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Europe%2FMoscow" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Indonesia</h3>
    <ul>
        <li>Capital: Yakarta</li>
        <li>Famoso por: Su biodiversidad, islas y cultura variada.</li>
        <li>Idioma: Indonesio</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/city/1642911"><span style="color:gray;">Hora actual en</span><br />Jakarta, Indonesia</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FJakarta" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Pakistán</h3>
    <ul>
        <li>Capital: Islamabad</li>
        <li>Famoso por: Su historia antigua, montañas y cultura rica.</li>
        <li>Idioma: Urdu e inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/pk"><span style="color:gray;">Hora actual en</span><br />Pakistán</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FKarachi" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Bangladesh</h3>
    <ul>
        <li>Capital: Daca</li>
        <li>Famoso por: Su cultura vibrante y el río Ganges.</li>
        <li>Idioma: Bengalí</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/bd"><span style="color:gray;">Hora actual en</span><br />Bangladesh</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FDhaka" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Filipinas</h3>
    <ul>
        <li>Capital: Manila</li>
        <li>Famoso por: Sus playas, cultura diversa y hospitalidad.</li>
        <li>Idioma: Filipino e inglés</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/ph"><span style="color:gray;">Hora actual en</span><br />Filipinas</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FManila" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Vietnam</h3>
    <ul>
        <li>Capital: Hanói</li>
        <li>Famoso por: Su historia, paisajes naturales y gastronomía.</li>
        <li>Idioma: Vietnamita</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/vn"><span style="color:gray;">Hora actual en</span><br />Vietnam</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Asia%2FHo_Chi_Minh" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>

    <h3>Turquía</h3>
    <ul>
        <li>Capital: Ankara</li>
        <li>Famoso por: Su rica historia, cultura y la mezcla de Oriente y Occidente.</li>
        <li>Idioma: Turco</li>
        <div style="text-align:center;padding:1em 0;"> <h4><a style="text-decoration:none;" href="https://www.zeitverschiebung.net/es/country/tr"><span style="color:gray;">Hora actual en</span><br />Turquía</a></h4> <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=es&size=small&timezone=Europe%2FIstanbul" width="100%" height="90" frameborder="0" seamless></iframe> </div>
    </ul>


        <iframe src="https://www.meteoblue.com/es/tiempo/mapas/widget/bogot%c3%a1_colombia_3688689?windAnimation=1&gust=1&satellite=1&cloudsAndPrecipitation=1&temperature=1&sunshine=1&extremeForecastIndex=1&geoloc=fixed&tempunit=C&windunit=km%252Fh&lengthunit=metric&zoom=5&autowidth=auto"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 100%; height: 720px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/es/tiempo/mapas/bogot%c3%a1_colombia_3688689?utm_source=map_widget&utm_medium=linkus&utm_content=map&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div>
        <iframe width="1920" height="479" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" id="gmap_canvas" src="https://maps.google.com/maps?width=1920&amp;height=479&amp;hl=en&amp;q=%20+()&amp;t=h&amp;z=12&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"></iframe> <a href='http://maps-generator.com/es'>maps en tu sitio web</a> <script type='text/javascript' src='https://embedmaps.com/google-maps-authorization/script.js?id=22d66b2584e428f60a6a4958c28370821b53d19d'></script>
    </body>
</html>'''

app.run(debug=True)
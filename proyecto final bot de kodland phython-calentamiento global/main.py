import discord
from discord.ext import commands
import pyttsx3
import asyncio
import threading

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="=", intents=intents)
engine = pyttsx3.init()

print("si no te sabes lo comandos del bot escribe =help")


lista_quiz = [
    {
        "texto": "¿Qué es el calentamiento global?",
        "opciones": ["Aumento de la temperatura media de la Tierra", "Un enfriamiento del núcleo del planeta", "El aumento de las lluvias", "La rotación más rápida de la Tierra"],
        "correcta": 0
    },
    {
        "texto": "¿Cuál es el principal gas de efecto invernadero emitido por las actividades humanas?",
        "opciones": ["Oxígeno", "Dióxido de carbono (CO2)", "Metano", "Nitrógeno"],
        "correcta": 1
    },
    {
        "texto": "¿Qué sector es uno de los mayores emisores de metano?",
        "opciones": ["El transporte", "La agricultura y ganadería", "La energía solar", "La minería de oro"],
        "correcta": 1
    },
    {
        "texto": "¿Qué consecuencia directa tiene el derretimiento acelerado de los glaciares?",
        "opciones": ["El aumento del nivel del mar", "Días con más luz solar", "La disminución de las lluvias", "La creación de nuevos bosques"],
        "correcta": 0
    },
    {
        "texto": "¿Qué significa el término 'huella de carbono'?",
        "opciones": ["Una marca de zapatos ecológicos", "La cantidad total de gases que emitimos", "El rastro que dejan los incendios forestales", "El peso del carbón en la atmósfera"],
        "correcta": 1
    },
    {
        "texto": "¿Cuál de estas es una fuente de energía renovable y limpia?",
        "opciones": ["El petróleo", "El carbón", "La energía eólica", "El gas natural"],
        "correcta": 2
    },
    {
        "texto": "¿Qué importante acuerdo internacional busca limitar el calentamiento global?",
        "opciones": ["El Acuerdo de París", "El Tratado de Versalles", "El Acuerdo de Ginebra", "El Pacto de Washington"],
        "correcta": 0
    },
    {
        "texto": "¿Qué acción personal ayuda directamente a reducir el calentamiento global?",
        "opciones": ["Dejar luces encendidas", "Usar más el automóvil", "Plantar árboles y reciclar", "Quemar la basura del hogar"],
        "correcta": 2
    },
    {
        "texto": "¿Cómo afecta principalmente el calentamiento global a los océanos?",
        "opciones": ["Los hace más dulces", "Los acidifica y calienta", "Los congela rápidamente", "Reduce su tamaño drásticamente"],
        "correcta": 1
    },
    {
        "texto": "¿Qué es el efecto invernadero?",
        "opciones": ["La construcción de invernaderos", "La retención del calor del sol en la atmósfera", "Un tipo de lluvia ácida", "Un clima tropical artificial"],
        "correcta": 1
    },
    {
        "texto": "¿Qué medio de transporte emite menos gases contaminantes?",
        "opciones": ["El avión", "El barco de carga", "El automóvil a gasolina", "La bicicleta"],
        "correcta": 3
    },
    {
        "texto": "¿Por qué los osos polares están en peligro por el calentamiento global?",
        "opciones": ["Pierden su hábitat de hielo marino", "Se están mudando al desierto", "Tienen que hibernar menos tiempo", "Se reproducen demasiado rápido"],
        "correcta": 0
    },
    {
        "texto": "¿Cuál de los siguientes NO es considerado un gas de efecto invernadero?",
        "opciones": ["El metano", "El oxígeno", "El óxido nitroso", "El vapor de agua"],
        "correcta": 1
    },
    {
        "texto": "¿Qué regla ayuda a generar menos basura y emisiones?",
        "opciones": ["Las 3 R (Reducir, Reutilizar, Reciclar)", "La regla de comprar y tirar", "La regla de quemar todo", "La regla de esconder la basura"],
        "correcta": 0
    },
    {
        "texto": "¿Qué fenómenos meteorológicos se vuelven más intensos por el calentamiento global?",
        "opciones": ["Huracanes, tormentas y sequías", "Las auroras boreales", "Los arcoíris dobles", "Los eclipses solares"],
        "correcta": 0
    }
]

class KahootView(discord.ui.View):



    def __init__(self):

        super().__init__()



    async def comprobar(self, interaction, opcion):



        global pregunta_actual



        pregunta = lista_quiz[pregunta_actual]



        if opcion == pregunta["correcta"]:

            mensaje = "¡Correcto!"

        else:

            mensaje = "Incorrecto"



        pregunta_actual += 1



        # ¿Hay más preguntas?

        if pregunta_actual < len(lista_quiz):



            siguiente = lista_quiz[pregunta_actual]



            texto = f"""

**{siguiente["texto"]}**



🅰 {siguiente["opciones"][0]}

🅱 {siguiente["opciones"][1]}

🇨 {siguiente["opciones"][2]}

🇩 {siguiente["opciones"][3]}

"""



            await interaction.response.edit_message(

                content=f"{mensaje}\n\n{texto}",

                view=KahootView()

            )



        else:

            await interaction.response.edit_message(

                content=f"{mensaje}\n\n ¡Juego terminado!",

                view=None

            )



    @discord.ui.button(label="A", style=discord.ButtonStyle.primary)

    async def boton_a(self, interaction, button):

        await self.comprobar(interaction, 0)



    @discord.ui.button(label="B", style=discord.ButtonStyle.success)

    async def boton_b(self, interaction, button):

        await self.comprobar(interaction, 1)



    @discord.ui.button(label="C", style=discord.ButtonStyle.danger)

    async def boton_c(self, interaction, button):

        await self.comprobar(interaction, 2)



    @discord.ui.button(label="D", style=discord.ButtonStyle.secondary)

    async def boton_d(self, interaction, button):

        await self.comprobar(interaction, 3)
def speak(text: str):
    global engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
        
    engine.say(text)
    engine.runAndWait()
    engine.stop()

@bot.command()
async def quiz(ctx): 
    
    global pregunta_actual
    pregunta_actual = 0
    pregunta = lista_quiz[pregunta_actual]
    texto = f"""

**{pregunta["texto"]}**



🅰 {pregunta["opciones"][0]}

🅱 {pregunta["opciones"][1]}

🇨 {pregunta["opciones"][2]}

🇩 {pregunta["opciones"][3]}

"""
    await ctx.send(texto, view=KahootView())



@bot.command()
async def start(ctx):
    texto = "hola, soy un bot de discord que te ayudara a comprender el calentamiento global, tambien te ayudare a concientizarte sobre la contaminacion y responder las preguntas que tienes. antes de nada, ¿que es el calentamiento global?. pues El calentamiento global es el aumento a largo plazo de la temperatura promedio de la Tierra. Este fenómeno ocurre principalmente porque estamos liberando gases que atrapan el calor en la atmósfera, lo que altera el clima de todo el planeta. Si tienes preguntas escribe: =info"
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def info(ctx):
    texto = "!perfecto!, parece que tienes algunas preguntas, aca te dejo lo que tienes que escribir para cada pregunta: porque es peligroso: =PEP, en que me afecta en mi vida cotidiana: =EQMAEMVC, cual es la causante: =CELC, como podemos contribuir para disminuir el peligro: =CPCPDEP, como puedo concientizar a las demas personas: =CPCALDPSECC, cual es la diferencia entre cambio climatico y calentamiento global: =DCCYCG, que es la huella de carbono: =QHDC, estamos a tiempo de detenerlo: =EATDD, que son los gases de efecto invernadero: =QSLGEI, cuales son las energias renovables: =CER, que pasara si no hacemos nada: =QPSNHA, y si quieres hacer un quiz sobre calentamiento global escribe =quiz"
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def PEP(ctx):
    texto = "El calentamiento global no es solo un aumento de temperatura que nos hace sentir más calor; es un desajuste completo del motor climático de nuestro planeta. Al retener más energía en la atmósfera, la Tierra experimenta un efecto dominó que afecta desde el agua que bebemos hasta la estabilidad de las ciudades donde vivimos. La peligrosidad del calentamiento global se resume en cuatro grandes frentes interconectados: Eventos climáticos extremos y más destructivos, El colapso de los océanos y el aumento del nivel del mar, Amenaza directa a la seguridad alimentaria y la salud humana, Pérdida masiva de biodiversidad."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def EQMAEMVC(ctx):
    texto = "Aunque el calentamiento global suena como un problema abstracto de osos polares y científicos, la realidad es que ya está alterando las rutinas más comunes de nuestro día a día. No es algo del futuro; afecta tu bolsillo, tu salud y hasta tus planes de la semana. Aquí te muestro cómo se traduce en tu vida cotidiana: El bolsillo: El costo de la vida sube, La salud y el bienestar físico, Tus rutinas, planes y logística."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def CELC(ctx):
    texto = "La causa principal del calentamiento global es el efecto invernadero artificial, provocado por las actividades humanas. Para entenderlo de forma sencilla: la Tierra tiene una capa natural de gases en la atmósfera que funciona como las paredes de vidrio de un invernadero. Su trabajo es retener un poco del calor del sol para que el planeta sea habitable. El problema es que los seres humanos hemos engrosado tanto esa capa de gases que ahora el planeta retiene demasiado calor y no puede liberarlo al espacio. Las actividades cotidianas e industriales que causan este problema son: La quema de combustibles fósiles, La deforestación, La agricultura y la ganadería intensiva, El consumo desmedido y los residuos."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def CPCPDEP(ctx):
    texto = "Para disminuir el peligro del calentamiento global, todos podemos aportar con pequeñas acciones. Aquí tienes cuatro ideas: 1. Ahorra energía en casa apagando luces y usando electrodomésticos eficientes. 2. Cambia tu forma de moverte, usando bicicleta, transporte público o caminando. 3. Aplica la regla de las tres R: Reduce, Reutiliza y Recicla para generar menos basura. 4. Disminuye el consumo de carnes rojas, ya que la ganadería intensiva genera muchos gases contaminantes. Cada pequeña acción cuenta."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def CPCALDPSECC(ctx):
    texto = "Concientizar a los demás es clave para crear un gran impacto. Puedes hacerlo liderando con el ejemplo; cuando tus amigos o familia vean tus acciones sostenibles, se inspirarán. Habla del tema sin regañar, comparte documentales o datos interesantes de forma amigable. También puedes usar tus redes sociales para compartir información verificada o unirte a grupos locales para limpiar parques o playas."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def DCCYCG(ctx):
    texto = "A menudo se usan como sinónimos, pero tienen diferencias importantes. El calentamiento global se refiere exclusivamente al aumento de la temperatura promedio de la Tierra. En cambio, el cambio climático es un término más amplio que incluye el calentamiento global y todos sus efectos secundarios, como el derretimiento de los glaciares, tormentas más intensas, sequías y la alteración de las estaciones."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def QHDC(ctx):
    texto = "La huella de carbono es como una marca que dejamos en el planeta. Es la cantidad total de gases de efecto invernadero que emitimos directa o indirectamente con nuestras actividades diarias. Conocer tu huella te ayuda a entender qué aspectos de tu estilo de vida contaminan más, como los viajes en auto, el uso de electricidad en casa o incluso los productos que compras."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def EATDD(ctx):
    texto = "¡Sí, aún estamos a tiempo! Los científicos indican que si reducimos drásticamente las emisiones en esta década, podemos evitar los peores escenarios. Aunque algunos cambios ya son irreversibles, cada fracción de grado que evitemos salvará millones de vidas, especies y ecosistemas. Por eso la acción climática urgente por parte de gobiernos, empresas y ciudadanos es tan importante."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

# --- NUEVAS PREGUNTAS (AÚN MÁS COMPLETAS) ---

@bot.command()
async def QSLGEI(ctx):
    texto = "Los gases de efecto invernadero son gases presentes en la atmósfera que atrapan el calor del sol. Los más comunes son el dióxido de carbono, el metano y el óxido nitroso. Aunque son necesarios en pequeñas cantidades para evitar que la Tierra se congele, el problema es que nuestras fábricas, autos y la agricultura masiva están liberando cantidades gigantescas, creando un efecto de horno alrededor del planeta."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def CER(ctx):
    texto = "Las energías renovables son aquellas que se obtienen de fuentes naturales inagotables, como el sol, el viento o la fuerza del agua. A diferencia del carbón o el petróleo, estas fuentes no emiten gases de efecto invernadero al generar electricidad. Cambiar nuestros sistemas hacia la energía solar, eólica e hidroeléctrica es el paso más importante que debemos dar como humanidad para frenar el calentamiento global."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def QPSNHA(ctx):
    texto = "Si no reducimos las emisiones y continuamos como hasta ahora, el planeta podría calentarse varios grados más para finales de siglo. Esto provocaría el derretimiento acelerado de los polos, inundando ciudades costeras enteras. Además, causaría sequías extremas que harían imposible cultivar alimentos en muchas regiones. Básicamente, pondríamos en grave riesgo la supervivencia de miles de especies y de nuestra propia civilización."
    await ctx.send(texto)
    await asyncio.to_thread(speak, texto)

@bot.command()
async def detener(ctx):
    global engine 
    if engine is not None:
        engine.stop()   
    
    await ctx.send("ahora la sinsetis de voz se a detenido") 
@bot.command()



async def ayuda(ctx):
    texto = """
**Lista de Comandos Disponibles**

Aquí tienes todos los comandos que puedes usar con el bot. ¡Solo escribe el prefijo `=` seguido del comando!

**Utilidades y Juegos:**
=start - Saludo inicial y breve explicación del calentamiento global.
=info - Muestra una guía rápida de las preguntas que puedes hacer.
=quiz - Inicia un cuestionario interactivo de 15 preguntas sobre el medio ambiente.
=detener - Detiene la síntesis de voz si está hablando,pero cuidado,si lo desactivas ya no se volvera a activar
=help - Muestra este mensaje de ayuda.

**Preguntas Informativas:**
=PEP - ¿Por qué es peligroso el calentamiento global?
=EQMAEMVC - ¿En qué me afecta en mi vida cotidiana?
=CELC - ¿Cuál es la causa principal?
=CPCPDEP - ¿Cómo podemos contribuir para disminuir el peligro?
=CPCALDPSECC - ¿Cómo puedo concientizar a las demás personas?
=DCCYCG - ¿Cuál es la diferencia entre cambio climático y calentamiento global?
=QHDC - ¿Qué es la huella de carbono?
=EATDD - ¿Estamos a tiempo de detenerlo?
=QSLGEI - ¿Qué son los gases de efecto invernadero?
=CER - ¿Cuáles son las energías renovables?
=QPSNHA - ¿Qué pasará si no hacemos nada?
"""
    # Solo enviamos el mensaje de texto, sin llamar a la función speak()
    await ctx.send(texto)



# Recuerda poner tu token aquí
bot.run("")
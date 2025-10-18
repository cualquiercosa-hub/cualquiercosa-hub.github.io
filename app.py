from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_costos_con_margen(costo_base):
    """
    Calcula el Costo Base más un margen del 30%, 80% y 100%.
    """
    # Cálculos de los márgenes
    margen_30 = costo_base * 0.30
    margen_80 = costo_base * 0.80
    margen_100 = costo_base * 1.00 

    # CÁLCULOS DE LOS TOTALES (Costo Base + Margen)
    total_30 = costo_base + margen_30
    total_80 = costo_base + margen_80
    total_100 = costo_base + margen_100 

    # Retorna todos los resultados para mostrarlos en la web
    return {
        "Costo Base": round(costo_base, 2),
        "Precio Venta (+30% margen)": round(total_30, 2),
        "Precio Venta (+80% margen)": round(total_80, 2),
        "Precio Venta (+100% margen)": round(total_100, 2)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = None
    costo_ingresado = None

    if request.method == 'POST':
        try:
            # Obtiene el valor del campo 'costo' del formulario
            costo_ingresado = float(request.form['costo'])
            
            # Llama a la función de cálculo
            resultados = calcular_costos_con_margen(costo_ingresado)
            
        except ValueError:
            # Si el usuario no ingresa un número válido
            resultados = {"Error": "Por favor, introduce un número válido."}

    # Renderiza la plantilla HTML, enviando los resultados
    return render_template('index.html', resultados=resultados, costo=costo_ingresado)
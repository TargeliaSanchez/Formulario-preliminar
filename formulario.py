import streamlit as st

# Configuración de la página
st.set_page_config(layout="wide")
st.title("📋 EVALUAR – BPS")

# --- Estilos CSS ---
st.markdown("""
<style>
    .question {
        padding: 0.2rem 0;
        border-bottom: 1px solid #eee;
    }
    .question-number {
        font-weight: bold;
        color: #2a9d8f;
    }
    .section {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
    }
    .section-title {
        color: #264653;
        font-weight: 500;
        font-size: 0.1rem;
        margin: 0.1rem 0 0.25rem 0 !important;
    }
    .subsection-title {
        color: #2a9d8f;
        font-weight: 500;
        margin: 0.5rem 0 0.5rem 0;
        font-size: 1.1rem;
        margin-bottom: 0.5rem !important;
    }
    .rating-tag {
        display: inline-block;
        padding: 0.2rem 0.5rem;
        border-radius: 12px;
        font-size: 0.8rem;
        margin-left: 0.5rem;
        vertical-align: middle;
        font-weight: bold;
    }
    .no-cumple { background-color: #ffebee; color: #c62828; border: 1px solid #ef9a9a; }
    .incipiente { background-color: #fff8e1; color: #f57f17; border: 1px solid #ffcc80; }
    .aceptable { background-color: #e8f5e9; color: #2e7d32; border: 1px solid #a5d6a7; }
    .satisfactorio { background-color: #e3f2fd; color: #1565c0; border: 1px solid #90caf9; }
    .optimo { background-color: #f1f8e9; color: #33691e; border: 1px solid #c5e1a5; }
    .dimension-rating {
        background-color: #e3f2fd;
        padding: 1.5rem 1.5rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        font-weight: bold;
    }
    .nav-buttons {
        display: flex;
        justify-content: space-between;
        margin-top: 0.1rem;
    }
    .progress-container {
        margin: 0.1rem 0;
    }
</style>
""", unsafe_allow_html=True)


# --- Estado de la sesión ---
if 'current_main_dim' not in st.session_state:
    st.session_state.current_main_dim = 0
if 'current_sub_dim' not in st.session_state:
    st.session_state.current_sub_dim = 0

# Opciones del selectbox
opciones = [
    ("1 - No cumple", 1),
    ("2 - Incipiente", 2),
    ("3 - Aceptable", 3),
    ("4 - Satisfecho", 4),
    ("5 - Óptimo", 5)
]

def guardar_respuesta(key, value):
    if "respuestas" not in st.session_state:
        st.session_state.respuestas = {}
    st.session_state.respuestas[key] = value


def determinar_calificacion(respuestas):
    # Filtra solo respuestas numéricas (ignora strings/texto)
    valores = []
    for resp in respuestas:
        if isinstance(resp, tuple) and isinstance(resp[1], int):  # Si es opción (texto, valor)
            valores.append(resp[1])
        elif isinstance(resp, int):  # Si es directamente un número
            valores.append(resp)

    if not valores:  # Si no hay valores numéricos
        return ("Sin calificación", "sin-calificacion", 0)

    # Lógica original de calificación
    if all(v == 5 for v in valores):
        return ("5. Óptimo", "optimo", 5)
    elif all(v == 1 for v in valores):
        return ("1. No cumple", "no-cumple", 1)
    elif sum(v >= 4 for v in valores) >= 3:
        return ("4. Satisfactorio", "satisfactorio", 4)
    elif sum(v >= 3 for v in valores) >= 3:
        return ("3. Aceptable", "aceptable", 3)
    elif any(v == 2 for v in valores):
        return ("2. Incipiente", "incipiente", 2)
    else:
        return ("1. No cumple", "no-cumple", 1)


import streamlit as st

# Inicializa respuestas en session_state si no existe
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

opciones = [
    "Seleccione",
    "Fisioterapia",
    "Fonoaudiología",
    "Terapia ocupacional",
    "Terapia Respiratoria",
    "Esp. medicina Física y Fehabilitación",
    "Psicología",
    "Trabajo Social",
    "Nutrición",
]

# Para layout en 4 columnas
cols = st.columns(4)
pares = 8  # Número de pares selectbox/number_input

for i in range(pares):
    select_key = f"DesP_{i+1}"
    number_key = f"numero_{i+1}"

    col = cols[i % 4]  # Distribuye en columnas

    with col:
        # Recupera y valida valor guardado para selectbox
        valor_guardado = st.session_state.respuestas.get(select_key, "Seleccione")
        if valor_guardado not in opciones:
            valor_guardado = "Seleccione"
        val = st.selectbox(
            "",
            options=opciones,
            index=opciones.index(valor_guardado),
            key=select_key,
        )
        st.session_state.respuestas[select_key] = val

        # Recupera valor guardado para number_input
        num_valor_guardado = st.session_state.respuestas.get(number_key, 0)
        num = st.number_input(
            "",
            min_value=0,
            max_value=100,
            value=num_valor_guardado,
            step=1,
            key=number_key,
        )
        st.session_state.respuestas[number_key] = num




for i in range(1, 8):
    st.markdown(f"""
        <div style="
        background-color: #e8f0fe ;
        color: black;
        padding: 4px 10px;
        font-weight: normal;
        border-radius: 0.5px;
        "><b> {i}. SERVICIOS DE REHABILITACIÓN HABILITADOS 
        </div>
        """, unsafe_allow_html=True)
    servicio = st.selectbox(
        "",
        options=["Seleccione", "Fisioterapia", "Fonoaudiología", "Terapia ocupacional", "Terapia Respiratoria", "Esp. medicina Física y Fehabilitación", "Psicología", "Trabajo Social", "Nutrición"],
        key=f"servicio_{i}"
    )   
    guardar_respuesta(f"servicio_{i}", servicio)
    col_dias, sep1, col_areas, sep2, col_modalidades, col_prestador = st.columns([1, 0.1, 1.3, 0.1, 1.8, 1])

    with col_dias:
        st.markdown("<div style='text-align: center;'><b>Días de atención</b></div>", unsafe_allow_html=True)
        st.markdown("Marque con una X los días de atención")
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1.1,1,1,1,1])
        dias = ["L", "M", "Mi", "J", "V", "S", "D"]
        cols = [col1, col2, col3, col4, col5, col6, col7]
        for col, dia in zip(cols, dias):
            with col:
                st.markdown(f"**{dia}**")
                valor = st.checkbox(
                    "",  # sin texto largo
                    value=st.session_state.respuestas.get(f"{dia}_{i}", False),
                    key=f"{dia}_{i}"
                )
                guardar_respuesta(f"{dia}_{i}", valor)
    with sep1:
        st.markdown("<div class='vertical-divider'></div>", unsafe_allow_html=True)
    with col_areas:
        st.markdown("<div style='text-align: center;'><b>Áreas asistenciales</b></div>", unsafe_allow_html=True)
        st.markdown("Marque con X las áreas donde se prestan servicios de rehabilitación")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.markdown("**CE**")
            area_CE = st.checkbox("", key=f"CE_{i}")
            guardar_respuesta(f"CE_{i}", area_CE)
        with col2:
            st.markdown("**HO**")
            area_HO = st.checkbox("", key=f"HO_{i}")
            guardar_respuesta(f"HO_{i}", area_HO)
        with col3:
            st.markdown("**UR**")
            area_UR = st.checkbox("", key=f"UR_{i}")
            guardar_respuesta(f"UR_{i}", area_UR)
        with col4:
            st.markdown("**U**")
            area_U = st.checkbox("", key=f"U_{i}")
            guardar_respuesta(f"U_{i}", area_U)
        with col5:
            st.markdown("**UCI**")
            area_UCI = st.checkbox("", key=f"UCI_{i}")
            guardar_respuesta(f"UCI_{i}", area_UCI)
        with col6:
            st.markdown("**Otr**")
            area_Otr = st.checkbox("", key=f"Otr_{i}")
            guardar_respuesta(f"Otr_{i}", area_Otr)
    with sep2:
        st.markdown("<div class='vertical-divider'></div>", unsafe_allow_html=True)
    with col_modalidades:
        st.markdown("<div style='text-align: center;'><b>Modalidades de prestación</b></div>", unsafe_allow_html=True)
        st.markdown("Marque con X  las modalidades habilitadas")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Intramural**")
            mod_AMB = st.checkbox("AMB", key=f"AMB_{i}")
            guardar_respuesta(f"AMB_{i}", mod_AMB)
            mod_HOS = st.checkbox("HOS", key=f"HOS_{i}")
            guardar_respuesta(f"HOS_{i}", mod_HOS)
        with col2:
            st.markdown("**Extramural**")
            mod_DOM = st.checkbox("DOM", key=f"DOM_{i}")
            guardar_respuesta(f"DOM_{i}", mod_DOM)
            mod_JORN = st.checkbox("JORN", key=f"JORN_{i}")
            guardar_respuesta(f"JORN_{i}", mod_JORN)
            mod_UNMOV = st.checkbox("UN.MOV", key=f"UNMOV_{i}")
            guardar_respuesta(f"UNMOV_{i}", mod_UNMOV)
        with col3:
            st.markdown("**Telemedicina**")
            mod_TMIA = st.checkbox("TM-IA", key=f"TMIA_{i}")
            guardar_respuesta(f"TMIA_{i}", mod_TMIA)
            mod_TMNIA = st.checkbox("TM-NIA", key=f"TMNIA_{i}")
            guardar_respuesta(f"TMNIA_{i}", mod_TMNIA)
            mod_TE = st.checkbox("TE", key=f"TE_{i}")
            guardar_respuesta(f"TE_{i}", mod_TE)
            mod_TMO = st.checkbox("TMO", key=f"TMO_{i}")
            guardar_respuesta(f"TMO_{i}", mod_TMO)
    with col_prestador:
        st.markdown("<div style='text-align: center;'><b>Prestador telemedicina</b></div>", unsafe_allow_html=True)
        st.markdown("marque con una X el tipo de prestador")
        prestador = st.radio("Tipo", ["P.REM", "P.REF"], key=f"prestador_{i}")
        guardar_respuesta(f"prestador_{i}", prestador)





# --- Estructura de datos ---
dimensiones = {
    "D1. ORGANIZACIÓN Y GESTIÓN DE LOS SERVICIOS DE REHABILITACIÓN": {
        "D1.1 La oferta de servicios de rehabilitación corresponde con el nivel de complejidad de la institución. ►": [
            {"texto": "La institución presta servicio de psicología y/o trabajo social", "key": "pD11_1"},
            {"texto": "La institución presta servicios de fisioterapia, fonoaudiología y/o terapia ocupacional", "key": "pD11_2"},
            {"texto": "Los servicios de rehabilitación disponibles corresponden con el nivel de complejidad.*", "key": "pD11_3"},
            {"texto": "Los servicios de rehabilitación se organizan en un área específica de la institución. ", "key": "pD11_4"},
        ],
        "D1.2 El talento humano de rehabilitación vinculado a la institución es acorde a la capacidad instalada versus la demanda de los servicios. ►": [
            {"texto": "Los servicios de rehabilitación habilitados cuentan continuamente con profesional[es] contratado[s] o vinculado[s]. ", "key": "pD12_1"},
            {"texto": "La disponibilidad del talento humano de rehabilitación es adecuada a la capacidad instalada versus la demanda de los servicios.", "key": "pD12_2"},
            {"texto": "La institución define el perfil del talento humano de rehabilitación según las necesidades de atención de los usuarios. ", "key": "pD12_3"},
            {"texto": "La institución designa un líder, coordinador o jefe de los servicios de rehabilitación. ", "key": "pD12_4"},
        ]
        ,
        "D1.3 La prestación de los servicios de rehabilitación se realiza en diferentes modalidades: intramural, extramural y/o telemedicina.": [
            {"texto": "Se prestan servicios de rehabilitación en modalidad ambulatoria y/o hospitalaria [si aplica].", "key": "pD13_1"},
            {"texto": "Se prestan servicios de rehabilitación en modalidad domiciliaria u otras modalidades extramurales [están definidos los criterios para la atención en esta modalidad].", "key": "pD13_2"},
            {"texto": "Se prestan servicios de rehabilitación en la modalidad de telemedicina.", "key": "pD13_3"},
            {"texto": "La prestación de servicios en la modalidad de telemedicina incluye especialidades médicas relacionadas con rehabilitación.", "key": "pD13_4"},
        ]
        ,
        "D1.4 La institución cuenta con un sistema unificado de historia clínica disponible para los profesionales que intervienen en el proceso de rehabilitación. ►": [
        {"texto": "La institución cuenta con historia clínica electrónica que incluye la información del usuario en las diferentes fases de la atención.", "key": "pD14_1"},
        {"texto": "La historia clínica registra las atenciones y procedimientos realizados a los usuarios en rehabilitación.", "key": "pD14_2"},
        {"texto": "La historia clínica está disponible para el registro simultáneo o inmediato de la atención.", "key": "pD14_3"},
        {"texto": "La historia clínica incluye contenido y/o formatos específicos para los servicios de rehabilitación.", "key": "pD14_4"}
        ],
        "D1.5 La atención de los usuarios de rehabilitación o “proceso de rehabilitación” se encuentra documentado en la institución. ►": [
        {"texto": "Se documentan los servicios de terapias [modalidades de prestación, actividades, talento humano, infraestructura, dotación, riesgos e indicadores].", "key": "pD15_1"},
      {"texto": "Se documenta la atención como un proceso continuo con un tiempo de duración definido.", "key": "pD15_2"},
    {"texto": "El proceso de rehabilitación integra los diferentes servicios desde el ingreso hasta el egreso del usuario.", "key": "pD15_3"},
    {"texto": "El documento del proceso de rehabilitación está actualizado y disponible en el sistema de gestión de calidad.", "key": "pD15_4"}
],
"D1.6 El proceso de rehabilitación se estructura por etapas o fases que orientan la atención del usuario en la institución. ►": [
    {"texto": "Se describen los mecanismos de entrada o ingreso del usuario.", "key": "pD16_1"},
    {"texto": "El proceso se estructura en fases: 1. Evaluación inicial, 2. Plan de atención, 3. Intervención y 4. Evaluación final.", "key": "pD16_2"},
    {"texto": "Cada etapa describe el alcance y las acciones para el logro de metas de rehabilitación.", "key": "pD16_3"},
    {"texto": "El proceso de rehabilitación se divulga al personal asistencial de la institución.", "key": "pD16_4"}
],
"D1.7 En los servicios de rehabilitación se encuentran disponibles guías de práctica clínica, protocolos de atención y/o procedimientos para orientar la toma de decisiones. ►": [
    {"texto": "Se encuentran disponibles protocolos de atención en los servicios de rehabilitación.", "key": "pD17_1"},
    {"texto": "La institución cuenta con guías de práctica clínica específicas para rehabilitación.", "key": "pD17_2"},
    {"texto": "Existe un procedimiento para la elaboración/adopción/adaptación de protocolos o GPC.", "key": "pD17_3"},
    {"texto": "Los protocolos y/o GPC están actualizados e implementados en la institución.", "key": "pD17_4"}
],
"D1.8 La institución estructura e implementa un plan de capacitación en atención o rehabilitación con enfoque biopsicosocial.": [
    {"texto": "La inducción de nuevos profesionales incluye el enfoque biopsicosocial.", "key": "pD18_1"},
    {"texto": "Se realizan capacitaciones periódicas sobre atención con enfoque biopsicosocial.", "key": "pD18_2"},
    {"texto": "Las capacitaciones están dirigidas al personal asistencial y administrativo.", "key": "pD18_3"},
    {"texto": "Se verifican acciones para comprobar el conocimiento del personal sobre el enfoque.", "key": "pD18_4"}
],
"D1.9 La institución cuenta con áreas de atención, dotación y tecnología para la implementación de intervenciones orientadas a optimizar el proceso de rehabilitación.": [
    {"texto": "Los servicios cuentan con equipos e insumos adecuados a las necesidades de los usuarios.", "key": "pD19_1"},
    {"texto": "Se realiza mantenimiento periódico y reparación oportuna de áreas, equipos e insumos.", "key": "pD19_2"},
    {"texto": "La tecnología disponible favorece el acceso, eficiencia y personalización de la atención.", "key": "pD19_3"},
    {"texto": "La institución cuenta con ambientes especializados para promover autonomía e independencia.", "key": "pD19_4"}
]

    },
    "D2. PROCESO DE REHABILITACIÓN": {
        "D2.1 Se realiza o se cuenta con valoración médica integral de la condición de salud de los usuarios de rehabilitación. ►": [
    {"texto": "La valoración médica de los usuarios de rehabilitación se encuentra disponible en la historia clínica.", "key": "pD21_1"},
    {"texto": "La valoración médica del usuario aborda integralmente la condición de salud para establecer el diagnóstico [principal y relacionados].", "key": "pD21_2"},
    {"texto": "La información de la valoración médica es pertinente y relevante para definir los objetivos y el plan de atención por rehabilitación.", "key": "pD21_3"},
    {"texto": "La institución cuenta con formato estandarizado para la valoración médica de los usuarios de rehabilitación.", "key": "pD21_4"}
],
"D2.2 Se usan pruebas estandarizadas o instrumentos para la evaluación de los usuarios de rehabilitación. ►": [
    {"texto": "Los profesionales de rehabilitación definen las pruebas o instrumentos de evaluación.", "key": "pD22_1"},
    {"texto": "La institución define criterios para la selección de pruebas o instrumentos de evaluación de los usuarios de rehabilitación.", "key": "pD22_2"},
    {"texto": "La institución cuenta con un método desarrollado o adaptado para la evaluación de los usuarios de rehabilitación.", "key": "pD22_3"},
    {"texto": "La institución disponen y usan pruebas estandarizadas o instrumentos específicos según las caracteristicas y necesidades de los usuarios. [la disponibilidad hace referencia a fácil acceso durante la atención. Ej. en historia clínica].", "key": "pD22_4"}
],
"D2.3 En la evaluación se valora el estado funcional del usuario ►": [
    {"texto": "La valoración del estado funcional incluye diferentes dominios o áreas del funcionamiento de los usuarios.", "key": "pD23_1"},
    {"texto": "La valoración del estado funcional se basa en parámetros medibles y los resultados se expresan en datos numéricos y/o categóricos.", "key": "pD23_2"},
    {"texto": "La valoración del estado funcional concluye con un perfil de funcionamiento o diagnóstico funcional.", "key": "pD23_3"},
    {"texto": "La valoración del estado funcional involucra un equipo multidisciplinario** que interviene en el proceso de rehabilitación.", "key": "pD23_4"}
],
"D2.4 La evaluación considera el desempeño y los roles del usuario en diferentes entornos.": [
    {"texto": "La valoración del estado funcional incluye diferentes dominios o áreas del funcionamiento de los usuarios. [Funciones, capacidad, desempeño, participación].", "key": "pD24_1"},
    {"texto": "La valoración del estado funcional se basa en parámetros medibles y los resultados se expresan en datos numéricos.", "key": "pD24_2"},
    {"texto": "La valoración del estado funcional concluye con un perfil de funcionamiento o diagnóstico funcional.", "key": "pD24_3"},
    {"texto": "La valoración del estado funcional involucra un equipo multidisciplinario** que interviene en el proceso de rehabilitación.", "key": "pD24_4"}
],
"D2.5 En la evaluación se identifican facilitadores y barreras del entorno que influyen en el proceso de rehabilitación del usuario.": [
    {"texto": "Se registran facilitadores y barreras relacionadas con:", "key": "pD25_1"},
    {"texto": "Acceso a servicios de salud según complejidad del diagnóstico o condición del usuario.", "key": "pD25_2"},
    {"texto": "Ayudas técnicas: disponibilidad, entrenamiento y adaptación, adecuación al entorno.", "key": "pD25_3"},
    {"texto": "Ajustes razonables en el entorno.", "key": "pD25_4"},
    {"texto": "Redes de apoyo", "key": "pD25_5"}
],
"D2.6 En la evaluación se registran las expectativas del usuario, la familia o cuidador respecto al proceso de rehabilitación. ►": [
    {"texto": "La historia clínica incluye un ítem para el registro de las expectativas del usuario, la familia o cuidador.", "key": "pD26_1"},
    {"texto": "Se registran las expectativas del usuario con relación al proceso de rehabilitación.", "key": "pD26_2"},
    {"texto": "Se registran las expectativas de la familia o cuidador, especialmente en usuarios pediátricos, con compromiso cognitivo o dependencia severa.", "key": "pD26_3"},
    {"texto": "Se implementan estrategias de acompañamiento a usuarios y/o familias con expectativas no realistas frente al proceso de rehabilitación.", "key": "pD26_4"}
],
"D2.7 El plan de atención del usuario de rehabilitación es estructurado acorde al modelo de atención y se centra en la persona. ►": [
    {"texto": "El plan de atención de los usuarios de rehabilitación hace parte de la historia clínica.", "key": "pD27_1"},
    {"texto": "El plan de atención tiene una estructura predeterminada que incluye los objetivos o metas de rehabilitación.", "key": "pD27_2"},
    {"texto": "En el plan de atención se definen las intervenciones a realizar por los profesionales o el equipo de rehabilitación.", "key": "pD27_3"},
    {"texto": "El plan de atención es individualizado y se basa en la condición de salud, el estado funcional, las necesidades y expectativas del usuario.", "key": "pD27_4"}
],
"D2.8 El plan de atención integra el manejo médico de la condición de salud y las intervenciones para el logro de los objetivos y/o metas de rehabilitación.": [
    {"texto": "Tratamiento médico: manejo farmacológico, procedimientos, ayudas técnicas, remisión a otros servicios [cuándo es necesario].", "key": "pD28_1"},
    {"texto": "Intervención terapéutica: terapias, psicología y otros servicios, modalidades de atención, intensidad y duración.", "key": "pD28_2"},
    {"texto": "Actividades de orientación y educación pertinentes para el usuario, la familia y/o cuidador.", "key": "pD28_3"},
    {"texto": "Actividades de canalización para gestionar servicios, apoyos y/o promover la participación.", "key": "pD28_4"}
],
"D2.9 Los profesionales definen con el usuario, la familia y/o cuidador, objetivos y/o metas de rehabilitación que se orientan a optimizar el funcionamiento. ►": [
    {"texto": "Los profesionales definen los objetivos y/o metas de rehabilitación.", "key": "pD29_1"},
    {"texto": "Los objetivos y/o metas de rehabilitación están orientadas a mejorar y/o potenciar la autonomía e independencia del usuario.", "key": "pD29_2"},
    {"texto": "Los profesionales involucran al usuario, la familia y/o cuidador en la definición de objetivos y/o metas de rehabilitación.", "key": "pD29_3"},
    {"texto": "Los objetivos y/o metas de rehabilitación se definen de manera concertada entre el equipo multidisciplinario,** el usuario, la familia y/o cuidador.", "key": "pD29_4"}
],
"D2.10 Se establecen objetivos y/o metas de rehabilitación medibles y alcanzables en un tiempo determinado. ►": [
    {"texto": "Los objetivos y/o metas de rehabilitación se basan en actividades funcionales alcanzables y relevantes para el usuario y/o la familia.", "key": "pD210_1"},
    {"texto": "Los objetivos y/o metas de rehabilitación son medibles y permiten determinar objetivamente los logros o resultados.", "key": "pD210_2"},
    {"texto": "Los objetivos y/o metas de rehabilitación se establecen en un plazo o tiempo para alcanzar los logros o resultados esperados.", "key": "pD210_3"},
    {"texto": "Los objetivos y/o metas de rehabilitacion consideran la secuencialidad y progresión del proceso de rehabilitación.", "key": "pD210_4"}
],
"D2.11 La intervención en rehabilitación del usuario se orienta a mejorar su autonomía e independencia. ►": [
    {"texto": "En la historia clínica de los usuarios de rehabilitación:", "key": "pD211_1"},
    {"texto": "Se registran intervenciones de rehabilitación orientadas a mejorar la realización de AVD y el desempeño del usuario en su entorno.", "key": "pD211_2"},
    {"texto": "Las intervenciones de rehabilitación registradas son coherentes con los objetivos y/o metas de rehabilitación.", "key": "pD211_3"},
    {"texto": "Los profesionales de rehabilitación registran la implementación de enfoques terapéuticos e intervenciones con respaldo en la evidencia.", "key": "pD211_4"},
    {"texto": "La intervención de los usuarios es realizada por equipo multidisciplinario** e incorpora dispositivos de asistencia y tecnología.", "key": "pD211_5"}
],
"D2.12 Durante la intervención del usuario los profesionales de rehabilitación realizan acciones conjuntas, coordinadas e interdependientes.": [
    {"texto": "Dos o más profesionales de rehabilitación de la institución intervienen al usuario de manera independiente con objetivos comunes.", "key": "pD212_1"},
    {"texto": "Los profesionales de rehabilitación realizan intervenciones disciplinares con objetivos comunes y disponen de espacios para coordinar la atención.", "key": "pD212_2"},
    {"texto": "Los profesionales de rehabilitación realizan intervenciones coordinadas y complementarias con objetivos comunes, y comparten el espacio de atención.", "key": "pD212_3"},
    {"texto": "El equipo multidisciplinario** dispone espacios formales para la evaluación, seguimiento y toma de decisiones frente a la atención de usuarios de mayor complejidad.", "key": "pD212_4"}
],
"D2.13 En el proceso de rehabilitación se implementan acciones con enfoque diferencial.": [
    {"texto": "La infraestructura institucional dispone de ajustes razonables para facilitar el acceso y autonomía de los usuarios.", "key": "pD213_1"},
    {"texto": "En los servicios de rehabilitación se cuenta con ambientes y atención diferencial para los usuarios.", "key": "pD213_2"},
    {"texto": "En los servicios de rehabilitación se cuenta con dispositivos y tecnología para facilitar la comunicación y participación de los usuarios.", "key": "pD213_3"},
    {"texto": "En los servicios de rehabilitación se implementan acciones con enfoque diferencial para los usuarios.", "key": "pD213_4"}
],
"D2.14 Durante el proceso de rehabilitación se realizan acciones para involucrar activamente al usuario, su familia y/o cuidador en el cumplimiento de los objetivos de rehabilitación.": [
    {"texto": "Durante la atención los profesionales de rehabilitación brindan información al usuario y la familia sobre su rol en el proceso de rehabilitación.", "key": "pD214_1"},
    {"texto": "Los profesionales de rehabilitación entregan al usuario, la familia y/o cuidador planes de ejercicios y/o actividades para realizar en casa o en otros entornos.", "key": "pD214_2"},
    {"texto": "En los servicios de rehabilitación se cuenta con recursos audiovisuales para informar y brindar contenido educativo a los usuarios, la familia y/o cuidador.", "key": "pD214_3"},
    {"texto": "En los servicios de rehabilitación se cuenta con dispositivos y recursos tecnológicos para el seguimiento o monitoreo remoto de los usuarios.", "key": "pD214_4"}
],
"D2.15 En la etapa o fase de intervención se realiza reevaluación del usuario para identificar los logros y de ser necesario, realizar ajustes al plan de atención. ►": [
    {"texto": "Los profesionales de rehabilitación realizan monitoreo de signos y/o síntomas relacionados con la condición del usuario.", "key": "pD215_1"},
    {"texto": "Se identifican cambios o logros en el estado funcional del paciente.", "key": "pD215_2"},
    {"texto": "Se verifican los objetivos de rehabilitación y se hacen ajustes a la intervención [cuando sea necesario].", "key": "pD215_3"},
    {"texto": "Se tiene preestablecido el tiempo de reevaluación periódica haciendo uso de pruebas estandarizadas o instrumentos.", "key": "pD215_4"}
],
"D2.16 El proceso de rehabilitación incluye acciones planificadas de orientación y canalización del usuario y su familia a otras instituciones o sectores que pueden contribuir a su participación.": [
    {"texto": "Los profesionales de rehabilitación orientan al usuario, la familia y/o cuidador sobre servicios o programas disponibles que contribuyen a la participación.", "key": "pD216_1"},
    {"texto": "Los profesionales derivan al usuario, la familia y/o cuidador a servicios o programas específicos para promover la participación del usuario.", "key": "pD216_2"},
    {"texto": "Los servicios de rehabilitación cuentan con estrategias para la canalización del usuario y su familia a instituciones o servicios que contribuyen a la participación.", "key": "pD216_3"},
    {"texto": "Los servicios de rehabilitación realizan trabajo en red con otras instituciones y servicios para incrementar las oportunidades de participación de los usuarios.", "key": "pD216_4"}
],
"D2.17 Se realiza evaluación final del usuario para determinar los logros, y definir el egreso o la pertinencia de continuar con el proceso de rehabilitación. ►": [
    {"texto": "El proceso de rehabilitación de los usuarios termina con la evaluación final.", "key": "pD217_1"},
    {"texto": "Se identifican los logros según los objetivos y/o metas de rehabilitación.", "key": "pD217_2"},
    {"texto": "Con los resultados de la evaluación final, se define el egreso del usuario o la continuidad del proceso de rehabilitación.", "key": "pD217_3"},
    {"texto": "Se entregan indicaciones y recomendaciones al usuario: estrategias de mantenimiento, control médico, participación.", "key": "pD217_4"}
],
"D2.18 Se implementan acciones específicas para la atención y el egreso de usuarios de rehabilitación de larga permanencia con pobre pronostico funcional.": [
    {"texto": "En los servicios de rehabilitación se identifican los usuarios de larga permanencia.", "key": "pD218_1"},
    {"texto": "La institución cuenta con criterios definidos para la admisión y reingreso de los usuarios de larga permanencia.", "key": "pD218_2"},
    {"texto": "En los servicios de rehabilitación se implementan medidas específicas para la atención de los usuarios de larga permanencia.", "key": "pD218_3"},
    {"texto": "La institución establece acuerdos formales con las aseguradoras para la atención de los usuarios de larga permanencia.", "key": "pD218_4"}
]
    },
    "3. RESULTADOS DEL PROCESO DE REHABILITACIÓN": {
        "D3.1 Se utilizan instrumentos adaptados y validados en el contexto nacional para evaluar los resultados del proceso de rehabilitación.": [
    {"texto": "Los instrumentos de evaluación de los usuarios de rehabilitación se encuentran validados. [priorizar instrumentos de evaluación funcional o condiciones más frecuentes]", "key": "pD216_1"},
    {"texto": "Los requisitos o condiciones de aplicación de los instrumentos [Ej., tiempo] son viables para su uso en los servicios de rehabilitación.", "key": "pD216_2"},
    {"texto": "El uso de instrumentos de evaluación cumple con las normas de licenciamiento o derechos de autor.", "key": "pD216_3"},
    {"texto": "Los profesionales de rehabilitación reciben capacitación o entrenamiento en el uso de instrumentos de evaluación. ", "key": "pD216_4"}
],
"D3.2 Se miden y analizan los resultados del estado funcional de los usuarios posterior al proceso de rehabilitación. ": [
    {"texto": "El estado funcional de los usuarios se evalúa al inicio y al final del proceso de rehabilitación. ", "key": "pD217_1"},
    {"texto": "En la evaluación inicial y final del estado funcional de los usuarios se usa un método o instrumento validado.", "key": "pD217_2"},
    {"texto": "Los resultados de la evaluación inicial y final del estado funcional de los usuarios se consolidan y analizan.", "key": "pD217_3"},
    {"texto": "La institución define indicadores de resultado relacionados con el estado funcional de los usuarios de rehabilitación.", "key": "pD217_4"}
],
"D3.3 Se mide la satisfacción de los usuarios con la atención recibida en los servicios de rehabilitación.": [
    {"texto": "Al finalizar el proceso de rehabilitación se mide la satisfacción de los usuarios.", "key": "pD218_1"},
    {"texto": "La medición de la satisfacción de los usuarios es estandarizada y los resultados se expresan en datos numéricos y/o categorías ordinales. ", "key": "pD218_2"},
    {"texto": "La evaluación de la satisfacción verifica la percepción de los usuarios sobre la oportunidad, seguridad, pertinencia y resultados de la atención.", "key": "pD218_3"},
    {"texto": "Los resultados de la satisfacción de los usuarios se consolidan, analizan y los resultados dan lugar a acciones de mejora.", "key": "pD218_4"}
]
    }
}


# --- Navegación ---
main_dim_keys = list(dimensiones.keys())
current_main_dim = main_dim_keys[st.session_state.current_main_dim]
sub_dim_keys = list(dimensiones[current_main_dim].keys())
current_sub_dim = sub_dim_keys[st.session_state.current_sub_dim]

# --- Mostrar progreso ---
total_main_dims = len(main_dim_keys)
total_sub_dims = len(sub_dim_keys)
current_progress = (st.session_state.current_main_dim + (st.session_state.current_sub_dim + 1)/total_sub_dims) / total_main_dims

st.markdown(f"""
<div class="progress-container">
    <strong></strong>
    Dimensión {st.session_state.current_main_dim + 1}/{total_main_dims} •
    Pregunta {st.session_state.current_sub_dim + 1}/{total_sub_dims}
</div>
""", unsafe_allow_html=True)
st.progress(current_progress)



# --- Contenido principal ---
st.markdown(f'<div class="section"><h2 class="section-title">{current_main_dim}</h2></div>', unsafe_allow_html=True)
st.markdown(f'<div class="subsection-title">{current_sub_dim}</div>', unsafe_allow_html=True)

# Mostrar todas las preguntas de la subdimensión actual
preguntas = dimensiones[current_main_dim][current_sub_dim]
for pregunta in preguntas:
    if pregunta["key"] not in st.session_state:
        st.session_state[pregunta["key"]] = "" if pregunta.get("tipo") == "texto" else opciones[0]

    col1, col2= st.columns([3, 1])
    with col1:
        st.markdown(f'<div class="question">{pregunta["texto"]}</div>', unsafe_allow_html=True)
    with col2:
        st.session_state[pregunta["key"]] = st.selectbox(
            "",
            options=opciones,
            format_func=lambda x: x[0],
            key=pregunta["key"]+"_select",
            label_visibility="collapsed"
        )


# Primero creamos un contenedor principal
with st.container():
    # Dividimos en dos columnas principales
    col_calif, col_obs = st.columns([1, 5])

    with col_calif:
        # Calificación de la subdimensión
        respuestas = [st.session_state[p["key"]] for p in preguntas]
        calif_text, clase, calif_num = determinar_calificacion(respuestas)
        st.markdown(
            f'<div class="dimension-rating">Calificación {current_sub_dim.split()[0]}: '
            f'<span class="rating-tag {clase}">{calif_text}</span></div>',
            unsafe_allow_html=True
        )

    with col_obs:
        # Observaciones (ajustado para mejor visualización)
        obs_key = f"obs_{current_sub_dim.replace(' ', '_')}"
        st.markdown("**Observaciones**", help="Comentarios adicionales sobre esta dimensión")
        st.session_state[obs_key] = st.text_area(
            "",
            value=st.session_state.get(obs_key, ""),
            key=f"{obs_key}_text",
            label_visibility="collapsed",
            height=70
        )

# Luego mostramos la tabla de preguntas (tu código existente)
# ... (aquí iría tu implementación actual de la tabla de preguntas)


# --- Navegación ---
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    # Botón Anterior
    if st.session_state.current_sub_dim > 0:
        if st.button("⏮ pregunta anterior"):
            st.session_state.current_sub_dim -= 1
            st.rerun()
    elif st.session_state.current_main_dim > 0:
        if st.button("⏮ Dimensión anterior"):
            st.session_state.current_main_dim -= 1
            st.session_state.current_sub_dim = len(dimensiones[main_dim_keys[st.session_state.current_main_dim]]) - 1
            st.rerun()

with col2:
    # Botón Siguiente
    if st.session_state.current_sub_dim < len(sub_dim_keys) - 1:
        if st.button("⏭ Siguiente pregunta"):
            st.session_state.current_sub_dim += 1
            st.rerun()
    elif st.session_state.current_main_dim < len(main_dim_keys) - 1:
        if st.button("⏭ Siguiente dimensión"):
            st.session_state.current_main_dim += 1
            st.session_state.current_sub_dim = 0
            st.rerun()
    else:
        if st.button("💾 Guardar evaluación completa"):
            st.balloons()
            st.success("Evaluación completada y guardada")

            # Generar reporte (ejemplo)
            reporte = {}
            for dim, subdims in dimensiones.items():
                reporte[dim] = {}
                for subdim, preguntas in subdims.items():
                    respuestas = [st.session_state[p["key"]] for p in preguntas]
                    calif_text, clase, calif_num = determinar_calificacion(respuestas)
                    reporte[dim][subdim] = {
                        "puntaje": calif_num,
                        "calificacion": calif_text,
                        "respuestas": [r[1] for r in respuestas]
                    }

            st.json(reporte)  # Mostrar resultados (puedes guardar en DB después)

st.markdown('</div>', unsafe_allow_html=True)





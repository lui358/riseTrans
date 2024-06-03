from lxml import etree
from googletrans import Translator

# Cargar y analizar el archivo XLIFF
xliff_file_path = '..archivos/Plan-docente-plataformas-educativas.xlf'
tree = etree.parse(xliff_file_path)
root = tree.getroot()

# Extraer los namespaces relevantes
namespaces = {'xliff': 'urn:oasis:names:tc:xliff:document:1.2'}

# Inicializar el traductor
translator = Translator()

# Función para traducir texto al portugués
def translate_to_portuguese(text):
    try:
        translated = translator.translate(text, src='es', dest='pt')
        return translated.text
    except Exception as e:
        return str(e)

# Iterar sobre las unidades de traducción y traducir el texto fuente
for trans_unit in root.xpath('//xliff:trans-unit', namespaces=namespaces):
    source_text = trans_unit.find('xliff:source', namespaces).text
    if source_text:
        translated_text = translate_to_portuguese(source_text)
        target_elem = trans_unit.find('xliff:target', namespaces)
        if target_elem is None:
            target_elem = etree.SubElement(trans_unit, 'target')
        target_elem.text = translated_text

# Guardar el archivo XLIFF traducido
translated_xliff_file_path = '..archivos/traducido/Plan-docente-plataformas-educativas-traducido.xlf'
tree.write(translated_xliff_file_path, encoding='utf-8', xml_declaration=True, pretty_print=True)

print("Traducción completada. Archivo guardado en:", translated_xliff_file_path)

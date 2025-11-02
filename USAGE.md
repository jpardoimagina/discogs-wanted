# Guía de Uso - Discogs Seller Finder

## Configuración Inicial

### 1. Obtener Token de Discogs

1. Ve a [Discogs Settings - Developers](https://www.discogs.com/settings/developers)
2. En la sección "Personal access tokens", genera un nuevo token
3. Copia el token (lo necesitarás en el siguiente paso)

### 2. Configurar Credenciales

```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Edita el archivo .env con tu editor favorito
nano .env  # o vim .env, code .env, etc.
```

Contenido del archivo `.env`:
```
DISCOGS_USER_TOKEN=tu_token_aquí
DISCOGS_USERNAME=tu_usuario_aquí
```

### 3. Instalar Dependencias

```bash
# Crea un entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt
```

## Uso Básico

### Ejecutar el Programa

```bash
python discogs_seller_finder.py
```

### Flujo del Programa

1. **Carga de Wantlist**: El programa obtiene automáticamente tu wantlist de Discogs
2. **Selección de Items**: Si tienes muchos items, te preguntará cuántos procesar
3. **Búsqueda**: Para cada item, busca disponibilidad en el marketplace
4. **Resultados**: Muestra una lista de items disponibles con enlaces directos

## Ejemplo de Salida

```
🎵 Discogs Seller Finder
================================================================================
📋 Obteniendo wantlist de mi_usuario...
✓ Encontrados 25 items en la wantlist

¿Procesar todos los 25 items? (s/n): n
¿Cuántos items procesar? (1-25): 10

🔍 Buscando vendedores para 10 items...
  [1/10] Pink Floyd - The Dark Side of the Moon
    ✓ 150 copias disponibles
  [2/10] The Beatles - Abbey Road
    ✓ 89 copias disponibles
  [3/10] Led Zeppelin - Led Zeppelin IV
    ✓ 120 copias disponibles
  ...

================================================================================
📊 RESULTADOS: Vendedores con múltiples items de tu wantlist
================================================================================

✓ Encontrados 8 items disponibles en el marketplace:

ℹ️  Para optimizar envíos, visita los siguientes enlaces en Discogs
   y busca vendedores que tengan múltiples items:

• Pink Floyd - The Dark Side of the Moon
  Copias disponibles: 150 | Precio mínimo: EUR 15.00
  URL: https://www.discogs.com/release/123456

• The Beatles - Abbey Road
  Copias disponibles: 89 | Precio mínimo: EUR 20.00
  URL: https://www.discogs.com/release/789012
  
...

================================================================================
✅ Proceso completado
```

## Cómo Optimizar Envíos

Una vez que tengas los resultados:

1. **Visita cada enlace** proporcionado en los resultados
2. En cada página, haz clic en "**For Sale**" o "**Marketplace**"
3. **Anota los vendedores** que aparecen en cada item
4. **Identifica vendedores comunes** que tengan varios de tus items
5. **Contacta al vendedor** para negociar un envío combinado

### Ejemplo de Estrategia

Si encuentras que el vendedor "VinylCollector123" tiene 5 items de tu wantlist:

1. Añade los 5 items a tu carrito
2. Antes de finalizar la compra, envía un mensaje al vendedor
3. Pregunta si puede combinar el envío para reducir costes
4. Espera confirmación antes de pagar

## Consejos y Mejores Prácticas

### Para Obtener Mejores Resultados

- **Wantlist Actualizada**: Mantén tu wantlist actualizada en Discogs
- **Procesa Todos los Items**: Si es posible, procesa toda tu wantlist para no perderte oportunidades
- **Guarda los Resultados**: Copia la salida a un archivo para futuras referencias
- **Revisa Regularmente**: Ejecuta el programa cada semana para ver nuevas disponibilidades

### Limitaciones a Tener en Cuenta

- **API Rate Limits**: Discogs limita el número de requests por minuto
- **Información de Vendedores**: Por restricciones de la API, debes visitar los enlaces para ver vendedores específicos
- **Precios Variables**: Los precios pueden cambiar entre la búsqueda y tu visita

## Solución de Problemas

### Error: "Debes configurar DISCOGS_USER_TOKEN"

**Solución**: Verifica que hayas creado el archivo `.env` y que contenga las variables correctas.

```bash
# Verifica que el archivo existe
ls -la .env

# Verifica el contenido
cat .env
```

### Error: "No se pudo acceder a la wantlist"

**Causas posibles**:
- Token inválido o expirado
- Usuario incorrecto
- Problemas de conexión a internet

**Solución**: 
1. Verifica tus credenciales en Discogs
2. Genera un nuevo token si es necesario
3. Verifica tu conexión a internet

### La búsqueda es muy lenta

**Solución**: 
- Reduce el número de items a procesar
- La API de Discogs tiene límites de velocidad, el programa respeta estos límites

## Ejecutar Tests

Para verificar que todo funciona correctamente:

```bash
python test_seller_finder.py
```

Deberías ver:
```
✅ Todos los tests pasaron exitosamente!
```

## Próximos Pasos

Después de usar el programa:

1. Visita los enlaces proporcionados
2. Identifica vendedores comunes
3. Contacta vendedores para negociar envíos combinados
4. Ahorra en costes de envío! 💰

## Soporte

Si encuentras problemas o tienes sugerencias:
- Abre un issue en GitHub
- Contacta al autor: [jpardoimagina](https://github.com/jpardoimagina)

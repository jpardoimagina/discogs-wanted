# Discogs Seller Finder

🎵 Herramienta para encontrar vendedores en Discogs que tengan múltiples items de tu wantlist, optimizando así los costes de envío al consolidar pedidos con un solo vendedor.

## Características

- 📋 Obtiene automáticamente tu wantlist de Discogs
- 🔍 Busca vendedores que tienen múltiples items de tu lista
- 📊 Muestra resultados ordenados por número de items disponibles
- 💰 Ayuda a optimizar costes de envío consolidando pedidos

## Requisitos

- Python 3.7+
- Cuenta de Discogs
- Token de API de Discogs

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/jpardoimagina/discogs-wanted.git
cd discogs-wanted
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura tus credenciales:
```bash
cp .env.example .env
```

4. Edita el archivo `.env` con tus credenciales:
   - Obtén tu token en: https://www.discogs.com/settings/developers
   - Añade tu token y nombre de usuario al archivo `.env`

## Uso

Ejecuta el script principal:

```bash
python discogs_seller_finder.py
```

El programa:
1. Se conectará a la API de Discogs
2. Obtendrá tu wantlist
3. Buscará items disponibles en el marketplace
4. Mostrará una lista de releases disponibles con enlaces directos

### Opciones

- Si tienes muchos items en tu wantlist, el programa te preguntará cuántos procesar
- Puedes modificar el número mínimo de items por vendedor en el código

## Ejemplo de salida

```
🎵 Discogs Seller Finder
================================================================================
📋 Obteniendo wantlist de usuario...
✓ Encontrados 25 items en la wantlist

🔍 Buscando vendedores para 25 items...
  [1/25] Pink Floyd - The Dark Side of the Moon
    ✓ 150 copias disponibles
  [2/25] The Beatles - Abbey Road
    ✓ 89 copias disponibles
  ...

================================================================================
📊 RESULTADOS: Vendedores con múltiples items de tu wantlist
================================================================================

✓ Encontrados 20 items disponibles en el marketplace:

ℹ️  Para optimizar envíos, visita los siguientes enlaces en Discogs
   y busca vendedores que tengan múltiples items:

• Pink Floyd - The Dark Side of the Moon
  Copias disponibles: 150 | Precio mínimo: €15.00
  URL: https://www.discogs.com/release/123456
...
```

## Limitaciones

Debido a las restricciones de la API de Discogs, el programa muestra los items disponibles con enlaces directos. Para encontrar vendedores específicos con múltiples items:

1. Visita los enlaces proporcionados
2. En la página de cada release, ve a la sección "Marketplace"
3. Busca vendedores que aparezcan en múltiples items de tu lista

## Contribuir

Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

- **jpardoimagina** - [GitHub](https://github.com/jpardoimagina)

## Agradecimientos

- API de Discogs por proporcionar acceso a los datos
- Comunidad de Discogs por mantener la base de datos más completa de música
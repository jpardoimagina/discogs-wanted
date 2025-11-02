#!/usr/bin/env python3
"""
Script de demostración del Discogs Seller Finder
Muestra un ejemplo del flujo de trabajo sin necesidad de credenciales reales
"""

from collections import defaultdict


def demo_workflow():
    """Demuestra el flujo completo del programa con datos de ejemplo."""
    
    print("🎵 DEMOSTRACIÓN: Discogs Seller Finder")
    print("="*80)
    print("\nEste es un ejemplo de cómo funciona el programa con datos simulados.\n")
    
    # Paso 1: Simular wantlist
    print("PASO 1: Obtener Wantlist")
    print("-"*80)
    mock_wantlist = [
        {"artist": "Pink Floyd", "title": "The Dark Side of the Moon", "id": 123456},
        {"artist": "The Beatles", "title": "Abbey Road", "id": 789012},
        {"artist": "Led Zeppelin", "title": "Led Zeppelin IV", "id": 345678},
        {"artist": "Queen", "title": "A Night at the Opera", "id": 234567},
        {"artist": "David Bowie", "title": "The Rise and Fall of Ziggy Stardust", "id": 456789},
        {"artist": "The Rolling Stones", "title": "Sticky Fingers", "id": 567890},
        {"artist": "Jimi Hendrix", "title": "Are You Experienced", "id": 678901},
        {"artist": "The Doors", "title": "The Doors", "id": 890123},
    ]
    
    print(f"✓ Wantlist obtenida: {len(mock_wantlist)} items")
    for i, item in enumerate(mock_wantlist[:3], 1):
        print(f"  {i}. {item['artist']} - {item['title']}")
    print(f"  ... y {len(mock_wantlist) - 3} más")
    
    # Paso 2: Simular búsqueda de vendedores
    print("\n\nPASO 2: Buscar Disponibilidad en Marketplace")
    print("-"*80)
    print("Buscando vendedores para cada item...\n")
    
    # Simular datos de marketplace
    marketplace_data = {
        123456: {"num_for_sale": 150, "lowest_price": "EUR 15.00"},
        789012: {"num_for_sale": 89, "lowest_price": "EUR 20.00"},
        345678: {"num_for_sale": 120, "lowest_price": "EUR 18.50"},
        234567: {"num_for_sale": 75, "lowest_price": "EUR 22.00"},
        456789: {"num_for_sale": 95, "lowest_price": "EUR 17.50"},
        567890: {"num_for_sale": 110, "lowest_price": "EUR 19.00"},
        678901: {"num_for_sale": 85, "lowest_price": "EUR 25.00"},
        890123: {"num_for_sale": 0, "lowest_price": "N/A"},
    }
    
    available_releases = []
    for item in mock_wantlist:
        marketplace = marketplace_data.get(item['id'], {"num_for_sale": 0, "lowest_price": "N/A"})
        status = "✓" if marketplace['num_for_sale'] > 0 else "✗"
        print(f"{status} {item['artist']} - {item['title']}")
        
        if marketplace['num_for_sale'] > 0:
            print(f"  Disponibles: {marketplace['num_for_sale']} | Precio mínimo: {marketplace['lowest_price']}")
            available_releases.append({
                'artist': item['artist'],
                'title': item['title'],
                'release_id': item['id'],
                'url': f"https://www.discogs.com/release/{item['id']}",
                'num_for_sale': marketplace['num_for_sale'],
                'lowest_price': marketplace['lowest_price']
            })
        else:
            print(f"  No disponible en este momento")
    
    # Paso 3: Mostrar resultados
    print("\n\nPASO 3: Resultados - Items Disponibles")
    print("="*80)
    print(f"\n✓ Encontrados {len(available_releases)} items disponibles en el marketplace:")
    print("\nℹ️  Para optimizar envíos, visita los siguientes enlaces en Discogs")
    print("   y busca vendedores que tengan múltiples items:\n")
    
    for item in available_releases:
        print(f"• {item['artist']} - {item['title']}")
        print(f"  Copias disponibles: {item['num_for_sale']} | Precio mínimo: {item['lowest_price']}")
        print(f"  URL: {item['url']}\n")
    
    # Paso 4: Estrategia recomendada
    print("\nPASO 4: Estrategia para Optimizar Envíos")
    print("-"*80)
    print("""
1. Visita cada uno de los enlaces anteriores
2. En cada página, busca la sección "For Sale" o "Marketplace"
3. Anota los nombres de vendedores que aparecen en varios items
4. Contacta a esos vendedores para negociar envío combinado

EJEMPLO:
Si encuentras que el vendedor "VinylCollector" tiene:
  - Pink Floyd - The Dark Side of the Moon (EUR 15.00)
  - Led Zeppelin - Led Zeppelin IV (EUR 18.50)
  - David Bowie - Ziggy Stardust (EUR 17.50)
  
Puedes contactarlo y negociar un envío único en lugar de 3 envíos separados,
ahorrando significativamente en costes de envío! 💰
    """)
    
    print("="*80)
    print("✅ Demostración completada\n")
    print("Para usar con tus datos reales:")
    print("  1. Configura tu .env con tus credenciales de Discogs")
    print("  2. Ejecuta: python discogs_seller_finder.py")


def demo_seller_aggregation():
    """Demuestra cómo se agregarían vendedores si tuviéramos acceso completo a la API."""
    
    print("\n\n🔍 DEMO ADICIONAL: Agregación de Vendedores (Concepto)")
    print("="*80)
    print("\nSi la API proporcionara acceso directo a los vendedores,")
    print("el programa podría mostrar algo así:\n")
    
    # Simular datos de vendedores
    sellers_items = {
        "VinylCollector123": [
            {"artist": "Pink Floyd", "title": "Dark Side of the Moon", "price": "EUR 15.00"},
            {"artist": "Led Zeppelin", "title": "Led Zeppelin IV", "price": "EUR 18.50"},
            {"artist": "David Bowie", "title": "Ziggy Stardust", "price": "EUR 17.50"},
        ],
        "RecordStore_UK": [
            {"artist": "The Beatles", "title": "Abbey Road", "price": "EUR 20.00"},
            {"artist": "The Rolling Stones", "title": "Sticky Fingers", "price": "EUR 19.00"},
        ],
        "MusicLover99": [
            {"artist": "Queen", "title": "A Night at the Opera", "price": "EUR 22.00"},
        ]
    }
    
    # Filtrar vendedores con 2+ items
    qualified_sellers = {k: v for k, v in sellers_items.items() if len(v) >= 2}
    
    # Ordenar por número de items
    sorted_sellers = sorted(qualified_sellers.items(), key=lambda x: len(x[1]), reverse=True)
    
    print(f"✓ Encontrados {len(sorted_sellers)} vendedores con 2+ items:\n")
    
    for seller, items in sorted_sellers:
        print(f"🏪 Vendedor: {seller}")
        print(f"   📦 {len(items)} items disponibles:")
        
        total_price = 0
        for item in items:
            price_str = item['price'].replace('EUR ', '').strip()
            try:
                total_price += float(price_str)
            except:
                pass
            print(f"      • {item['artist']} - {item['title']}")
            print(f"        Precio: {item['price']}")
        
        if total_price > 0:
            print(f"   💰 Total items: EUR {total_price:.2f}")
            print(f"   💡 Ahorro estimado en envío: EUR 10-20 (envío combinado vs. envíos separados)")
        print()


if __name__ == "__main__":
    demo_workflow()
    demo_seller_aggregation()
    
    print("\n" + "="*80)
    print("📚 Para más información, consulta:")
    print("  • README.md - Información general del proyecto")
    print("  • USAGE.md - Guía detallada de uso")
    print("  • discogs_seller_finder.py - Código fuente principal")
    print("="*80)

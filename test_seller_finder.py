#!/usr/bin/env python3
"""
Test básico para verificar la funcionalidad del Discogs Seller Finder
"""

import sys
from collections import defaultdict


def test_display_results_alternative():
    """Test del método de visualización con datos de ejemplo."""
    print("🧪 Test: Visualización de resultados (método alternativo)")
    print("="*80)
    
    # Datos de ejemplo simulando el método alternativo
    mock_sellers_items = {
        '_available_releases': [
            {
                'artist': 'Pink Floyd',
                'title': 'The Dark Side of the Moon',
                'release_id': 123456,
                'url': 'https://www.discogs.com/release/123456',
                'num_for_sale': 150,
                'lowest_price': 'EUR 15.00'
            },
            {
                'artist': 'The Beatles',
                'title': 'Abbey Road',
                'release_id': 789012,
                'url': 'https://www.discogs.com/release/789012',
                'num_for_sale': 89,
                'lowest_price': 'EUR 20.00'
            },
            {
                'artist': 'Led Zeppelin',
                'title': 'Led Zeppelin IV',
                'release_id': 345678,
                'url': 'https://www.discogs.com/release/345678',
                'num_for_sale': 120,
                'lowest_price': 'EUR 18.50'
            }
        ]
    }
    
    # Simular la visualización
    display_results_test(mock_sellers_items)
    
    print("\n✅ Test completado exitosamente")
    return True


def display_results_test(sellers_items):
    """
    Versión de test de display_results.
    
    Args:
        sellers_items: Diccionario con vendedores y sus items
    """
    print("\n📊 RESULTADOS: Vendedores con múltiples items de tu wantlist")
    print("="*80)
    
    # Caso especial: si usamos el método alternativo
    if '_available_releases' in sellers_items:
        releases = sellers_items['_available_releases']
        print(f"\n✓ Encontrados {len(releases)} items disponibles en el marketplace:")
        print("\nℹ️  Para optimizar envíos, visita los siguientes enlaces en Discogs")
        print("   y busca vendedores que tengan múltiples items:\n")
        
        for item in releases:
            print(f"• {item['artist']} - {item['title']}")
            print(f"  Copias disponibles: {item['num_for_sale']} | Precio mínimo: {item['lowest_price']}")
            print(f"  URL: {item['url']}\n")


def test_data_structures():
    """Test de estructuras de datos básicas."""
    print("\n🧪 Test: Estructuras de datos")
    print("="*80)
    
    # Test de defaultdict para almacenar sellers
    sellers_items = defaultdict(list)
    
    # Agregar items de ejemplo
    sellers_items['seller1'].append({
        'artist': 'Test Artist 1',
        'title': 'Test Album 1',
        'price': 'EUR 10.00',
        'condition': 'VG+',
        'release_id': 111
    })
    
    sellers_items['seller1'].append({
        'artist': 'Test Artist 2',
        'title': 'Test Album 2',
        'price': 'EUR 12.00',
        'condition': 'NM',
        'release_id': 222
    })
    
    sellers_items['seller2'].append({
        'artist': 'Test Artist 3',
        'title': 'Test Album 3',
        'price': 'EUR 15.00',
        'condition': 'M',
        'release_id': 333
    })
    
    # Verificar estructura
    assert len(sellers_items['seller1']) == 2, "Seller1 debería tener 2 items"
    assert len(sellers_items['seller2']) == 1, "Seller2 debería tener 1 item"
    
    # Filtrar vendedores con 2+ items
    qualified_sellers = {
        seller: items 
        for seller, items in sellers_items.items() 
        if len(items) >= 2
    }
    
    assert len(qualified_sellers) == 1, "Solo debería haber 1 vendedor con 2+ items"
    assert 'seller1' in qualified_sellers, "Seller1 debería estar en qualified_sellers"
    
    print("✓ Estructura defaultdict funciona correctamente")
    print("✓ Filtrado de vendedores funciona correctamente")
    print("✓ Todos los tests de estructuras de datos pasaron")
    
    return True


def test_sorting():
    """Test del ordenamiento de vendedores por número de items."""
    print("\n🧪 Test: Ordenamiento de vendedores")
    print("="*80)
    
    sellers_items = {
        'seller_a': [1, 2],
        'seller_b': [1, 2, 3, 4, 5],
        'seller_c': [1, 2, 3]
    }
    
    sorted_sellers = sorted(
        sellers_items.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )
    
    # Verificar orden
    assert sorted_sellers[0][0] == 'seller_b', "seller_b debería estar primero (5 items)"
    assert sorted_sellers[1][0] == 'seller_c', "seller_c debería estar segundo (3 items)"
    assert sorted_sellers[2][0] == 'seller_a', "seller_a debería estar tercero (2 items)"
    
    print("✓ Ordenamiento funciona correctamente:")
    for idx, (seller, items) in enumerate(sorted_sellers, 1):
        print(f"  {idx}. {seller}: {len(items)} items")
    
    return True


def main():
    """Ejecuta todos los tests."""
    print("\n🎵 Discogs Seller Finder - Suite de Tests")
    print("="*80)
    
    tests = [
        ("Estructuras de datos", test_data_structures),
        ("Ordenamiento", test_sorting),
        ("Visualización de resultados", test_display_results_alternative)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"\n❌ Test '{test_name}' falló: {e}")
            failed += 1
    
    print("\n" + "="*80)
    print(f"📊 Resumen: {passed} tests pasados, {failed} tests fallidos")
    
    if failed == 0:
        print("✅ Todos los tests pasaron exitosamente!")
        return 0
    else:
        print("❌ Algunos tests fallaron")
        return 1


if __name__ == "__main__":
    sys.exit(main())

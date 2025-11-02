#!/usr/bin/env python3
"""
Discogs Seller Finder
Encuentra vendedores en Discogs que tienen múltiples items de tu wantlist
para optimizar costes de envío consolidando pedidos.
"""

import os
import sys
from collections import defaultdict
from typing import Dict, List, Tuple
import discogs_client
from dotenv import load_dotenv


class DiscogsSellerFinder:
    """Clase para buscar vendedores con múltiples items de la wantlist."""
    
    def __init__(self, user_token: str, username: str):
        """
        Inicializa el cliente de Discogs.
        
        Args:
            user_token: Token de usuario de Discogs API
            username: Nombre de usuario de Discogs
        """
        self.client = discogs_client.Client(
            'DiscogsSellerFinder/1.0',
            user_token=user_token
        )
        self.username = username
        self.user = self.client.user(username)
    
    def get_wantlist(self) -> List:
        """
        Obtiene la wantlist del usuario.
        
        Returns:
            Lista de items en la wantlist
        """
        print(f"📋 Obteniendo wantlist de {self.username}...")
        wantlist = []
        try:
            for item in self.user.wantlist:
                wantlist.append(item)
            print(f"✓ Encontrados {len(wantlist)} items en la wantlist")
            return wantlist
        except Exception as e:
            print(f"✗ Error obteniendo wantlist: {e}")
            return []
    
    def find_sellers_with_items(self, wantlist: List, max_items: int = None) -> Dict[str, List[Dict]]:
        """
        Busca vendedores que tienen múltiples items de la wantlist.
        
        Args:
            wantlist: Lista de items de la wantlist
            max_items: Número máximo de items a procesar (None = todos)
            
        Returns:
            Diccionario con vendedores y sus items disponibles
        """
        sellers_items = defaultdict(list)
        
        items_to_process = wantlist[:max_items] if max_items else wantlist
        total = len(items_to_process)
        
        print(f"\n🔍 Buscando vendedores para {total} items...")
        
        for idx, want_item in enumerate(items_to_process, 1):
            try:
                release = want_item.release
                print(f"  [{idx}/{total}] Buscando: {release.artists[0].name} - {release.title}")
                
                # Obtener marketplace listings para este release
                marketplace = release.marketplace_stats
                if hasattr(marketplace, 'lowest_price'):
                    # Buscar listings en el marketplace
                    try:
                        listings = self.client.search(
                            release_id=release.id,
                            type='release'
                        )
                        
                        # Para cada listing, registrar el vendedor
                        if listings:
                            for listing in listings:
                                if hasattr(listing, 'marketplace'):
                                    seller_name = getattr(listing, 'seller', 'Unknown')
                                    price = getattr(listing, 'price', 'N/A')
                                    condition = getattr(listing, 'condition', 'N/A')
                                    
                                    sellers_items[seller_name].append({
                                        'artist': release.artists[0].name,
                                        'title': release.title,
                                        'price': price,
                                        'condition': condition,
                                        'release_id': release.id
                                    })
                    except Exception as e:
                        print(f"    ⚠ No se pudieron obtener listings: {e}")
                        
            except Exception as e:
                print(f"    ✗ Error procesando item: {e}")
                continue
        
        return sellers_items
    
    def find_sellers_alternative(self, wantlist: List, max_items: int = None) -> Dict[str, List]:
        """
        Método alternativo para buscar vendedores usando la API de marketplace.
        
        Args:
            wantlist: Lista de items de la wantlist
            max_items: Número máximo de items a procesar (None = todos)
            
        Returns:
            Diccionario con vendedores y sus items disponibles
        """
        sellers_items = defaultdict(list)
        
        items_to_process = wantlist[:max_items] if max_items else wantlist
        total = len(items_to_process)
        
        print(f"\n🔍 Buscando vendedores para {total} items...")
        
        for idx, want_item in enumerate(items_to_process, 1):
            try:
                release = want_item.release
                artist_name = release.artists[0].name if release.artists else "Unknown Artist"
                print(f"  [{idx}/{total}] {artist_name} - {release.title}")
                
                # Obtener el release completo para acceder a marketplace
                try:
                    release_obj = self.client.release(release.id)
                    
                    # Intentar obtener marketplace listings
                    if hasattr(release_obj, 'marketplace_stats'):
                        stats = release_obj.marketplace_stats
                        if hasattr(stats, 'num_for_sale') and stats.num_for_sale > 0:
                            print(f"    ✓ {stats.num_for_sale} copias disponibles")
                            
                            # Por limitaciones de la API, guardamos la info del release
                            # El usuario deberá visitar Discogs para ver los vendedores específicos
                            sellers_items['_available_releases'].append({
                                'artist': artist_name,
                                'title': release.title,
                                'release_id': release.id,
                                'url': release_obj.url if hasattr(release_obj, 'url') else f"https://www.discogs.com/release/{release.id}",
                                'num_for_sale': stats.num_for_sale,
                                'lowest_price': getattr(stats, 'lowest_price', 'N/A')
                            })
                        else:
                            print(f"    ⚠ No hay copias disponibles")
                    
                except Exception as e:
                    print(f"    ✗ Error accediendo al marketplace: {e}")
                    
            except Exception as e:
                print(f"    ✗ Error procesando item: {e}")
                continue
        
        return sellers_items
    
    def display_results(self, sellers_items: Dict[str, List], min_items: int = 2):
        """
        Muestra los resultados de vendedores con múltiples items.
        
        Args:
            sellers_items: Diccionario con vendedores y sus items
            min_items: Número mínimo de items que debe tener un vendedor
        """
        print("\n" + "="*80)
        print("📊 RESULTADOS: Vendedores con múltiples items de tu wantlist")
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
            return
        
        # Filtrar vendedores con al menos min_items items
        qualified_sellers = {
            seller: items 
            for seller, items in sellers_items.items() 
            if len(items) >= min_items
        }
        
        if not qualified_sellers:
            print(f"\n⚠ No se encontraron vendedores con {min_items}+ items de tu wantlist")
            print("\nPuedes intentar:")
            print("  1. Reducir el número mínimo de items")
            print("  2. Ampliar tu wantlist")
            print("  3. Buscar manualmente en Discogs")
            return
        
        # Ordenar vendedores por número de items (descendente)
        sorted_sellers = sorted(
            qualified_sellers.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )
        
        print(f"\n✓ Encontrados {len(sorted_sellers)} vendedores con {min_items}+ items:\n")
        
        for seller, items in sorted_sellers:
            print(f"🏪 Vendedor: {seller}")
            print(f"   📦 {len(items)} items disponibles:")
            
            for item in items:
                print(f"      • {item['artist']} - {item['title']}")
                print(f"        Precio: {item['price']} | Condición: {item['condition']}")
            print()


def main():
    """Función principal del programa."""
    # Cargar variables de entorno
    load_dotenv()
    
    user_token = os.getenv('DISCOGS_USER_TOKEN')
    username = os.getenv('DISCOGS_USERNAME')
    
    if not user_token or not username:
        print("❌ Error: Debes configurar DISCOGS_USER_TOKEN y DISCOGS_USERNAME")
        print("\n1. Copia .env.example a .env")
        print("2. Obtén tu token en: https://www.discogs.com/settings/developers")
        print("3. Edita .env con tus credenciales")
        sys.exit(1)
    
    print("🎵 Discogs Seller Finder")
    print("="*80)
    
    finder = DiscogsSellerFinder(user_token, username)
    
    # Obtener wantlist
    wantlist = finder.get_wantlist()
    
    if not wantlist:
        print("\n❌ Tu wantlist está vacía o no se pudo acceder.")
        sys.exit(1)
    
    # Preguntar cuántos items procesar
    max_items = None
    if len(wantlist) > 10:
        try:
            response = input(f"\n¿Procesar todos los {len(wantlist)} items? (s/n): ")
            if response.lower() != 's':
                max_input = input(f"¿Cuántos items procesar? (1-{len(wantlist)}): ")
                max_items = int(max_input)
        except (ValueError, KeyboardInterrupt):
            print("\nUsando los primeros 10 items...")
            max_items = 10
    
    # Buscar vendedores (usando método alternativo por limitaciones de API)
    sellers_items = finder.find_sellers_alternative(wantlist, max_items)
    
    # Mostrar resultados
    finder.display_results(sellers_items, min_items=2)
    
    print("\n" + "="*80)
    print("✅ Proceso completado")


if __name__ == "__main__":
    main()

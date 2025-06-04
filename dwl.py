#!/usr/bin/env python3
"""
Script para baixar playlists do YouTube com seleção de qualidade
Requer: pip install yt-dlp
"""

import os
import sys
import subprocess
from urllib.parse import urlparse

def verificar_yt_dlp():
    """Verifica se o yt-dlp está instalado"""
    try:
        subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def instalar_yt_dlp():
    """Instala o yt-dlp automaticamente"""
    print("yt-dlp não encontrado. Instalando...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp'], check=True)
        print("yt-dlp instalado com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("Erro ao instalar yt-dlp. Instale manualmente com: pip install yt-dlp")
        return False

def validar_url(url):
    """Valida se a URL é do YouTube"""
    parsed = urlparse(url)
    return 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc

def obter_formatos(url):
    """Obtém os formatos disponíveis para a playlist"""
    try:
        cmd = ['yt-dlp', '--list-formats', '--flat-playlist', url]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao obter formatos: {e}")
        return None

def mostrar_opcoes_qualidade():
    """Mostra as opções de qualidade disponíveis"""
    opcoes = {
        '1': ('best', 'Melhor qualidade disponível (vídeo + áudio)'),
        '2': ('worst', 'Pior qualidade disponível'),
        '3': ('bestvideo+bestaudio', 'Melhor vídeo + melhor áudio separados'),
        '4': ('720p', 'HD 720p'),
        '5': ('480p', 'SD 480p'),
        '6': ('360p', 'SD 360p'),
        '7': ('bestaudio', 'Apenas áudio (melhor qualidade)'),
        '8': ('mp3', 'Áudio em MP3'),
        '9': ('custom', 'Formato personalizado')
    }
    
    print("\n=== OPÇÕES DE QUALIDADE ===")
    for key, (format_code, desc) in opcoes.items():
        print(f"{key}. {desc}")
    
    return opcoes

def baixar_playlist(url, formato, pasta_destino="downloads"):
    """Baixa a playlist com o formato especificado"""
    # Criar pasta de destino se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Configurar comando base
    cmd = [
        'yt-dlp',
        '-o', f'{pasta_destino}/%(playlist_title)s/%(title)s.%(ext)s',
        '--ignore-errors'
    ]
    
    # Adicionar formato específico
    if formato == 'mp3':
        cmd.extend([
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', '192K'
        ])
    elif formato == 'bestaudio':
        cmd.extend(['-f', 'bestaudio'])
    else:
        cmd.extend(['-f', formato])
    
    cmd.append(url)
    
    print(f"\nIniciando download...")
    print(f"Formato: {formato}")
    print(f"Destino: {pasta_destino}")
    print("-" * 50)
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✅ Download concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro durante o download: {e}")
    except KeyboardInterrupt:
        print("\n⚠️ Download interrompido pelo usuário")

def main():
    print("🎥 YouTube Playlist Downloader")
    print("=" * 40)
    
    # Verificar se yt-dlp está instalado
    if not verificar_yt_dlp():
        if not instalar_yt_dlp():
            return
    
    # Solicitar URL da playlist
    while True:
        url = input("\n📋 Digite a URL da playlist do YouTube: ").strip()
        if not url:
            print("URL não pode estar vazia!")
            continue
        if not validar_url(url):
            print("URL inválida! Use uma URL do YouTube.")
            continue
        break
    
    # Mostrar opções de qualidade
    opcoes = mostrar_opcoes_qualidade()
    
    # Solicitar escolha do usuário
    while True:
        escolha = input("\n🎯 Escolha uma opção (1-9): ").strip()
        if escolha in opcoes:
            break
        print("Opção inválida! Escolha um número de 1 a 9.")
    
    # Processar escolha
    formato_escolhido, descricao = opcoes[escolha]
    
    if formato_escolhido == 'custom':
        formato_escolhido = input("Digite o formato personalizado (ex: 'best[height<=720]'): ").strip()
        if not formato_escolhido:
            formato_escolhido = 'best'
    
    # Solicitar pasta de destino (opcional)
    pasta = input("\n📁 Pasta de destino (Enter para 'downloads'): ").strip()
    if not pasta:
        pasta = "downloads"
    
    # Confirmar antes de baixar
    print(f"\n📋 RESUMO:")
    print(f"URL: {url}")
    print(f"Qualidade: {descricao}")
    print(f"Destino: {pasta}")
    
    confirmar = input("\n✅ Confirma o download? (s/N): ").strip().lower()
    if confirmar in ['s', 'sim', 'y', 'yes']:
        baixar_playlist(url, formato_escolhido, pasta)
    else:
        print("Download cancelado.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa encerrado pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

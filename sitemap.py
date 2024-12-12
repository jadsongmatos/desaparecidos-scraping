import os
import requests
from tenacity import retry, stop_after_attempt, wait_fixed
import requests_cache
from tqdm import tqdm
import xml.etree.ElementTree as ET
from playwright.sync_api import sync_playwright

# Configuração do cache em disco (o arquivo 'namus_cache' armazenará as respostas)
requests_cache.install_cache('namus_cache', expire_after=86400)  # 1 dia de cache

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def make_request(url, payload=None, headers=None, method="GET"):
    try:
        if method == "POST":
            response = requests.post(url, json=payload, headers=headers)
        elif method == "GET":
            response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP {response.status_code}: {response.text}")
        raise

def parse_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [url.find('ns:loc', namespace).text for url in root.findall('ns:url', namespace)]
    return urls

def save_page_with_playwright(page, url, output_dir='pages'):
    try:
        page.goto(url, timeout=60000)
        # Opcional: esperar por algum elemento específico
        # page.wait_for_selector('#elemento-especifico')
        
        rendered_html = page.content()
        
        os.makedirs(output_dir, exist_ok=True)
        filename = url.replace('https://', '').replace('http://', '').replace('/', '_').replace('?', '_') + '.html'
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(rendered_html)
        
        return filepath
    except Exception as e:
        print(f"Erro ao salvar a página {url}: {e}")
        raise

def main():
    sitemap_url = 'https://osuleomeupais.org/sitemap_index.xml'
    urls = parse_sitemap(sitemap_url)
    
    total_count = len(urls)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        with tqdm(total=total_count, desc="Baixando registros") as pbar:
            for url in urls:
                try:
                    save_page_with_playwright(page, url)
                    pbar.update(1)
                except Exception as e:
                    print(f"Falha ao processar {url}: {e}")
        
        browser.close()

if __name__ == "__main__":
    main()

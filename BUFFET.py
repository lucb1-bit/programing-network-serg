import time
import os
from playwright.sync_api import sync_playwright
from datetime import datetime

# --- DATOS ---
PERSONAS = "5"
MES_OBJETIVO = "agosto"
ARCHIVO_SESION = "sesion.json"


def comprobar_disponibilidad():
    with sync_playwright() as p:
        # headless=False es vital aquí para que veas si el bot "se pelea" con el popup
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=ARCHIVO_SESION if os.path.exists(ARCHIVO_SESION) else None)
        page = context.new_page()

        try:
            ahora = datetime.now().strftime('%H:%M:%S')
            print(f"[{ahora}] Entrando en la web...")
            page.goto("https://reservation.lesgrandsbuffets.com/contact", wait_until="networkidle")

            # --- MANEJO DEL POP-UP ---
            # Esperamos un poco a que salte el pop-up
            page.wait_for_timeout(2000)

            # Buscamos botones con textos comunes de aceptación
            # Puedes añadir más palabras a la lista si el botón dice otra cosa
            botones_popup = ["Aceptar", "He leído", "Comprendido", "Cerrar", "Accept", "Ok"]

            for texto in botones_popup:
                boton = page.get_by_role("button", name=texto, exact=False)
                if boton.is_visible():
                    print(f"Popup detectado. Haciendo click en '{texto}'...")
                    boton.click()
                    page.wait_for_timeout(1000)  # Pausa para que se quite la cortina gris
                    break

            # --- CONTINUAR CON EL FORMULARIO ---
            # Seleccionamos personas
            if page.locator("select").first.is_visible():
                page.select_option("select", label=PERSONAS)
                print(f"Personas seleccionadas: {PERSONAS}")

            # Buscamos el botón para ir al calendario
            # A veces es un botón tipo 'submit' o que dice 'Continuar'
            btn_siguiente = page.locator(
                "button:has-text('Siguiente'), button:has-text('Continuar'), input[type='submit']")
            if btn_siguiente.first.is_visible():
                btn_siguiente.first.click()
                print("Pasando al calendario...")
                page.wait_for_load_state("networkidle")

            # --- BUSCAR MES ---
            for _ in range(6):
                texto_mes = page.locator(".ui-datepicker-month").first.inner_text().lower()
                if MES_OBJETIVO in texto_mes:
                    break
                page.click(".ui-datepicker-next")
                page.wait_for_timeout(500)

            # --- REVISAR DÍAS ---
            dias = page.locator("td:not(.ui-state-disabled):not(.full) a").all_inner_texts()

            if dias:
                print(f"🚨 ¡HAY MESA! Días: {', '.join(dias)}")
                for _ in range(10): print('\a'); time.sleep(0.2)
            else:
                print(f"Sin disponibilidad en {MES_OBJETIVO}.")

            context.storage_state(path=ARCHIVO_SESION)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()


if __name__ == "__main__":
    while True:
        comprobar_disponibilidad()
        print("Próxima revisión en 30 min. No cierres la terminal.\n")
        time.sleep(1800)
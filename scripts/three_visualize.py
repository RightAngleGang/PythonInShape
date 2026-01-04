import socket
import subprocess
import time
import webbrowser
from pathlib import Path
from scripts.Space import Space


# On garde une référence au process Vite pour éviter de relancer 10 fois
_VITE_PROCESS = None


def _is_port_open(host: str, port: int, timeout: float = 0.25) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def show_data(space: Space) -> None:
    """
    Exporte le Space dans three-json-viewer/public/data.json,
    démarre Vite si nécessaire, puis ouvre le navigateur.
    """
    global _VITE_PROCESS

    # 1) Localiser le dossier three-json-viewer
    # -> ici on part du principe que ce fichier python est dans ton projet,
    # et que three-json-viewer est à la racine du repo (ajuste si besoin).
    project_root = Path.cwd()
    viewer_dir = project_root / "three-json-viewer"

    if not viewer_dir.exists():
        raise FileNotFoundError(
            f"Impossible de trouver '{viewer_dir}'. "
            "Lance le script depuis la racine du projet ou ajuste viewer_dir."
        )

    # 2) Chemin data.json (Vite: public/ est le mieux)
    public_dir = viewer_dir / "public"
    public_dir.mkdir(parents=True, exist_ok=True)

    data_path = public_dir / "data.json"

    # 3) Export JSON vers le viewer
    try:
        space.export_to_json(str(data_path))
        print(f"✅ Export JSON OK -> {data_path}")
    except Exception as e:
        raise RuntimeError(f"Erreur export vers {data_path}: {e}") from e

    # 4) Démarrer le serveur Vite si pas déjà up
    host = "127.0.0.1"
    port = 5173
    url = f"http://localhost:{port}/"

    server_up = _is_port_open(host, port)

    if not server_up:
        # Lance vite dans three-json-viewer/
        # npm run dev (non bloquant)
        print("▶️  Démarrage du serveur Vite…")
        _VITE_PROCESS = subprocess.Popen(
            ["npm", "run", "dev", "--", "--host", "127.0.0.1", "--port", str(port)],
            cwd=str(viewer_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        # Attendre que le port réponde
        deadline = time.time() + 8.0
        while time.time() < deadline:
            if _is_port_open(host, port):
                server_up = True
                break
            time.sleep(0.15)

        if not server_up:
            # Affiche quelques logs utiles
            logs = ""
            try:
                if _VITE_PROCESS and _VITE_PROCESS.stdout:
                    logs = "".join([_VITE_PROCESS.stdout.readline() for _ in range(30)])
            except Exception:
                pass
            raise RuntimeError(
                "Le serveur Vite ne démarre pas (port 5173 injoignable). "
                "Vérifie que `npm install` a été fait dans three-json-viewer/.\n"
                f"Logs:\n{logs}"
            )

        print(f"✅ Vite OK -> {url}")
    else:
        print(f"✅ Serveur déjà lancé -> {url}")

    # 5) Ouvrir le navigateur
    webbrowser.open(url)
    print("🌐 Navigateur ouvert.")

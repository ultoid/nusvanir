import subprocess
import sys

def run(cmd, desc):
    print(f"\n>>> {desc}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    return result.returncode

def main():
    print("=" * 60)
    print(" Sinkronisasi Dua Repositori: Nusvanir & Game Project")
    print("=" * 60)

    # 1. Root Worldbuilding repo
    code1 = run("git pull origin main", "Menarik repo utama (Nusvanir World Building)")

    # 2. Game Project repo
    code2 = run('git -C "Game Project/Tales of The Dark Time" pull origin main', "Menarik repo game (Tales of The Dark Time)")

    print("\n" + "=" * 60)
    if code1 == 0 and code2 == 0:
        print(" SUCCESS: Kedua repositori berhasil disinkronkan!")
    else:
        print(" WARNING: Salah satu penarikan repo mengalami kendala.")
    print("=" * 60)

if __name__ == "__main__":
    main()


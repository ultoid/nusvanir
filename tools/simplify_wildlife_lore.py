"""One-time separation of Wildlife lore Markdown from game JSON."""
import json
from bestiary_audit import BEST, ROOT, REPORT, read

# Ringkasan dari deskripsi dan habitat yang sudah ada; tanpa asal-usul baru.
LORE = {
    'Ayam_Hutan': [
        'Unggas darat liar yang hidup di hutan ringan.',
        'Berwujud unggas darat.',
        'Menjaga sarangnya.',
        'Hutan ringan.'],
    'Babi_Hutan': [
        'Fauna penghuni pinggiran hutan yang dapat membahayakan pemburu ketika terprovokasi atau terdesak.',
        None,
        'Menggali tanah untuk mencari makanan dan menanduk ketika merasa terpojok. Memanfaatkan akar, umbi, dan sisa tanaman budidaya.',
        'Pinggiran Jenggala, terutama kawasan semak dan tepi hutan.',
        'Kehadirannya dekat lahan pertanian dapat mengganggu tanaman dan aktivitas penduduk.'],
    'Bebek_Danau': [
        'Unggas penghuni danau di Mandala.',
        None,
        'Berjalan beriringan ketika mencari makan.',
        'Danau Mandala.'],
    'Beruang_Madu_Raksasa': [
        'Beruang besar yang menghuni kawasan hutan dan gua.',
        'Bertubuh besar, sesuai sebutan raksasa yang melekat pada namanya.',
        'Bersifat defensif ketika wilayahnya terganggu dan dapat menjadi agresif saat terancam.',
        'Gua-gua hutan dan kawasan hutan lebat.',
        'Kehadirannya dapat mengganggu jalur penebangan dan ekspedisi berburu.'],
    'Buaya_Rawa': [
        'Pemangsa perairan dangkal yang menghuni rawa.',
        None,
        'Dikenal memiliki pertahanan tubuh yang kokoh.',
        'Rawa Beracun.'],
    'Burung_Puyuh_Hutan': [
        'Unggas hutan yang hidup di antara semak-semak.',
        'Memiliki sayap pendek.',
        None,
        'Semak-semak hutan.'],
    'Ikan_Sisik_Perak': [
        'Ikan air tawar yang mudah ditangkap.',
        None,
        None,
        'Sungai dan danau air tawar.'],
    'Kambing_Arkananta': [
        'Kambing tangguh yang menghuni Pegunungan Arkananta.',
        None,
        'Mahir melompat di tebing-tebing pegunungan.',
        'Pegunungan Arkananta.'],
    'Kelinci_Padang': [
        'Hewan buruan pasif yang hidup di kawasan Lingkar Bumi.',
        None,
        'Lincah dan tidak dikenal sebagai hewan agresif.',
        'Lingkar Bumi.'],
    'Kura_Kura_Sungai': [
        'Kura-kura yang hidup di sekitar sungai.',
        'Memiliki tempurung yang tebal.',
        None,
        'Tepian sungai.'],
    'Macan_Kumbang': [
        'Predator nokturnal yang bergerak di tajuk dan celah pohon besar.',
        None,
        'Mengandalkan pengintaian, posisi tinggi, dan serangan mendadak ketika memburu mangsa.',
        'Pohon-pohon tinggi Jenggala.',
        'Keberadaannya menjadi ancaman bagi pemburu dan ekspedisi yang melewati hutan.'],
    'Rusa_Tanduk_Cabang': [
        'Rusa herbivora yang menghuni Hutan Astradipa.',
        'Berbadan besar dengan tanduk bercabang.',
        'Memakan tumbuhan.',
        'Hutan Astradipa.'],
    'Sapi_Perah_Mandala': [
        'Ternak penghasil susu yang menjadi bagian dari kehidupan agraris Mandala.',
        None,
        'Cenderung tenang, bergerombol, dan mudah panik ketika terancam.',
        'Padang rumput dan kawasan peternakan Mandala.',
        'Dipelihara sebagai sumber susu dan bahan pangan bagi penduduk Mandala.'],
    'Serigala_Kelabu': [
        'Pemburu berkelompok yang menghuni hutan rimbun.',
        None,
        'Lincah dan mengandalkan serangan terkoordinasi bersama kawanannya.',
        'Hutan rimbun.',
        'Kawanan yang mendekati jalur penduduk dapat mengancam ternak dan rombongan kecil.'],
    'Ular_Piton_Pohon': [
        'Ular penghuni pepohonan yang mampu melilit mangsanya.',
        None,
        'Selain lilitannya, ular ini juga dikenal dapat meracuni mangsa.',
        'Ranting-ranting besar di pepohonan.'],
}


def main():
    paths = sorted((BEST / '01_Alam_Liar').glob('*.json'))
    archive = REPORT / 'pre_lore_split_markdown.json'
    if archive.exists():
        raise SystemExit('Migration already archived; edit lore Markdown directly.')
    originals = {p.with_suffix('.md').relative_to(ROOT).as_posix(): p.with_suffix('.md').read_text(encoding='utf-8-sig') for p in paths}
    archive.write_text(json.dumps(originals, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for p in paths:
        obj = read(p)
        name = obj['title']
        lines = ['---', 'title: ' + name, 'tags:', '  - Bestiary', '---', '', '# ' + name]
        for heading, paragraph in zip(['Deskripsi', 'Bentuk', 'Ciri-ciri', 'Habitat', 'Lore'], LORE[p.stem]):
            if paragraph:
                lines += ['', '## ' + heading, '', paragraph]
        p.with_suffix('.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
        obj['v2']['presentation'] = {
            'markdown_role': 'lore_only',
            'lore_source': p.with_suffix('.md').relative_to(ROOT).as_posix(),
            'game_data_source': p.relative_to(ROOT).as_posix(),
            'previous_markdown_archive': archive.relative_to(ROOT).as_posix(),
            'sync_policy': 'Edit lore in Markdown; edit game data in JSON. Do not render game data into Markdown.',
            'worldbuilding_snapshot': 'Existing JSON prose is historical context; Markdown is authoritative for current narrative.'
        }
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Simplified {len(paths)} Wildlife Markdown files; game data preserved in JSON.')


if __name__ == '__main__':
    main()

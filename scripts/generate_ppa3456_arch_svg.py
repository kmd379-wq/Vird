#!/usr/bin/env python3
"""Generate PPA 3-6 architecture SVG files with valid UTF-8 XML."""
from pathlib import Path
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent.parent / "assets" / "figures" / "ppa3456"
OUT.mkdir(parents=True, exist_ok=True)

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def svg_root(w=900, h=720):
    root = ET.Element(f"{{{NS}}}svg", width=str(w), height=str(h), viewBox=f"0 0 {w} {h}")
    ET.SubElement(root, f"{{{NS}}}rect", width=str(w), height=str(h), fill="#ffffff")
    return root


def rect(parent, x, y, w, h, fill="#fafafa", stroke="#222222", sw="1.2", dash=None):
    attrs = {"x": str(x), "y": str(y), "width": str(w), "height": str(h),
             "fill": fill, "stroke": stroke, "stroke-width": sw}
    if dash:
        attrs["stroke-dasharray"] = dash
    return ET.SubElement(parent, f"{{{NS}}}rect", attrs)


def text_el(parent, x, y, content, size="9", bold=False, anchor=None, fill="#111111"):
    attrs = {"x": str(x), "y": str(y), "fill": fill,
             "font-family": "Arial, Helvetica, sans-serif", "font-size": size}
    if bold:
        attrs["font-weight"] = "bold"
    if anchor:
        attrs["text-anchor"] = anchor
    t = ET.SubElement(parent, f"{{{NS}}}text", attrs)
    t.text = content
    return t


def arrow_down(parent, x, y1, y2):
    ET.SubElement(parent, f"{{{NS}}}line",
                  x1=str(x), y1=str(y1), x2=str(x), y2=str(y2),
                  stroke="#222222", **{"stroke-width": "1.2"})
    ET.SubElement(parent, f"{{{NS}}}polygon",
                  points=f"{x},{y2+6} {x-4},{y2-2} {x+4},{y2-2}", fill="#222222")


def arrow_right(parent, x1, y, x2):
    ET.SubElement(parent, f"{{{NS}}}line",
                  x1=str(x1), y1=str(y), x2=str(x2), y2=str(y),
                  stroke="#222222", **{"stroke-width": "1.2"})
    ET.SubElement(parent, f"{{{NS}}}polygon",
                  points=f"{x2+6},{y} {x2-2},{y-4} {x2-2},{y+4}", fill="#222222")


def write(name, root):
    tree = ET.ElementTree(root)
    path = OUT / name
    tree.write(path, encoding="UTF-8", xml_declaration=True)
    ET.parse(path)
    data = path.read_bytes()
    bad = [b for b in data if b < 32 and b not in (9, 10, 13)]
    if bad:
        raise ValueError(f"{name}: invalid control bytes {bad[:5]}")
    print(f"OK {name} ({len(data)} bytes)")


def ppa3():
    r = svg_root()
    text_el(r, 48, 40, "PPA №3 — Архитектура модульного умного шкафа", "14", True)
    text_el(r, 48, 58, "Слияние датчиков · умное стекло · динамическое ценообразование · ручная выдача", "10", fill="#555555")

    rect(r, 350, 72, 200, 36, fill="#e8f2f2", stroke="#0f4d4d")
    text_el(r, 450, 94, "ПОЛЬЗОВАТЕЛЬ", "10", True, "middle", "#0f4d4d")
    arrow_down(r, 450, 108, 122)

    for x, t1, t2 in [(80, "105 Биокамера", "Возраст · ID"), (380, "110 Дисплей", "Цены · согласие"), (680, "Платёж", "Tap-to-pay")]:
        rect(r, x, 132, 140, 48)
        text_el(r, x + 70, 152, t1, "9", True, "middle")
        text_el(r, x + 70, 166, t2, "8", anchor="middle", fill="#555555")

    rect(r, 120, 224, 660, 100, fill="#e8f2f2", stroke="#0f4d4d", sw="1.4")
    text_el(r, 450, 244, "400 ПЕРИФЕРИЙНЫЙ КОНТРОЛЛЕР", "11", True, "middle", "#0f4d4d")
    for x, t1, t2 in [(200, "Слияние датчиков", "RFID + камера + вес"), (450, "Движок ценообразования", "sensory · space-yield"), (700, "Доступ · транзакции", "offline · кэш")]:
        text_el(r, x, 264, t1, "8", anchor="middle")
        text_el(r, x, 276, t2, "7", anchor="middle", fill="#555555")
    text_el(r, 450, 308, "Локальный кэш — работа без облака", "8", anchor="middle", fill="#555555")
    arrow_down(r, 450, 324, 344)

    for x, t1, t2 in [(48, "Шина питания", "вертикальная"), (200, "Камера", "зона перекрытия"), (352, "RFID-матрица", "LED умный край"), (504, "140 Замок", "двери"), (656, "ИБП", "аккумулятор")]:
        rect(r, x, 356, 130, 44)
        text_el(r, x + 65, 376, t1, "8", True, "middle")
        text_el(r, x + 65, 390, t2, "7", anchor="middle", fill="#555555")
    arrow_down(r, 450, 400, 420)

    rect(r, 48, 432, 804, 120, fill="none", dash="6,4")
    text_el(r, 58, 450, "200 ТОРГОВАЯ ЗОНА — сменные модули (ручная выдача)", "9", True)
    mods = ["A Толкатель", "B Крючок", "C Весовая", "D Затвор", "E/F Лоток", "G Авто-утил."]
    xs = [68, 188, 308, 428, 548, 668]
    for x, m in zip(xs, mods):
        rect(r, x, 462, 100, 52)
        text_el(r, x + 50, 484, m, "8", True, "middle")

    for x in (80, 360, 640):
        rect(r, x, 596, 180, 52)
    text_el(r, 170, 618, "Умное стекло PDLC", "9", True, "middle")
    text_el(r, 450, 618, "Умная корзина отходов", "9", True, "middle")
    text_el(r, 730, 618, "Станция индукции", "9", True, "middle")
    text_el(r, 48, 708, "PPA №3", "12", True)
    write("PPA3_ARCH_RU.svg", r)


def ppa4():
    r = svg_root()
    text_el(r, 48, 40, "PPA №4 — Токен · split-платежи · multi-tenant", "14", True)
    text_el(r, 48, 58, "QR-сессия · согласие до unlock · master–slave · offline журнал", "10", fill="#555555")

    rect(r, 48, 80, 160, 52)
    text_el(r, 128, 102, "Мобильное app", "9", True, "middle")
    text_el(r, 128, 116, "QR · токен KYC", "8", anchor="middle", fill="#555555")
    rect(r, 292, 80, 120, 40)
    text_el(r, 352, 104, "QR-сканер", "9", True, "middle")
    arrow_right(r, 208, 106, 280)

    rect(r, 300, 148, 520, 120, fill="#e8f2f2", stroke="#0f4d4d", sw="1.4")
    text_el(r, 560, 168, "КОНТРОЛЛЕР + МОДУЛЬ ТРАНЗАКЦИЙ", "11", True, "middle", "#0f4d4d")
    text_el(r, 560, 252, "Pre-auth · согласие · virtual basket · split · offline ledger", "8", anchor="middle", fill="#555555")
    arrow_down(r, 560, 268, 288)

    rect(r, 120, 368, 660, 36)
    text_el(r, 450, 390, "Интерфейс с регулируемым положением — шина · кабель-канал · жгут", "9", True, "middle")
    arrow_down(r, 450, 404, 420)

    rect(r, 48, 432, 804, 72, fill="none", dash="6,4")
    text_el(r, 58, 450, "500 МОДУЛИ + внутренние датчики (RFID · тензо · камера)", "9", True)
    arrow_down(r, 450, 504, 524)

    rect(r, 80, 540, 200, 64, fill="#e8f2f2", stroke="#0f4d4d")
    text_el(r, 180, 562, "MASTER", "9", True, "middle", "#0f4d4d")
    rect(r, 350, 540, 160, 64)
    text_el(r, 430, 568, "SLAVE 1", "9", True, "middle")
    rect(r, 540, 540, 160, 64)
    text_el(r, 620, 568, "SLAVE N", "9", True, "middle")
    rect(r, 720, 540, 160, 64)
    text_el(r, 800, 562, "Сервер", "9", True, "middle")
    arrow_right(r, 280, 572, 342)
    arrow_right(r, 510, 572, 532)
    arrow_right(r, 700, 572, 714)

    rect(r, 200, 624, 500, 36)
    text_el(r, 450, 646, "Split: оператор + поставщик A + поставщик B (один чек)", "9", anchor="middle")
    text_el(r, 48, 708, "PPA №4", "12", True)
    write("PPA4_ARCH_RU.svg", r)


def ppa5():
    r = svg_root()
    text_el(r, 48, 40, "PPA №5 — Выравнивание · VTL · ESL/FIFO", "14", True)
    text_el(r, 48, 58, "Моторизованные опоры · слой визуального отслеживания · облачная биометрия", "10", fill="#555555")

    rect(r, 350, 72, 200, 40)
    text_el(r, 450, 90, "601 ИНКЛИНОМЕТР", "9", True, "middle")
    arrow_down(r, 450, 112, 128)

    rect(r, 120, 140, 660, 72, fill="#e8f2f2", stroke="#0f4d4d", sw="1.4")
    text_el(r, 450, 160, "КОНТРОЛЛЕР ШКАФА", "11", True, "middle", "#0f4d4d")
    text_el(r, 450, 178, "Наклон > 0,5° → опоры → ЗАПРЕТ транзакции", "8", anchor="middle")

    rect(r, 180, 244, 200, 56)
    text_el(r, 280, 266, "602 Моторизованные опоры", "9", True, "middle")
    rect(r, 520, 244, 200, 56)
    text_el(r, 620, 266, "VTL — внутренние камеры", "9", True, "middle")

    rect(r, 80, 348, 280, 72)
    text_el(r, 220, 370, "ЗОНА ВЫСОКОЙ ЦЕННОСТИ", "9", True, "middle")
    text_el(r, 220, 388, "тензодатчик + RFID", "8", anchor="middle", fill="#555555")
    rect(r, 540, 348, 280, 72)
    text_el(r, 680, 370, "СТАНДАРТНАЯ ЗОНА", "9", True, "middle")
    text_el(r, 680, 388, "луч + храповик", "8", anchor="middle", fill="#555555")
    arrow_right(r, 360, 384, 532)

    rect(r, 300, 452, 300, 40, fill="#e8f2f2", stroke="#0f4d4d")
    text_el(r, 450, 476, "СЛИЯНИЕ VTL + физический слой", "9", True, "middle", "#0f4d4d")

    rect(r, 80, 524, 200, 64)
    text_el(r, 180, 546, "603 ESL / LCD", "9", True, "middle")
    text_el(r, 180, 562, "FIFO: цена + срок", "8", anchor="middle", fill="#555555")
    rect(r, 280, 608, 340, 48, fill="#e8f2f2", stroke="#0f4d4d")
    text_el(r, 450, 630, "Облачное хранилище биометрии", "9", True, "middle", "#0f4d4d")
    text_el(r, 48, 708, "PPA №5", "12", True)
    write("PPA5_ARCH_RU.svg", r)


def ppa6():
    r = svg_root()
    text_el(r, 48, 40, "PPA №6 — Dual-zone · нагрев · fluid · ИИ-цены", "14", True)
    text_el(r, 48, 58, "Предоплата до нагрева · abandonment penalty · master–slave", "10", fill="#555555")

    rect(r, 300, 72, 300, 44, fill="#e8f2f2", stroke="#0f4d4d")
    text_el(r, 450, 92, "MASTER (опционально)", "10", True, "middle", "#0f4d4d")
    arrow_down(r, 450, 116, 132)

    rect(r, 120, 144, 660, 80, fill="#e8f2f2", stroke="#0f4d4d", sw="1.4")
    text_el(r, 450, 164, "КОНТРОЛЛЕР ШКАФА", "11", True, "middle", "#0f4d4d")
    text_el(r, 450, 208, "Pre-pay → heat → timer → penalty 200%", "8", anchor="middle", fill="#555555")

    rect(r, 48, 260, 380, 140, fill="none", dash="6,4")
    text_el(r, 58, 278, "701 ХОЛОДИЛЬНИК (+2…+4°C)", "9", True)
    rect(r, 472, 260, 380, 140, fill="none", dash="6,4")
    text_el(r, 482, 278, "702 ЗОНА НАГРЕВА (индукция)", "9", True)

    rect(r, 200, 432, 500, 48)
    text_el(r, 450, 452, "703 ГИБРИДНАЯ ЖИДКОСТНАЯ СТАНЦИЯ", "9", True, "middle")
    rect(r, 200, 604, 500, 52, fill="#e8f2f2", stroke="#0f4d4d")
    text_el(r, 450, 626, "ОБЛАКО + мобильные приложения", "9", True, "middle", "#0f4d4d")
    text_el(r, 48, 708, "PPA №6", "12", True)
    write("PPA6_ARCH_RU.svg", r)


if __name__ == "__main__":
    ppa3()
    ppa4()
    ppa5()
    ppa6()
    print("Done:", OUT)

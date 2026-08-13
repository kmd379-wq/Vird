# Micro Shop — ТЗ модуль «Овощ» (MS-PRODUCE-01)

**Версия:** 1.0  
**Дата:** 2026-08-13  
**Обозначение:** MS-PRODUCE-01  
**Роль в установке:** Slave (RS-485 / MSBP-0)  
**Рынок MVP:** РФ, lab-стенд  

**Связанные документы:**

- [MVP_SCOPE_v1_RU.md](./MVP_SCOPE_v1_RU.md)  
- [MVP_TZ_HARDWARE_v1.md](./MVP_TZ_HARDWARE_v1.md) §3  
- [MVP_BOM_v1.xlsx](./MVP_BOM_v1.xlsx)  
- [MVP_TEST_PLAN_v1.md](./MVP_TEST_PLAN_v1.md) §6.1  
- Патентные иллюстрации: `assets/figures/FIG_05_RU.svg`, `FIG_08_RU.svg`, `FIG_03_RU.svg`  

---

## 1. Общие положения

### 1.1. Назначение документа

Техническое задание на проектирование, изготовление и испытание модуля **«Овощ»** — автономного шкафа выдачи **свежей и фасованной продукции** в составе MVP Micro Shop.

### 1.2. Назначение изделия

Модуль обеспечивает:

1. **Хранение и выдачу** овощей/фруктов в фасовке (лотки) и насыпью/сетках (бункеры).  
2. **Фиксацию факта выдачи** по изменению массы слота.  
3. **Сигнал PICK_EVENT** на edge-контроллер для мгновенной оплаты (FIG 3).  
4. **Интеграцию** в модульную систему шкафов (FIG 5) через slave-шину.  

### 1.3. Место в системе (FIG 5)

По [FIG 5 — модульная система шкафов](../assets/figures/FIG_05_RU.svg) модуль «Овощ» относится к типу:

| Тип на FIG 5 | Реализация в MS-PRODUCE-01 |
|---|---|
| **Без охлаждения (Ambient)** | Основной режим: повседневная фасованная и свежая продукция без активного климата |
| **Контролируемые** | *Не в MVP* (мясные лотки — другой модуль / v1.1) |
| **Продуктовые узлы выдачи** | Бункеры P-1/P-2 + станция выдачи овощей |

Типичная локация на FIG 5: **6–8 шкафов**; в MVP модуль «Овощ» — **1 из 3** на lab-стенде.

### 1.4. Границы MVP (ссылка на Scope cut list)

| Патент / функция | MVP v1 | v1.1 / серия |
|---|---|---|
| Бункер 45° (PPA 8) | Lab-прототип 40–50° | Серийная точность 45° |
| Одна тензоячейка на шкаф (PPA 8) | **1 ячейка на слот** (проще) | Общая ячейка + алгоритм |
| Автосамовыравнивание | Фиксированные слоты | Полная реализация |
| ИИ-ценообразование (FIG 8) | Ручная цена в admin | Dynamic pricing |
| Утилизация / shrinkage (PPA 8) | Ручной учёт + log delta | Авто waste-weigh |
| PPA №10 контроль тары | Out of scope | Пилот |
| Motorized dispenser | Out of scope | TBD |

---

## 2. Патентный и архитектурный контур

### 2.1. Карта PPA → модуль «Овощ»

| PPA | Тема | Что реализуем в MS-PRODUCE-01 |
|---|---|---|
| **PPA 7** | Модульная розничная система | Slave-модуль, vertical bus interface, продуктовый узел выдачи, переконфигурируемые слоты |
| **PPA 8** | Контроль качества **сыпучих/фасованных** продуктов | Конусный бункер ~45°, тензоячейка, PICK по delta mass; *упрощённо* — без полного waste-AI контура |
| **PPA 1–4** | Платформа прямой торговли | Сессия → pick → платформа; модуль не содержит marketplace logic |
| **PPA 9** | Верифицированная обратная связь | Out of MVP (только лог событий для будущего) |
| **PPA 10** | Контроль тары | Out of MVP |

### 2.2. FIG 5 — модульная система

**Иллюстрация:** [FIG_05_RU.svg](../assets/figures/FIG_05_RU.svg)

**Требования к модулю как элементу системы:**

| ID | Требование |
|---|---|
| F5-01 | Габарит и интерфейс крепления совместимы с MS-CHILL-01 и MS-MEAL-01 (фронт ±2 mm) |
| F5-02 | Единая высота ~1800–2000 mm, ширина 600–800 mm |
| F5-03 | Slave-порт шины: IN от master, OUT к следующему slave (linear) |
| F5-04 | Маркировка на шильдике: `MS-PRODUCE-01`, serial, версия HW |
| F5-05 | Слоты P-1…P-5 промаркированы внутри камеры |

### 2.3. FIG 8 — операционный слой ИИ

**Иллюстрация:** [FIG_08_RU.svg](../assets/figures/FIG_08_RU.svg)

| Блок FIG 8 | MVP «Овощ» | Интерфейс |
|---|---|---|
| Оптимизация ассортимента | Out | Backend v1.1 |
| Рейтинг поставщиков | Out | Backend |
| **Динамическое ценообразование** | Out | Admin: фикс. цена/SKU |
| **Обнаружение потерь и аномалий** | **Partial** | Порог delta без PICK; log `WEIGHT_ANOMALY` |
| Прогноз пополнения | Out | Admin manual restock |

**MVP-minimum по FIG 8 для produce:** firmware отправляет сырые weight events; backend может flag аномалию (вес ↓ без PICK_EVENT > порога).

### 2.4. FIG 3 — процесс покупки (интеграция)

**Иллюстрация:** [FIG_03_RU.svg](../assets/figures/FIG_03_RU.svg)

Модуль участвует в шагах:

| Шаг FIG 3 | Ответственность MS-PRODUCE-01 |
|---|---|
| Регистрация / оплата | Backend + app (модуль не участвует) |
| Вход / сессия | Unlock door по `SESSION_OPEN` |
| **Взятие товара** | Weight + optional camera log |
| **Мгновенная оплата** | `PICK_EVENT` → master → edge → charge |
| Чек | Backend (модуль не участвует) |

---

## 3. Функциональные требования

### 3.1. Основные функции (F)

| ID | Функция | Приоритет |
|---|---|---|
| F-01 | Блокировка двери вне активной сессии | Must |
| F-02 | Unlock ≤ 500 ms после `SESSION_OPEN` | Must |
| F-03 | Детекция снятия товара по delta mass | Must |
| F-04 | Генерация `PICK_EVENT(slot_id, delta_g, sku_hint)` | Must |
| F-05 | Идентификация SKU по слоту + допуску веса | Must |
| F-06 | Индикация состояния: idle / session / fault | Must |
| F-07 | Safe lock при bus timeout > 30 s | Must |
| F-08 | Логирование door open/close | Must |
| F-09 | Restock: сброс baseline веса через admin/command | Must |
| F-10 | Ambient temp/humidity log | Should |
| F-11 | USB camera snapshot on PICK | Optional (TBD-07) |

### 3.2. Товарные слоты

| Слот | Тип узла | Выдача | SKU MVP | Ном. вес | Допуск | Min active |
|---|---|---|---|---|---|---|
| **P-1** | Бункер 45° | Гравитация + направляющие | Картофель 1 кг сетка | 1000 g | ±50 g | ✓ |
| **P-2** | Бункер 45° | Гравитация | Лук 500 г | 500 g | ±30 g | ✓ |
| **P-3** | Лоток на весах | Ручная выдача из лотка | Яблоки ~600 g | 600 g | ±40 g | ✓ |
| **P-4** | Лоток на весах | Ручная | Морковь 500 g | 500 g | ±30 g | Should |
| **P-5** | Лоток / резерв | — | TBD | — | — | Optional |

**Приёмка MVP:** минимум **3 активных слота** (P-1, P-2, P-3).

### 3.3. Сценарии использования

#### UC-01 — Покупка из бункера (P-1)

1. Пользователь открыл сессию; дверь разблокирована.  
2. Открывает дверь, снимает сетку картофеля.  
3. Delta mass слота P-1 ≈ −1000 g (stable ≥ 200 ms).  
4. Slave → `PICK_EVENT(P-1, 1000, SKU-P1)`.  
5. Edge → оплата → чек.  
6. Дверь закрыта; при `SESSION_CLOSE` — lock.

#### UC-02 — Покупка из лотка (P-3)

1. Аналогично UC-01; пользователь снимает упаковку яблок из фиксированного лотка.  
2. Delta ≈ −600 g → SKU-P3.

#### UC-03 — Restock (оператор)

1. `RESTOCK_MODE` через admin / service command.  
2. Door unlock; оператор кладёт товар.  
3. По `RESTOCK_COMMIT` — новый baseline weight per slot.

#### UC-04 — Fault: bus loss

1. Связь с master потеряна > 30 s.  
2. Door locked; status `FAULT_BUS`; LED fault pattern.

---

## 4. Конструкция и механика

### 4.1. Общая компоновка

```
┌──────────────────────────────────────┐
│  MS-PRODUCE-01                       │
│  ┌────────────┐  ┌────────────┐        │
│  │ P-1 Bunker │  │ P-2 Bunker │  ←45°  │
│  │  + load    │  │  + load    │        │
│  └────────────┘  └────────────┘        │
│  ┌──────┐ ┌──────┐ ┌──────┐          │
│  │ P-3  │ │ P-4  │ │ P-5  │  trays   │
│  │ tray │ │ tray │ │ tray │          │
│  └──────┘ └──────┘ └──────┘          │
│  [Door + EM lock + reed]             │
│  [Slave MCU] [Bus IN/OUT] [24V IN]   │
└──────────────────────────────────────┘
```

### 4.2. Каркас и обшивка

| Параметр | Требование |
|---|---|
| Каркас | Алюминий 40×40 mm или сталь 1.5–2 mm |
| Обшивка | Металл / ЛДСП v0; съёмные задняя и боковая панели |
| Внутренняя отделка | Food-grade у зон контакта с продуктом |
| Дверь | Одна на всю камеру; опционально PC-вставка для обзора |
| Петли | 110°; soft-close |
| Замок | EM lock 12 V, ≥ 300 N holding |

### 4.3. Бункер P-1 / P-2 (PPA 8)

| Параметр | Требование | MVP | Серия |
|---|---|---|---|
| Материал контакта | AISI 304 или PP food-grade | ✓ | ✓ |
| Угол наклона стенок | **45°** (целевой) | 40–50° допустимо | 45° ±2° |
| Тип | Конусный / hopper с гравитационной выдачей | ✓ | ✓ |
| Ёмкость | ≥ 5 kg начальной загрузки на бункер | ✓ | ✓ |
| Выход | Направляющие, без motorized auger на v0 | ✓ | TBD |
| Очистка | Съёмный бункер или люк обслуживания | Should | Must |
| Анти-зависание | Минимальная задняя стенка без dead zone | Must | Must |

**Критерий AC-P-04:** 3 последовательные выдачи без ручного толкания продукта.

### 4.4. Лотки P-3…P-5

| Параметр | Требование |
|---|---|
| Крепление | Фиксированная позиция на load platform |
| Формат | Под сетку / clamshell / tray поставщика |
| Max load | 3 kg на слот |
| Разделители | Визуальная маркировка зон (не смешанный pick без слота) |

### 4.5. Самовыравнивание (PPA / site)

| Версия | Реализация |
|---|---|
| **MVP** | Каждый слот — отдельная платформа/ячейка; «выравнивание» не требуется |
| **v1.1** | Общая платформа + одна ячейка + алгоритм самовыравнивания (PPA 8) |

---

## 5. Весовой контур (PPA 8)

### 5.1. Архитектура MVP

| Параметр | Значение |
|---|---|
| Схема | **1 load cell на слот** (до 5 ячеек) |
| Датчик | Single-point, 3 kg, класс C3 min |
| ADC | HX711 или 24-bit industrial ADC |
| Частота опроса | ≥ 10 Hz raw; stable detection 200 ms |
| Разрешение | ≤ 1 g |
| Дрейф | ≤ ±3 g / 24 h после калибровки |

### 5.2. Алгоритм PICK (firmware)

```
1. baseline[slot] = stable_weight при restock commit
2. on session active + door open:
     if stable(weight) for 200ms:
       delta = baseline[slot] - current_weight
       if delta >= sku.min_pick_threshold:
         emit PICK_EVENT(slot, delta)
         baseline[slot] -= delta   // or wait confirm from cloud
3. debounce vibration: ignore spikes < 50ms
4. overload: if weight > 120% slot_max → FAULT_OVERLOAD
```

### 5.3. SKU matching

| Поле | Источник |
|---|---|
| slot_id | Hardware fixed |
| sku_id | Config map slot → SKU |
| expected_delta | SKU nominal weight |
| tolerance | SKU ± band |
| price | Backend catalog (не в модуле) |

### 5.4. Утилизация / shrinkage (PPA 8 — partial)

| MVP | v1.1 |
|---|---|
| Оператор фиксирует списание в admin | Авто: delta без session = shrinkage event |
| Log `WEIGHT_ANOMALY` если delta > X без PICK | ИИ-цена и shrinkage (FIG 8) |

---

## 6. Электрика и электроника

### 6.1. Питание

| Параметр | Значение |
|---|---|
| Вход | 24 V DC от MS-CHILL-01 (master PSU) |
| Потребление | ≤ 40 W typical; peak ≤ 80 W (lock) |
| Защита | Reverse polarity; fuse 3 A on module |
| Разъёмы | Power IN, Bus IN, Bus OUT, Service USB |

### 6.2. Состав электроники

| Компонент | Qty | Примечание |
|---|---|---|
| Slave MCU (ESP32 / STM32) | 1 | Bus slave, weight, lock |
| Load cell + HX711 | 3–5 | Per slot |
| EM lock driver | 1 | MOSFET + flyback |
| Door reed | 1 | NC/NO per design |
| LED strip RGB or mono | 1 | Status |
| RS-485 transceiver | 1 | Bus |
| Temp/humidity (optional) | 1 | SHT31 |
| Camera USB (optional) | 1 | TBD-07 |

### 6.3. Шина и протокол

| Параметр | Значение |
|---|---|
| Interface | RS-485 (default TBD-02) |
| Role | Slave |
| Address | `0x01` (configurable) |
| Commands IN | `SESSION_OPEN`, `SESSION_CLOSE`, `RESTOCK_MODE`, `RESTOCK_COMMIT`, `PING` |
| Events OUT | `PICK_EVENT`, `DOOR_STATE`, `FAULT`, `HEARTBEAT`, `WEIGHT_ANOMALY` |

*Детали кадров MSBP-0 — отдельная спецификация firmware.*

### 6.4. Индикация LED

| Состояние | Pattern |
|---|---|
| Idle | Off / dim white |
| Session active | Solid green |
| Door open | Blink green |
| Fault | Blink red |
| Bus lost | Solid red |

---

## 7. Программное обеспечение (границы)

| Слой | Ответственность | Не в модуле |
|---|---|---|
| **Slave firmware** | Weight, lock, bus, PICK | Payment, fiscal |
| **Edge (master host)** | Aggregate events, cloud | SKU catalog edit UI |
| **Backend** | SKU, price, txn, receipt | — |
| **App** | UX, QR session | — |

### 7.1. Config parameters (per slot)

```yaml
slot_id: P-1
sku_id: SKU-P1
nominal_g: 1000
tolerance_g: 50
min_pick_g: 200
max_slot_g: 3000
type: bunker   # bunker | tray
```

---

## 8. Безопасность и материалы

| ID | Требование |
|---|---|
| SF-01 | Материалы food-contact — AISI 304 / PP food-grade |
| SF-02 | Нет острых кромок в зоне выдачи |
| SF-03 | Door pinch protection (hinge design) |
| SF-04 | Lock fails secure (door closed by default on power loss — уточнить тип замка) |
| SF-05 | Sanitation: бункеры и лотки моются без демонтажа electronics |
| SF-06 | IP rating target v0: IP20 indoor lab |

---

## 9. Условия эксплуатации

| Параметр | Значение |
|---|---|
| Tamb | +10…+28 °C |
| Влажность | 20–80% |
| Хранение продукта | Ambient; без активного охлаждения |
| Срок годности SKU | Контроль оператором; MVP без автоматики expiry |
| Санитария | Ежедневная проверка lab; без «Честного ЗНАКа» на MVP-SKU |

---

## 10. Критерии приёмки

| ID | Критерий | Метод | Pass |
|---|---|---|---|
| AC-P-01 | 100 циклов open/take/close | Auto/manual | No lock jam |
| AC-P-02 | PICK accuracy 3 SKU | 100 tries | ≥ 99% |
| AC-P-03 | Unlock latency | Log | ≤ 500 ms |
| AC-P-04 | Bunker gravity feed | 3 SKUs | No manual push |
| AC-P-05 | Bus disconnect | 35 s | Lock + FAULT |
| AC-P-06 | Restock baseline | Procedure | Weight reset ±5 g |
| AC-P-07 | False trigger | Vibration test | ≤ 1% / 1000 cycles |

**Ссылка:** [MVP_TEST_PLAN_v1.md](./MVP_TEST_PLAN_v1.md) TC-P-01…TC-P-07.

---

## 11. Комплект поставки v0

| # | Артефакт |
|---|---|
| 1 | Модуль MS-PRODUCE-01 assembled |
| 2 | Электрическая схема as-built |
| 3 | Firmware binary + config YAML слотов |
| 4 | Протокол H1 (standalone test) |
| 5 | CAD STEP / PDF чертёж бункера |
| 6 | BOM фактический (delta от MVP_BOM_v1) |

---

## 12. Чертёжи и иллюстрации

| Документ | Назначение |
|---|---|
| [FIG_05_RU.svg](../assets/figures/FIG_05_RU.svg) | Место модуля в системе (Ambient) |
| [FIG_08_RU.svg](../assets/figures/FIG_08_RU.svg) | Контекст ИИ-слоя (MVP partial) |
| [FIG_03_RU.svg](../assets/figures/FIG_03_RU.svg) | User flow pick + pay |
| MS-PRD-MECH-01 | Сборочный чертёж каркаса *(создать)* |
| MS-PRD-BUNKER-01 | Бункер 45° P-1/P-2 *(создать)* |
| MS-PRD-WEIGHT-01 | Схема весовых платформ *(создать)* |
| MS-PRD-EL-01 | Однолинейная + wiring *(создать)* |

---

## 13. Открытые пункты (TBD)

| ID | Вопрос | Влияние |
|---|---|---|
| TBD-P01 | Fail-safe vs fail-secure замок | Схема питания lock |
| TBD-P02 | Камера на v0 | BOM, privacy |
| TBD-P03 | P-4/P-5 активны или заглушки | Кол-во load cells |
| TBD-P04 | Точный угол бункера после mockup | AC-P-04 |
| TBD-P05 | PP vs mesh bag как стандарт упаковки | Габарит слота |

---

## 14. Связь с BOM

Позиции для MS-PRODUCE-01 в [MVP_BOM_v1.xlsx](./MVP_BOM_v1.xlsx):

- E03-001 load cells ×5  
- E04-001 lock ×1  
- E08-003 bunker ×2  
- E08-004 trays ×3  
- E02-001 MCU ×1  
- E07-002 RS-485 ×1  
- E09-004, E09-006 optional sensors  

---

## 15. История изменений

| Версия | Дата | Изменения |
|---|---|---|
| 1.0 | 2026-08-13 | Первая версия. PPA 7/8, FIG 5/8, MVP scope |

---

*Изменения — через revision документа. Отклонения от PPA формулировок в MVP — согласуются с patent counsel перед публичным пилотом.*

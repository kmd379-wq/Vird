# PPA №10 — пакет материалов для патентного поверенного

**Кому:** патентный поверенный (US provisional)  
**От:** команда Micro Shop / заявитель  
**Изобретение (EN):** Through-Tracking Tare Control System  
**Изобретение (RU):** Система сквозного контроля переносимой тары с предотвращением подмены, обработкой выдачи/оставления системной тары и распределением событий между сессиями  
**Проект:** Micro Shop  
**Дата пакета:** 2026-08-17  
**Язык заявки:** EN (specification и claims — в исходном PDF); **настоящий файл — RU пояснения и материалы по вашему заданию**

---

## Сопроводительное письмо (кратко)

Ниже — **единый комплект** по шести пунктам вашего задания. Цифровые чертежи FIG. 1–4 приложены отдельными SVG-файлами (см. § «Приложения»). Полный текст specification и формулировки claims 1–23 — в файле **`PPA#10_Tare Tracking.pdf`** (17 стр., EN).

Просим использовать настоящий документ как **пояснительную записку** при подготовке provisional; при необходимости — перевести captions и описания в patent drawing format.

---

## Сверка с заданием поверенного

| № | Требование поверенного | Статус | Где в пакете |
|---|------------------------|--------|--------------|
| 1 | **Эскизы или чертежи** устройства/системы (от руки или цифровые) | ✅ Готово (цифровые черновики) | **§1** + приложение: `PPA10_FIG_01_EN.svg` … `PPA10_FIG_04_EN.svg` |
| 2 | **Схема**, как основные компоненты **соединяются и взаимодействуют** | ✅ Готово | **§2** |
| 3 | **Блок-схема** или **пошаговое описание** процесса/метода | ✅ Готово | **§3** |
| 4 | **Простое описание** каждого компонента и его функций | ✅ Готово | **§4** |
| 5 | **1–2 конкретных примера** применения | ✅ Готово (2 примера) | **§5** |
| 6 | **Всё, что отличает** версию от существующих/аналогичных продуктов | ✅ Готово | **§6** |

### Что ещё нужно от заявителя (не входит в RU-пакет)

| Пункт | Статус | Действие |
|-------|--------|----------|
| Текст specification (EN) | ✅ есть | Приложить `PPA#10_Tare Tracking.pdf` |
| Claims 1–23 (EN) | ✅ есть | В том же PDF |
| Provisional cover sheet | ⬜ заявитель | Имена изобретателей, assignee, micro/small entity |
| Filing fee | ⬜ заявитель | По инструкции поверенного |
| Финальная полировка FIG | ⚠️ черновик | Поверенный/драфтsmen — patent line art перед подачей |

---

## Краткое описание изобретения (для контекста)

Автономная торговая система с **контролируемым проходом** покупателя: на **входе** регистрируется переносимая тара (ID + начальный вес), в **торговой зоне** фиксируются изменения массы тары при покупках, на **выходе** повторно проверяются ID и вес **активной** тары и сравниваются с **ожидаемым** весом, рассчитанным по журналу событий сессии. При расхождении или подмене тары — **protective response** (блокировка, повторная проверка, алерт). Поддерживаются: несколько единиц тары в одной сессии (своя + системная), зона возврата системной тары, двухзонная платформа (вес пользователя не в расчёте), параллельные сессии у одного модуля.

---

# §1. Эскизы и чертежи (FIG. 1–4)

> **Формат приложения:** 4 отдельных листа, patent line art, чёрный на белом, ссылочные numerals.  
> **Файлы:** `assets/figures/ppa10/PPA10_FIG_01_EN.svg` … `PPA10_FIG_04_EN.svg`

---

### FIG. 1 — Архитектура входа и выхода

**Caption (EN для заявки):**  
*FIG. 1 is a front view of an example entry and exit architecture illustrating a controlled user passage, an entry tare-registration zone, an entry monitor for displaying terms and obtaining user consent, a retail zone, an exit tare-verification zone, and an exit barrier.*

**Концептуальный эскиз:**

```
                    ┌─────────────────────────────────────────┐
  ВХОД              │           RETAIL ZONE                   │              ВЫХОД
                    │  (модули шкафов, зона возврата тары)    │
 ┌──────────┐       │    ┌─────┐  ┌─────┐  ┌─────┐           │       ┌──────────┐
 │ Entry    │       │    │Mod 1│  │Mod 2│  │Mod N│           │       │ Exit     │
 │ Monitor  │       │    └──┬──┘  └──┬──┘  └──┬──┘           │       │ Verify   │
 │ (terms + │       │       └────────┴────────┘              │       │ + Alert  │
 │ consent) │       │         Return zone                     │       │          │
 └────┬─────┘       │         (system tare)                   │       └────┬─────┘
 ┌────▼─────┐       │                                         │       ┌────▼─────┐
 │ Entry    │──────►│         shopping session                │──────►│ Exit     │
 │ Tare Reg │       │                                         │       │ Weigh    │
 │ + Weigh  │       │                                         │       └────┬─────┘
 └────┬─────┘       │                                         │     [Exit Barrier]
 [Entry Barrier]     │                                         │
      ▼             │                                         │            ▼
   Пользователь ───►│                                         │──► выход
```

**Нумерация элементов FIG. 1:**

| Ref | Компонент | Функция |
|-----|-----------|---------|
| 100 | Entry group | Контроль доступа, регистрация тары |
| 110 | Entry monitor | Условия, согласие на обработку данных |
| 120 | Entry tare-registration zone | Идентификация + начальный вес тары |
| 130 | Entry weighing structure | Взвешивание тары на входе |
| 140 | Entry barrier | Пропуск после успешной регистрации |
| 200 | Retail zone | Торговые модули, выдача товаров |
| 210 | Return zone | Возврат/оставление системной тары |
| 300 | Exit group | Верификация на выходе |
| 310 | Exit tare-verification zone | Re-ID + вес активной тары |
| 320 | Exit barrier | Разблокировка при успехе |
| 330 | User alert interface | Предупреждение при нарушении |
| 500 | Retail module(s) | Smart-шкафы в торговой зоне |

---

### FIG. 2 — Архитектура контроллера

**Caption (EN):**  
*FIG. 2 is a structural diagram of an example controller and user-session architecture including a tare identification module, a tare ID assignment module, a retail module, a tare event log, an expected exit tare weight calculation module, a discrepancy-and-tare-substitution detection module, and a protective response module.*

**Концептуальный эскиз:**

```
                    ┌─────────────────────────────────────┐
                    │           CONTROLLER (400)           │
                    │  Tare Event Log (410)               │
                    │  Expected Exit Tare Weight (420)    │
                    │  Discrepancy & Substitution (430)   │
                    │  Protective Response (440)            │
                    └───────┬──────────┬──────────┬────────┘
                            │          │          │
         ┌──────────────────┘          │          └──────────────────┐
         ▼                               ▼                               ▼
┌─────────────────┐           ┌─────────────────┐           ┌─────────────────┐
│ Tare ID         │           │ Retail Module(s)│           │ Tare Profile    │
│ Assignment (450)│           │ (500)           │           │ Store (460)     │
│ + ID (455)      │           │ tare-change     │           │ baseline weight │
└────────┬────────┘           └────────┬────────┘           └─────────────────┘
         │                             │
         ▼                             ▼
   Entry Group (100)            Exit Group (300)
   Cloud Platform (470)
```

---

### FIG. 3 — Двухзонная платформа

**Caption (EN):**  
*FIG. 3 is a detailed view of an example dual-zone platform in which a first zone is configured for placement of a carried receptacle and is associated with a weighing structure, and a second zone is configured for placement of a user, wherein the controller is configured to exclude the user's weight from tare calculations.*

**Концептуальный эскиз (вид сверху):**

```
┌─────────────────────────────────────────────┐
│           DUAL-ZONE PLATFORM (600)           │
│  ┌─────────────────────┐ ┌─────────────────┐ │
│  │  ZONE 1 (610)       │ │  ZONE 2 (620)   │ │
│  │  TARE / RECEPTACLE  │ │  USER STAND     │ │
│  │  bag on load cell   │ │  (weight NOT    │ │
│  │  [Weighing 630]     │ │   in tare calc) │ │
│  └─────────────────────┘ └─────────────────┘ │
│  Optional: camera 650, positioning barriers   │
└─────────────────────────────────────────────┘
```

**Смысл:** вес пользователя не включается в расчёт массы тары; отклонение измерения, если тара удерживается рукой, на полу или частично вне зоны 1.

---

### FIG. 4 — Workflow пользовательской сессии

**Caption (EN):**  
*FIG. 4 is a high-level process diagram of an example user-session workflow including display of terms of use and receipt of consent, registration or assignment of a tare identifier, determination of an initial tare weight, tracking of tare-change events in the retail zone, performance of exit identification and exit weighing of the tare, comparison with an expected weight, and execution of a release scenario or a protective response.*

*(Детальная блок-схема — §3; FIG. 4 = её графическое представление.)*

---

# §2. Схема соединения и взаимодействия компонентов

### 2.1. Физические и логические связи

```
┌─────────────── ENTRY GROUP (100) ───────────────┐
│ Monitor (110) ──► Consent OK ──► Tare ID read/assign (450, 455)
│ Tare Reg Zone (120) ──► Weighing (130) ──► Initial weight
│ Side-mounted tare reader (optional, claim 2)
└────────────────────┬──────────────────────┘
                     │ session start + tare profile
                     ▼
┌────────────── CONTROLLER (400) ─────────────────────────────┐
│ ◄──► Tare Profile Store (460)                             │
│ ◄──► Cloud Platform (470) — optional remote               │
│ Maintains: user sessions × N, tare units × M per session   │
└───────┬───────────────────────────────┬───────────────────┘
        │                               │
        ▼                               ▼
┌─────────────── RETAIL ZONE (200) ────┐   ┌──── EXIT GROUP (300) ────┐
│ Retail Module (500)                  │   │ Exit verify (310)        │
│ - weight sections / cabinets         │   │ Exit load cell           │
│ - tare-change events                 │   │ Exit tare reader         │
│ - multi-session allocation           │   │ Exit barrier (320)       │
│ Return Zone (210)                    │   │ Alert UI (330)           │
└──────────────────────────────────────┘   └──────────────────────────┘
```

### 2.2. Потоки данных

| Поток | От → К | Данные |
|-------|--------|--------|
| D1 | Entry → Controller | tare_id, initial_weight, consent, tare_type |
| D2 | Controller → Entry | unlock barrier / deny |
| D3 | Retail Module → Controller | tare_change_event, item_remove/add, session_hint |
| D4 | Return Zone → Controller | tare_returned / left_confirmed, tare_id |
| D5 | Controller → Retail | session_state, restriction |
| D6 | Exit → Controller | exit_tare_id, exit_weight |
| D7 | Controller → Exit | unlock / lock barrier, alert message |
| D8 | Controller → Cloud | audit log, ambiguity events, operator alert |

### 2.3. Типы сенсоров (без ограничения реализации)

- Load cells / weighing structures (entry, exit, retail modules, return zone)  
- RFID / NFC / barcode / QR readers (tare ID)  
- Cameras (trajectory, placement confirmation)  
- Presence sensors (dual-zone platform)  
- Tare-presence sensors в return/storage zone  

---

# §3. Блок-схема процесса (метод работы)

### 3.1. Общий алгоритм (соответствует FIG. 4)

```
START
  │
  ▼
[A] Display terms + tare registration notice on Entry Monitor (110)
  │
  ▼
[B] User consent? ──NO──► Deny entry ──► END
  │
 YES
  ▼
[C] Tare identification OR assign tare_id (450, 455)
  │     (read tag / apply label / issue system tare / temp ID)
  ▼
[D] Measure initial tare weight (130 / dual-zone 600)
  │
  ▼
[E] Create user session + tare profile(s) in Controller (400)
  │     status = ACTIVE_FOR_EXIT
  ▼
[F] Unlock entry barrier (140) → User enters RETAIL ZONE (200)
  │
  ├──────────────────────────────────────┐
  ▼                                      ▼
[G] Shopping loop                    [H] Optional: issue system tare
  │  Retail module (500) events:         register new tare unit in session
  │  - item removed → tare weight ↓      │
  │  - item added to tare → weight ↑     ▼
  │  - log to tare event log (410)   [I] Return/leave system tare?
  │                                      YES → confirm in return zone (210)
  │                                      → status = RETURNED/LEFT
  │                                      → exclude from exit calc
  ▼
[J] Multi-user same module? → allocate event to session
  │     confidence low? → AMBIGUITY EVENT → verification mode
  ▼
[K] User proceeds to EXIT GROUP (300)
  │
  ▼
[L] Re-read tare_id + measure exit weight (active tare only)
  │
  ▼
[M] Controller: expected_exit_weight = f(initial, tare_event_log, active statuses)
  │     (module 420)
  ▼
[N] Checks (module 430):
  │  N1: exit_tare_id == session active tare_id?  ──NO──► TARE SUBSTITUTION
  │  N2: |exit_weight - expected| ≤ threshold?   ──NO──► WEIGHT DISCREPANCY
  │  N3: unresolved ambiguity?                    ──YES──► PROTECTIVE RESPONSE
  ▼
 ALL PASS
  │
  ▼
[O] Unlock exit barrier (320) → Close session → END

 PROTECTIVE RESPONSE (440) — при любом fail:
  - lock exit barrier
  - re-identify / re-weigh
  - inspection zone / operator alert (330)
  - audit log
```

### 3.2. Расчёт ожидаемого веса на выходе

```
expected_exit_weight = Σ (active_tare_units)

  для каждой active unit:
    weight = initial_tare_weight
           + Σ tare_change_events (add to tare)
           - Σ tare_change_events (remove from tare)

  ИСКЛЮЧИТЬ units со статусом:
    RETURNED, LEFT_IN_ZONE (confirmed), INACTIVE
```

### 3.3. Несколько покупателей у одного модуля (claims 20–23)

При параллельных сессиях контроллер распределяет события по:

1. Временной корреляции (timestamp)  
2. Зоне взаимодействия (interaction zone / slot)  
3. tare_id активной тары  
4. Траектории пользователя (camera)  
5. Последовательности sensor events  

Если confidence < порога → **ambiguity event** → verification mode; событие не дублируется в двух сессиях без правила allocation (claim 23).

---

# §4. Описание компонентов и их функций

| Ref | Компонент | Простое описание |
|-----|-----------|------------------|
| 100 | Entry group | Входная группа: не пускает в торговую зону, пока тара не зарегистрирована и не взвешена. |
| 110 | Entry monitor | Экран с правилами и **согласием** на регистрацию/взвешивание тары и обработку данных. |
| 120 | Entry tare-registration zone | Место, куда покупатель кладёт сумку/корзину для ID и начального веса. |
| 130 | Entry weighing structure | Весы на входе (load cell / platform). |
| 140 | Entry barrier | Турникет/дверь — открывается после успешной регистрации. |
| 200 | Retail zone | Торговая зона с модулями выдачи товаров. |
| 210 | Return zone | Зона возврата **системной** тары: подтверждает «оставил/вернул». |
| 300 | Exit group | Выходная группа: повторная проверка тары перед выходом. |
| 310 | Exit tare-verification zone | Re-ID + взвешивание **активной** тары. |
| 320 | Exit barrier | Блокируется при расхождении веса или подмене тары. |
| 330 | User alert interface | Сообщение пользователю при ошибке/подозрении. |
| 400 | Controller | «Мозг»: сессии, журнал событий, расчёт ожидаемого веса, решение pass/fail. |
| 410 | Tare event log | Хронология всех изменений массы тары в сессии. |
| 420 | Expected exit tare weight module | Считает, сколько должна весить тара на выходе. |
| 430 | Discrepancy & substitution detection | Сравнивает факт vs ожидание; ловит подмену ID. |
| 440 | Protective response module | Блокировка, повторное взвешивание, инспекция, алерт оператору. |
| 450 | Tare ID assignment module | Назначает метку/ID при выдаче системной тары или untagged mode. |
| 455 | Tare identification module | Считывает RFID/NFC/QR/штрихкод или создаёт временный ID. |
| 460 | Tare profile store | База профилей: тип тары, базовый вес, допустимое отклонение. |
| 470 | Cloud platform | Удалённый сервер: аудит, аналитика, оператор (optional). |
| 500 | Retail module(s) | Smart-шкаф / полка: фиксирует изменение массы тары при покупке. |
| 600 | Dual-zone platform | Две зоны: зона 1 — тара на весах, зона 2 — пользователь (его вес не считается). |
| 610 | Zone 1 (tare) | Зона размещения переносимой тары. |
| 620 | Zone 2 (user) | Зона стояния пользователя. |
| 630 | Weighing structure (platform) | Весовая структура двухзонной платформы. |
| 640 | User presence sensor | Датчик присутствия пользователя в зоне 2. |
| 650 | Camera / positioning | Камера и/или ограничители позиционирования (optional). |

**Tare unit (единица тары):** сумка, корзина, рюкзак, тележка или **системная корзина** магазина — каждая со статусом (active / returned / left / excluded from exit).

**Side-mounted tare reader (claim 2):** считыватель вдоль коридора — серия reads при проходе для anti-substitution.

**Smart tare container (claim 8):** тара со встроенным ID и, опционально, датчиками — прямая связь с контроллером.

---

# §5. Примеры применения

### Пример 1 — Модульный micro-shop в лобби ЖК (Micro Shop)

**Контекст:** автономная зона 3–6 smart-шкафов без кассира.

1. Покупатель подходит к **entry group (100)**: на monitor (110) — согласие на регистрацию своей сумки.  
2. Кладёт сумку в **dual-zone platform (600)**: система фиксирует `tare_id` (NFC-бирка) и `initial_weight = 420 g`.  
3. Дополнительно выдаётся **system tare** (корзина магазина, 680 g) — вторая единица в сессии.  
4. В retail module (500) покупатель снимает молоко и овощи — модуль шлёт **tare_change_events** (−1030 g, −500 g) в controller (400).  
5. Корзину магазина оставляет в **return zone (210)** — controller меняет статус на `LEFT_CONFIRMED`, исключает 680 g из exit calc.  
6. На **exit (300)**: активна только personal bag; `expected ≈ 420 + 1530 = 1950 g`; факт 1940 g → **pass**, exit barrier (320) open.

**Практический смысл:** контроль **непрерывности тары** вход→выход + учёт **нескольких** тар + **системная** корзина не создаёт ложное срабатывание на выходе.

---

### Пример 2 — Два покупателя у одного шкафа (multi-session)

**Контекст:** один retail module (500), две параллельные сессии (claims 20–22).

1. Пользователи A и B одновременно в активных сессиях; у каждого своя `tare_id`.  
2. На одной weight section почти одновременно два события снятия товара.  
3. Controller (400) коррелирует: camera (650) + zone slot 3 → session A; slot 7 → session B.  
4. Если correlation confidence 45% → **ambiguity event** → обе сессии в verification mode, exit temporarily restricted.  
5. Оператор или side reader разрешает ambiguity → сессии закрываются нормально.

**Практический смысл:** масштабирование автономной розницы без ограничения «один покупатель на весь магазин».

---

# §6. Отличия от существующих и аналогичных решений

| Аналог | Что делает | Чего **нет** (наше отличие PPA #10) |
|--------|------------|-------------------------------------|
| **Amazon Go / grab-and-go** | Computer vision, sensor fusion, account billing | Сквозной **through-tracking** конкретной **переносимой тары** entry→exit; явная **exit verification** mass vs expected |
| **Smart fridge / один шкаф** | Вес полки, charge on take | Нет controlled passage; нет **multi-tare session** (своя + системная); нет **return zone** logic |
| **Classic EAS / RFID gate** | Anti-theft tag at exit | Не учитывает **начальный вес тары** и **накопленные tare-change events** в сессии |
| **Self-checkout scale** | Одно взвешивание на кассе | Нет регистрации тары **на входе**; нет tracking **during** session в modular retail |
| **Deposit basket systems** | Возврат тележки | Нет привязки к **user session** и **expected exit weight** с учётом покупок |
| **Simple «weigh at exit»** | Одно финальное взвешивание | Не различает **подмену тары** (ID mismatch); не обрабатывает **оставленную** системную тару |

### Ключевые патентуемые акцents (prior art / examiner)

1. **Through-tracking:** entry register → session log → exit verify (не точечный snapshot).  
2. **Tare substitution prevention:** ID continuity + weight profile + side reader timeline (claims 2–3, 7, 10).  
3. **Multi-tare per session:** user-carried + system-provided; dynamic **active set** for exit.  
4. **Provided-tare leaving:** confirmed leave/return **не** = discrepancy (claims 5–6, 16–19).  
5. **Multi-session allocation** на одном module + **ambiguity event** (claims 20–23).  
6. **Dual-zone platform:** исключение веса пользователя из tare calc (claims 6–7).  
7. **Untagged tare mode** с reduced confidence (claim 15).  
8. **Protective response** как structured scenario, не просто alarm (claims 1(ix), 12).

---

# Приложения

## A. Файлы для отправки поверенному (полный комплект)

| № | Файл | Назначение |
|---|------|------------|
| 1 | **`docs/PPA10_PATENT_ATTORNEY_PACKAGE_RU.md`** | **Настоящий документ** — все 6 пунктов задания |
| 2 | **`PPA#10_Tare Tracking.pdf`** | Specification + claims 1–23 (EN) — у заявителя |
| 3 | `assets/figures/ppa10/PPA10_FIG_01_EN.svg` | FIG. 1 — entry/exit architecture |
| 4 | `assets/figures/ppa10/PPA10_FIG_02_EN.svg` | FIG. 2 — controller architecture |
| 5 | `assets/figures/ppa10/PPA10_FIG_03_EN.svg` | FIG. 3 — dual-zone platform |
| 6 | `assets/figures/ppa10/PPA10_FIG_04_EN.svg` | FIG. 4 — user-session workflow |

**Как отправить:** e-mail или облако — приложить PDF + этот `.md` (или экспорт в PDF) + 4 SVG (или PDF-экспорт каждого листа).

## B. Checklist USPTO provisional

- [ ] Provisional cover sheet (inventor names, assignee, entity status)  
- [ ] Specification — `PPA#10_Tare Tracking.pdf`  
- [ ] Claims 1–23 — в PDF  
- [x] FIG. 1–4 — SVG-черновики (финальная полировка — по усмотрению поверенного)  
- [ ] Abstract / title — из PDF  
- [ ] Filing fee  

## C. Mapping claims → фигуры

| Claims | Основные FIG |
|--------|--------------|
| 1 (system) | FIG. 1, 2, 4 |
| 2–3 (side reader) | FIG. 1, 2 |
| 4–5 (tare compartment) | FIG. 1, 3 |
| 6–7 (dual-zone) | FIG. 3 |
| 8–10 (smart tare, retail sensor) | FIG. 2 |
| 11 (profile store) | FIG. 2 |
| 12 (protective response) | FIG. 2, 4 |
| 13–15 (ID assignment, untagged) | FIG. 2, 4 |
| 16–19 (return zone, expected weight) | FIG. 1, 4 |
| 20–23 (multi-session, ambiguity) | FIG. 2, 4 |

---

*Документ не заменяет юридическую консультацию. Английский текст заявки — в `PPA#10_Tare Tracking.pdf`.*

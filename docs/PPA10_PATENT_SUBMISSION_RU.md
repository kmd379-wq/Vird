# PPA №10 — материалы для подачи патентной заявки

**Изобретение:** Through-Tracking Tare Control System  
**Русское название:** Система сквозного контроля переносимой тары с предотвращением подмены, обработкой выдачи/оставления системной тары и распределением событий между сессиями  
**Источник:** `PPA#10_Tare Tracking.pdf`  
**Проект:** Micro Shop  
**Дата:** 2026-08-14  
**Язык заявки:** EN (текст PDF); настоящий документ — **RU пояснения для поверенного / USPTO provisional**

---

## Как использовать этот документ

| Требование заявки | Где в документе |
|---|---|
| Эскизы / чертежи | **§1** (FIG. 1–4) + ASCII-эскизы |
| Схема соединения компонентов | **§2** |
| Блок-схема / пошаговый процесс | **§3** |
| Описание компонентов | **§4** |
| Примеры применения | **§5** |
| Отличия от аналогов | **§6** |

**Для подачи:** приложить FIG. 1–4 (цифровые или от руки), текст описания из PDF, формулировки claims из PDF. Настоящий файл — **пояснительная записка** на русском для команды и патентного поверенного.

---

## §1. Эскизы и чертежи (FIG. 1–4)

> По PDF заявки предусмотрены **4 фигуры**. Ниже — содержание каждой, текст для подписей (captions) и **концептуальные эскизы** (пригодны для перевода в патентные рисунки от руки или в Illustrator/CAD).

---

### FIG. 1 — Архитектура входа и выхода (Entry and Exit Architecture)

**Caption (EN для заявки):**  
*FIG. 1 is a front view of an example entry and exit architecture illustrating a controlled user passage, an entry tare-registration zone, an entry monitor for displaying terms and obtaining user consent, a retail zone, an exit tare-verification zone, and an exit barrier.*

**Что показать на рисунке:**

```
                    ┌─────────────────────────────────────────┐
  ВХОД              │           RETAIL ZONE                   │              ВЫХОД
                    │  (модули шкафов, зона возврата тары)    │
 ┌──────────┐       │                                         │       ┌──────────┐
 │ Entry    │       │    ┌─────┐  ┌─────┐  ┌─────┐           │       │ Exit     │
 │ Monitor  │       │    │Mod 1│  │Mod 2│  │Mod N│           │       │ Verify   │
 │ (terms + │       │    └──┬──┘  └──┬──┘  └──┬──┘           │       │ + Alert  │
 │ consent) │       │       │        │        │              │       │          │
 └────┬─────┘       │       └────────┴────────┘              │       └────┬─────┘
      │             │                                         │            │
 ┌────▼─────┐       │         Return zone                     │       ┌────▼─────┐
 │ Entry    │       │         (system tare)                   │       │ Exit     │
 │ Tare Reg │──────►│                                         │──────►│ Tare     │
 │ + Weigh  │       │                                         │       │ Weigh    │
 └────┬─────┘       │                                         │       └────┬─────┘
      │             │                                         │            │
 [Entry Barrier]     │                                         │     [Exit Barrier]
      │             │                                         │            │
      ▼             │                                         │            ▼
   Пользователь ───►│  shopping session  ───────────────────►│──► выход
```

**Элементы FIG. 1 (нумерация для чертежа):**

| Ref | Компонент | Функция |
|---|---|---|
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

---

### FIG. 2 — Архитектура контроллера и сессий (Controller Architecture)

**Caption (EN):**  
*FIG. 2 is a structural diagram of an example controller and user-session architecture including a tare identification module, a tare ID assignment module, a retail module, a tare event log, an expected exit tare weight calculation module, a discrepancy-and-tare-substitution detection module, and a protective response module.*

**Эскиз FIG. 2:**

```
                    ┌─────────────────────────────────────┐
                    │           CONTROLLER (400)           │
                    │  ┌─────────────────────────────┐    │
                    │  │ Tare Event Log (410)        │    │
                    │  └──────────────┬──────────────┘    │
                    │  ┌──────────────▼──────────────┐    │
                    │  │ Expected Exit Tare Weight   │    │
                    │  │ Calculation (420)           │    │
                    │  └──────────────┬──────────────┘    │
                    │  ┌──────────────▼──────────────┐    │
                    │  │ Discrepancy & Substitution  │    │
                    │  │ Detection (430)             │    │
                    │  └──────────────┬──────────────┘    │
                    │  ┌──────────────▼──────────────┐    │
                    │  │ Protective Response (440)   │    │
                    │  └─────────────────────────────┘    │
                    └───────┬──────────┬──────────┬────────┘
                            │          │          │
         ┌──────────────────┘          │          └──────────────────┐
         ▼                               ▼                               ▼
┌─────────────────┐           ┌─────────────────┐           ┌─────────────────┐
│ Tare ID         │           │ Retail Module(s)│           │ Tare Profile    │
│ Assignment (450)│           │ (500)           │           │ Store (460)     │
│ + Tare ID       │           │ weighing +      │           │ baseline weight │
│   Identification│           │ tare-change     │           │ deviation range │
│   (455)         │           │ events          │           │                 │
└────────┬────────┘           └────────┬────────┘           └─────────────────┘
         │                             │
         ▼                             ▼
   Entry Group (100)            Exit Group (300)
   + Cloud Platform (470)
```

---

### FIG. 3 — Двухзонная платформа (Dual-Zone Platform)

**Caption (EN):**  
*FIG. 3 is a detailed view of an example dual-zone platform in which a first zone is configured for placement of a carried receptacle and is associated with a weighing structure, and a second zone is configured for placement of a user, wherein the controller is configured to exclude the user's weight from tare calculations.*

**Эскиз FIG. 3 (вид сверху):**

```
┌─────────────────────────────────────────────┐
│           DUAL-ZONE PLATFORM (600)           │
│  ┌─────────────────────┐ ┌─────────────────┐ │
│  │  ZONE 1 (610)       │ │  ZONE 2 (620)   │ │
│  │  TARE / RECEPTACLE  │ │  USER STAND     │ │
│  │  ┌───────────────┐  │ │     ○ user      │ │
│  │  │ bag / basket  │  │ │                 │ │
│  │  │ on load cell  │  │ │  (weight NOT    │ │
│  │  └───────────────┘  │ │   in tare calc) │ │
│  │  [Weighing 630]    │ │  [Presence 640] │ │
│  └─────────────────────┘ └─────────────────┘ │
│  Optional: camera 650, positioning barriers   │
└─────────────────────────────────────────────┘
```

**Смысл для патента:** вес пользователя не включается в расчёт массы тары; система отклоняет измерение, если тара удерживается рукой, на полу или частично вне зоны 1.

---

### FIG. 4 — Workflow пользовательской сессии (User-Session Workflow)

**Caption (EN):**  
*FIG. 4 is a high-level process diagram of an example user-session workflow including display of terms of use and receipt of consent, registration or assignment of a tare identifier, determination of an initial tare weight, tracking of tare-change events in the retail zone, performance of exit identification and exit weighing of the tare, comparison with an expected weight, and execution of a release scenario or a protective response.*

*(Полная блок-схема — §3 ниже; FIG. 4 = её графическое представление для заявки.)*

---

### Связь с рисунками Micro Shop (сайт)

| PPA FIG | Аналог в проекте | Примечание |
|---|---|---|
| FIG. 1–4 (PPA #10) | `assets/figures/ppa10/PPA10_FIG_01_EN.svg` … `PPA10_FIG_04_EN.svg` | Черновики SVG (900×640, patent style); не путать с FIG_01…10 сайта |
| FIG_09 (сайт) | Логика безопасности / protective response | Дополняет, не заменяет FIG. 2/4 |
| FIG_10 (сайт) | Сетевая архитектура edge + cloud | Контроллер 400 ↔ cloud 470 |

**Рекомендация поверенному:** для provisional приложить **4 отдельных листа FIG. 1–4** по PDF; стиль — patent line art (чёрный на белом, ссылочные numerals).

---

## §2. Схема соединения и взаимодействия компонентов

### 2.1. Физические и логические связи

```
┌─────────────── ENTRY GROUP ───────────────┐
│ Monitor ──► Consent OK ──► Tare ID read/assign
│ Tare Reg Zone ──► Load cell ──► Initial weight
│ Side-mounted tare reader (optional, claim 2)
└────────────────────┬──────────────────────┘
                     │ session start + tare profile
                     ▼
┌────────────── CONTROLLER 400 ─────────────────────────────┐
│ ◄──► Tare Profile Store 460                               │
│ ◄──► Cloud 470 (optional remote)                          │
│ Maintains: user sessions × N, tare units × M per session   │
└───────┬───────────────────────────────┬───────────────────┘
        │                               │
        ▼                               ▼
┌─────────────── RETAIL ZONE ──────────┐   ┌──── EXIT GROUP ────┐
│ Retail Module 500                    │   │ Exit tare verify   │
│ - weight sections / cabinets         │   │ Exit load cell     │
│ - tare-change events (add/remove)    │   │ Exit tare reader   │
│ - multi-session allocation           │   │ Exit barrier 320   │
│ Return Zone 210 (system tare)        │   │ Alert UI 330       │
└──────────────────────────────────────┘   └────────────────────┘
```

### 2.2. Потоки данных

| Поток | От → К | Данные |
|---|---|---|
| D1 | Entry → Controller | tare_id, initial_weight, consent, tare_type |
| D2 | Controller → Entry | unlock barrier / deny |
| D3 | Retail Module → Controller | tare_change_event, item_remove/add, session_hint |
| D4 | Return Zone → Controller | tare_returned / left_confirmed, tare_id |
| D5 | Controller → Retail | session_state, restriction |
| D6 | Exit → Controller | exit_tare_id, exit_weight |
| D7 | Controller → Exit | unlock / lock barrier, alert message |
| D8 | Controller → Cloud | audit log, ambiguity events, operator alert |

### 2.3. Сенсоры (не ограничивая реализацию)

- Load cells / weighing structures (entry, exit, retail modules, return zone)  
- RFID / NFC / barcode / QR readers (tare ID)  
- Cameras (trajectory, placement confirmation)  
- Presence sensors (dual-zone platform)  
- Tare-presence sensors in return/storage zone  

---

## §3. Блок-схема процесса (метод работы)

### 3.1. Общий алгоритм (FIG. 4)

```
START
  │
  ▼
[A] Display terms + tare registration notice on Entry Monitor
  │
  ▼
[B] User consent? ──NO──► Deny entry ──► END
  │
 YES
  ▼
[C] Tare identification OR assign tare_id
  │     (read tag / apply label / issue system tare / temp ID)
  ▼
[D] Measure initial tare weight (entry weighing / dual-zone)
  │
  ▼
[E] Create user session + tare profile(s) in Controller
  │     status = ACTIVE_FOR_EXIT
  ▼
[F] Unlock entry barrier → User enters RETAIL ZONE
  │
  ├──────────────────────────────────────┐
  ▼                                      ▼
[G] Shopping loop                    [H] Optional: issue system tare
  │  Retail module events:               register new tare unit in session
  │  - item removed → tare weight ↓      │
  │  - item added to tare → weight ↑     ▼
  │  - log to tare event log         [I] Return/leave system tare?
  │                                      YES → confirm in return zone
  │                                      → status = RETURNED/LEFT
  │                                      → exclude from exit calc
  ▼
[J] Multi-user same module? → allocate event to session
  │     confidence low? → AMBIGUITY EVENT → verification mode
  ▼
[K] User proceeds to EXIT GROUP
  │
  ▼
[L] Re-read tare_id + measure exit weight (active tare only)
  │
  ▼
[M] Controller: expected_exit_weight = f(initial, tare_event_log, active statuses)
  │
  ▼
[N] Checks:
  │  N1: exit_tare_id == session active tare_id?  ──NO──► TARE SUBSTITUTION
  │  N2: |exit_weight - expected| ≤ threshold?   ──NO──► WEIGHT DISCREPANCY
  │  N3: unresolved ambiguity?                    ──YES──► PROTECTIVE RESPONSE
  ▼
 ALL PASS
  │
  ▼
[O] Unlock exit barrier → Close session → END

 PROTECTIVE RESPONSE (any fail):
  - lock exit barrier
  - re-identify / re-weigh
  - inspection zone / operator alert
  - audit log
```

### 3.2. Расчёт ожидаемого веса на выходе (упрощённо)

```
expected_exit_weight = Σ (active_tare_units)
  where each active unit:
    weight = initial_tare_weight
           + Σ tare_change_events (add to tare)
           - Σ tare_change_events (remove from tare)

  EXCLUDE units with status:
    RETURNED, LEFT_IN_ZONE (confirmed), INACTIVE
```

### 3.3. Распределение событий при нескольких покупателях (claim 20–23)

При одновременной работе нескольких сессий у одного retail module контроллер использует:

1. Временную корреляцию (timestamp)  
2. Зону взаимодействия (interaction zone / slot)  
3. tare_id, считанный у активной тары  
4. Траекторию пользователя (camera)  
5. Последовательность sensor events  

Если confidence < порога → **ambiguity event** → событие не дублируется в двух сессиях без правила allocation (claim 23).

---

## §4. Описание компонентов и их функций

| Компонент | Простое описание |
|---|---|
| **Entry group (100)** | «Входная группа»: не пускает в торговую зону, пока тара не зарегистрирована и не взвешена. |
| **Entry monitor (110)** | Экран с правилами и **согласием** на регистрацию/взвешивание тары и обработку данных. |
| **Entry tare-registration zone (120)** | Место, куда покупатель кладёт сумку/корзину для ID и начального веса. |
| **Entry weighing structure (130)** | Весы на входе (load cell / platform). |
| **Entry barrier (140)** | Турникет/дверь/шлагbaum — открывается после успешной регистрации. |
| **Exit group (300)** | «Выходная группа»: повторная проверка тары перед выходом. |
| **Exit tare-verification zone (310)** | Зона повторного считывания ID и взвешивания **активной** тары. |
| **Exit barrier (320)** | Блокируется при расхождении веса или подмене тары. |
| **User alert interface (330)** | Сообщение пользователю при ошибке/подозрении. |
| **Retail module (500)** | Smart-шкаф / полка / модуль: фиксирует изменение массы тары при покупке. |
| **Return zone (210)** | Зона возврата **системной** тары (корзины магазина): подтверждает «оставил/вернул». |
| **Controller (400)** | «Мозг»: сессии, журнал событий, расчёт ожидаемого веса, решение pass/fail. |
| **Tare identification module (455)** | Считывает RFID/NFC/QR/штрихкод тары или создаёт временный ID. |
| **Tare ID assignment module (450)** | Назначает метку/ID при выдаче системной тары или untagged mode. |
| **Tare profile store (460)** | База профилей: тип тары, базовый вес, допустимое отклонение. |
| **Tare event log (410)** | Хронология всех изменений массы тары в сессии. |
| **Expected exit tare weight module (420)** | Считает, сколько должна весить тара на выходе. |
| **Discrepancy & substitution detection (430)** | Сравнивает факт vs ожидание; ловит подмену ID. |
| **Protective response module (440)** | Блокировка, повторное взвешивание, инспекция, алерт оператору. |
| **Dual-zone platform (600)** | Две зоны: зона 1 — тара на весах, зона 2 — пользователь (его вес не считается). |
| **Side-mounted tare reader (claim 2)** | Считыватель вдоль коридора — серия reads при проходе для anti-substitution. |
| **Smart tare container (claim 8)** | Тара со встроенным ID и, опционально, датчиками — прямая связь с контроллером. |
| **Cloud platform (470)** | Удалённый сервер: аудит, аналитика, оператор (optional). |

**Tare unit (единица тары):** сумка, корзина, рюкзак, тележка, **или системная корзина**, выданная магазином — каждая со статусом (active / returned / left / excluded from exit).

---

## §5. Примеры применения

### Пример 1 — Модульный micro-shop в лобби ЖК (Micro Shop)

**Контекст:** автономная зона 3–6 smart-шкафов без кассира.

1. Покупатель подходит к **entry group**: на monitor — согласие на регистрацию своей сумки.  
2. Кладёт сумку в **dual-zone platform**: система фиксирует `tare_id` (NFC-бирка) и `initial_weight = 420 g`.  
3. Дополнительно выдаётся **system tare** (корзина магазина, 680 g) — вторая единица в сессии.  
4. В retail module покупатель снимает молоко и овощи — модуль шлёт **tare_change_events** (−1030 g, −500 g) в controller.  
5. Корзину магазина оставляет в **return zone** — controller меняет статус на `LEFT_CONFIRMED`, исключает 680 g из exit calc.  
6. На **exit**: активна только personal bag; `expected = 420 + 1530 = 1950 g` (упрощённо); факт 1940 g → **pass**, exit barrier open.

**Отличие от «просто весового шкафа»:** контроль **непрерывности тары** вход→выход + учёт **нескольких** тар + **системная** корзина не создаёт false alarm.

---

### Пример 2 — Два покупателя у одного шкафа (multi-session)

**Контекст:** один retail module, две параллельные сессии (claim 20–22).

1. Пользователь A и B одновременно открыты сессии; у каждого своя `tare_id`.  
2. На одной weight section почти одновременно два события снятия товара.  
3. Controller correlates: camera + zone slot 3 → session A; slot 7 → session B.  
4. Если correlation confidence 45% → **ambiguity event** → обе сессии в verification mode, exit для A и B temporarily restricted до уточнения.  
5. Оператор или дополнительный sensor (side reader) разрешает ambiguity → сессии закрываются нормально.

**Практическая ценность:** масштабирование автономной розницы без «один покупатель на весь магазин».

---

## §6. Отличия от существующих / аналогичных решений

| Аналог | Что делает | Чего **нет** (наше отличие PPA #10) |
|---|---|---|
| **Amazon Go / grab-and-go** | Computer vision, sensor fusion, account billing | Сквозной **through-tracking** конкретной **переносимой тары** entry→exit; явная **exit verification** mass vs expected |
| **Smart fridge / один шкаф** | Вес полки, charge on take | Нет controlled passage; нет **multi-tare session** (своя + системная); нет **return zone** logic |
| **Classic EAS / RFID gate** | Anti-theft tag at exit | Не учитывает **начальный вес тары** и **накопленные tare-change events** в сессии |
| **Self-checkout scale** | Одно взвешивание на кассе | Нет регистрации тары **на входе**; нет tracking **during** session в modular retail |
| **Deposit basket systems** | Возврат тележки | Нет привязки к **user session** и **expected exit weight** с учётом покупок |
| **Simple «weigh at exit»** | Одно финальное взвешивание | Не различает **подмену тары** (ID mismatch); не обрабатывает **оставленную** системную тару |

### Ключевые патентуемые акценты (для ответа examiner / prior art)

1. **Through-tracking:** entry register → session log → exit verify (не точечный snapshot).  
2. **Tare substitution prevention:** ID continuity + weight profile + side reader timeline (claims 2–3, 7, 10).  
3. **Multi-tare per session:** user-carried + system-provided; dynamic **active set** for exit.  
4. **Provided-tare leaving:** confirmed leave/return **не** = discrepancy (claims 5–6, 16–19).  
5. **Multi-session allocation** на одном module + **ambiguity event** (claims 20–23).  
6. **Dual-zone platform:** исключение веса пользователя из tare calc (claims 6–7).  
7. **Untagged tare mode** с reduced confidence (claim 15).  
8. **Protective response** как structured scenario, не просто alarm (claims 1(ix), 12).

---

## §7. Checklist для подачи provisional (USPTO)

- [ ] Форма provisional cover sheet (micro entity / small entity — по статусу)  
- [ ] Текст specification (PDF `PPA#10_Tare Tracking.pdf` — 17 стр.)  
- [ ] Claims 1–23 (в PDF)  
- [x] **FIG. 1** — entry/exit architecture → `assets/figures/ppa10/PPA10_FIG_01_EN.svg` (черновик)  
- [x] **FIG. 2** — controller block diagram → `assets/figures/ppa10/PPA10_FIG_02_EN.svg` (черновик)  
- [x] **FIG. 3** — dual-zone platform → `assets/figures/ppa10/PPA10_FIG_03_EN.svg` (черновик)  
- [x] **FIG. 4** — workflow diagram → `assets/figures/ppa10/PPA10_FIG_04_EN.svg` (черновик)  
- [ ] Abstract / title (из PDF)  
- [ ] Inventor names, assignee (если через юрлицо)  
- [ ] Filing fee  

**Примечание:** provisional не требует formal claims review, но **качество FIG. 1–4** критично для non-provisional в течение 12 месяцев.

---

## §8. Mapping claims → фигуры (для поверенного)

| Claims | Основные FIG |
|---|---|
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

## §9. История

| Версия | Дата | Примечание |
|---|---|---|
| 1.0 | 2026-08-14 | RU материалы для подачи PPA #10 на базе PDF |

---

*Документ не заменяет юридическую консультацию патентного поверенного. Английский текст заявки — в `PPA#10_Tare Tracking.pdf`.*

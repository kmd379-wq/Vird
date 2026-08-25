# Modular Cabinet Platform — пакет материалов для патентного поверенного (PPA №3–6)

**Кому:** патентный поверенный  
**От:** команда Micro Shop / заявитель  
**Контур:** Modular Cabinet Platform  
**Дата пакета:** 2026-08-25  
**Язык:** русский (пояснения); тексты claims и specification — EN в исходных PDF

> **Индекс и чеклист отправки:** [`MODULAR_CABINET_PATENT_ATTORNEY_INDEX_RU.md`](MODULAR_CABINET_PATENT_ATTORNEY_INDEX_RU.md)

---

# PPA №3 — Modular Smart Vending Cabinet

**EN:** Modular Smart Vending Cabinet with Smart-Glass Inspection Mode, Sensor-Fusion Manual Retrieval, and Quality-Based Dynamic Pricing  
**RU:** Модульный умный торговый шкаф со smart-glass режимом осмотра, ручной выдачей под sensor-fusion и динамическим ценообразованием по качеству  
**Источник:** `PPA#3-ModularSmartVendingCabinet_Revised.pdf`  
**Рисунки:** `PPA#3 FIGURES.pdf` (FIG. 1–4)

## Краткое описание

Автономный модульный шкаф на едином шасси с вертикальной шиной питания/данных, сменными модулями выдачи (pusher, hook, scale-box, gated gravity, sliding tray, auto-purge) и **ручным** изъятием товара — без роботизированного gantry. Система sensor-fusion (RFID-матрица + камера + тензодатчики) подтверждает каждое снятие. Для age-gated товаров — smart-glass (PDLC): непрозрачный режим → биометрическая проверка возраста → прозрачный режим осмотра → pre-auth → доступ. Движок ценообразования учитывает **sensory decay** (потеря качества до срока годности) и **space-yield displacement** (скидка для освобождения «застоявшегося» слота).

---

## §1. Эскизы и чертежи (FIG. 1–4)

> **Формат:** 4 отдельных листа, patent line art. Официальные — в `PPA#3 FIGURES.pdf`.

### FIG. 1 — Вид спереди: архитектура шкафа

**Подпись:** *FIG. 1 — front view of autonomous retail cabinet: door, display, biometric camera, payment interface, smart shelves, linear front-zone antenna region.*

```
┌─────────────────────────────────────────┐
│  [110 Display]  [105 Biometric "Eye"]   │
│  [Payment]                              │
├─────────────────────────────────────────┤
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
│  │Mod A│ │Mod B│ │Mod C│ │Mod D│       │  ← interchangeable modules
│  │push │ │hook │ │scale│ │gate │       │
│  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘       │
│     │antenna matrix + LED strip (smart edge)
├─────────────────────────────────────────┤
│         Smart Waste Bin (purge)         │
└─────────────────────────────────────────┘
      ▲ user-facing front zone
```

| Ref | Компонент | Функция |
|-----|-----------|---------|
| 100 | Корпус / дверь | Защищённый объём, access-control |
| 105 | Биометрическая камера («The Eye») | Возраст / идентификация до доступа |
| 110 | Дисплей / UI | Условия, цены, согласие, digital sommelier |
| 120 | Зона регистрации / front zone | Линейная RFID-матрица вдоль фронта полки |
| 130 | Весовая структура (вход/модули) | Load cells в scale-box и weighing dish |
| 200 | Торговая зона (interior) | Модули A–G на шасси |
| 400 | Edge controller | Локальный «мозг», кэш, pricing engine |
| 500 | Модули выдачи | Pusher, hook, scale-box, gated gravity, sliding tray, auto-purge |

### FIG. 2 — Вид сбоку: edge controller и offline-архитектура

**Подпись:** *FIG. 2 — electronics bay: edge controller, local DB/cache, comm modules, UPS.*

```
┌──────────────── Cabinet ────────────────┐
│  Modules ◄──► Vertical Power Busbar     │
│              (rear wall)                │
│  ┌─────────────────────────────┐      │
│  │ Edge Controller (400)        │      │
│  │ · pricing engine             │      │
│  │ · sensor-fusion              │      │
│  │ · local cache / ledger       │      │
│  └──────────┬──────────────────┘      │
│             │ LTE / Wi-Fi / Ethernet    │
│  [UPS / Battery]  [Casters + leveling feet]
└─────────────────────────────────────────┘
         ▲ works offline: lock, count, debit
```

### FIG. 3 — Деталь: геометрия sensing и overlap-зона

**Подпись:** *FIG. 3 — shelf sensing: front-zone antenna array, camera FOV, overlap region for sensor fusion.*

```
        Camera FOV
           ╲  │  ╱
            ╲ │ ╱
   ──────────●──────────  ← overlap region
   [Ant][Ant][Ant][Ant]   ← linear antenna matrix (front edge)
   ┌──────────────────┐
   │  product slot    │
   └──────────────────┘

Hand in FOV + NO RFID removal → alarm / deposit hold
```

### FIG. 4 — Процесс индукции и загрузки (FIFO)

**Подпись:** *FIG. 4 — induction station: barcode → RFID tag → expiration → rear-load FIFO.*

```
Staff: [Scan SKU] → [Program RFID] → [Enter expiry]
                          │
                          ▼
              Rear-load into module (FIFO)
                          │
                          ▼
         Front edge: tag read + camera + weight at sale
```

---

## §2. Схема соединения и взаимодействия (PPA 3)

```
┌─── USER ───┐     ┌─── EDGE CONTROLLER (400) ───────────────────────┐
│ Biometric  │────►│ pricing · sensor-fusion · access · transactions │
│ Display    │◄───►│ local cache · offline mode                    │
│ Payment    │     └───┬──────────┬──────────┬──────────┬───────────┘
└────────────┘         │          │          │          │
                       ▼          ▼          ▼          ▼
              Vertical busbar   Camera(s)   RFID matrix  Load cells
                       │          │          │          │
                       ▼          └────┬─────┴────┬─────┘
              Modules A–G (push/hook/   overlap fusion zone
              scale/gate/tray/purge)
                       │
                       ▼
              Smart Waste Bin (load cell + RFID)
                       │
                       ▼ (optional)
              Cloud / Mobile App (inventory, digital twin, ads)
```

| Поток | От → К | Данные |
|-------|--------|--------|
| D1 | Induction station → Controller | SKU, RFID UID, expiry, batch |
| D2 | Module sensors → Controller | tag read, weight delta, gate state |
| D3 | Camera → Controller | hand entry, removal gesture |
| D4 | Controller → Display/LED | price, discount cue, navigation |
| D5 | Controller → Door lock | unlock / lock / smart-glass state |
| D6 | Controller → Payment | incremental hold per item |
| D7 | Controller ↔ Cloud | pricing policies, sync, mobile handshake |

---

## §3. Блок-схема процесса (PPA 3)

### 3.1. Стандартный режим (ambient/chilled)

```
СТАРТ → Tap-to-pay / auth → Unlock door
  │
  ▼
Pay-as-you-pick loop:
  User removes item manually
  → Sensor fusion (RFID + camera [+ weight])
  → Incremental hold / charge at dynamic price
  → Update inventory
  │
  ▼
User closes door → Release remaining pre-auth → КОНЕЦ
```

### 3.2. Restricted-goods mode (Unit A, smart-glass)

```
СТАРТ → User approaches (smart glass OPAQUE)
  │
  ▼
Biometric age verification (105)
  │
  ├─ FAIL → deny
  ▼
Smart glass → TRANSPARENT (inspection mode)
  → Display product info (digital sommelier)
  │
  ▼
Pre-authorization / deposit (risk-based amount)
  │
  ▼
Unlock → Manual retrieval
  → Triple fusion: antenna + overhead camera + load cell
  → Capture charge → КОНЕЦ
```

### 3.3. Gated gravity-feed (Module D)

```
Item 1 in weighing dish → Gate LOCKED
  → User removes item 1 (weight → 0, camera confirms)
  → Gate opens → Item 2 drops to dish → Gate LOCKED again
```

### 3.4. Dynamic pricing

```
Inputs: expiry, stocking time, env sensors, camera quality hints, turnover
  │
  ├─ Sensory decay model → accelerated discount before expiry
  ├─ Space-yield metric → discount stagnant slot
  └─ Time-based decay curve
  │
  ▼
Update price → LED strip / display highlight
```

---

## §4. Описание компонентов (PPA 3)

| Ref / Module | Компонент | Простое описание |
|--------------|-----------|------------------|
| Chassis | Transformer base | Единое шасси; vertical power busbar; casters + leveling feet; rear-load FIFO |
| Module A | Pusher | Пружинный трек + регулируемый разделитель; one-way ratchet |
| Module B | Hook / rod | Подвесные товары; задняя загрузка |
| Module C | Scale-box | Зона на load cell; мягкая/аморфная упаковка; multi-pick |
| Module D | Gated gravity | Наклонный chute → weighing dish → sequential gate |
| Module E/F | Sliding tray | Low-friction полка без пружин; deli, meat, cheese |
| Module G | Auto-purge | Retractable stop → item drops to smart waste |
| Smart edge | Antenna matrix + LED | Virtual zoning, navigation, discount cues |
| Smart glass | PDLC panel | Opaque sleep → transparent inspection |
| Edge controller | Processor + cache | Pricing, fusion, offline transactions, UPS-backed |
| Smart waste | Bin + load cell + RFID | Quarantine tracking; anti-scavenger charge |

---

## §5. Примеры применения (PPA 3)

### Пример 1 — Micro-shop в лобби ЖК (ambient + chilled)

1. Покупатель авторизуется tap-to-pay на дисплее.  
2. Дверь открывается; он вручную снимает йогурт с pusher-модуля — RFID + камера фиксируют снятие, списание по текущей динамической цене.  
3. Шоколадный батончик на sliding tray: sensory decay model снизил цену на 30% — LED подсвечивает слот.  
4. При закрытии двери остаток pre-auth возвращается.

### Пример 2 — Secure unit с алкоголем (smart-glass)

1. Smart-glass непрозрачен. Камера оценивает возраст ≥21.  
2. Стекло становится прозрачным; на экране — vintage, region, pairing notes.  
3. Pre-auth $50; дверь открывается.  
4. Снятие бутылки подтверждается triple fusion; частичное потребление/возврат детектируется load cell → блокировка/штраф.

---

## §6. Отличия от аналогов (PPA 3)

| Аналог | Что делает | Чего нет (наше отличие) |
|--------|------------|-------------------------|
| Роботизированный vending (gantry) | Робот достаёт товар | **Прямое ручное** изъятие + unified sensor-fusion |
| ID-scan age gate | Скан документа → выдача | **Privacy-first smart-glass inspection** до доступа |
| Простой dynamic pricing | Скидка по expiry date | **Sensory decay** + **space-yield displacement** |
| Классический vending | Один тип механики | **6+ типов модулей** на одном шасси с busbar |
| Amazon Go | CV-only, без модульной механики | Аппаратно-якоренная модульность + offline edge |

**Ключевые патентуемые акценты:** unified chassis + busbar; sensor-fusion overlap geometry; smart-glass restricted workflow; sensory/space-yield pricing; gated gravity sequencing; auto-purge + smart waste; sales-final anti-reverse (mechanical + software penalty).

---

---

# PPA №4 — Smart Retail Cabinet with Tokenized Access and Split Payments

**EN:** Smart Retail Cabinet with Tokenized Access and Split Payments  
**RU:** Умный торговый шкаф с токенизированным доступом и split-платежами  
**Источник:** `PPA#4_SMART_RETAIL CABINET_WITH_TOKENIZED_ACCESS_AND_SPLIT_PAYMENTS.pdf`  
**Рисунки:** `PPA#4 FIGURES.pdf`

## Краткое описание

Модульный шкаф с **position-adjustable power/data interface** (busbar / drag-chain / flexible harness), токенизированным доступом через QR из мобильного приложения и/или биометрию, **обязательным согласием** с условиями (immediate charge, no returns) до unlock. Split settlement: один checkout → несколько merchant accounts по tenant/slot. Multi-tenant shelf rental: поставщики управляют своими полками. Master–slave кластер: одна сессия, virtual basket, consolidated capture. Offline financial ledger + UPS.

---

## §1. Эскизы (FIG. 1–4) — PPA 4

Структура рисунков **аналогична PPA 3** (FIG. 1 front chassis, FIG. 2 controller architecture, FIG. 3 sensing geometry + secure compartment, FIG. 4 induction workflow). Дополнительные акценты PPA 4:

- **FIG. 1:** position-adjustable interface (busbar / drag-chain / harness); LED information strip  
- **FIG. 2:** transaction module — token decode, pre-auth, offline ledger, split routing, fiscal receipt  
- **FIG. 3:** external biometric zone + internal inventory imaging; smart glass secure compartment  
- **FIG. 4:** **upstream induction** — supplier warehouse tags goods → allow-list manifest sync → cabinet recognizes without local scan

---

## §2. Схема соединения (PPA 4)

```
Mobile App ──QR/token──► Optical Scanner ──► Controller
                              │
Biometric (external) ─────────┤
                              │
                    ┌─────────▼──────────┐
                    │ Transaction Module  │
                    │ · pre-auth token    │
                    │ · consent record    │
                    │ · virtual basket    │
                    │ · split settlement  │
                    │ · offline ledger    │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
   Master unit           Slave unit(s)        Remote server
   (payment, AI,         (sensors, locks,    (manifests,
    biometric)            extra volume)       supplier UI)
         │                    │
         └──── single session / virtual basket ────┘
```

---

## §3. Блок-схема процесса (PPA 4)

```
СТАРТ
  │
  ▼
[1] Scan QR / Biometric → Decode session token
  │
  ▼
[2] Pre-authorization (reserve funds)
  │
  ▼
[3] Display transaction terms:
    · immediate charge upon removal
    · no returns
    · penalty logic
  → Require "I AGREE" (affirmative consent)
  │
  ▼
[4] Restricted mode? → KYC age from token OR biometric
  │
  ▼
[5] Unlock access barrier
  │
  ▼
[6] Loop: manual retrieval
    → Internal sensors detect removal
    → Increment reserved amount + legal purchase commitment
    → Mode A: instant capture OR Mode B: defer to session end
    → Split route $ to operator + supplier merchant accounts
  │
  ▼
[7] Session end → Aggregated capture (if Mode B)
  → Digital + fiscal receipt → mobile app / email
  │
  ▼
Network down? → Offline ledger debits → async reconcile later
Power down? → UPS maintains locks + recording
```

---

## §4. Описание компонентов (PPA 4)

| Компонент | Описание |
|-----------|----------|
| Position-adjustable interface | Busbar / drag-chain / harness — power+data без перепайки при смене высоты полки |
| Token / QR scanner | Session token из KYC-verified mobile app |
| External biometric sensor | На корпусе / bezel — идентификация вне storage volume |
| Internal inventory sensors | RFID matrix, load cells, internal camera — fusion внутри объёма |
| Consent UI | Display + "I Agree"; time-stamped consent record |
| Transaction module | Pre-auth, incremental hold, instant vs aggregated capture |
| Split settlement engine | Basket splitting по item/slot → multiple merchant accounts |
| Multi-tenant controller | Per-supplier inventory, pricing, alerts |
| Offline ledger | Local balance/token debits during network outage |
| UPS / battery | Locks + sensors + ledger during power loss |
| Master–slave cluster | Shared payment/AI at master; slaves report sensors/locks |

---

## §5. Примеры применения (PPA 4)

### Пример 1 — Multi-tenant micro-shop в аэропорту

1. Покупатель сканирует QR в приложении Micro Shop.  
2. Pre-auth €30; экран показывает условия → «Согласен».  
2. Снимает воду (tenant: Operator A) и снек (tenant: Supplier B).  
3. Split settlement: €2 → Operator A, €4.50 → Supplier B; один чек в приложении.

### Пример 2 — Master–slave кластер (6 шкафов, 1 терминал)

1. Auth один раз at master unit.  
2. Покупатель ходит между slave 1–5, снимает товары.  
3. Virtual basket на master controller; aggregated capture при exit/timeout.  
4. Один consolidated fiscal receipt.

---

## §6. Отличия от аналогов (PPA 4)

| Аналог | Наше отличие |
|--------|--------------|
| Обычный vending | Нет tokenized session + mandatory consent audit trail |
| Single-merchant cabinet | **Multi-tenant** shelves + **hardware-triggered split** settlement |
| Standalone-only cabinets | **Master–slave** с shared BOM cost reduction |
| Cloud-dependent grab-and-go | **Offline ledger + UPS** — продажи при outage |
| Local-only induction | **Upstream manifest** — pre-tagged goods без локального scan |

**Ключевые акценты:** token + consent before unlock; split payments per item; multi-tenant platform; master–slave virtual basket; three interface types for repositionable shelves; dual-mode standard/restricted without hardware change.

---

---

# PPA №5 — Smart Retail Cabinet (Tokenized Access, rev.)

**EN:** Smart Retail Cabinet with Tokenized Access and Split Payments (revised)  
**RU:** Умный торговый шкаф — ревизия: auto-leveling, Visual Tracking Layer, ESL/FIFO  
**Источник:** `PPA#5_SmartRetailCabinet_TokenizedAccess_SplitPayments.pdf`  
**Рисунки:** `PPA#5 FIGURES.pdf`

## Краткое описание

Развитие PPA 4 с **активным motorized leveling** (inclinometer + screw-drive feet, порог ~0.5°), **Visual Tracking Layer** (always-on internal cameras) + selectable physical layer (load cell+RFID vs break-beam+anti-reverse), **ESL/LCD shelf-edge** с FIFO metadata queue, **progressive biometric enrollment** с cloud roaming, **punitive penalty** = multiple of highest-value SKU.

---

## §1. Эскизы (FIG. 1–4) — PPA 5

Базовая топология как PPA 4, плюс:

- **FIG. 1:** motorized leveling feet; ESL/LCD strip с expiration + dynamic price; rear service door  
- **FIG. 2:** Visual Tracking Layer + dual detection configs; progressive biometric enrollment flow  
- **FIG. 3:** high-value zone (load cell + RFID) vs standard zone (break-beam + ratchet)  
- **FIG. 4:** FIFO queue → ESL auto-update on removal

---

## §2. Схема соединения (PPA 5)

```
Inclinometer ──► Controller ──► Motorized leveling feet
                      │
Internal cameras (Visual Tracking Layer, continuous)
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
  High-value zone              Standard zone
  Load cell + RFID             Break-beam + anti-reverse ratchet
         │                         │
         └──────── fusion ─────────┘
                      │
              ESL / LCD shelf-edge
                      │
         Token / Biometric → Session → Split settlement
                      │
              Cloud biometric repository (roaming)
```

---

## §3. Блок-схема процесса (PPA 5)

### 3.1. Startup / leveling

```
Power ON → Read inclinometer
  │
  ├─ tilt > 0.5° → Drive actuators → re-level
  │
  ├─ still over threshold → INHIBIT session start
  ▼
Ready for transactions
```

### 3.2. FIFO metadata on ESL

```
Maintain virtual FIFO queue (expiry timestamps per slot)
  │
  Display: price + expiry for FRONT item on ESL
  │
  Removal detected → Update ESL to NEXT item in queue
```

### 3.3. Progressive biometric enrollment

```
Session 1: QR token auth → optional face capture + opt-in consent
  │
  ▼
Upload biometric vector to cloud repository
  │
  ▼
Session N at different cabinet/region:
  Recognize user → Validate payment instrument for region
  ├─ invalid → block + "refresh payment method"
  └─ valid → seamless biometric entry
```

### 3.4. Punitive penalty

```
Unauthorized weight increase / forced return
  AND NOT corroborated by Visual Tracking Layer
  │
  ▼
Charge = MULTIPLE × highest-value item in enclosure
(record consent was obtained pre-unlock)
```

---

## §4. Описание компонентов (PPA 5)

| Компонент | Описание |
|-----------|----------|
| Motorized leveling system | Electric actuators + inclinometer; auto-level; inhibit sales if tilted |
| Visual Tracking Layer | Always-on internal cameras; hand/item tracking |
| Selectable physical layer | High-value: load cell+RFID; Standard: break-beam+ratchet |
| ESL / LCD shelf-edge | Real-time price + batch/expiry; FIFO auto-update |
| Smart bin | Dedicated load cell; amorphous goods; weight-loss debit |
| Gravity tray (fragile) | Low-friction incline + temp sensor + sale interlock |
| UI variants | Door-integrated OR boom-mounted articulating display |
| Cloud biometric repo | Cross-cabinet / cross-region recognition |
| Punitive penalty engine | Fraud deterrence beyond unit price |

---

## §5. Примеры применения (PPA 5)

### Пример 1 — Шкаф с молоком в пакетах (smart bin)

1. Leveling: inclinometer 0.3° — OK.  
2. QR auth + consent.  
3. Покупатель берёт 2 milk pouches из smart bin — weight loss 1020 g → debit.  
4. Попытка вернуть один пакет: weight +510 g, camera не подтверждает → punitive charge = 3× max SKU price.

### Пример 2 — Deli tray с temperature interlock

1. ESL показывает «Salad · exp 2026-08-26 · €4.20».  
2. Temp sensor: 8°C > limit 6°C → controller **inhibits sale** для слота.  
3. Staff re-levels cabinet after move; session blocked until tilt < 0.5°.

---

## §6. Отличия от аналогов (PPA 5)

| vs PPA 4 / market | Отличие PPA 5 |
|-------------------|---------------|
| Static leveling feet | **Active motorized** leveling with transaction inhibit |
| RFID-only or camera-only | **Dual-layer fusion**: always-on CV + zone-specific physics |
| Static shelf labels | **ESL FIFO queue** — auto metadata for next item |
| Per-device biometrics | **Progressive enrollment + cloud roaming** + regional payment validation |
| Flat return penalty | **Punitive multiple of max SKU** |

---

---

# PPA №6 — Modular Retail System with Adaptive Architecture

**EN:** Modular Retail System with Adaptive Architecture, AI-Driven Pricing, and Integrated Consumables Management  
**RU:** Модульная розничная система с адаптивной архитектурой, AI-ценообразованием и управлением расходниками  
**Источник:** `PPA#6_Modular_Retail_System.pdf`  
**Рисунки:** `PPA#6 FIGURES.pdf`

## Краткое описание

Роботизированная/автономная экосистема: standalone **или** master–slave; **dual-zone climate** (+2…+4°C vault + isolated heating positions); **induction** до target consumption temp без кипения; **secure pre-payment before heating**; abandonment penalty (200% если не забрали за 5 min); **profiled dispensing channel** с ratchet anti-reverse; **hybrid fluid station** (dry additive + hot water); **floating smart bin**; **composite vessel** с selective heating zones; **AI bidirectional pricing**; conditional remote reservation (walk-in priority when n>1).

---

## §1. Эскизы (FIG. 1–4) — PPA 6

- **FIG. 1:** Modular cabinet front — reconfigurable chassis, sensing zone, LED/LCD strips (shared figure style with 4/5)  
- **FIG. 2:** Controller — heating queue, payment gating, AI pricing, master–slave orchestration  
- **FIG. 3:** Dual-zone climate section — cold vault / heating bay / thermal shutter; profiled channel cross-section  
- **FIG. 4:** Transaction + heating workflow — pre-pay → heat → retrieval timer → penalty

**Дополнительный концептуальный эскиз — dual-zone + heating:**

```
┌──────────────────────────────────────┐
│  COLD VAULT (+2…+4°C)                │
│  [Profiled channel][Gravity][Bin]    │
│  ─── thermal shutter ───             │
│  HEATING POSITIONS (induction)       │
│  [Slot 1][Slot 2][Slot 3]            │
│  LCD strip: "READY" flash            │
├──────────────────────────────────────┤
│  Hybrid Fluid Station (interlocked)  │
│  Utensil Dispenser · Waste Chute     │
└──────────────────────────────────────┘
```

**Profiled guide tray (cross-section):**

```
      ┌── container ──┐
      │               │
   ┌──┴───────────────┴──┐  ← U-shaped profile cradles body
   │ ═══ ratchet floor ══ │  ← one-way forward lock
   └─────────────────────┘
        ▲ spring pusher
```

---

## §2. Схема соединения (PPA 6)

```
                    ┌── Master Unit (optional) ──┐
                    │ Payment · AI · Session      │
                    └──────────┬──────────────────┘
                               │
    ┌──────────────────────────▼──────────────────────────┐
    │              Cabinet Controller                      │
    │  Auto-leveling · Heating queue · AI pricing · Locks  │
    └──┬────────┬─────────┬──────────┬──────────┬──────────┘
       │        │         │          │          │
       ▼        ▼         ▼          ▼          ▼
   Inclinometer Induction  Load cells  RFID/LCD  Fluid station
   + level feet  coils     (floating   strips    (interlock)
                            bin)
       │        │         │          │          │
       ▼        ▼         ▼          ▼          ▼
   Cold vault   Heating   Product    Expired    Utensil
   modules      positions  channels   tag lock   dispenser
       │
       ▼
   Cloud: fleet telemetry, remote pricing, conditional reservation
   Mobile: vendor app + consumer app
```

---

## §3. Блок-схема процесса (PPA 6)

### 3.1. Heated product flow

```
User selects heated item (QR/biometric)
  │
  ▼
Read Digital Passport from tag (target temp, heating profile)
  │
  ▼
Display price + confirm on slot map UI
  │
  ▼
** PRE-PAYMENT CAPTURE ** (before heating energy)
  │
  ▼
Verify tilt ≤ threshold (auto-level if needed)
  │
  ▼
Activate induction per profile; impedance check (authentic packaging)
  │
  ▼
Heating complete → Flash LCD "READY" → Start retrieval timer (e.g. 5 min)
  │
  ├─ Retrieved in time → OK
  └─ NOT retrieved → Lock slot · Flag waste · Route to waste module
                     · Punitive fee (e.g. 200% value)
```

### 3.2. Hybrid fluid (noodles / coffee)

```
Verified SKU in position at fluid station
  │
  ▼
Electronic interlock releases:
  · Boiling water (noodles/tea) OR
  · Hot steamed water (coffee/porridge)
  │
  ▼
Dry additive in container reconstitutes
```

### 3.3. AI bidirectional pricing

```
Inputs: internal shelf-life, demand/surge, external competitor prices (API/scrape)
  │
  ▼
Increase OR decrease price in real time
  │
  ▼
Publish to shelf-edge LCD + block expired RFID tags (disable pusher)
```

### 3.4. Conditional remote reservation

```
Mobile reservation request for SKU X
  │
  ├─ inventory count ≤ 1 → DENY (walk-in priority)
  └─ count > N → GRANT reservation + timer
        │
        ├─ User scans at unit within timer → fulfill
        └─ Timeout → auto-release reservation
```

---

## §4. Описание компонентов (PPA 6)

| Компонент | Описание |
|-----------|----------|
| Master–slave architecture | Standalone mode OR slave deferring payment/AI to master |
| Dual-zone climate | Cold vault + thermally isolated heating positions + shutters |
| Active auto-leveling | Tilt sensor + motorized feet; inhibit heat/fluid if tilted |
| Profiled dispensing channel | U-profile tray; variable height containers; ratchet floor |
| Composite vessel | Inner liner + patterned susceptor + insulating shell |
| Smart combo tray | Active susceptor zones + passive RF-transparent zones |
| Induction subsystem | Target temp under sealed film; impedance authentication |
| Hybrid fluid station | Temperature/volume controlled; SKU-gated interlock |
| Floating smart bin | Single-point mount; conical funnel; door-slam filter |
| Intelligent utensil dispenser | SKU → spoon vs stirrer vs fork, one at a time |
| Waste chute / module | Sealed collection; expired/heated abandonment |
| AI pricing module | Decay + surge + external market; mechanical lockout on expiry |
| Reservation server | n>1 rule; timer; walk-in priority |

---

## §5. Примеры применения (PPA 6)

### Пример 1 — Офисный hot-food cabinet

1. Пользователь сканирует QR; на карте слотов видит «Soup #3 — €5.90».  
2. Подтверждает → **оплата до нагрева**.  
3. Induction по Digital Passport: 72°C, 90 sec; LCD мигает «READY».  
4. Забирает за 2 min. Parallel: второй слот греет лапшу для другого пользователя.

### Пример 2 — Abandonment + fluid combo

1. User orders noodle cup → pays → heating starts.  
2. LCD «READY»; user не приходит 5 min → slot locked, €5.90 × 200% penalty, cup → waste chute.  
3. Другой user: dry coffee cup → pays → fluid station injects hot water → utensil dispenser выдаёт stirrer.

---

## §6. Отличия от аналогов (PPA 6)

| Аналог | Наше отличие |
|--------|--------------|
| Microwave vending | **Induction + Digital Passport + impedance auth**; pre-pay before energy |
| Standard hot-food locker | Нет **abandonment penalty + waste routing** |
| Hanging-cup dispensers | **Profiled channel** — guides body, not rim hang |
| Static pricing vending | **AI bidirectional** + external market + mechanical expiry lockout |
| Simple reservation apps | **Conditional n>1** walk-in priority rule |
| Fixed load-cell bins | **Vibration-isolated floating bin** with conical centering |

**Ключевые акценты:** pre-payment gating before heating; dual-zone + level-sensitive operations; profiled channel + ratchet; composite vessel selective heating; hybrid fluid interlock; floating bin metrology; AI pricing with safety lockout; master–slave cost sharing.

---

---

# Общие приложения (PPA 3–6)

## A. Соответствие рисунков и claims (сводка)

| Тема | PPA 3 | PPA 4 | PPA 5 | PPA 6 |
|------|-------|-------|-------|-------|
| Chassis / busbar | ✓ cl.1,19–21 | ✓ cl.1–4 | ✓ cl.1 | ✓ cl.1–2 |
| Sensor fusion | ✓ cl.1,11–12 | ✓ cl.1,3–4 | ✓ cl.1,5–8 | ✓ cl.5 |
| Token / consent | — | ✓ cl.1,5–9 | ✓ cl.1,10 | — |
| Split / multi-tenant | — | ✓ cl.11–12 | ✓ cl.11 | — |
| Master–slave | — | ✓ cl.16 | ✓ cl.13 | ✓ cl.1 |
| Auto-leveling | feet (manual) | feet | ✓ motorized cl.1–2 | ✓ cl.1 |
| Smart glass / restricted | ✓ cl.1,4,9 | ✓ cl.1,9,15 | inherited | — |
| Pricing AI | sensory+space | time+sensory+space | bidirectional cl.12 | AI cl.6 |
| Heating / fluid | — | — | temp interlock | ✓ cl.1–3,7 |
| FIFO / ESL | LED strip | LED strip | ✓ cl.3–4,14 | LCD strips |

## B. Дополнительные SVG в репозитории (черновики, RU)

| Файл | Может иллюстрировать |
|------|---------------------|
| `assets/figures/FIG_05_RU.svg` | Модульная система шкафов (типы модулей) |
| `assets/figures/FIG_03_RU.svg` | Процесс покупки (регистрация → оплата → чек) |
| `assets/figures/FIG_04_RU.svg` | Компоненты операционной платформы |

## C. PPA №7 — статус

**Не включён в настоящий пакет** (PDF заявки не приложены). По проектной документации (`MVP_TZ_PRODUCE_v1.md`): slave-модуль, vertical bus interface, перекonfigурируемые слоты, продуктовый узел выдачи. Требуется отдельная подготовка §1–6 после получения PDF.

---

*Документ не заменяет юридическую консультацию. Английские тексты заявок и claims — в исходных PDF заявителя.*

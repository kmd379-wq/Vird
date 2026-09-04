# Micro Shop — Submission Package for Ali (Patent Attorney)

**Language:** English (explanatory memo) · **Applications:** PPA #3, #4, #5, #6, #7  
**Date:** September 4, 2026  
**From:** Micro Shop / Applicant  
**Platform:** Modular Cabinet Platform

> **Russian version of this package:** [`MicroShop_Ali_Submission_RU.md`](MicroShop_Ali_Submission_RU.md)  
> **Architecture SVGs:** `assets/figures/ppa3456/PPA{3,4,5,6,7}_ARCH_RU.svg`  
> **Official EN specifications & claims:** applicant PDF files (listed below)

---

## Cover Letter

Dear Ali,

Please find our **complete inventor materials** for the Modular Cabinet Platform family, structured according to your **six requested items** for each provisional application.

**Your requirements (per application):**
1. Rough sketches or drawings of the device/system (hand-drawn or digital is fine)  
2. A diagram showing how the main components connect and interact  
3. A flowchart or step-by-step walkthrough of how the process/method works  
4. A plain-language description of each component and what it does  
5. One or two concrete examples of the invention in use  
6. Anything that makes your version different from existing/similar products  

**Process (as discussed):** Send **one complete application at a time**. Do not add or change materials during your preparation without agreement. Allow **≥2 weeks** per application after receipt of the full bundle.

**Note on PPA #6 vs PPA #7:** Both share the same English title (*Modular Retail System with Adaptive Architecture…*) but have **different claim sets and emphasis**. Please distinguish by USPTO application number and filing date, not title alone.

---

## Requirement Mapping (all PPAs)

| # | Your requirement | Where answered | Attachments |
|---|------------------|----------------|-------------|
| 1 | Sketches / drawings | **§1** below | `PPA#N FIGURES.pdf` + `PPA{N}_ARCH_RU.svg` |
| 2 | Connection diagram | **§2** | §2 + architecture SVG |
| 3 | Flowchart / process | **§3** | §3 |
| 4 | Component descriptions | **§4** | §4 tables |
| 5 | Use examples | **§5** | 2 examples each |
| 6 | Prior-art differences | **§6** | §6 tables |

### Applicant file checklist

| PPA | EN specification PDF | FIGURES | Filing receipt |
|-----|---------------------|---------|----------------|
| 3 | `PPA#3-ModularSmartVendingCabinet_Revised.pdf` | `PPA#3 FIGURES.pdf` | APP.FILE.REC |
| 4 | `PPA#4_SMART RETAIL CABINET_WITH_TOKENIZED_ACCESS_AND_SPLIT_PAYMENTS.pdf` | `PPA#4 FIGURES.pdf` | APP.FILE.REC |
| 5 | `PPA#5_SmartRetailCabinet_TokenizedAccess_SplitPayments.pdf` | `PPA#5 FIGURES.pdf` | APP.FILE.REC |
| 6 | `PPA#6_Modular_Retail_System.pdf` | `PPA#6 FIGURES.pdf` | APP.FILE.REC |
| 7 | `docs/source/ppa7/PPA7_Modular_Retail_System.pdf` | **`PPA#6 FIGURES.pdf`** (same drawings) | TBD |
| 7 RU | `docs/source/ppa7/02.09.2026_PPA7_RU.docx` | — | — |

**Suggested send order:** #3 → #4 → #5 → #6 → #7

---

# PPA #3 — Modular Smart Vending Cabinet

**Title:** Modular Smart Vending Cabinet with Smart-Glass Inspection Mode, Sensor-Fusion Manual Retrieval, and Quality-Based Dynamic Pricing  
**Claims:** 1–30 · **Figures:** FIG. 1–4 in `PPA#3 FIGURES.pdf`

## Summary

Autonomous modular cabinet on a unified chassis with vertical power/data bus and interchangeable dispensing modules (pusher, hook, scale zone, gravity gate channel, sliding tray, auto-disposal). **Manual** product retrieval — no gantry robot. **Sensor fusion** (RFID matrix + camera + load cells) confirms every pick. **Smart glass (PDLC)** for age-restricted items: opaque → biometric age check → transparent inspection → payment pre-auth → access. Pricing engine uses **sensory decay model** and **space-yield slot liberation** algorithm.

---

## §1. Sketches and Drawings (FIG. 1–4)

**Attachments:** `PPA#3 FIGURES.pdf` (official patent line art) · `PPA3_ARCH_RU.svg` (architecture block diagram)

**FIG. 1 — Front view:** Display (110), biometric camera “Eye” (105), payment interface, interchangeable modules A–D (pusher, hook, scale, gate), front-edge antenna matrix + LED smart edge, smart waste basket.

**FIG. 2 — Side view:** Peripheral controller (400), pricing engine, sensor fusion, local cache, UPS, vertical power bus, LTE/Wi-Fi.

**FIG. 3 — Sensor geometry:** Front antenna array, camera field of view, overlap zone for fusion. Hand in view without RFID pick event → alarm / deposit hold.

**FIG. 4 — Stock induction (FIFO):** Scan SKU → program RFID → enter expiry → rear-load FIFO → front-edge read at sale.

| Ref | Component | Function |
|-----|-----------|----------|
| 100 | Enclosure / door | Protected volume, access control |
| 105 | Biometric camera | Age verification before restricted access |
| 110 | Display / UI | Terms, prices, consent, digital sommelier |
| 120 | Front registration zone | Linear RFID matrix along shelf front edge |
| 400 | Edge controller | Pricing, fusion, offline cache, transactions |
| 500 | Dispensing modules A–G | Pusher, hook, scale, gate, tray, disposal |

---

## §2. Component Connection Diagram

```
USER (biometrics, display, payment)
        │
        ▼
EDGE CONTROLLER (400)
  · pricing · sensor fusion · access · transactions · offline cache
        │
   ┌────┼────┬────────┬─────────┐
   ▼    ▼    ▼        ▼         ▼
 Power  Camera RFID   Load    Modules A–G
 bus           matrix cells   (manual pick)
        │
        ▼
 Smart waste basket → (optional) Cloud / mobile app
```

| Flow | From → To | Data |
|------|-----------|------|
| D1 | Induction station → Controller | SKU, RFID UID, expiry, batch |
| D2 | Module sensors → Controller | Tag read, weight delta, gate state |
| D3 | Camera → Controller | Hand intrusion, pick gesture |
| D6 | Controller → Payment | Incremental capture per item |

---

## §3. Process Flowchart

**Standard mode:** Payment tap → unlock door → user manually removes item → sensor fusion (RFID + camera [+ weight]) → incremental charge at dynamic price → door close → release unused pre-auth.

**Restricted mode (smart glass):** Opaque glass → biometric age check → transparent inspection mode → product info on display → pre-auth → unlock → triple fusion (antenna + overhead camera + load cell) → charge.

**Gravity gate module (D):** Item 1 in scale bowl, gate locked → user takes item 1 → gate opens → item 2 drops → gate locks again.

**Dynamic pricing:** Inputs: expiry, dwell time, environment sensors, camera quality hints, turnover → sensory decay discount + space-yield slot discount → LED/display update.

---

## §4. Plain-Language Component Descriptions

| Module | Description |
|--------|-------------|
| Transformer-base chassis | Unified frame; vertical power bus; rear FIFO loading |
| Module A — Pusher | Spring track + adjustable divider; one-way ratchet |
| Module C — Scale box | Load cell zone for soft/amorphous packs |
| Module D — Gravity gate | Incline chute → weigh bowl → sequential gate |
| Smart edge | Antenna matrix + LED for zoning, navigation, discount cues |
| Smart glass (PDLC) | Opaque sleep mode → transparent inspection after age verify |
| Edge controller | Pricing, fusion, offline transactions, UPS-backed |
| Smart waste bin | Load cell + RFID for quarantine accounting |

---

## §5. Concrete Use Examples

**Example 1 — Residential lobby micro-store:** Tap-to-pay; manual yogurt pick from pusher module — RFID + camera capture, dynamic price charge; chocolate bar on sliding tray at 30% sensory-decay discount (LED highlight); unused pre-auth returned on door close.

**Example 2 — Age-restricted alcohol (smart glass):** Glass opaque until age ≥21 verified; transparent for vintage/region pairing info; $50 pre-auth; bottle removal confirmed by triple sensor fusion; partial consumption or return detected by load cell → lock / penalty.

---

## §6. Differences from Existing Products

| Prior art | Our difference |
|-----------|----------------|
| Gantry vending robot | **Manual pick** + unified sensor fusion |
| ID scan age gate | **Confidential smart-glass inspection** before access |
| Date-only dynamic pricing | **Sensory decay** + **space-yield slot liberation** |
| Single-mechanism vending | **6+ module types** on one power-bus chassis |
| Vision-only grab-and-go | Hardware-modular anchor + autonomous edge controller |

---

---

# PPA #4 — Tokenized Access & Split Payments

**Title:** Smart Retail Cabinet with Tokenized Access and Split Payments  
**Claims:** 1–20 · **Figures:** `PPA#4 FIGURES.pdf`

## Summary

Modular cabinet with **position-adjustable power/data interface** (bus / cable tray / harness), **QR token** access from mobile app and/or biometrics, **mandatory consent** (immediate charge on pick, no returns) before unlock. **Split settlement:** one checkout → multiple merchant accounts by tenant/slot. Multi-tenant shelf model. **Master–slave cluster:** one session, virtual basket, consolidated capture. Offline financial ledger + UPS.

---

## §1. Sketches and Drawings

Same figure topology as PPA #3 with PPA #4 emphasis:
- **FIG. 1:** Adjustable-position interface; LED info strip  
- **FIG. 2:** Transaction module — token decode, pre-auth, offline ledger, split routing, fiscal receipt  
- **FIG. 3:** External biometrics + internal inventory cameras; smart-glass restricted compartment  
- **FIG. 4:** **Upstream induction** — supplier warehouse tags product → allowed-manifest sync → cabinet recognizes without local scan  

**Attachments:** `PPA#4 FIGURES.pdf` · `PPA4_ARCH_RU.svg`

---

## §2. Component Connection Diagram

```
Mobile app ──QR token──► Scanner ──► Controller
Biometrics (external) ──────────────┤
                                    ▼
                          Transaction module
                          · pre-auth token · consent record
                          · virtual basket · split settlement
                          · offline ledger
                                    │
              ┌─────────────────────┼─────────────────────┐
              ▼                     ▼                     ▼
         MASTER block          SLAVE blocks         Remote server
         (payment, AI)         (sensors, locks)     (manifests, suppliers)
```

---

## §3. Process Flowchart

```
START → Scan QR / biometrics → Decode session token
  → Pre-authorization (fund hold)
  → Display terms: immediate charge · no returns · penalty rules
  → Require explicit AGREE
  → Restricted items? → Age from KYC token OR biometrics
  → Unlock access barrier
  → LOOP: manual pick → internal sensors → increment hold + purchase obligation
         → Mode A: instant capture OR Mode B: deferred until session end
         → Split routing to operator + supplier accounts
  → Session end → consolidated capture (Mode B) → digital + fiscal receipt
  → No network? Offline ledger capture → async reconciliation
  → No power? UPS maintains locks + event logging
```

---

## §4. Plain-Language Component Descriptions

| Component | What it does |
|-----------|--------------|
| Position-adjustable interface | Power/data without rewiring when shelf height changes |
| QR / token scanner | Session token from KYC-verified mobile app |
| External biometric sensor | ID outside storage volume |
| Consent UI | Display + “Agree”; timestamped consent record |
| Transaction module | Pre-auth, incremental hold, instant vs consolidated capture |
| Split settlement engine | Basket split by item/slot → multiple merchant accounts |
| Multi-tenant controller | Per-supplier inventory, pricing, alerts |
| Offline ledger | Local capture when network down |
| Master–slave cluster | Payment/AI on master; slaves provide sensors and locks |

---

## §5. Concrete Use Examples

**Example 1 — Multi-tenant airport micro-store:** QR scan; €30 pre-auth; agree to terms; water (Tenant A) + snack (Supplier B); split: €2 → A, €4.50 → B; one receipt in app.

**Example 2 — Master–slave cluster (6 cabinets, 1 terminal):** Single authorization on master; customer walks slaves 1–5; virtual basket on master; consolidated capture on exit; one fiscal receipt.

---

## §6. Differences from Existing Products

| Prior art | Our difference |
|-----------|----------------|
| Standard vending | No tokenized session + auditable mandatory consent |
| Single-vendor cabinet | **Multi-tenant shelves** + **hardware-initiated payment split** |
| Standalone cabinets only | **Master–slave** BOM reduction |
| Cloud-dependent grab-and-go | **Offline ledger + UPS** |
| Local induction only | **Upstream manifest** — pre-tagged goods without local scan |

---

---

# PPA #5 — Revision: Leveling, Visual Tracking, ESL/FIFO

**Title:** Smart Retail Cabinet with Tokenized Access and Split Payments (revised)  
**Claims:** 1–16 · **Figures:** `PPA#5 FIGURES.pdf`

## Summary

Evolution of PPA #4 with **motorized auto-leveling** (inclinometer + screw jacks, ~0.5° threshold), **Visual Tracking Layer** (always-on internal cameras) + selectable physical layer (load cell + RFID vs beam break + anti-return), **ESL/LCD shelf-edge displays** with **FIFO metadata queue**, **progressive biometric enrollment** with cloud roaming, **punitive penalty** = multiple of highest SKU price in cabinet.

---

## §1. Sketches and Drawings

PPA #4 topology plus:
- **FIG. 1:** Motorized leveling feet; ESL strip with expiry + dynamic price; rear service door  
- **FIG. 2:** Visual Tracking Layer + dual detection configs; progressive biometric enrollment flow  
- **FIG. 3:** High-value zone (load cell + RFID) vs standard zone (beam break + ratchet)  
- **FIG. 4:** FIFO queue → automatic ESL update when item removed  

**Attachments:** `PPA#5 FIGURES.pdf` · `PPA5_ARCH_RU.svg`

---

## §2. Component Connection Diagram

```
Inclinometer ──► Controller ──► Motorized leveling feet
                      │
Internal cameras (Visual Tracking Layer, continuous)
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
  High-value zone              Standard zone
  Load cell + RFID             Beam break + anti-return ratchet
                      │
              ESL / LCD shelf edge
                      │
         Token / biometrics → Session → Split payments
                      │
              Cloud biometric vault (roaming)
```

---

## §3. Process Flowchart

**Leveling:** Power on → read inclinometer → if tilt >0.5° → drive actuators → if still above threshold → **block session start**.

**ESL FIFO:** Virtual FIFO queue by slot expiry → display price + expiry of **first** item in queue → on pick → update ESL for **next** item.

**Progressive biometrics:** Session 1: QR auth → optional face capture + enrollment consent → upload vector to cloud → Session N elsewhere: face match → validate regional payment instrument → seamless biometric entry or block.

**Penalty:** Unauthorized weight increase / forced return not confirmed by Visual Tracking Layer → charge = **MULTIPLE × highest SKU price** (consent recorded before unlock).

---

## §4. Plain-Language Component Descriptions

| Component | What it does |
|-----------|--------------|
| Motorized leveling system | Actuators + inclinometer; auto-level; block sales when tilted |
| Visual Tracking Layer | Always-on internal cameras; hand and product tracking |
| Selectable physical layer | High-value: scale + RFID; Standard: beam break + ratchet |
| ESL / LCD shelf edge | Real-time price and batch/expiry; auto FIFO update |
| Smart bin | Dedicated load cell; amorphous goods; charge by weight loss |
| Cloud biometric vault | Cross-cabinet / cross-region recognition |
| Penalty engine | Fraud deterrent beyond unit price |

---

## §5. Concrete Use Examples

**Example 1 — Milk pouch smart bin:** Leveling OK (0.3°); QR + consent; customer takes 2 pouches (−1020 g) → charge; attempt to return one pouch (+510 g) without camera confirmation → penalty = 3× max SKU.

**Example 2 — Deli tray temperature lock:** ESL shows salad expiry €4.20; temp sensor 8°C > 6°C limit → **sale blocked**; cabinet moved — session blocked until tilt <0.5°.

---

## §6. Differences from Existing Products

| vs PPA #4 / market | PPA #5 difference |
|--------------------|-------------------|
| Static leveling feet | **Active motorized leveling** with transaction block |
| RFID-only or camera-only | **Dual-layer fusion**: continuous CV + zonal physics |
| Paper / static price tags | **ESL FIFO queue** — auto metadata for next item |
| Device-only biometrics | **Progressive enrollment + cloud roaming** + regional payment check |
| Flat return penalty | **Multiple of maximum SKU price** |

---

---

# PPA #6 — Adaptive Architecture (Climate, Heating, Fluid)

**Title:** Modular Retail System with Adaptive Architecture, AI-Driven Pricing, and Integrated Consumables Management  
**Claims:** 1–8 · **Figures:** `PPA#6 FIGURES.pdf`

## Summary

Autonomous or **master–slave** ecosystem; **dual-zone climate** (fridge +2…+4°C + isolated heating positions); **induction heating** to consumption temperature without boiling; **mandatory pre-pay before heating starts**; **abandonment penalty** (200% if not collected in 5 min); **profiled dispensing channel** with anti-return ratchet; **hybrid fluid station** (dry mix + hot water); **floating smart bin**; **composite vessel** with selective heating zones; **bidirectional AI pricing**; conditional remote reservation (walk-in priority when stock n>1).

---

## §1. Sketches and Drawings

- **FIG. 1:** Front view — reconfigurable chassis, sensor zone, LED/LCD strips  
- **FIG. 2:** Controller — heating queue, payment lock, AI pricing, master–slave orchestration  
- **FIG. 3:** Dual-zone climate cross-section — fridge / heating zone / thermal curtain; profiled channel section  
- **FIG. 4:** Transaction + heating flow — pre-pay → heat → pickup timer → penalty  

**Concept sketch — dual zone:**
```
┌ FRIDGE (+2…+4°C) ─ thermal curtain ─ HEATING (induction) ─┐
│ Profiled channel · gravity · floating bin                  │
│ LCD strip: flashing "READY"                              │
├ Hybrid fluid station (interlocked) · utensil dispenser · waste chute ┤
└──────────────────────────────────────────────────────────┘
```

**Attachments:** `PPA#6 FIGURES.pdf` · `PPA6_ARCH_RU.svg`

---

## §2. Component Connection Diagram

```
Optional MASTER (payment · AI · session)
        │
        ▼
Cabinet controller (leveling · heat queue · AI prices · locks)
        │
   ┌────┼────┬────────┬──────────┬──────────┐
   ▼    ▼    ▼        ▼          ▼          ▼
Inclinometer Induction Load    RFID/LCD   Fluid station
             coils    cells              (interlock)
        │
        ▼
Cloud telemetry · remote pricing · conditional reservation
Mobile apps: supplier + consumer
```

---

## §3. Process Flowchart

**Heated product:** Select item (QR/biometric) → read Digital Cooking Passport from tag → show price on slot map → confirm → **PRE-PAY BEFORE HEAT** → check tilt / auto-level → run induction profile + impedance auth → heat complete → LCD “READY” → 5 min timer → collected OK OR slot lock + waste route + 200% penalty.

**Fluid station (noodles/coffee):** Confirmed SKU at fluid position → pre-pay → heat/dispense hot water → utensil dispenser releases spoon/stirrer per SKU.

**Conditional reservation:** Mobile reservation request → if stock ≤1 → **DENY** (walk-in priority) → if stock >N → hold + timer → scan in time OR timeout releases hold.

---

## §4. Plain-Language Component Descriptions

| Component | What it does |
|-----------|--------------|
| Master–slave architecture | Standalone OR slave delegates payment/AI to master |
| Dual-zone climate | Fridge + thermally isolated heating positions + curtains |
| Active auto-leveling | Inclinometer + motorized feet; block heat/fluid when tilted |
| Profiled dispensing channel | U-profile + ratchet; varied container heights |
| Induction subsystem | Target temp under film; impedance packaging authentication |
| Hybrid fluid station | Temperature/volume control; SKU interlock |
| Floating smart bin | Vibration-isolated; conical centering; door-slam filter |
| AI pricing module | Decay + surge + external market; mechanical lock on expired RFID |
| Reservation server | n>1 rule; timer; walk-in priority |

---

## §5. Concrete Use Examples

**Example 1 — Office hot-food cabinet:** QR scan; slot map shows “Soup #3 — €5.90”; confirm → **pay before heat**; induction to 72°C / 90 sec; LCD “READY”; collected in 2 min; parallel slot heats noodles for another user.

**Example 2 — Abandonment + fluid station:** User orders cup noodles → pays → heating starts; “READY” but no pickup in 5 min → slot locked, €5.90 × 200% penalty, cup to waste chute. Another user: dry coffee cup → pay → fluid station fills hot water → stirrer dispensed.

---

## §6. Differences from Existing Products

| Prior art | Our difference |
|-----------|----------------|
| Microwave vending | **Induction + Digital Passport + impedance auth**; pre-pay before energy |
| Standard hot-food locker | No **abandonment penalty + waste routing** |
| Rim-hang dispensers | **Profiled channel** guides body, not rim |
| Static-price vending | **Bidirectional AI** + external market + mechanical expired-tag lock |
| Simple reservation apps | **Conditional n>1 rule** — walk-in shelf priority |
| Fixed bin load cells | **Vibration-isolated floating bin** |

---

---

# PPA #7 — Extended Ecosystem (same title as #6, different claims)

**Title (EN):** Modular Retail System with Adaptive Architecture, AI-Driven Pricing, and Integrated Consumables Management  
**Claims:** 1–5 · **Figures:** **`PPA#6 FIGURES.pdf`** (same FIG. 1–4 as PPA #6 — confirmed by applicant)  
**EN PDF:** `docs/source/ppa7/PPA7_Modular_Retail_System.pdf`  
**RU translation:** `docs/source/ppa7/02.09.2026_PPA7_RU.docx`

> **⚠️ Same title as PPA #6 — different content.** PPA #7 adds: hermetic induction chamber + **negative-pressure ventilation**, **freezer waste module** (< −2°C), **45° conical bunker** with **single central load cell**, **shrinkage compensation**, **aggregate weight verification gate** at exit, **smart water cooler + utensil dispenser sync**, **Space-Yield Engine**, **instant split smart contract**, extension to **open retail (ESL)**.

## Summary

Autonomous retail **ecosystem**: reconfigurable “transformer-base” chassis, interchangeable storage/processing modules, distributed sensor network. **Hybrid thermal architecture:** cold storage + **hermetic induction chamber** with susceptor packaging and RFID culinary profile; **negative-pressure ventilation** removes steam/odors from cold zone; **freezer waste module** for unclaimed heated items + transactional penalty. **Bulk station:** **45° conical bunker** with **one central load cell**, motorized leveling, **shrinkage price compensation**, **exit aggregate weight gate**. **Space-Yield Displacement Engine**. Ecosystem sync with **smart water cooler** and **utensil dispenser**; multi-tenant **instant payment split smart contract**.

---

## §1. Sketches and Drawings

**Official figures:** `PPA#6 FIGURES.pdf` (identical to PPA #6).  
**Supplement:** `PPA7_ARCH_RU.svg`

**FIG. 1 — Front view:** Transformer-base chassis; vertically repositionable shelves on power/data bus; front sensor zone with antenna grid + LED strip; induction chamber; smart glass.

**FIG. 2 — Controller / transactions:** Biometrics and/or QR token; pre-auth; offline ledger; split payments; cloud manifest/pricing.

**FIG. 3 — Shelf sensor geometry:** Front antenna grid, overhead camera, load cells; PDLC smart-glass compartment for restricted goods.

**FIG. 4 — Stock induction + transactions:** Supplier tags product → manifest sync → customer auth → pick → split charge → receipt.

| Ref | Component | Function |
|-----|-----------|----------|
| 110 | Induction chamber | Hermetic susceptor heating per RFID culinary profile |
| 120 | −ΔP ventilation | Steam/odor exhaust away from cold zone |
| 130 | Freezer waste module | < −2°C; timeout disposal + penalty |
| 140 | 45° bunker | Single central load cell; no corner-load errors |
| 150 | Aggregate weight gate | Exit barrier only if Σ weights match |
| 160 | Space-Yield Engine | AI pricing: quality + volume + demand |
| 170 | Smart cooler / utensils | 350 ml water per SKU; fork/spoon/chopsticks by dish type |

---

## §2. Component Connection Diagram

```
EDGE CONTROLLER + TRANSACTION MODULE
  Auth · offline · split · Space-Yield AI
        │
   ┌────┼────┬──────────┬─────────────┐
   ▼    ▼    ▼          ▼             ▼
Sensor  Induction  45° bunker   PDLC smart glass
network  + −ΔP     + leveling
        │
        ▼
Aggregate weight gate (exit)
        │
   ┌────┼────┬──────────────┐
   ▼    ▼    ▼              ▼
Freezer  Smart water   Utensil
waste    cooler         dispenser
        │
Master–slave cluster ↔ Cloud ↔ Supplier apps (multi-tenant)
```

---

## §3. Process Flowchart

**Heated item:** Auth → select SKU with Digital Passport → pre-pay → induction in sealed chamber with −ΔP active → “READY” + pickup timer → collected OR timeout → disposal to freezer waste (< −2°C) → log → penalty.

**Bulk + exit gate:** Pick from 45° bunker → central load cell delta → SKU match → accumulate Σ weight (bulk + packaged) → exit platform weighs Σ → match within tolerance → barrier opens OR alarm.

**Space-Yield + split:** AI: texture (camera) + shrinkage (weight) + occupied volume → price adjustment → smart contract instant split operator ↔ supplier.

---

## §4. Plain-Language Component Descriptions

| Component | What it does |
|-----------|--------------|
| Transformer-base chassis | Vertical bus; swap modules without rewiring |
| Hermetic induction chamber | Susceptor heating per RFID profile |
| Negative-pressure ventilation | Keeps steam out of refrigerated zone |
| Freezer waste module | Sanitary disposal; bacterial growth stop |
| 45° bunker + 1 load cell | Gravity to center; simpler calibration |
| Motorized leveling | Gyro + actuators for gravimetric accuracy |
| Shrinkage compensation | Exponential unit-price correction for moisture loss |
| Aggregate weight gate | Exit control for sum of all session picks |
| Space-Yield Engine | Optical + gravimetric quality; spatial opportunity cost |
| Smart cooler sync | Dispense exact water volume (e.g. 350 ml) for SKU |
| Utensil dispenser | Fork/spoon/chopsticks matched to product type |
| Multi-tenant split | Supplier manages own cell; instant revenue split |
| Open retail extension | Methods apply to ESL-equipped open shelves, not only closed cabinet |

---

## §5. Concrete Use Examples

**Example 1 — Office: soup + water + utensil:** Biometric auth; smart glass stays opaque for alcohol until separate age check; soup induction with −ΔP; cabinet commands **smart cooler** for 350 ml water; **utensil dispenser** releases spoon; split payment: operator + soup supplier + water supplier.

**Example 2 — Bulk produce + exit gate:** Customer takes potato net from 45° bunker and tray pack; controller sums weights; **shrinkage compensation** lowers €/kg if moisture loss detected; exit platform Σ matches → barrier opens; another user misses heated lunch 5 min after “READY” → item to **freezer waste**, 200% penalty.

---

## §6. Differences from Existing Products

| Prior art | PPA #7 difference |
|-----------|-------------------|
| PPA #6 (same title) | PPA #7: **−ΔP vent**, **freezer waste < −2°C**, **45°/1 sensor**, **Σ exit gate**, **cooler+utensils**, **open retail ESL** |
| Microwave vending | Induction + susceptor + RFID profile; steam routed from cold zone |
| Fridge with inline heater | Zone separation + sealed chamber + sanitary freezer disposal |
| Multi-cell bunker scales | **Single central cell** at 45° |
| No exit verification | **Aggregate weight gate** |
| Static pricing | **Space-Yield Engine** |
| Centralized escrow | **Instant split smart contract** |
| Closed cabinet only | Extends to **open retail** with ESL + cameras |

---

---

# Send Instructions (one application at a time)

### Example email — PPA #3 (send first)

**Subject:** Micro Shop — PPA #3 — Complete Material Package

**Attachments:**
1. `PPA#3-ModularSmartVendingCabinet_Revised.pdf`  
2. `PPA#3 FIGURES.pdf`  
3. APP.FILE.REC  
4. `PPA3_ARCH_RU.svg`  
5. This document — **PPA #3 section (§1–6)** exported to PDF  
6. (Optional) Full `MicroShop_Ali_Submission_EN.md` or `MicroShop_Ali_Submission_RU.md`

Repeat for PPA #4, #5, #6, #7 with respective files. For **PPA #7**, attach `PPA#6 FIGURES.pdf` instead of a separate figure set.

---

*This memo does not replace legal advice. English specification PDFs and claim text remain authoritative for USPTO filing.*

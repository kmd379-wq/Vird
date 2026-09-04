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

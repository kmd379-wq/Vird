# PPA #3 — Modular Smart Vending Cabinet

**Title:** Modular Smart Vending Cabinet with Smart-Glass Inspection Mode, Sensor-Fusion Manual Retrieval, and Quality-Based Dynamic Pricing  
**Claims:** 1–30 · **Figures:** FIG. 1–4 in `PPA#3 FIGURES.pdf`

## Summary

Autonomous modular cabinet on a unified chassis with vertical power/data bus and interchangeable dispensing modules (pusher, hook, scale zone, gravity gate channel, sliding tray, auto-disposal). **Manual** product retrieval — no gantry robot. **Sensor fusion** (RFID matrix + camera + load cells) confirms every pick. **Smart glass (PDLC)** for age-restricted items: opaque → biometric age check → transparent inspection → payment pre-auth → access. Pricing engine uses **sensory decay model** and **space-yield slot liberation** algorithm.

---

## §1. Sketches and Drawings (FIG. 1–4)

**Attachments:** `PPA#3 FIGURES.pdf` (filed USPTO line art, FIG. 1–4) · `PPA3_ARCH_EN.svg` (supplemental platform architecture)

> **Scope note:** Filed FIG. 1–4 emphasize front-zone hardware, offline edge architecture, dual-loop pricing/transaction control, and the induction workflow. Interchangeable dispensing modules A–G, smart glass (PDLC), smart waste basket, vertical power bus, and sensor-overlap geometry are disclosed in the specification and illustrated in **`PPA3_ARCH_EN.svg`** (new supplemental figure for NPPA #1).

### FIG. 1 — Autonomous Retail Cabinet Front View and Front-Zone Antenna

**Caption (filed):** *Camera and front-zone antenna support sensor-fusion anti-theft monitoring.*

| Element shown | Description |
|---------------|-------------|
| 105 Biometric / age-verification camera | Top center; downward field of view into cabinet interior |
| 110 User-facing display | Terms, prices, cart / session UI on right panel |
| Payment interface | Contactless (NFC), card slot, payment network logos |
| Smart shelves | Multi-level shelving stocked with retail products |
| 120 Front-zone antenna region | Linear **RFID antenna array along shelf front edge** |
| Sensor-fusion (caption) | Camera + front-zone RFID jointly support anti-theft monitoring |

**Not shown in filed FIG. 1** (specification + `PPA3_ARCH_EN.svg`): interchangeable modules A–G (pusher, hook, scale zone, gravity gate, sliding tray, auto-disposal), PDLC smart-glass compartment, smart waste basket, LED smart edge.

### FIG. 2 — Side Section Showing Electronics Bay and Offline Architecture

**Caption (filed):** *Side section — electronics bay and offline-capable edge architecture.*

| Element shown | Description |
|---------------|-------------|
| Main storage volume | Upper cabinet interior (dashed shelf lines) |
| Electronics bay | Lower compartment housing edge processing |
| 400 Edge controller | Main processing unit; hub for all local subsystems |
| Local database / cache | Product catalog, session state, pricing rules cache |
| Local transaction buffer | Offline storage when network / cloud unavailable |
| Communication modules | LTE / Wi-Fi / Ethernet uplink |
| Door control | Door lock and actuators |
| Item counting | Shelf sensors / item counters |
| Cabinet sensors | Environment, temperature, tamper, etc. |
| External network / cloud AI | Dashed path; **“Operation continues when unavailable”** |

**Not shown in filed FIG. 2** (specification + architecture SVG): vertical power bus, UPS, explicit pricing-engine block, physical module-to-bus wiring.

### FIG. 3 — Dual-Loop Control: Background Shrinkage Monitoring and Transaction Processing

**Caption (filed):** *Dual-loop control — continuous background monitoring and item-removal transaction processing.*

**Left column — continuous background monitoring (loop):**

1. Read bin weight **W(t)**
2. Compute shrinkage **ΔW%** vs. initial weight **W₀**
3. Classify gradual evaporation-driven shrinkage (e.g., produce moisture loss)
4. Update freshness index **FI**
5. Update current dynamic unit price **P(t)** → loop back to step 1

**Right column — transaction loop (item removal events):**

1. Detect sudden weight drop
2. Correlate with vision audit (camera evidence)
3. Confirm item removal event
4. Compute charge = exact removed weight × current unit price **P(t)**
5. Log transaction (per-user session)
6. Provide data for exit security verification (compare exit weight vs. charged weight)

**Cross-loop data (dashed):** updated **FI** and **P(t)** feed the transaction loop (vision correlation and charge computation).

**Relationship to other figures:** FIG. 3 covers **quality-based dynamic pricing** and **weight + vision fusion at transaction time**. Front-zone RFID anti-theft geometry is shown in FIG. 1 and FIG. 4; full modular dispensing layout is in `PPA3_ARCH_EN.svg`.

### FIG. 4 — Induction and Stocking Workflow Linked to Front-Zone Hardware

**Caption (filed):** *Induction and stocking workflow linked to front-zone hardware.*

| Step | Action |
|------|--------|
| 1 | **Induction station / handheld scanner** — staff-facing mobile terminal |
| 2 | Parallel capture: scan product **barcode** · scan/program **RFID tag** · input **expiration date** |
| 3 | **Associate SKU + expiration data with unique RFID identifier** (database record) |
| 4 | **Stock items on smart shelves** |
| 5 | **Front-zone antenna array + camera** — hardware that monitors the stocked shelf edge |
| 6 | **Monitoring during user sessions:** detect removals via RFID · verify hand movements via camera · **sensor-fusion for anti-theft** |

**Specification detail not drawn on FIG. 4:** rear **FIFO** loading into specific dispensing modules (A–G); front-edge read at sale (FIG. 1 / FIG. 4 together imply this sequence).

### Reference numerals (specification ↔ figures)

| Ref | Component | In filed FIG. 1–4? |
|-----|-----------|-------------------|
| 100 | Enclosure / door | FIG. 1 (implied) |
| 105 | Biometric camera | FIG. 1 |
| 110 | Display / UI | FIG. 1 |
| 120 | Front registration zone (RFID matrix) | FIG. 1, FIG. 4 |
| 130 | Load cells / scale structures | FIG. 3 (weight loops); architecture SVG |
| 400 | Edge controller | FIG. 2 |
| 500 | Dispensing modules A–G | Architecture SVG + specification only |

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

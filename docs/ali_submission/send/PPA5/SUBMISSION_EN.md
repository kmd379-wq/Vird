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

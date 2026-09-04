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

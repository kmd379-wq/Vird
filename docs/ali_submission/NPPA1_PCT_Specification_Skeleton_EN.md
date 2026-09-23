# PCT Specification Skeleton — Application #1
## Modular Cabinet Platform (Priority: U.S. PPAs #3–#7)

**Document type:** Draft framework for attorney / draftsman — **not** a filed specification  
**Source memo:** `NPPA1_Modular_Cabinet_Platform_EN.md` (2026-09-06)  
**Status:** Content migrated; claims and figure renumbering **TBD by counsel**

---

## Document map (standard PCT / US non-provisional order)

| Order | Section | Status in this draft |
|------:|---------|----------------------|
| — | Title | §1 below |
| — | Cross-Reference to Related Applications | §2 below |
| 1 | Technical Field | §3 below |
| 2 | Background of the Invention | §4 below |
| 3 | Summary of the Invention | §5 below |
| 4 | Brief Description of the Drawings | §6 below |
| 5 | Detailed Description of Embodiments | §7 below |
| 6 | **Claims** | §8 below — **PLACEHOLDERS ONLY** |
| 7 | Abstract | §9 below |

**Figure strategy (for counsel):** Filed `PPA#3 FIGURES.pdf` … `PPA#5 FIGURES.pdf` and shared `PPA#6 FIGURES.pdf` (PPA #6 + #7) remain the primary USPTO drawings. Supplemental architecture SVGs (`PPA3_ARCH_EN.svg` … `PPA7_ARCH_EN.svg`) support re-drafting into formal PCT figures. Renumber into a single continuous FIG. 1–N series before filing.

---

# §1. TITLE OF THE INVENTION

**[PROPOSED TITLE — counsel to finalize]**

> **Modular Retail Cabinet Platform with Sensor-Fusion Checkout, Tokenized Multi-Tenant Settlement, Adaptive Climate and Induction Modules, and Integrated Consumables Ecosystem**

*Alternate short title (aligned with PPA #3 filed title):*  
> Modular Smart Vending Cabinet with Smart-Glass Age Verification, Sensor-Fusion Anti-Theft, and Dynamic Pricing

---

# §2. CROSS-REFERENCE TO RELATED APPLICATIONS

**[ATTORNEY: insert exact application numbers, filing dates, and titles from USPTO receipts]**

This application claims the benefit of priority under 35 U.S.C. § 119(e) and/or as a continuation-in-part (if applicable) of the following U.S. provisional patent applications, each incorporated herein by reference in its entirety:

| Ref | Provisional | Filed title (short) | Claims | Figures |
|-----|-------------|----------------------|--------|---------|
| PPA #3 | `[APP. NO. TBD]` / `[DATE TBD]` | Modular Smart Vending Cabinet … Smart-Glass … Sensor-Fusion … Dynamic Pricing | 1–30 | `PPA#3 FIGURES.pdf` |
| PPA #4 | `[APP. NO. TBD]` / `[DATE TBD]` | Smart Retail Cabinet with Tokenized Access and Split Payments | 1–20 | `PPA#4 FIGURES.pdf` |
| PPA #5 | `[APP. NO. TBD]` / `[DATE TBD]` | Smart Retail Cabinet … (leveling, VTL, ESL) | 1–16 | `PPA#5 FIGURES.pdf` |
| PPA #6 | `[APP. NO. TBD]` / `[DATE TBD]` | Modular Retail System … Adaptive Architecture, AI Pricing, Consumables | 1–8 | `PPA#6 FIGURES.pdf` |
| PPA #7 | `[APP. NO. TBD]` / `[DATE TBD]` | *Same English title as PPA #6* | 1–5 | `PPA#6 FIGURES.pdf` *(same)* |

**Priority note (per counsel guidance):** NPPA #1 / PCT should list priority to **each** of PPAs #3–#7 where subject matter is adequately supported. For overlapping disclosure in PPA #6 and PPA #7 (identical filed figures, different claims), claim dual priority to both where supported. USPTO does not examine entitlement to priority during prosecution; support may be tested in litigation.

---

# §3. TECHNICAL FIELD

The present disclosure relates to automated retail systems, and more particularly to modular unattended retail cabinets and platforms that combine:

- reconfigurable hardware chassis with interchangeable dispensing modules;
- manual customer retrieval with multi-modal sensor fusion for inventory and anti-theft verification;
- tokenized access, mandatory consent capture, and multi-tenant payment splitting;
- reliability subsystems including motorized leveling, visual tracking, and electronic shelf-label FIFO queues;
- dual-zone climate control with induction heating, pre-payment gating, fluid dispensing, and abandonment handling; and
- ecosystem extensions including hermetic induction, negative-pressure ventilation, aggregate exit weight verification, and AI-driven space-yield pricing.

The systems may operate fully or partially offline at the edge, with deferred cloud settlement and upstream supplier manifest synchronization.

*(Platform scope: PPA #3 hardware core → PPA #4 access/payments → PPA #5 reliability → PPA #6 thermal/fluid → PPA #7 ecosystem extension.)*

---

# §4. BACKGROUND OF THE INVENTION

## 4.1 Conventional unattended retail

Conventional vending machines typically employ a single dispensing mechanism (spiral, elevator, or gantry), limited payment interfaces, and static pricing. Grab-and-go smart coolers often rely on weight change alone or on vision alone, which can produce false charges or missed detections when items are similar in weight or occluded.

## 4.2 Access, consent, and multi-tenant settlement

Prior QR-based retail flows may lack auditable, hardware-enforced consent before unlocking inventory. Multi-supplier shelves in a single physical cabinet rarely support automatic split settlement initiated at the edge without a centralized point-of-sale terminal per tenant.

## 4.3 Physical reliability and presentation

Cabinet tilt affects load-cell accuracy and can invalidate weight-based charging. Static electronic shelf labels do not automatically reflect first-expired-first-out queue changes when a front-facing unit is removed. Continuous camera monitoring and zonal physical sensors are not commonly fused with progressive cloud-stored biometric enrollment across locations.

## 4.4 Heated food, fluids, and abandonment

Microwave-based vending does not typically authenticate a tagged culinary profile via induction impedance, pre-authorize payment before energizing a heating coil, or route abandoned heated product through a timed waste path with a contractual penalty. Dual-zone cabinets may suffer odor and steam migration from a hot zone into a refrigerated zone without dedicated negative-pressure exhaust.

## 4.5 Bulk dispensing and exit verification

Bulk product channels often use multiple load cells or rim-hung weighing that drifts under vibration. Exit gates in manual-pick cabinets may verify individual RFID events but not aggregate session weight against a platform scale at egress.

## 4.6 Distinctions sought (summary)

The platform addresses these gaps through, inter alia: manual pick with RFID + camera (+ weight) fusion; smart-glass confidential age inspection; sensory-decay and space-yield dynamic pricing; tokenized sessions with mandatory AGREE consent and offline ledger; master–slave cabinet clusters; motorized leveling with session block; Visual Tracking Layer fused with zonal physics; ESL FIFO metadata queues; induction pre-pay with Digital Cooking Passport; hermetic induction with −ΔP ventilation and freezer waste; 45° conical bunker with single central load cell; aggregate Σ weight exit gate; and smart cooler / utensil synchronization with instant split smart contracts.

**[ATTORNEY: expand with formal prior-art citations if required for PCT ISR]**

---

# §5. SUMMARY OF THE INVENTION

In one aspect, a modular retail cabinet platform comprises a transformer-base chassis supporting a plurality of interchangeable modules on a shared power and data bus, an edge controller with offline transaction cache, a front-zone RFID antenna array combined with at least one camera for sensor-fusion monitoring of manual retrieval, and a payment interface configured for dynamic pricing based on at least one of expiry, dwell time, environmental condition, and visual quality hints.

In another aspect, a tokenized access subsystem decodes a session QR or equivalent token, captures mandatory consent with timestamp before unlock, routes multi-tenant split settlement among operator, shelf tenant, and upstream supplier accounts, and maintains an offline ledger when cloud connectivity is unavailable.

In another aspect, a reliability layer includes motorized leveling feet driven by an inclinometer with transaction block above a tilt threshold, a Visual Tracking Layer operating concurrently with zone-specific physical detectors, electronic shelf labels updated from a FIFO metadata queue, and a penalty engine applying a multiple of a highest SKU price upon unauthorized weight increase or unconfirmed return.

In another aspect, a dual-zone climate subsystem separates refrigerated and heating regions with a thermal curtain, provides induction heating only after pre-payment confirmation, executes a Digital Cooking Passport profile read from an item tag, and upon pickup timeout routes the item to waste while applying an abandonment penalty.

In another aspect, an ecosystem extension includes a hermetic induction chamber with susceptor packaging, negative-pressure exhaust (−ΔP) venting steam away from the cold zone, a freezer waste module below −2 °C for timed disposal, a 45° conical bulk bunker with a single central load cell and shrinkage compensation, an aggregate weight verification gate comparing summed session pick weights to an exit platform measurement, a Space-Yield Displacement Engine adjusting price by optical quality, occupied volume, and demand, and synchronized smart water cooler and utensil dispensers with instant split settlement.

Methods of operating the platform, computer-readable media, and master–slave clusters are also contemplated.

**[ATTORNEY: align summary paragraphs with independent claims selected in §8]**

---

# §6. BRIEF DESCRIPTION OF THE DRAWINGS

The following description references drawings. Reference numerals are illustrative; counsel should harmonize numerals across merged figures.

## 6.1 Filed figures (from provisional applications)

### From PPA #3 (`PPA#3 FIGURES.pdf`)

**FIG. 1** is a front view of an autonomous retail cabinet showing a biometric/age camera (105), display (110), payment interface, smart shelves, and an RFID antenna array along a shelf front edge (120).

**FIG. 2** is a side section showing an electronics bay with edge controller (400), local database/cache, offline transaction buffer, communications (LTE/Wi-Fi/Ethernet), door control, item counting, and cabinet sensors; cloud connectivity is shown as optional with operation continuing when unavailable.

**FIG. 3** is a dual-loop control diagram: a background shrinkage monitoring loop (W(t) → ΔW% vs W₀ → evaporation classification → freshness index FI → dynamic price P(t)) and a transaction loop (sudden weight drop → vision audit → confirm removal → charge = weight × P(t) → log session → exit weight verification).

**FIG. 4** is an induction and stocking workflow linked to front-zone hardware: barcode + RFID program + expiry → associate SKU with UID → stock smart shelves → front-zone antenna + camera → session monitoring.

### From PPA #4 (`PPA#4 FIGURES.pdf`)

**FIG. [TBD]** *(renumber)* shows a position-adjustable power/data interface and LED information strip.

**FIG. [TBD]** shows a transaction module with token decode, pre-authorization, offline ledger, split routing, and fiscal receipt generation.

**FIG. [TBD]** shows external biometrics and internal inventory cameras with a smart-glass restricted compartment.

**FIG. [TBD]** shows upstream induction: supplier warehouse tags product → allowed-manifest sync → cabinet recognition without local scan.

### From PPA #5 (`PPA#5 FIGURES.pdf`)

**FIG. [TBD]** shows motorized leveling feet, ESL strip displaying expiry and dynamic price, and rear service door.

**FIG. [TBD]** shows Visual Tracking Layer cameras and dual detection configurations with progressive biometric enrollment.

**FIG. [TBD]** contrasts a high-value zone (load cell + RFID) with a standard zone (beam break + anti-return ratchet).

**FIG. [TBD]** shows FIFO metadata queue driving automatic ESL update when a front item is removed.

### From PPA #6 and PPA #7 (shared `PPA#6 FIGURES.pdf`)

**FIG. [TBD]** is a front view of a reconfigurable chassis with sensor zone and LED/LCD strips.

**FIG. [TBD]** is a controller diagram with heating queue, payment lock, AI pricing, and master–slave orchestration.

**FIG. [TBD]** is a dual-zone cross-section: refrigerated zone / heating zone / thermal curtain; profiled dispensing channel.

**FIG. [TBD]** is a transaction and heating flow: pre-pay → heat → pickup timer → penalty on timeout.

## 6.2 Supplemental architecture figures (to be formalized for PCT)

| Draft figure | Source file | Depicts |
|--------------|-------------|---------|
| FIG. [TBD] | `PPA3_ARCH_EN.svg` | Modules A–G, smart glass (PDLC), waste basket, power bus, induction station |
| FIG. [TBD] | `PPA4_ARCH_EN.svg` | QR session, transaction module, split settlement, master–slave cluster |
| FIG. [TBD] | `PPA5_ARCH_EN.svg` | Inclinometer, VTL + physical fusion, ESL FIFO, cloud biometrics |
| FIG. [TBD] | `PPA6_ARCH_EN.svg` | Dual-zone fridge/heating, fluid station, pre-pay flow, reservation logic |
| FIG. [TBD] | `PPA7_ARCH_EN.svg` | −ΔP vent, freezer waste, 45° bunker, Σ exit gate, cooler/utensils, Space-Yield |

## 6.3 PPA #7 supplemental element table (for detailed description)

| Ref | Component | Function |
|-----|-----------|----------|
| 110 | Hermetic induction chamber | Susceptor heating per RFID culinary profile |
| 120 | −ΔP ventilation | Steam/odor exhaust away from refrigerated zone |
| 130 | Freezer waste module | < −2 °C; timeout disposal + transactional penalty |
| 140 | 45° conical bunker | Single central load cell; gravity-centered weighing |
| 150 | Aggregate weight gate | Exit barrier opens only if Σ session weights match |
| 160 | Space-Yield Engine | AI: optical quality + shrinkage + spatial opportunity cost |
| 170 | Smart cooler / utensils | e.g. 350 ml water per SKU; fork/spoon/chopsticks by dish type |

---

# §7. DETAILED DESCRIPTION OF EMBODIMENTS

**Introductory boilerplate [standard]:**

Embodiments described herein are illustrative and not limiting. Like reference numerals refer to like elements unless stated otherwise. Features from different embodiments may be combined unless incompatible. The edge controller and transaction module may be implemented as dedicated hardware, FPGA, SoC, or software on a general-purpose processor with non-transitory memory storing instructions to perform the methods described.

---

## 7.1 Platform overview and modular chassis (PPA #3 core)

### 7.1.1 Transformer-base chassis and modules A–G

The cabinet comprises a transformer-base chassis supporting interchangeable modules on a shared power and data bus, including without limitation: (A) pusher shelf, (B) hook rack, (C) scale zone, (D) gravity-gate bowl dispenser, (E) tray, (F) disposal/waste interface, and (G) additional specialty modules. Modules hot-swap while exposing standardized power/data connectors to the edge controller.

*See supplemental `PPA3_ARCH_EN.svg` for module layout not visible on filed FIG. 1.*

### 7.1.2 Smart edge, RFID matrix, and front-zone antenna

Smart shelves integrate an RFID matrix and LED indicators. A front-zone antenna array (120) along the shelf front edge cooperates with camera (105) for sensor-fusion anti-theft monitoring during manual retrieval.

### 7.1.3 Smart glass (PDLC) age-gated compartment

A polymer-dispersed liquid crystal (PDLC) smart glass panel switches from opaque to transparent after biometric age verification at camera (105), enabling confidential visual inspection before pre-authorization and triple fusion (RFID + camera + weight) on item removal.

### 7.1.4 Edge controller and offline architecture

As shown in filed FIG. 2, edge controller (400) maintains local database/cache, offline transaction buffer, door control, item counting, and cabinet sensors. Communications via LTE, Wi-Fi, or Ethernet are optional; **operation continues when cloud is unavailable**, with deferred sync.

### 7.1.5 Smart waste bin

A smart waste basket combines load cell and RFID to track disposal events linked to dynamic pricing and shrinkage monitoring.

---

## 7.2 Sensor fusion, dynamic pricing, and checkout methods (PPA #3)

### 7.2.1 Dual-loop control (filed FIG. 3)

**Background loop:** weight W(t) sampled over time → percentage change ΔW% relative to baseline W₀ → evaporation classification → freshness index FI → dynamic price P(t).

**Transaction loop:** sudden weight drop → vision audit → confirm removal event → charge = weight × P(t) → log session → supply exit weight verification data.

### 7.2.2 Standard checkout method

Tap-to-pay or equivalent → unlock → customer manual pick → fusion of RFID + camera [+ weight] → dynamic charge → door close → release unused pre-authorization hold.

### 7.2.3 Smart-glass checkout method

Smart glass opaque → biometric age verify → transparent inspection → pre-auth → triple fusion on pick → charge.

### 7.2.4 Gravity-gate module (module D)

Item rests in bowl with gate locked → customer takes item → gate opens → next item drops by gravity.

### 7.2.5 Dynamic pricing inputs

Pricing module adjusts P(t) based on expiry, dwell time, environmental sensors, and camera-derived quality hints, implementing sensory decay modeling and space-yield slot discount for underperforming facings.

### 7.2.6 Stocking / induction workflow (filed FIG. 4)

Barcode scan + RFID program + expiry entry → associate SKU with tag UID → stock smart shelves → front-zone antenna + camera monitor sessions.

### 7.2.7 Use examples (PPA #3)

1. **Lobby micro-store:** yogurt from pusher module — RFID + camera charge; chocolate at sensory-decay discount.  
2. **Age-restricted alcohol:** smart glass opaque until age verified; pre-auth hold; triple fusion on bottle removal.

---

## 7.3 Tokenized access, consent, and multi-tenant settlement (PPA #4)

### 7.3.1 Session token and QR decode

Mobile application generates a session token encoded in QR form. Scanner at cabinet decodes token and passes session identity to controller.

*See `PPA4_ARCH_EN.svg` for connection diagram.*

### 7.3.2 Transaction module

Transaction module performs: token decode → pre-authorization → display terms (immediate charge, no returns) → require **AGREE** with timestamp → age check for restricted SKUs → unlock enable.

### 7.3.3 Virtual basket and split settlement

During session loop: manual pick → sensors confirm → increment hold → split routing among operator, shelf tenant, and supplier (instant capture or deferred capture) → consolidated fiscal receipt.

### 7.3.4 Offline ledger and UPS

If network unavailable, events append to offline ledger; UPS maintains electronic locks until sync.

### 7.3.5 Master–slave cluster

Optional master block authorizes multiple slave cabinets; single virtual basket; consolidated capture on cluster exit.

### 7.3.6 Upstream induction manifest

Supplier warehouse tags product upstream; allowed-manifest sync to cabinet; cabinet recognizes tagged inventory without local induction scan at restock.

### 7.3.7 Position-adjustable interface

Power/data interface modules adjust position along chassis rail for heterogeneous module heights; LED info strip displays slot status.

### 7.3.8 Use examples (PPA #4)

1. **Airport multi-tenant store:** QR + pre-auth; water (Tenant A) + snack (Supplier B) → split charges; one app receipt.  
2. **Master–slave cluster:** six cabinets, one terminal; single master authorization; consolidated capture on exit.

---

## 7.4 Leveling, visual tracking, ESL FIFO, and penalties (PPA #5)

### 7.4.1 Motorized leveling

Inclinometer (601) on power-on measures tilt; if tilt > 0.5°, motorized feet (602) actuate; if still above threshold, **session start is blocked**.

*See `PPA5_ARCH_EN.svg`.*

### 7.4.2 Visual Tracking Layer (VTL)

Always-on internal cameras form Visual Tracking Layer fused with selectable physical layer: high-value zone (load cell + RFID) vs standard zone (beam break + anti-return ratchet).

### 7.4.3 ESL FIFO metadata queue

Virtual queue ordered by slot expiry; ESL/LCD strip shows front item price and expiry; on pick, controller updates display for next queue member automatically.

### 7.4.4 Progressive cloud biometrics

Session 1: QR + optional face enrollment to cloud vault. Session N at different site: face match + regional payment instrument check.

### 7.4.5 Punitive penalty engine

Unauthorized weight increase or unconfirmed return triggers charge = **MULTIPLE × highest SKU price** in cabinet ( punitive deterrent).

### 7.4.6 Use examples (PPA #5)

1. **Milk pouch smart bin:** leveling OK; QR + consent; weight delta charge; return attempt without camera confirm → 3× max SKU penalty.  
2. **Deli tray:** ESL shows price; temperature 8 °C above 6 °C limit → sale blocked; cabinet moved → session blocked until tilt < 0.5°.

---

## 7.5 Dual-zone climate, induction pre-pay, fluids, reservation (PPA #6)

### 7.5.1 Dual-zone cross-section

Refrigerated zone and heating zone separated by thermal curtain; profiled dispensing channel guides bulk flow.

*See `PPA6_ARCH_EN.svg` and filed PPA #6 FIG. 3.*

### 7.5.2 Controller orchestration

Cabinet controller manages leveling, heating queue, AI prices, locks; optional master orchestrates multiple cabinets.

### 7.5.3 Heated product method — pre-pay before heat

Select item → read Digital Cooking Passport from RFID tag → display price → user confirm → **PRE-PAY BEFORE HEAT** → verify tilt → run induction profile with impedance authentication → LCD shows READY → pickup timer starts → on collection, complete transaction OR on timeout slot lock + waste route + **200% abandonment penalty**.

### 7.5.4 Fluid station

After SKU confirmation and pre-pay, dispense hot water volume per recipe; release stirrer/spoon matched to SKU; interlocked with payment state.

### 7.5.5 Conditional reservation

If stock ≤ 1, **DENY** reservation (walk-in priority). If stock > N, allow hold with timer.

### 7.5.6 AI pricing module (PPA #6)

Bidirectional AI pricing module adjusts offer prices from telemetry, dwell, and inventory pressure.

### 7.5.7 Floating smart bin

Vibration-isolated floating smart bin for bulk weight metrology with mechanical lock of expired RFID tags.

### 7.5.8 Use examples (PPA #6)

1. **Office hot-food cabinet:** slot map display; pay before heat; induction to target temp/time; LCD READY; collected within window.  
2. **Abandonment + fluid:** cup noodles heated; no pickup in 5 min → 200% penalty + waste chute; parallel user receives coffee + hot water + stirrer.

---

## 7.6 Ecosystem extension — hermetic heat, −ΔP, exit gate, Space-Yield (PPA #7)

*Filed figures identical to PPA #6; additional elements from PPA #7 claims 1–5 and `PPA7_ARCH_EN.svg`.*

### 7.6.1 Hermetic induction chamber (110)

Sealed chamber accepts susceptor packaging; heating follows RFID-stored culinary profile; reduces steam release into cabinet volume compared to non-hermetic induction.

### 7.6.2 Negative-pressure ventilation (120)

−ΔP exhaust actively routes steam and odor away from refrigerated zone during heating cycle.

### 7.6.3 Freezer waste module (130)

Unclaimed heated items after timeout transfer to freezer waste module maintained below −2 °C for sanitary hold until disposal; linked to transactional penalty.

### 7.6.4 45° conical bunker (140)

Bulk loose product dispensed from 45° conical bunker onto single central load cell; gravity centers load; shrinkage compensation adjusts €/kg or equivalent during session.

### 7.6.5 Aggregate weight verification gate (150)

Controller accumulates Σ pick weights during session; exit platform load cell verifies Σ against measured egress weight; barrier opens only on match within tolerance, else alarm.

### 7.6.6 Space-Yield Displacement Engine (160)

AI engine adjusts price from optical texture/quality, shrinkage rate, and occupied volume opportunity cost ( Space-Yield Displacement).

### 7.6.7 Smart cooler and utensil sync (170)

On heated SKU selection, controller commands smart water cooler for configured volume (e.g. 350 ml per SKU) and utensil dispenser for type (fork, spoon, chopsticks) by dish class; settlement uses instant split smart contract among operator, food supplier, water supplier.

### 7.6.8 Open retail extension

Methods extend to open retail layouts with ESL and overhead cameras instead of closed door, preserving fusion and settlement logic.

### 7.6.9 PPA #6 vs PPA #7 distinction (support table)

| Topic | PPA #6 emphasis | PPA #7 addition |
|-------|-----------------|-----------------|
| Induction | Dual-zone; pre-pay before heat | Hermetic chamber + susceptor + RFID culinary profile |
| Ventilation | Thermal curtain | −ΔP exhaust away from cold zone |
| Waste / timeout | Waste chute; 200% penalty | Freezer waste < −2 °C |
| Bulk weighing | Floating smart bin; profiled channel | 45° bunker + single central load cell + shrinkage compensation |
| Exit control | Per-item sensor fusion | Aggregate Σ weight verification gate |
| Ecosystem | Basic fluid + utensil | Smart cooler sync + utensil type matching + instant split contract |
| Pricing AI | Bidirectional AI module | Space-Yield Displacement Engine |
| Deployment | Closed cabinet | Open retail + ESL + cameras |

### 7.6.10 Use examples (PPA #7)

1. **Office soup + water + utensil:** biometric auth; soup induction with −ΔP; cooler dispenses 350 ml water; spoon released; split among operator, soup supplier, water supplier.  
2. **Bulk produce + exit gate:** potato net from 45° bunker + tray pack; shrinkage compensation lowers unit price; exit Σ match opens barrier; missed heated lunch → freezer waste + 200% penalty.

---

## 7.7 System diagrams and data flows (consolidated)

**Edge data flows (PPA #3):** induction station → controller (SKU, UID, expiry); module sensors → controller (tag, weight, gate); camera → controller (hand intrusion); controller → payment (incremental capture).

**Access data flows (PPA #4):** mobile app → QR token → scanner → controller → transaction module → master/slave blocks / remote server (manifests, multi-tenant).

**Reliability data flows (PPA #5):** inclinometer → controller → leveling feet; VTL cameras → fusion engine; ESL ← FIFO queue ← inventory events.

**Thermal data flows (PPA #6–#7):** controller → induction coils, −ΔP fan, fluid station, utensil/cooler actuators; load cells → Σ gate; cloud ↔ reservation / Space-Yield / split contract.

---

## 7.8 Definitions (optional subsection — counsel to expand)

| Term | Working definition |
|------|-------------------|
| Sensor fusion | Correlated decision from ≥2 of RFID, camera, weight, beam break |
| Digital Cooking Passport | RFID-stored time/temperature/impedance profile for induction |
| Space-Yield Displacement | Price adjustment from quality × shrinkage × facings opportunity cost |
| FIFO metadata queue | Ordered slot expiry list driving ESL without manual relabel |
| Offline ledger | Append-only local store of session events for later settlement |
| Σ exit gate | Egress barrier conditioned on sum of session pick weights |

---

# §8. CLAIMS

> **⚠ PLACEHOLDER SECTION — NO LEGAL CLAIMS BELOW**  
> Attorney to draft from PPA #3–#7 provisional claims 1–30, 1–20, 1–16, 1–8, 1–5 respectively.  
> Strategy note (Ali): do not attempt to claim all aspects in one filing; prioritize most novel subject matter to reduce restriction practice and excess claim fees. Consider multiple independent claim sets with shared dependent chains.

---

## ═══ CLAIM SET I — MODULAR CABINET APPARATUS (PPA #3 priority) ═══

**Independent claim 1 — apparatus**

```
[PLACEHOLDER — Independent Claim 1]

A modular retail cabinet apparatus comprising:
  (a) a chassis supporting a plurality of interchangeable dispensing modules on a shared power and data bus;
  (b) an edge controller configured to operate with an offline transaction cache when cloud connectivity is unavailable;
  (c) a front-zone RFID antenna array along at least one shelf edge;
  (d) at least one camera configured to cooperate with the RFID antenna array to detect manual retrieval of tagged items;
  (e) a payment interface configured to compute a charge based on sensor-fusion confirmation of retrieval; and
  (f) a dynamic pricing module configured to adjust price based on at least one of expiry, dwell time, or environmental condition;

wherein the apparatus is configured for customer manual pick without an automated gantry dispenser.
```

**Dependent claims 2–15+ (PPA #3 themes)**

```
[PLACEHOLDER — Claim 2]  The apparatus of claim 1, wherein the dispensing modules comprise one or more of: pusher shelf, hook rack, scale zone, gravity-gate bowl, tray module, or disposal module.

[PLACEHOLDER — Claim 3]  The apparatus of claim 1, further comprising a PDLC smart glass panel configured to switch from opaque to transparent after biometric age verification.

[PLACEHOLDER — Claim 4]  The apparatus of claim 1, wherein the dynamic pricing module implements a dual-loop control comprising a background shrinkage monitoring loop and a transaction confirmation loop.

[PLACEHOLDER — Claim 5]  The apparatus of claim 4, wherein the background loop computes a freshness index from weight change over time and updates P(t).

[PLACEHOLDER — Claim 6]  The apparatus of claim 1, further comprising a smart waste bin comprising a load cell and RFID reader.

[PLACEHOLDER — Claim 7–N]  [TBD — migrate from PPA #3 claims 7–30; mark discontinued if merged or withdrawn]
```

---

## ═══ CLAIM SET II — CHECKOUT AND PRICING METHODS (PPA #3 priority) ═══

**Independent claim [N] — method**

```
[PLACEHOLDER — Independent Method Claim]

A computer-implemented method of operating a modular retail cabinet, comprising:
  receiving a payment pre-authorization;
  unlocking cabinet access;
  detecting manual retrieval of an item by sensor fusion of RFID and camera data [and optionally weight];
  computing a charge using a dynamic price P(t); and
  capturing payment upon door close while releasing unused pre-authorization.
```

**Dependent method claims**

```
[PLACEHOLDER — Claim N+1]  wherein detecting comprises triple fusion of RFID, camera, and weight for age-restricted compartment items.

[PLACEHOLDER — Claim N+2]  wherein computing P(t) comprises sensory decay and space-yield slot discount.

[PLACEHOLDER — Claim N+3–M]  [TBD — PPA #3 method claims]
```

---

## ═══ CLAIM SET III — TOKENIZED ACCESS & SPLIT SETTLEMENT (PPA #4 priority) ═══

**Independent claim [P] — system/method**

```
[PLACEHOLDER — Independent Claim — Tokenized Access]

A retail access and settlement system comprising:
  a token scanner configured to decode a session token from a mobile device;
  a consent interface configured to require explicit user agreement before unlock and to store a timestamp;
  a transaction module configured to pre-authorize payment and increment holds during picks;
  a split settlement engine configured to route portions of capture to a plurality of tenant accounts; and
  an offline ledger configured to record session events when a network is unavailable.
```

**Dependent claims**

```
[PLACEHOLDER — Claim P+1]  master–slave cabinet cluster with consolidated virtual basket.

[PLACEHOLDER — Claim P+2]  upstream supplier manifest synchronization without local restock scan.

[PLACEHOLDER — Claim P+3–Q]  [TBD — PPA #4 claims 2–20]
```

---

## ═══ CLAIM SET IV — LEVELING, VTL, ESL FIFO, PENALTY (PPA #5 priority) ═══

**Independent claim [R] — apparatus**

```
[PLACEHOLDER — Independent Claim — Reliability Layer]

A smart retail cabinet comprising:
  an inclinometer and motorized leveling feet;
  a controller configured to block session start when tilt exceeds a threshold;
  a visual tracking layer comprising at least one always-on internal camera;
  a zone-specific physical detector fused with the visual tracking layer;
  an electronic shelf label driven by a FIFO metadata queue; and
  a penalty engine configured to charge a multiple of a highest SKU price upon unauthorized weight increase or unconfirmed return.
```

**Dependent claims**

```
[PLACEHOLDER — Claim R+1]  high-value zone with load cell + RFID vs standard zone with beam break + anti-return ratchet.

[PLACEHOLDER — Claim R+2]  progressive cloud biometric enrollment and cross-location face match.

[PLACEHOLDER — Claim R+3–S]  [TBD — PPA #5 claims 2–16]
```

---

## ═══ CLAIM SET V — DUAL-ZONE CLIMATE, INDUCTION PRE-PAY, FLUIDS (PPA #6 priority) ═══

**Independent claim [T] — apparatus/method**

```
[PLACEHOLDER — Independent Claim — Dual-Zone / Induction]

A modular retail system comprising:
  a refrigerated zone and a heating zone separated by a thermal curtain;
  an induction subsystem configured to heat a tagged item according to a Digital Cooking Passport read from RFID;
  a payment lock configured to prevent energizing the induction subsystem until pre-payment is confirmed;
  a pickup timer configured to trigger waste routing and an abandonment penalty upon timeout; and
  a fluid station interlocked to dispense liquid and a utensil after SKU-specific pre-pay.
```

**Dependent claims**

```
[PLACEHOLDER — Claim T+1]  impedance authentication of susceptor during induction.

[PLACEHOLDER — Claim T+2]  conditional reservation denying hold when stock ≤ 1.

[PLACEHOLDER — Claim T+3]  bidirectional AI pricing module.

[PLACEHOLDER — Claim T+4–U]  [TBD — PPA #6 claims 2–8]
```

---

## ═══ CLAIM SET VI — ECOSYSTEM EXTENSION (PPA #7 priority) ═══

**Independent claim [V] — apparatus/method**

```
[PLACEHOLDER — Independent Claim — PPA #7 Ecosystem]

A modular retail ecosystem comprising:
  a hermetic induction chamber configured to heat susceptor packaging according to an RFID culinary profile;
  a negative-pressure exhaust configured to vent steam away from the refrigerated zone during heating;
  a freezer waste module maintained below −2 °C for timed disposal of unclaimed heated items;
  a 45-degree conical bulk bunker coupled to a single central load cell with shrinkage compensation;
  an aggregate weight verification gate at an exit configured to compare a sum of session pick weights to a platform measurement; and
  a settlement engine configured to execute instant split payment among an operator and a plurality of suppliers including a smart water cooler supplier.
```

**Dependent claims**

```
[PLACEHOLDER — Claim V+1]  Space-Yield Displacement Engine adjusting price by optical quality, shrinkage, and occupied volume.

[PLACEHOLDER — Claim V+2]  utensil dispenser releasing type matched to heated SKU dish class.

[PLACEHOLDER — Claim V+3]  open retail deployment with ESL and overhead cameras.

[PLACEHOLDER — Claim V+4–W]  [TBD — PPA #7 claims 2–5]
```

---

## ═══ CLAIM SET VII — CROSS-CUTTING (optional, counsel discretion) ═══

```
[PLACEHOLDER — Computer-readable medium claim mirroring method of Claim Set II]

[PLACEHOLDER — System claim combining transaction module of Claim Set III with apparatus of Claim Set I]

[PLACEHOLDER — Master–slave cluster claim spanning Claim Sets I and III]

[PLACEHOLDER — CRM / processor claims for Space-Yield Engine — Claim Set VI]
```

---

## Claim drafting checklist for counsel

| # | Task | Source |
|---|------|--------|
| 1 | Map each PPA independent claim to one of Sets I–VI or merge | PPA #3–#7 filed PDFs |
| 2 | Eliminate obvious double-patenting overlap between Set V and VI | §7.6.9 table |
| 3 | Decide apparatus vs method vs CRM split for PCT national phase | Ali strategy call |
| 4 | Limit total independent claims if fee-sensitive | Ali guidance |
| 5 | Add "configured to" / "non-transitory" boilerplate per current US practice | Firm template |
| 6 | Verify §119 support for each claim element | Provisional specs + figures |

---

# §9. ABSTRACT

**[PLACEHOLDER — ≤150 words, single paragraph, counsel to finalize after claims]**

A modular retail cabinet platform includes interchangeable dispensing modules on a shared bus, an edge controller with offline cache, RFID-and-camera sensor fusion for manual pick checkout, and dynamic pricing from expiry and shrinkage data. Tokenized QR sessions require mandatory consent before unlock and support multi-tenant split settlement with offline ledger backup. Motorized leveling blocks sessions when tilt exceeds a threshold; visual tracking fuses with zonal detectors; electronic shelf labels follow a FIFO metadata queue. Dual-zone climate separates refrigeration from induction heating with pre-payment gating, Digital Cooking Passport profiles, fluid dispensing, and abandonment penalties. Extensions include hermetic induction, negative-pressure exhaust, freezer waste disposal, a conical bulk bunker with central load cell, aggregate exit weight verification, Space-Yield pricing, and synchronized water and utensil dispensers with instant supplier splits.

*(Word count placeholder: ~120 — expand or trim to comply with PCT Rule 8.)*

---

# APPENDIX A — PLATFORM EVOLUTION (reference only — omit from filed spec)

```
PPA #3  Hardware chassis · sensor fusion · smart glass · dynamic pricing · offline edge
   │
PPA #4  + Tokenized access · mandatory consent · multi-tenant split · master–slave · upstream manifest
   │
PPA #5  + Motorized leveling · Visual Tracking Layer · ESL FIFO · cloud biometrics · punitive penalty
   │
PPA #6  + Dual-zone climate · induction pre-pay · fluid station · abandonment routing · AI pricing · reservation
   │
PPA #7  + Hermetic heat · −ΔP · freezer waste · 45° bunker · Σ exit gate · ecosystem sync · open retail ESL
```

---

# APPENDIX B — SOURCE MAPPING (internal — omit from filed spec)

| Memo section | PCT section |
|--------------|-------------|
| §0 Platform scope | §3, §4, §5 intro |
| PPA #3 §1–§6 | §6.1, §7.1–§7.2 |
| PPA #4 §1–§6 | §6.1, §7.3 |
| PPA #5 §1–§6 | §6.1, §7.4 |
| PPA #6 §1–§6 | §6.1, §7.5 |
| PPA #7 §1–§6 | §6.2–6.3, §7.6 |
| Ali six-point Q&A | Covered across §6–§7 |

---

*End of PCT specification skeleton — Application #1 (PPAs #3–#7)*

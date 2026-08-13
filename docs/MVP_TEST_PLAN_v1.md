# Micro Shop — MVP Test Plan v1

**План испытаний MVP**  
**Версия:** 1.0  
**Дата:** 2026-08-13  
**Рынок:** Российская Федерация  
**Статус:** для lab-стенда и приёмки MVP Ready  

**Связанные документы:**

- [MVP_SCOPE_v1_RU.md](./MVP_SCOPE_v1_RU.md) — Definition of Done  
- [MVP_TZ_HARDWARE_v1.md](./MVP_TZ_HARDWARE_v1.md) — критерии приёмки модулей  
- [MVP_BOM_v1.xlsx](./MVP_BOM_v1.xlsx) — конфигурация установки  

---

## 1. Назначение

Документ описывает **что, как и когда тестировать** для приёмки Micro Shop MVP на lab-площадке в РФ: от bench-теста весов до 100 end-to-end транзакций с оплатой и фискальным чеком.

**Цель испытаний:** подтвердить, что установка (3 модуля + edge + backend + app) выполняет ключевой цикл:

> Регистрация → сессия → взятие товара → оплата при взятии → чек ≤ 5 сек  

и соответствует критериям **MVP Ready** из MVP Scope v1.

---

## 2. Область тестирования

### 2.1. In scope

| Слой | Что тестируем |
|---|---|
| **Hardware** | MS-PRODUCE-01, MS-CHILL-01, MS-MEAL-01, шина, питание, безопасность |
| **Edge / firmware** | Сессии, PICK_EVENT, bus, offline-буфер, индукция |
| **Backend** | Auth, каталог, транзакции, API edge, admin |
| **Mobile app** | Регистрация, оплата, QR-сессия, чек |
| **Payments + fiscal (РФ)** | Эквайринг, онлайн-касса, ОФД, 54-ФЗ |
| **Integration E2E** | Полный путь пользователя на 3 SKU-сценариях |
| **Reliability** | 7-суточный soak, 100 транзакций |

### 2.2. Out of scope (не блокирует MVP Ready)

- Marketplace / multi-supplier  
- ИИ-ценообразование, split payments  
- PPA №10 (контроль тары), биометрия  
- Нагрузочное тестирование > 50 concurrent users  
- Публичная коммерческая локация (ЖК, БЦ)  
- EAC / сертификация оборудования  
- iOS (если v1 — только Android)  

---

## 3. Тестовая среда

### 3.1. Lab-стенд

| Параметр | Требование |
|---|---|
| Площадка | Закрытое помещение, РФ |
| Установка | 3 модуля: Produce + Chill (master) + Meal |
| Электрика | L1 logic (UPS), L2 холод, L3 индукция — по ТЗ |
| Сеть | Ethernet primary; Wi-Fi fallback |
| Backend | Staging (cloud или local server) |
| Payments | **Sandbox** провайдера → prod только после S4 |
| Fiscal | Тестовая касса / sandbox ОФД (по возможности провайдера) |

### 3.2. Тестовые устройства

| Устройство | Минимум |
|---|---|
| Android-смартфон | 2 модели (разные OEM) |
| iOS | Optional, если в scope app |
| Эталонный термометр | 1 (пищевой probe) |
| Эталонные гири | 100 g, 500 g, 1 kg |
| Multimeter / clamp meter | Для E-stop и induction |

### 3.3. Тестовые SKU (черновик)

| ID | Модуль | Слот | Товар | Ном. вес | Допуск |
|---|---|---|---|---|---|
| SKU-P1 | Produce | P-1 | Картофель 1 кг | 1000 g | ±50 g |
| SKU-P2 | Produce | P-2 | Лук 500 г | 500 g | ±30 g |
| SKU-C1 | Chill | C-1 | Молоко 1 L | 1030 g | ±15 g |
| SKU-C2 | Chill | C-2 | Кефир 1 L | 1030 g | ±15 g |
| SKU-M1 | Meal | M-1 | Рис с курицей | 380 g | ±15 g |
| SKU-M2 | Meal | M-2 | Рис с овощами | 380 g | ±15 g |

*Финальный список — в admin после калибровки слотов.*

### 3.4. Роли

| Роль | Ответственность |
|---|---|
| **Test lead** | План, протоколы, sign-off |
| **Hardware engineer** | H0–H3, дефекты механики/электрики |
| **Embedded dev** | Edge, bus, PICK algorithm |
| **Backend / mobile dev** | S1–S3, API, app |
| **Product owner** | Приёмка MVP Ready, UX на 20 пользователях |
| **Observer** | Бухгалтерия/юрист — чек 54-ФЗ (S4) |

---

## 4. Уровни и фазы испытаний

```
H0 ──► H1 ──► H2 ──► H3 ──► H4 ──► H5
 │      │       │       │       ▲       │
 │      └───────┴───────┴───────┘       │
 │         Hardware standalone          │
 │                                      │
S0 ──► S1 ──► S2 ──► S3 ──► S4 ──► E2E ──► MVP READY
         Software layers      Integration  Sign-off
```

| Фаза | ID | Объект | Блокирует |
|---|---|---|---|
| Bench | **H0** | Load cell + алгоритм веса | H1–H4 |
| Hardware unit | **H1** | MS-PRODUCE-01 | H4 |
| Hardware unit | **H2** | MS-CHILL-01 + edge boot | H4 |
| Hardware unit | **H3** | MS-MEAL-01 + safety | H4 |
| Hardware integration | **H4** | 3 модуля + bus + edge | E2E |
| Reliability | **H5** | 7-day soak | MVP Ready |
| Software unit | **S0** | Backend API (mock edge) | S3 |
| Software unit | **S1** | Edge firmware (mock cloud) | H4 |
| Software unit | **S2** | Mobile app (mock backend) | E2E |
| Integration | **S3** | Edge ↔ backend ↔ app (no payment) | S4 |
| Payments | **S4** | Sandbox payment + fiscal | E2E |
| End-to-end | **E2E** | Full user journey × 100 | MVP Ready |
| UX | **U1** | 20 пользователей, time ≤ 120 s | MVP Ready |

---

## 5. Entry / Exit criteria по фазам

### H0 — Bench (вес)

| | Критерий |
|---|---|
| **Entry** | Load cell + HX711 + MCU на столе |
| **Exit** | Stable weight ≤ 1 s; drift ≤ ±3 g / 24 h; 100 g / 500 g калибровка ±2 g |

### H1 — MS-PRODUCE-01

| | Критерий |
|---|---|
| **Entry** | H0 exit; модуль собран; ≥ 3 слота активны |
| **Exit** | AC-P-01…AC-P-05 *(см. §6.1)* |

### H2 — MS-CHILL-01

| | Критерий |
|---|---|
| **Entry** | Компрессор установлен; edge hardware в шкафу |
| **Exit** | AC-C-01…AC-C-06 *(см. §6.2)* |

### H3 — MS-MEAL-01

| | Критерий |
|---|---|
| **Entry** | Индукция + E-stop проводка; холод/Peltier |
| **Exit** | AC-M-01…AC-M-06 *(см. §6.3)* |

### H4 — Hardware integration

| | Критерий |
|---|---|
| **Entry** | H1+H2+H3 exit; S1 exit (edge firmware) |
| **Exit** | Протокол §8.2 ТЗ hardware — 7 шагов без critical fail |

### H5 — Soak 7 days

| | Критерий |
|---|---|
| **Entry** | H4 exit |
| **Exit** | Uptime edge ≥ 95%; temp log без alarm > 10 min; 0 critical faults |

### S0–S4 — Software

| Фаза | Exit (кратко) |
|---|---|
| **S0** | Auth, catalog, session API — Postman 100% must cases |
| **S1** | PICK_EVENT → mock payment trigger; offline buffer 30 s |
| **S2** | App: register, bind card (test), QR session UI |
| **S3** | E2E без денег: session → pick → inventory update |
| **S4** | Sandbox charge + fiscal receipt in app/email |

### E2E + MVP Ready

| | Критерий |
|---|---|
| **Entry** | H4 + S4 exit |
| **Exit** | Все пункты §10 Sign-off checklist |

---

## 6. Тест-кейсы: Hardware

### 6.1. MS-PRODUCE-01

| ID | Название | Шаги | Ожидаемый результат | Pass |
|---|---|---|---|---|
| **TC-P-01** | Unlock по SESSION_OPEN | 1. Отправить SESSION_OPEN на slave | Замок открывается ≤ 500 ms | AC-P-03 |
| **TC-P-02** | PICK картофель P-1 | 1. Open session 2. Open door 3. Снять SKU-P1 | PICK_EVENT(P-1, Δ≈1000g) ≤ 300 ms local | AC-P-02 |
| **TC-P-03** | PICK лук P-2 | Аналогично SKU-P2 | Δ≈500g, SKU match | AC-P-02 |
| **TC-P-04** | Ложное срабатывание | Постучать по корпусу без снятия товара | Нет PICK или weight < threshold | ≤ 1% false |
| **TC-P-05** | 100 циклов замка | Auto open/close 100× | Без заклинивания | AC-P-01 |
| **TC-P-06** | Bus disconnect | Отключить RS-485 35 s | Safe lock; FAULT code | AC-P-05 |
| **TC-P-07** | Бункер 45° | 3 выдачи без ручной помощи | Товар сходит сам | AC-P-04 |

**Метрика AC-P-02:** 100 попыток на 3 SKU → ≥ 99 успешных.

---

### 6.2. MS-CHILL-01 (Master)

| ID | Название | Шаги | Ожидаемый результат | Pass |
|---|---|---|---|---|
| **TC-C-01** | Temp hold 24 h | Запустить компрессор, log 5 min | +2…+6 °C весь период | AC-C-01 |
| **TC-C-02** | Temp alarm | Имитация: отключить компрессор 15 min | Alarm T > +8 °C; notify | AC-C-06 |
| **TC-C-03** | PICK молоко C-1 | Session + снять SKU-C1 | PICK_EVENT, Δ≈1030g | AC-C-02 |
| **TC-C-04** | PICK кефир C-2 | Аналогично | ≥ 99% / 100 tries | AC-C-02 |
| **TC-C-05** | Edge boot | Power cycle L1 | Cloud heartbeat ≤ 90 s | AC-C-03 |
| **TC-C-06** | Bus master poll | 24 h log | Poll slaves ≤ 200 ms; 0 loss | AC-C-04 |
| **TC-C-07** | UPS hold | Отключить L1 на 10 min | Edge alive; locks state known | AC-C-05 |
| **TC-C-08** | Vibration decouple | Compressor on + PICK | Вес stable, no false PICK | — |

---

### 6.3. MS-MEAL-01

| ID | Название | Шаги | Ожидаемый результат | Pass |
|---|---|---|---|---|
| **TC-M-01** | PICK M-1 | Session + снять контейнер | PICK_EVENT; оплата триггер | AC-M-01 |
| **TC-M-02** | PICK M-2 | 100 tries both SKU | ≥ 99% correct | AC-M-01 |
| **TC-M-03** | Heat profile | HEAT_START после PICK | T ≥ 65 °C proxy ≤ 120 s | AC-M-02 |
| **TC-M-04** | E-stop | Нагрев → нажать E-stop | Power off ≤ 100 ms | AC-M-03 |
| **TC-M-05** | No pan | HEAT_START без контейнера | Blocked; FAULT | AC-M-04 |
| **TC-M-06** | Heat endurance | 100 циклов нагрева | 0 critical fault | AC-M-05 |
| **TC-M-07** | Meal storage temp | 24 h log (cold mode) | +2…+8 °C | AC-M-06 |
| **TC-M-08** | Door open during heat | Открыть дверь зоны нагрева | Heat abort | S-03 |

---

### 6.4. H4 — Integration hardware

| ID | Название | Шаги | Pass |
|---|---|---|---|
| **TC-H4-01** | Cold start | Power all → edge online | ≤ 90 s |
| **TC-H4-02** | Session policy | SESSION_OPEN | Только целевой модуль unlock |
| **TC-H4-03** | Triple PICK | 1 SKU из каждого модуля | 3 PICK_EVENT |
| **TC-H4-04** | Heat after pick | M-1 + HEAT | HEAT_DONE |
| **TC-H4-05** | Network offline | Drop WAN 30 s during session | Buffer → sync |
| **TC-H4-06** | Bus fault | Disconnect one slave bus | Safe lock + FAULT |
| **TC-H4-07** | 100 full cycles | Repeat TC-H4-03…04 | 0 critical; ≥ 99% PICK |

---

## 7. Тест-кейсы: Software

### 7.1. S0 — Backend API

| ID | Endpoint / функция | Pass |
|---|---|---|
| **TC-S0-01** | POST /auth/register | 201, token |
| **TC-S0-02** | POST /payments/bind-card (sandbox) | token saved |
| **TC-S0-03** | GET /catalog?location=lab | SKU list |
| **TC-S0-04** | POST /sessions/open | session_id, TTL |
| **TC-S0-05** | POST /edge/pick-event | inventory ↓, txn created |
| **TC-S0-06** | POST /transactions/charge | status=paid (mock) |
| **TC-S0-07** | GET /receipts/{id} | fiscal fields present |

### 7.2. S1 — Edge firmware

| ID | Сценарий | Pass |
|---|---|---|
| **TC-S1-01** | Poll slaves 200 ms | stable 1 h |
| **TC-S1-02** | PICK → POST cloud | latency ≤ 500 ms p95 |
| **TC-S1-03** | Offline 30 s, 3 PICK | All synced in order |
| **TC-S1-04** | OTA update package | Reboot + resume |
| **TC-S1-05** | HEAT_START → slave | HEAT_DONE/FAULT |
| **TC-S1-06** | Session timeout | Auto lock all doors |

### 7.3. S2 — Mobile app

| ID | Сценарий | Pass |
|---|---|---|
| **TC-S2-01** | Register + SMS/email | OK |
| **TC-S2-02** | Bind test card | OK |
| **TC-S2-03** | Scan QR → session active UI | ≤ 3 s |
| **TC-S2-04** | Push/in-app during purchase | State updates |
| **TC-S2-05** | Receipt screen + email | PDF/link visible |

### 7.4. S3 — Integration (no real money)

| ID | Сценарий | Pass |
|---|---|---|
| **TC-S3-01** | Full flow mock payment | Inventory + session closed |
| **TC-S3-02** | Wrong slot weight | Reject / manual review flag |
| **TC-S3-03** | Double PICK same slot | 2 txn or block per policy |
| **TC-S3-04** | Admin restock | Weight baseline reset |

### 7.5. S4 — Payments + fiscal (РФ)

| ID | Сценарий | Pass |
|---|---|---|
| **TC-S4-01** | Sandbox charge on PICK | success ≥ 99% |
| **TC-S4-02** | Fiscal receipt ОФД | QR OFD valid (test env) |
| **TC-S4-03** | Receipt ≤ 5 s after PICK | p95 ≤ 5 s |
| **TC-S4-04** | Moment расчёта = выдача | Юрист/бух confirm |
| **TC-S4-05** | Declined card | User message; no inventory loss |
| **TC-S4-06** | 54-ФЗ required fields | All present in receipt |

---

## 8. Тест-кейсы: End-to-End (E2E)

### 8.1. Основные user journeys

| ID | Journey | Модули | Pass |
|---|---|---|---|
| **TC-E2E-01** | «Только молоко» | Chill | Pay + receipt ≤ 5 s |
| **TC-E2E-02** | «Только овощ» | Produce | Pay + receipt |
| **TC-E2E-03** | «Горячее полный» | Meal pick + heat | Pay + heat + receipt |
| **TC-E2E-04** | «Комбо 3 категории» | All | 3 charges, 3 receipts |
| **TC-E2E-05** | Repeat × 100 | All | ≥ 99 success; 0 critical |

### 8.2. Негативные сценарии

| ID | Сценарий | Ожидание |
|---|---|---|
| **TC-E2E-N01** | App kill mid-session | Session recover or safe timeout |
| **TC-E2E-N02** | No network at charge | Queue + retry; user informed |
| **TC-E2E-N03** | Power loss mid-purchase | UPS: state recover or fail-safe |
| **TC-E2E-N04** | Wrong product slot | No charge or wrong-SKU block |
| **TC-E2E-N05** | Session without registration | Block at QR |

### 8.3. UX — U1 (20 пользователей)

| ID | Метрика | Pass |
|---|---|---|
| **TC-U1-01** | Time-to-complete (register already done) | avg ≤ 120 s |
| **TC-U1-02** | Task success rate | ≥ 90% без помощи |
| **TC-U1-03** | SUS / опрос 5 вопросов | Зафиксировать baseline |
| **TC-U1-04** | Confusion points | Log для v1.1 |

**Профиль testers:** 10 «техничных», 10 «обычных»; все signed consent 152-ФЗ.

---

## 9. Нефункциональные требования

| ID | Метрика | Target | Как мерить |
|---|---|---|---|
| **NFR-01** | PICK local latency | p95 ≤ 300 ms | Edge log |
| **NFR-02** | Charge + receipt | p95 ≤ 5 s | Backend timestamp |
| **NFR-03** | Weight accuracy | ≥ 99% | 100 PICK vs ground truth |
| **NFR-04** | Chill temperature | +2…+6 °C 24 h | DS18B20 CSV |
| **NFR-05** | Edge uptime | ≥ 95% / 7 d | Heartbeat monitor |
| **NFR-06** | API availability staging | ≥ 99% test period | Uptime check |
| **NFR-07** | Heat safety E-stop | ≤ 100 ms | Scope / video |

---

## 10. Sign-off checklist — MVP Ready

*Копия для протокола приёмки. Все пункты — PASS.*

### Пользовательский сценарий

- [ ] Регистрация + привязка карты (sandbox/prod по решению)
- [ ] QR-сессия на lab-точке
- [ ] Оплата при взятии — 3 категории
- [ ] Чек app/email ≤ 5 s (p95)
- [ ] U1: avg purchase time ≤ 120 s (n ≥ 20)

### Техника

- [ ] 100 E2E транзакций ≥ 99% success
- [ ] Chill +2…+6 °C — 24 h log
- [ ] Induction safety: E-stop, no-pan, timeout
- [ ] Offline 30 s — events synced
- [ ] Edge uptime ≥ 95% / 7 d (H5)

### Юридическое (РФ)

- [ ] 54-ФЗ чек validated (test or prod)
- [ ] 152-ФЗ: consent + privacy policy linked in app
- [ ] Lab placement agreement

### Артефакты

- [ ] Протокол H0–H5 + S0–S4 + E2E
- [ ] CSV: temp log, weight events, transactions
- [ ] Defect log + closed critical/high
- [ ] Demo video 3–5 min
- [ ] As-built photos + BOM actuals

**Подписи:** Product owner __________  Test lead __________  Date __________

---

## 11. Логирование и артефакты

### 11.1. Обязательные логи

| Лог | Формат | Период | Owner |
|---|---|---|---|
| `temp_chill.csv` | timestamp, T_air, T_evap | H2, H5 | Hardware |
| `weight_events.csv` | ts, module, slot, delta_g, sku, stable_ms | H1–H4 | Embedded |
| `edge_heartbeat.csv` | ts, status, bus_ok | H4, H5 | Embedded |
| `transactions.csv` | ts, session, sku, amount, pay_status, receipt_id | E2E | Backend |
| `defects.csv` | id, severity, phase, description, status | All | Test lead |

### 11.2. Шаблон записи дефекта

```
ID:          DEF-YYYY-NNN
Severity:    Critical / High / Medium / Low
Phase:       H1 / S4 / E2E / ...
Summary:     ...
Steps:       ...
Expected:    ...
Actual:      ...
Evidence:    log / photo / video link
Status:      Open / Fixed / Won't fix
```

### 11.3. Severity — правила

| Уровень | Пример | Блокирует MVP Ready |
|---|---|---|
| **Critical** | Нагрев без E-stop; charge без receipt; door open + free pick | Да |
| **High** | PICK accuracy < 99%; temp out of range > 30 min | Да |
| **Medium** | Slow receipt 5–10 s; UI confusion | Нет*, если waiver PO |
| **Low** | Label typo; cosmetic | Нет |

---

## 12. Расписание (ориентир)

| Неделя | Фазы | Deliverable |
|---|---|---|
| W1–2 | H0, начало H1 | Bench report |
| W3–5 | H1, H2 | Module test reports |
| W4–6 | S0, S1 parallel | API + edge test reports |
| W6–8 | H3, S2 | Meal safety + app report |
| W8–10 | H4, S3 | Integration report |
| W10–11 | S4 | Payment/fiscal report |
| W11–12 | E2E × 100, U1 | E2E protocol |
| W12–13 | H5 soak | Soak report |
| W13 | Sign-off | MVP Ready protocol |

*Параллелится при большей команде.*

---

## 13. Риски тестирования

| Риск | Митигация |
|---|---|
| Sandbox fiscal ≠ prod | Ранний S4; prod smoke перед demo инвестору |
| SKU calibration drift | Recalibrate before E2E block |
| Lab ≠ real traffic | U1 с «naive» users; не заменяет пилот |
| Hardware delay | S0–S2 на mocks без блокировки |
| Seasonal ambient temp | Log Tamb; test at +25 °C reference |

---

## 14. История изменений

| Версия | Дата | Изменения |
|---|---|---|
| 1.0 | 2026-08-13 | Первая версия. РФ, lab MVP. |

---

*Изменения — через revision документа. Новые тест-кейсы вне scope MVP — change request к MVP_SCOPE_v1_RU.md.*

# Как отправить материалы Ali — по одной заявке за раз

**Патентный поверенный:** Ali  
**Заявки:** PPA №3 → №4 → №5 → №6 → №7 (строго **по очереди**)  
**Правило Ali:** все 6 пунктов + PDF + рисунки — **одним письмом**, когда комплект готов. Следующую PPA — **только после** подтверждения, что предыдущая принята в работу (~2 недели на заявку).

---

## Общая схема (5 писем)

```
Письмо 1 ──► PPA №3  ──► ждём ≥2 недели / подтверждение Ali
Письмо 2 ──► PPA №4  ──► ждём …
Письмо 3 ──► PPA №5  ──► ждём …
Письмо 4 ──► PPA №6  ──► ждём …
Письмо 5 ──► PPA №7  ──► готово
```

**Не отправляйте** PPA №4–7, пока Ali не подтвердил получение и начало работы по предыдущей.

---

## Что лежит в папках

Каждая заявка — отдельная папка `docs/ali_submission/send/PPA{N}/`:

| Файл | Назначение |
|------|------------|
| **`EMAIL_RU.txt`** | Текст письма на русском — скопировать в тело email |
| **`EMAIL_EN.txt`** | Текст письма на английском (для Ali) |
| **`SUBMISSION_RU.md`** | Ответы на 6 пунктов Ali (§1–§6) — **русский** |
| **`SUBMISSION_EN.md`** | То же — **английский** |
| **`CHECKLIST_RU.md`** | Список вложений — отметить перед отправкой |

---

## Пошагово для каждого письма

### Шаг 1. Открыть папку заявки

| Очередь | Папка |
|---------|--------|
| 1-е письмо | [`send/PPA3/`](send/PPA3/) |
| 2-е | [`send/PPA4/`](send/PPA4/) |
| 3-е | [`send/PPA5/`](send/PPA5/) |
| 4-е | [`send/PPA6/`](send/PPA6/) |
| 5-е | [`send/PPA7/`](send/PPA7/) |

### Шаг 2. Экспорт пояснений в PDF (рекомендуется)

Из папки PPA{N} экспортируйте в PDF **оба** или один на выбор Ali:
- `SUBMISSION_EN.md` → `PPA3_Submission_EN.pdf`
- `SUBMISSION_RU.md` → `PPA3_Submission_RU.pdf`

Способы: Word (открыть .md или вставить текст) → «Сохранить как PDF»; или [Pandoc](https://pandoc.org):  
`pandoc SUBMISSION_EN.md -o PPA3_Submission_EN.pdf`

### Шаг 3. Собрать вложения по CHECKLIST

Откройте **`CHECKLIST_RU.md`** в папке заявки. Файлы PDF заявителя лежат у вас в:

`c:\Start-up\23.08.2026.документы на патенты\23.08.2026. 1 пакет документов для патента\Папка PPA#3,#4,#5,#6\`

SVG из репозитория:

`C:\Users\kmd37\Projects\vird\assets\figures\ppa3456\PPA{N}_ARCH_RU.svg`

### Шаг 4. Написать письmo

1. Скопируйте текст из **`EMAIL_EN.txt`** (Ali обычно на английском) или **`EMAIL_RU.txt`**.  
2. **Тема (Subject)** — указана в начале EMAIL_*.txt.  
3. Приложите все файлы из чеклиста одним письмом.

### Шаг 5. Отправить и дождаться ответа

- Дождитесь **подтверждения получения** от Ali.  
- **Не меняйте** материалы после отправки (иначе доп. fees).  
- Только после этого переходите к следующей папке PPA{N+1}.

---

## Краткая таблица: что приложить к каждому письму

| № | PPA | EN specification PDF | FIGURES | SVG | Пояснения §1–6 | Прочее |
|---|-----|----------------------|---------|-----|----------------|--------|
| 1 | **3** | `PPA#3-ModularSmartVendingCabinet_Revised.pdf` | `PPA#3 FIGURES.pdf` | `PPA3_ARCH_RU.svg` | SUBMISSION_EN/RU → PDF | APP.FILE.REC |
| 2 | **4** | `PPA#4_SMART RETAIL CABINET_…pdf` | `PPA#4 FIGURES.pdf` | `PPA4_ARCH_RU.svg` | SUBMISSION_EN/RU → PDF | APP.FILE.REC |
| 3 | **5** | `PPA#5_SmartRetailCabinet_…pdf` | `PPA#5 FIGURES.pdf` | `PPA5_ARCH_RU.svg` | SUBMISSION_EN/RU → PDF | APP.FILE.REC |
| 4 | **6** | `PPA#6_Modular_Retail_System.pdf` | `PPA#6 FIGURES.pdf` | `PPA6_ARCH_RU.svg` | SUBMISSION_EN/RU → PDF | APP.FILE.REC |
| 5 | **7** | `docs/source/ppa7/PPA7_Modular_Retail_System.pdf` | **`PPA#6 FIGURES.pdf`** | `PPA7_ARCH_RU.svg` | SUBMISSION_EN/RU → PDF | `02.09.2026_PPA7_RU.docx` |

---

## Шесть пунктов Ali (напоминание)

| № | Вопрос Ali | Где в пакете |
|---|------------|--------------|
| 1 | Эскизы / чертежи | §1 + FIGURES.pdf + SVG |
| 2 | Схема связей | §2 |
| 3 | Блок-схема процесса | §3 |
| 4 | Описание компонентов | §4 |
| 5 | Примеры использования | §5 |
| 6 | Отличия от аналогов | §6 |

---

## ⚠️ PPA №6 и №7

Одинаковое **английское название**, разные **claims** и пояснения. В письме по PPA №7 явно укажите: *«Same title as PPA #6; different claims 1–5; separate application.»*

---

## Если Ali просит один язык

- **Только EN:** приложите `SUBMISSION_EN.pdf` + EN specification PDF.  
- **Только RU:** `SUBMISSION_RU.pdf` + для PPA №7 ещё docx-перевод.  
- **Оба:** оба PDF пояснений — безопасный вариант.

---

## Контакты и данные (заполнить до 1-го письма)

- [ ] Имена изобретателей (USPTO)  
- [ ] Assignee, адрес  
- [ ] Micro/small entity  
- [ ] Power of attorney (если ещё не подписана)  

Эти данные можно отправить **в первом письме (PPA №3)** или отдельным письмом до него — уточните у Ali.

---

*Полные объединённые файлы: [`../MicroShop_Ali_Submission_EN.md`](../MicroShop_Ali_Submission_EN.md) · [`../MicroShop_Ali_Submission_RU.md`](../MicroShop_Ali_Submission_RU.md)*

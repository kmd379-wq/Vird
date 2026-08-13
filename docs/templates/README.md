# Micro Shop — шаблоны CSV-логов MVP

Версия: 1.0 · 2026-08-13

Шаблоны для испытаний по [MVP_TEST_PLAN_v1.md](../MVP_TEST_PLAN_v1.md) §11.

## Файлы

| Файл | Назначение | Фазы |
|---|---|---|
| `temp_chill.csv` | Температура холодильного модуля | H2, H5 |
| `weight_events.csv` | Весовые события и PICK | H0–H4 |
| `edge_heartbeat.csv` | Состояние edge и шины | H4, H5 |
| `transactions.csv` | Платежи и чеки | S4, E2E |
| `defects.csv` | Журнал дефектов | All |

## Как использовать

1. **Копируйте** нужный шаблон в `docs/logs/` или `docs/logs/YYYY-MM-DD/` (создайте папку на дату прогона).
2. **Не удаляйте** строку заголовков (первая строка).
3. **Пример строки** (вторая строка) — удалите перед реальным логированием или оставьте как reference.
4. **Время** — ISO 8601 с timezone: `2026-08-13T14:30:00+03:00`.
5. **Кодировка** — UTF-8 with BOM (открывается в Excel без кракозябр).

## Именование прогонов

```
docs/logs/
  2026-08-13_H2_chill/
    temp_chill.csv
  2026-08-20_H4_integration/
    weight_events.csv
    edge_heartbeat.csv
  2026-09-01_E2E/
    transactions.csv
  defects.csv          ← один общий на проект или per sprint
```

## Связь с test plan

- NFR-04 → `temp_chill.csv`
- NFR-01, NFR-03 → `weight_events.csv`
- NFR-05 → `edge_heartbeat.csv`
- NFR-02 → `transactions.csv` (`latency_pick_to_receipt_ms`)

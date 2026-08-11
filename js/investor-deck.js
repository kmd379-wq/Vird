(function () {
  var PLACEHOLDER = '—';

  function fmtMoney(value, currency) {
    if (value == null || value === '') return PLACEHOLDER;
    return new Intl.NumberFormat('ru-RU', {
      style: 'currency',
      currency: currency || 'USD',
      maximumFractionDigits: 0,
    }).format(value);
  }

  function fmtNum(value, suffix) {
    if (value == null || value === '') return PLACEHOLDER;
    var s = new Intl.NumberFormat('ru-RU').format(value);
    return suffix ? s + ' ' + suffix : s;
  }

  function fmtPct(value) {
    if (value == null || value === '') return PLACEHOLDER;
    return value + '%';
  }

  function setText(id, text) {
    var el = document.getElementById(id);
    if (el) el.textContent = text;
  }

  fetch('data/investor-metrics.json')
    .then(function (r) {
      if (!r.ok) throw new Error('metrics load failed');
      return r.json();
    })
    .then(render)
    .catch(function () {
      document.querySelectorAll('[data-metrics-fallback]').forEach(function (el) {
        el.textContent = PLACEHOLDER;
      });
    });

  function render(data) {
    var c = data.currency || 'USD';
    var k = data.known || {};

    setText('m-round-name', data.round.name || PLACEHOLDER);
    setText('m-round-target', fmtMoney(data.round.target, c));
    setText('m-round-premoney', fmtMoney(data.round.preMoney, c));
    setText('m-runway', fmtNum(data.round.runwayMonths, 'мес.'));

    setText('m-ppa', fmtNum(k.ppaCount));
    setText('m-streams', fmtNum(k.revenueStreams));
    setText('m-purchase-time', k.purchaseSecondsMin + '–' + k.purchaseSecondsMax + ' сек');
    setText('m-cabinets', k.cabinetsMin + '–' + k.cabinetsMax);
    setText('m-mvp', fmtNum(k.mvpScenarios));

    ['tam', 'sam', 'som'].forEach(function (key) {
      var m = data.market[key];
      setText('m-' + key, fmtNum(m.value, m.unit));
      setText('m-' + key + '-note', m.note || '');
    });

    var ue = data.unitEconomics;
    setText('m-capex', fmtMoney(ue.capexPerLocation, c));
    setText('m-rev-loc', fmtMoney(ue.monthlyRevenueLocation, c));
    setText('m-opex-loc', fmtMoney(ue.monthlyOpexLocation, c));
    setText('m-platform-fee', fmtMoney(ue.platformFeeMonthly, c));
    setText('m-slots', fmtNum(ue.supplierSlotsAvg));
    setText('m-tx-day', fmtNum(ue.transactionsPerDay));
    setText('m-avg-check', fmtMoney(ue.avgCheck, c));
    setText('m-payback', fmtNum(ue.paybackMonths, 'мес.'));
    setText('m-margin', fmtPct(ue.grossMarginPct));

    var fundsEl = document.getElementById('use-of-funds');
    if (fundsEl && data.useOfFunds) {
      var target = data.round && data.round.target;
      fundsEl.innerHTML = data.useOfFunds
        .map(function (item) {
          var amt =
            item.amount != null
              ? item.amount
              : target != null && item.pct != null
                ? Math.round((target * item.pct) / 100)
                : null;
          var amtStr = fmtMoney(amt, c);
          var pct = item.pct != null ? item.pct : 0;
          return (
            '<div class="fund-row">' +
            '<div class="fund-meta"><span class="fund-label">' + item.label + '</span>' +
            '<span class="fund-amount">' + amtStr + ' · ' + pct + '%</span></div>' +
            '<div class="fund-bar"><div class="fund-bar-fill" style="width:' + pct + '%"></div></div>' +
            '</div>'
          );
        })
        .join('');
    }

    var forecastEl = document.getElementById('forecast-table-body');
    if (forecastEl && data.forecast) {
      forecastEl.innerHTML = data.forecast
        .map(function (row) {
          return (
            '<tr><td>Год ' + row.year + '</td>' +
            '<td>' + fmtNum(row.locations) + '</td>' +
            '<td>' + fmtMoney(row.revenue, c) + '</td>' +
            '<td>' + fmtMoney(row.ebitda, c) + '</td></tr>'
          );
        })
        .join('');
    }

    var mileEl = document.getElementById('milestones-list');
    if (mileEl && data.milestones) {
      mileEl.innerHTML = data.milestones
        .map(function (m) {
          return (
            '<div class="roadmap-item">' +
            '<span class="roadmap-step">' + m.quarter + '</span>' +
            '<div><h4>' + m.event + '</h4>' +
            '<p>KPI: ' + (m.kpi != null ? m.kpi : PLACEHOLDER) + '</p></div></div>'
          );
        })
        .join('');
    }
  }
})();

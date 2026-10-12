# Brief operativo — seduta di lunedì 12/10/2026

Generato lunedì 12/10/2026 alle 07:30 (ora di Roma) · morning-brief/1.1.0 · sola lettura, nessun ordine automatico.

## In breve

- **Seduta USA**: lunedì 12/10/2026, 09:30–16:00 ET = **15:30–22:00 ora di Roma**
- **Expansion 50M**: nessun piano · posizioni del modello aperte: 2
- **Post-Catalyst**: 1 candidati finora (QUMS) · decisione alle 15:20, nuove notizie ammesse fino alle 15:05
- **Salute**: Expansion ATTENZIONE · Post-Catalyst ATTENZIONE
- **Telegram attesi**: POST-CATALYST SIGNAL verso le 15:20 (solo con piano OK); dopo le 22:15 EXPANSION INGRESSO MODELLO CONFERMATO (se un piano della seduta è stato riempito) e PIANO PRONTO per la seduta successiva

## Expansion 50M — piani per la seduta

Nessun piano Expansion per questa seduta.

Piani in attesa per altre sedute: PENG (05/10)

### Posizioni del modello

- **LIND**: ingresso 02/10 a 34,53 $ · stop 30,96 $ · target 41,68 $ · chiusura del 02/10 34,78 $ (+0,07 R) · seduta 1 di 5 · uscita a tempo alla chiusura del 08/10 se non tocca stop o target
- **AAOI**: ingresso 02/10 a 110,36 $ · stop 97,11 $ · target 136,86 $ · chiusura del 02/10 115,59 $ (+0,39 R) · seduta 1 di 5 · uscita a tempo alla chiusura del 08/10 se non tocca stop o target

Ingressi del modello nella seduta del 02/10: LIND, AAOI.
- Uscita **VIAV** (02/10): USCITA A TEMPO · modello +1,47 R · con il tuo money management (27 azioni): +€ 132,95 (+1,45 R), stima

Coorte: sedute acquisite 6 · trade 4 (chiusi 2) · date d'ingresso indipendenti 2 su 10 (test di accettazione operativa) · R netto del modello +0,55 R · drawdown massimo 1,28 R · stato del motore OBSERVING.

## Post-Catalyst V1 — candidati per la decisione

Decisione premarket alle **15:20** ora di Roma (09:20 ET, dati SIP ritardati 15 minuti); le notizie fino alle 15:05 (09:05 ET) possono aggiungere candidati. Il SIGNAL arriva su Telegram solo se il piano è OK, già con la QUANTITÀ FINECO.

- **QUMS**: M&A · notizia di ven 09/10 22:07 · "Fortune Favor Technology Announces $600M SPAC Merger With Quantumsphere Acquisition Corp."

Ultima decisione: seduta del 09/10 (DONE): candidati 17, piani OK 11.
- **GRRR**: trigger 12,54 $ · stop 11,75 $ · esito EXPIRED_NO_TRIGGER
- **HOVR**: trigger 1,75 $ · stop 1,55 $ · esito EXPIRED_NO_TRIGGER
- **MCHP**: trigger 77,14 $ · stop 75,90 $ · esito EXPIRED_NO_TRIGGER
- **MIST**: trigger 0,8029 $ · stop 0,7132 $ · esito EXPIRED_NO_TRIGGER
- **MLYS**: trigger 22,42 $ · stop 22,22 $ · esito CANCEL_OPEN_ABOVE_CEILING
- **PENN**: trigger 15,82 $ · stop 15,72 $ · esito CANCEL_OPEN_ABOVE_CEILING
- **PHVS**: trigger 32,07 $ · stop 30,37 $ · esito EXPIRED_NO_TRIGGER
- **SBUX**: trigger 93,51 $ · stop 92,37 $ · esito EXPIRED_NO_TRIGGER
- **SHC**: trigger 17,79 $ · stop 17,70 $ · esito CANCEL_OPEN_ABOVE_CEILING
- **SVC**: trigger 7,08 $ · stop 6,18 $ · esito FILLED, STOP -1,11 R
- **XMAX**: trigger 8,97 $ · stop 8,80 $ · esito FILLED, STOP -1,16 R

Dall'attivazione (25/09): eventi in perimetro 230 · sedute decise 10 · piani OK 140 · esiti di piano 206 · R realizzati -44,29 R.

## Salute dei sistemi

**Expansion 50M: ATTENZIONE**
- Runner: task DISABILITATA, ultima esecuzione 05/10 14:00 (esito 0), prossima 12/10 13:00
- Ultimo esito del runner: INGESTED (seduta 02/10, 02/10 22:32)
- Ultima seduta acquisita: 02/10 (attesa: 09/10)
- Controllo di salute esterno: task DISABILITATA, ultima esecuzione 05/10 14:10 (esito 0), prossima 12/10 13:10; nessuna condizione attiva (ultimo controllo 05/10 14:10)
- Problema: runner: task disabilitata
- Problema: controllo di salute: task disabilitata
- Problema: seduta del 09/10 non ancora nel ledger (ultima acquisita: 02/10)
- Problema: piani di una seduta passata ancora in attesa: PENG

**Post-Catalyst V1: ATTENZIONE**
- Listener: ultimo heartbeat 12/10 07:30 (OK); task pronta, ultima esecuzione 12/10 07:30 (esito 0), prossima 12/10 07:32
- Watchdog: ultimo heartbeat 12/10 07:23 (OK); task pronta, ultima esecuzione 12/10 07:23 (esito 0), prossima 12/10 07:53
- Ultime 24 ore: notizie 53 · esecuzioni FAIL 0 · notizie in errore 0 · messaggi L2/HEALTH non consegnati 48
- Problema: messaggi Telegram L2/HEALTH non consegnati: 48

## Promemoria operativi

- Money management: controvalore massimo € 1.000,00, perdita massima € 100,00 allo stop del piano. Lo stop del piano non si modifica mai.
- Conto Fineco Trading: 0,19% per eseguito (min € 2,95, max € 19,00) più lo spread di cambio (0,0033 a conversione): su € 1.000,00 circa € 11,82 andata e ritorno.
- Nessun ordine automatico: sono piani di ricerca e shadow. Apertura, stop e limite massimo d'ingresso si controllano a mano.
- Da verificare su Fineco: disponibilità di ordini condizionati d'ingresso per azioni USA sul conto Trading.

## Laboratorio

Da LAB_STATUS.md, aggiornato il 25/09/2026:
- Shadow attivo: EXPANSION_DELAYED_SIP_15M_SHADOW_50M (v1.0.0, SHADOW_OPERATIONAL dal 2026-09-25, freeze operativo)
- Ricerca attiva: POST_CATALYST_CONTINUATION_V1 (dal 2026-09-25; EARNINGS è una sua categoria)
- Backlog: ORB / Stocks in Play (`lab/backlog/ORB.md`): nessun codice, nessuna task
- Backlog: Candidate V2 di Expansion 50M e Post-Catalyst (`lab/backlog/V2_CANDIDATES.md`, annotate il 2026-09-26): uscita secondaria (rinviata), costi e dimensione reali, tassonomia, universo, replay storico; nessuna attiva

---
Fonti: ledger locali in sola lettura, calendario Alpaca, cambio BCE. Nessuna raccomandazione finanziaria.

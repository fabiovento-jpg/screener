# Brief operativo — seduta di lunedì 28/09/2026

Generato domenica 27/09/2026 alle 17:50 (ora di Roma) · morning-brief/1.1.0 · sola lettura, nessun ordine automatico.

## In breve

- **Seduta USA**: lunedì 28/09/2026, 09:30–16:00 ET = **15:30–22:00 ora di Roma** — oggi la borsa USA è chiusa: il brief riguarda la prossima seduta
- **Expansion 50M**: 3 piani validi: AAON, VIAV, MXL · posizioni del modello aperte: 0
- **Post-Catalyst**: 3 candidati finora (ACET, FMAC, KOD) · decisione alle 15:20, nuove notizie ammesse fino alle 15:05
- **Salute**: Expansion OK · Post-Catalyst OK
- **Telegram attesi**: POST-CATALYST SIGNAL verso le 15:20 (solo con piano OK); dopo le 22:15 EXPANSION INGRESSO MODELLO CONFERMATO (se un piano della seduta è stato riempito) e PIANO PRONTO per la seduta successiva

## Expansion 50M — piani per la seduta

### AAON
- Ingresso sopra **90,18 $** · limite massimo d'ingresso **91,70 $** · stop **84,09 $** (−6,8% dall'ingresso teorico)
- **Quantità Fineco: 12 azioni** · controvalore stimato € 949,95 · perdita stimata allo stop € 65,01
- Target 2R indicativo 102,62 $ (su ingresso teorico 90,27 $)
- Costi Fineco stimati andata e ritorno: € 11,43 (0,18 R)
- Quantità modello: 3 (solo ricerca, non per Fineco) · segnale della seduta 25/09

### VIAV
- Ingresso sopra **40,99 $** · limite massimo d'ingresso **41,93 $** · stop **37,21 $** (−9,3% dall'ingresso teorico)
- **Quantità Fineco: 27 azioni** · controvalore stimato € 971,49 · perdita stimata allo stop € 90,36
- Target 2R indicativo 48,66 $ (su ingresso teorico 41,03 $)
- Costi Fineco stimati andata e ritorno: € 11,55 (0,13 R)
- Quantità modello: 5 (solo ricerca, non per Fineco) · segnale della seduta 25/09

### MXL
- Ingresso sopra **96,53 $** · limite massimo d'ingresso **99,41 $** · stop **85,00 $** (−12,0% dall'ingresso teorico)
- **Quantità Fineco: 9 azioni** · controvalore stimato € 762,61 · perdita stimata allo stop € 91,76
- Target 2R indicativo 119,87 $ (su ingresso teorico 96,62 $)
- Costi Fineco stimati andata e ritorno: € 10,34 (0,11 R)
- Quantità modello: 1 (solo ricerca, non per Fineco) · segnale della seduta 25/09

Cambio EUR/USD usato: 1,1403 (BCE del 25/09/2026).

**Regole all'apertura (15:30 ora di Roma)**: apertura ≤ stop → non entrare · apertura > limite massimo d'ingresso → non entrare · se in seduta non tocca l'ingresso → nessun ingresso. Valido solo per questa seduta.

### Posizioni del modello

Nessuna posizione aperta del modello.

Coorte: sedute acquisite 1 · trade 0 (chiusi 0) · date d'ingresso indipendenti 0 su 10 (test di accettazione operativa) · R netto del modello +0,00 R · drawdown massimo 0,00 R · stato del motore OBSERVING.

## Post-Catalyst V1 — candidati per la decisione

Decisione premarket alle **15:20** ora di Roma (09:20 ET, dati SIP ritardati 15 minuti); le notizie fino alle 15:05 (09:05 ET) possono aggiungere candidati. Il SIGNAL arriva su Telegram solo se il piano è OK, già con la QUANTITÀ FINECO.

- **ACET**: CLINICAL_RESULT · notizia di ven 25/09 22:01 · "Adicet Bio To Report Clinical Data From Phase 1 Study Evaluating Prulacabtagene Leucel As Potential Treatment For Patients With Systemic…"
- **FMAC**: M&A · notizia di ven 25/09 23:02 · "Future Money Acquisition Corp. Receives Nasdaq Deficiency Notice Over Delayed July 31, 2026 Quarterly Form 10-Q Filing"
- **KOD**: CLINICAL_RESULT · notizia di sab 26/09 00:03 · "Kodiak Sciences To Host Webcast To Report Phase 3 DAYBREAK Topline Results For Wet AMD Candidates On September 28 At 8:30 AM Eastern Time"

Nessuna decisione ancora registrata dall'attivazione.

Dall'attivazione (25/09): eventi in perimetro 3 · sedute decise 0 · piani OK 0 · esiti di piano 0 · R realizzati 0.

## Salute dei sistemi

**Expansion 50M: OK**
- Runner: task pronta, ultima esecuzione 25/09 23:00 (esito 0), prossima 28/09 13:00
- Ultimo esito del runner: INGESTED (seduta 25/09, 25/09 22:33)
- Ultima seduta acquisita: 25/09 (attesa: 25/09)
- Controllo di salute esterno: task pronta, ultima esecuzione 26/09 18:54 (esito 0), prossima 28/09 13:10; nessuna condizione attiva (ultimo controllo 26/09 18:54)

**Post-Catalyst V1: OK**
- Listener: ultimo heartbeat 27/09 17:50 (OK); task pronta, ultima esecuzione 27/09 17:50 (esito 0), prossima 27/09 17:52
- Watchdog: ultimo heartbeat 27/09 17:23 (OK); task pronta, ultima esecuzione 27/09 17:23 (esito 0), prossima 27/09 17:53
- Ultime 24 ore: notizie 28 · esecuzioni FAIL 1 · notizie in errore 0 · messaggi L2/HEALTH non consegnati 0

## Promemoria operativi

- Money management: controvalore massimo € 1.000,00, perdita massima € 100,00 allo stop del piano. Lo stop del piano non si modifica mai.
- Conto Fineco Trading: 0,19% per eseguito (min € 2,95, max € 19,00) più lo spread di cambio (0,0033 a conversione): su € 1.000,00 circa € 11,72 andata e ritorno.
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

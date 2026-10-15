# Digest Telegram — MOMENTUM 12-1 LIQUID500

Digest **separato** da ogni altro messaggio dello scanner. Non si fonde con il
brief operativo giornaliero e non ne condivide il formato: e' un canale di
osservazione di ricerca, non un output operativo.

L'intestazione a quattro righe e' obbligatoria e non va abbreviata in nessun
messaggio, anche quando non ci sono nuovi ingressi.

---

## Intestazione obbligatoria

```
📊 MOMENTUM 12-1 LIQUID500
CANDIDATE SHADOW
NOT VALIDATED FOR CAPITAL
NO AUTOMATIC ORDER
```

## Corpo — per ogni ranking mensile

```
Ranking: <YYYY-MM-DD>
Titoli Liquid500: <n>
Soglia ADV20 del 500°: <valore>
Classificabili: <n>
Titoli Q5: <n>
Nuovi ingressi: <n>
Uscite previste: <n>
Uscite effettuate: <n>
Versione: MOMENTUM_12_1_LIQUID500_V1
Stato: CANDIDATE_SHADOW
```

## Per ogni nuovo ingresso

```
<TICKER>
PRET: <valore>
ADV20: <valore>
Entry previsto: next session open (<YYYY-MM-DD>)
Exit prevista: 126a seduta (<YYYY-MM-DD>)
```

## Chiusura obbligatoria

```
Nessun consiglio di acquisto. Nessun ordine automatico.
```

---

## Esempio completo

Primo digest forward atteso. I numeri sono **segnaposto illustrativi**: nessun
ranking e' stato calcolato, e questo repository non contiene il motore che lo
calcola.

```
📊 MOMENTUM 12-1 LIQUID500
CANDIDATE SHADOW
NOT VALIDATED FOR CAPITAL
NO AUTOMATIC ORDER

Ranking: 2026-10-30
Titoli Liquid500: 500
Soglia ADV20 del 500°: 8.412.000 USD
Classificabili: 487
Titoli Q5: 97
Nuovi ingressi: 12
Uscite previste: 0
Uscite effettuate: 0
Versione: MOMENTUM_12_1_LIQUID500_V1
Stato: CANDIDATE_SHADOW

NUOVI INGRESSI

AVGO
PRET: 0,7321
ADV20: 12.500.000 USD
Entry previsto: next session open (2026-11-02)
Exit prevista: 126a seduta (2027-05-06)

ANET
PRET: 0,6854
ADV20: 9.800.000 USD
Entry previsto: next session open (2026-11-02)
Exit prevista: 126a seduta (2027-05-06)

[... altri 10 ingressi ...]

Coorti forward complete: 0 / 12 minimo (24 preferite)

Nessun consiglio di acquisto. Nessun ordine automatico.
```

---

## Regole del messaggio

1. **`Classificabili` e' distinto da `Titoli Liquid500`.** Un titolo nell'universo
   senza 252+21 sedute di storico non e' classificabile e non entra nel ranking.
   La differenza fra i due numeri va sempre mostrata, mai nascosta: e' la misura
   di quanto del campione e' stato effettivamente valutato.
2. **Il conteggio delle coorti complete va in ogni digest**, nella forma
   `n / 12 minimo (24 preferite)`. Serve a non leggere i risultati parziali come
   evidenza.
3. **Nessun prezzo di ingresso nel digest del ranking.** L'entry e' all'open
   della seduta successiva, che al momento del messaggio non esiste ancora.
   Dichiarare un prezzo prima dell'apertura sarebbe un'invenzione.
4. **Nessun ordinamento per attrattivita', nessun "migliore", nessun punteggio
   di convinzione.** I titoli si elencano in ordine di PRET decrescente perche'
   e' il ranking, non perche' sia una classifica di preferenza.
5. **Se il ranking non e' disponibile** (dati mancanti, universo non
   ricostruibile point-in-time, motore non eseguito), il digest lo dichiara e
   **non emette alcun segnale**:

   ```
   📊 MOMENTUM 12-1 LIQUID500
   CANDIDATE SHADOW
   NOT VALIDATED FOR CAPITAL
   NO AUTOMATIC ORDER

   Ranking: 2026-10-30
   NESSUN SEGNALE EMESSO
   Motivo: <motivo esplicito>
   Versione: MOMENTUM_12_1_LIQUID500_V1
   Stato: CANDIDATE_SHADOW

   Nessun consiglio di acquisto. Nessun ordine automatico.
   ```

   Un ranking parziale o ricostruito in altro modo **non e' il ranking**: la
   coorte salta e viene registrata come mancante. Un segnale improvvisato
   contaminerebbe il campione forward in modo irreversibile.

## Punto di collegamento

Questo file definisce **il formato**, non l'invio. Il bot Telegram e il motore
che calcola il ranking Liquid500 point-in-time vivono nel progetto locale, non
in questo repository: qui non ci sono credenziali ne' pipeline di universo.

L'invio va agganciato dove risiede il bot, leggendo:

- `forward/MOMENTUM_12_1_LIQUID500_V1/freeze.json` per stato, versione e date;
- `forward/MOMENTUM_12_1_LIQUID500_V1/ledger_FORWARD_ONLY.csv` per il conteggio
  delle coorti complete (`tools/forward_ledger.py --summary`).

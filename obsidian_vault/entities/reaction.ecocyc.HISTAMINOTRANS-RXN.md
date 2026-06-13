---
entity_id: "reaction.ecocyc.HISTAMINOTRANS-RXN"
entity_type: "reaction"
name: "HISTAMINOTRANS-RXN"
source_database: "EcoCyc"
source_id: "HISTAMINOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HISTAMINOTRANS-RXN

`reaction.ecocyc.HISTAMINOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HISTAMINOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-HISTIDINOL-P + 2-KETOGLUTARATE -> IMIDAZOLE-ACETOL-P + GLT; direction=REVERSIBLE EcoCyc reaction equation: L-HISTIDINOL-P + 2-KETOGLUTARATE -> IMIDAZOLE-ACETOL-P + GLT; direction=REVERSIBLE.

## Biological Role

Catalyzed by histidinol-phosphate aminotransferase (complex.ecocyc.HISTPHOSTRANS-CPLX). Substrates: 2-Oxoglutarate (molecule.C00026), L-Histidinol phosphate (molecule.C01100). Products: L-Glutamate (molecule.C00025), 3-(Imidazol-4-yl)-2-oxopropyl phosphate (molecule.C01267).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

L-HISTIDINOL-P + 2-KETOGLUTARATE -> IMIDAZOLE-ACETOL-P + GLT; direction=REVERSIBLE

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.HISTPHOSTRANS-CPLX|complex.ecocyc.HISTPHOSTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01267|molecule.C01267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01100|molecule.C01100]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HISTAMINOTRANS-RXN`

## Notes

L-HISTIDINOL-P + 2-KETOGLUTARATE -> IMIDAZOLE-ACETOL-P + GLT; direction=REVERSIBLE

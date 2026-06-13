---
entity_id: "reaction.ecocyc.VAGL-RXN"
entity_type: "reaction"
name: "VAGL-RXN"
source_database: "EcoCyc"
source_id: "VAGL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# VAGL-RXN

`reaction.ecocyc.VAGL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:VAGL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-AMINOPENTANOATE + 2-KETOGLUTARATE -> GLT + CPD-280; direction=REVERSIBLE EcoCyc reaction equation: 5-AMINOPENTANOATE + 2-KETOGLUTARATE -> GLT + CPD-280; direction=REVERSIBLE.

## Biological Role

Catalyzed by 4-aminobutyrate aminotransferase GabT (complex.ecocyc.GABATRANSAM-CPLX), puuE (protein.P50457). Substrates: 2-Oxoglutarate (molecule.C00026), 5-Aminopentanoate (molecule.C00431). Products: L-Glutamate (molecule.C00025), 5-Oxopentanoate (molecule.C03273).

## Enriched Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Annotation

5-AMINOPENTANOATE + 2-KETOGLUTARATE -> GLT + CPD-280; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.GABATRANSAM-CPLX|complex.ecocyc.GABATRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P50457|protein.P50457]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03273|molecule.C03273]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00431|molecule.C00431]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:VAGL-RXN`

## Notes

5-AMINOPENTANOATE + 2-KETOGLUTARATE -> GLT + CPD-280; direction=REVERSIBLE

---
entity_id: "reaction.ecocyc.RXN0-7317"
entity_type: "reaction"
name: "RXN0-7317"
source_database: "EcoCyc"
source_id: "RXN0-7317"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7317

`reaction.ecocyc.RXN0-7317`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7317`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CADAVERINE + 2-KETOGLUTARATE -> CPD-12763 + GLT; direction=REVERSIBLE EcoCyc reaction equation: CADAVERINE + 2-KETOGLUTARATE -> CPD-12763 + GLT; direction=REVERSIBLE.

## Biological Role

Catalyzed by putrescine aminotransferase (complex.ecocyc.CPLX0-8159). Substrates: 2-Oxoglutarate (molecule.C00026), Cadaverine (molecule.C01672). Products: L-Glutamate (molecule.C00025), 5-Aminopentanal (molecule.C12455).

## Enriched Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Annotation

CADAVERINE + 2-KETOGLUTARATE -> CPD-12763 + GLT; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8159|complex.ecocyc.CPLX0-8159]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C12455|molecule.C12455]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7317`

## Notes

CADAVERINE + 2-KETOGLUTARATE -> CPD-12763 + GLT; direction=REVERSIBLE

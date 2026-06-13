---
entity_id: "reaction.ecocyc.2.6.1.57-RXN"
entity_type: "reaction"
name: "2.6.1.57-RXN"
source_database: "EcoCyc"
source_id: "2.6.1.57-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.6.1.57-RXN

`reaction.ecocyc.2.6.1.57-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.6.1.57-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Aromatic-Amino-Acids + 2-KETOGLUTARATE -> Aromatic-Oxoacids + GLT; direction=REVERSIBLE EcoCyc reaction equation: Aromatic-Amino-Acids + 2-KETOGLUTARATE -> Aromatic-Oxoacids + GLT; direction=REVERSIBLE.

## Biological Role

Catalyzed by tyrosine aminotransferase (complex.ecocyc.TYRB-DIMER). Substrates: 2-Oxoglutarate (molecule.C00026), an aromatic amino acid (molecule.ecocyc.Aromatic-Amino-Acids). Products: L-Glutamate (molecule.C00025), an aromatic 2-oxo-acid (molecule.ecocyc.Aromatic-Oxoacids).

## Annotation

Aromatic-Amino-Acids + 2-KETOGLUTARATE -> Aromatic-Oxoacids + GLT; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.TYRB-DIMER|complex.ecocyc.TYRB-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Aromatic-Oxoacids|molecule.ecocyc.Aromatic-Oxoacids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aromatic-Amino-Acids|molecule.ecocyc.Aromatic-Amino-Acids]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.6.1.57-RXN`

## Notes

Aromatic-Amino-Acids + 2-KETOGLUTARATE -> Aromatic-Oxoacids + GLT; direction=REVERSIBLE

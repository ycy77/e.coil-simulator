---
entity_id: "reaction.ecocyc.5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN"
entity_type: "reaction"
name: "5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN"
source_database: "EcoCyc"
source_id: "5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN

`reaction.ecocyc.5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-METHYLTHIOADENOSINE + Pi -> ADENINE + CPD-444; direction=REVERSIBLE EcoCyc reaction equation: 5-METHYLTHIOADENOSINE + Pi -> ADENINE + CPD-444; direction=REVERSIBLE.

## Biological Role

Catalyzed by yfiH (protein.P33644). Substrates: 5'-Methylthioadenosine (molecule.C00170), phosphate (molecule.ecocyc.Pi). Products: Adenine (molecule.C00147), S-Methyl-5-thio-D-ribose 1-phosphate (molecule.C04188).

## Annotation

5-METHYLTHIOADENOSINE + Pi -> ADENINE + CPD-444; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33644|protein.P33644]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04188|molecule.C04188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00170|molecule.C00170]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN`

## Notes

5-METHYLTHIOADENOSINE + Pi -> ADENINE + CPD-444; direction=REVERSIBLE

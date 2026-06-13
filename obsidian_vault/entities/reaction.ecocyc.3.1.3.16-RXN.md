---
entity_id: "reaction.ecocyc.3.1.3.16-RXN"
entity_type: "reaction"
name: "3.1.3.16-RXN"
source_database: "EcoCyc"
source_id: "3.1.3.16-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PROTEIN PHOSPHATASE-2C"
  - "PROTEIN PHOSPHATASE-2B"
  - "PROTEIN PHOSPHATASE-2A"
  - "PROTEIN PHOSPHATASE-1"
  - "PHOSPHOPROTEIN PHOSPHATASE"
---

# 3.1.3.16-RXN

`reaction.ecocyc.3.1.3.16-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.3.16-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A group of reactions removing the serine- or threonine-bound phosphate group from a wide range of phosphoproteins, including enzymes that have been phosphorylated by the action of a kinase (cf EC 3.1.3.48). In some cases, these reactions can also act on phenolic phosphates and phosphamides. EcoCyc reaction equation: Protein-Ser-or-Thr-phosphate + WATER -> Protein-L-serine-or-L-threonine + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. A group of reactions removing the serine- or threonine-bound phosphate group from a wide range of phosphoproteins, including enzymes that have been phosphorylated by the action of a kinase (cf EC 3.1.3.48). In some cases, these reactions can also act on phenolic phosphates and phosphamides.

## Biological Role

Catalyzed by pphA (protein.P55798), pphB (protein.P55799), pphC (protein.P76395). Substrates: H2O (molecule.C00001), a [protein] (L-serine/L-threonine) phosphate (molecule.ecocyc.Protein-Ser-or-Thr-phosphate). Products: phosphate (molecule.ecocyc.Pi), a [protein]-(L-serine/L-threonine) (molecule.ecocyc.Protein-L-serine-or-L-threonine).

## Annotation

A group of reactions removing the serine- or threonine-bound phosphate group from a wide range of phosphoproteins, including enzymes that have been phosphorylated by the action of a kinase (cf EC 3.1.3.48). In some cases, these reactions can also act on phenolic phosphates and phosphamides.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P55798|protein.P55798]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P55799|protein.P55799]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76395|protein.P76395]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-L-serine-or-L-threonine|molecule.ecocyc.Protein-L-serine-or-L-threonine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Ser-or-Thr-phosphate|molecule.ecocyc.Protein-Ser-or-Thr-phosphate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.3.16-RXN`

## Notes

Protein-Ser-or-Thr-phosphate + WATER -> Protein-L-serine-or-L-threonine + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

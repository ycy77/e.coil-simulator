---
entity_id: "reaction.ecocyc.PROTEIN-KINASE-RXN"
entity_type: "reaction"
name: "PROTEIN-KINASE-RXN"
source_database: "EcoCyc"
source_id: "PROTEIN-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Phosphorylase B kinase kinase"
  - "Glycogen synthase A kinase"
  - "Hydroxyalkyl-protein kinase"
  - "Serine(threonine) protein kinase"
  - "HEART &alpha"
  - "-KINASE"
  - "HORMONALLY UPREGULATED NEU TUMOR-ASSOCIATED KINASE"
  - "INHIBITOR OF NUCLEAR FACTOR KAPPA-B KINASE &alpha"
  - "SUBUNIT"
  - "INHIBITOR OF NUCLEAR FACTOR KAPPA-B KINASE &epsilon"
  - "INHIBITOR OF NUCLEAR FACTOR KAPPA B KINASE &beta"
  - "inhibitor of kappa light polypeptide gene enhancer in B-cells, kinase &beta"
  - "TRAF2 AND NCK INTERACTING KINASE, SPLICE VARIANT 6"
  - "integrin-linked kinase-2"
  - "interleukin-1 receptor-associated kinase 1"
  - "INTERLEUKIN-1 RECEPTOR-ASSOCIATED KINASE 3"
  - "INTERLEUKIN-1 RECEPTOR-ASSOCIATED KINASE 4"
  - "INTERLEUKIN-1 RECEPTOR-ASSOCIATED KINASE-2"
  - "INTESTINAL CELL KINASE ISOFORM A"
  - "LIM domain kinase 2 isoform 2a"
---

# PROTEIN-KINASE-RXN

`reaction.ecocyc.PROTEIN-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PROTEIN-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-L-serine-or-L-threonine + ATP -> Protein-Ser-or-Thr-phosphate + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Protein-L-serine-or-L-threonine + ATP -> Protein-Ser-or-Thr-phosphate + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yeaG (protein.P0ACY3), srkA (protein.P0C0K3). Substrates: ATP (molecule.C00002), a [protein]-(L-serine/L-threonine) (molecule.ecocyc.Protein-L-serine-or-L-threonine). Products: ADP (molecule.C00008), H+ (molecule.C00080), a [protein] (L-serine/L-threonine) phosphate (molecule.ecocyc.Protein-Ser-or-Thr-phosphate).

## Annotation

Protein-L-serine-or-L-threonine + ATP -> Protein-Ser-or-Thr-phosphate + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0ACY3|protein.P0ACY3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0C0K3|protein.P0C0K3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Ser-or-Thr-phosphate|molecule.ecocyc.Protein-Ser-or-Thr-phosphate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-serine-or-L-threonine|molecule.ecocyc.Protein-L-serine-or-L-threonine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PROTEIN-KINASE-RXN`

## Notes

Protein-L-serine-or-L-threonine + ATP -> Protein-Ser-or-Thr-phosphate + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

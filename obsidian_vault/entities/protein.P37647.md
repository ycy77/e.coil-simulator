---
entity_id: "protein.P37647"
entity_type: "protein"
name: "kdgK"
source_database: "UniProt"
source_id: "P37647"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdgK yhjI b3526 JW5668"
---

# kdgK

`protein.P37647`

## Static

- Type: `protein`
- Source: `UniProt:P37647`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of 2-keto-3-deoxygluconate (KDG) to produce 2-keto-3-deoxy-6-phosphogluconate (KDPG). {ECO:0000269|PubMed:4944816}. 2-dehydro-3-deoxygluconokinase catalyzes the ATP-dependent phosphorylation of the first common intermediate in the D-glucuronate and D-galacturonate degradation pathways, 2-dehydro-3-deoxy-D-gluconate . The activity of KdgK increases 5-fold in cells grown on galacturonate or glucoronate rather than on glucose . KdgK: "2-keto-3-deoxygluconokinase"

## Biological Role

Catalyzes ATP:2-dehydro-3-deoxy-D-gluconate 6-phosphotransferase (reaction.R01541), DEOXYGLUCONOKIN-RXN (reaction.ecocyc.DEOXYGLUCONOKIN-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of 2-keto-3-deoxygluconate (KDG) to produce 2-keto-3-deoxy-6-phosphogluconate (KDPG). {ECO:0000269|PubMed:4944816}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01541|reaction.R01541]] `KEGG` `database` - via EC:2.7.1.45
- `catalyzes` --> [[reaction.ecocyc.DEOXYGLUCONOKIN-RXN|reaction.ecocyc.DEOXYGLUCONOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3526|gene.b3526]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37647`
- `KEGG:ecj:JW5668;eco:b3526;ecoc:C3026_19105;`
- `GeneID:948041;`
- `GO:GO:0005524; GO:0005829; GO:0006974; GO:0008673; GO:0019698; GO:0042840`
- `EC:2.7.1.45`

## Notes

2-dehydro-3-deoxygluconokinase (EC 2.7.1.45) (2-keto-3-deoxygluconokinase) (3-deoxy-2-oxo-D-gluconate kinase) (KDG kinase)

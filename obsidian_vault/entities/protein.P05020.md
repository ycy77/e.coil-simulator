---
entity_id: "protein.P05020"
entity_type: "protein"
name: "pyrC"
source_database: "UniProt"
source_id: "P05020"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrC b1062 JW1049"
---

# pyrC

`protein.P05020`

## Static

- Type: `protein`
- Source: `UniProt:P05020`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible cyclization of carbamoyl aspartate to dihydroorotate. {ECO:0000255|HAMAP-Rule:MF_00219, ECO:0000269|PubMed:15610022, ECO:0000269|PubMed:6142052}.

## Biological Role

Component of dihydroorotase (complex.ecocyc.DIHYDROOROT-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible cyclization of carbamoyl aspartate to dihydroorotate. {ECO:0000255|HAMAP-Rule:MF_00219, ECO:0000269|PubMed:15610022, ECO:0000269|PubMed:6142052}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DIHYDROOROT-CPLX|complex.ecocyc.DIHYDROOROT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1062|gene.b1062]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05020`
- `KEGG:ecj:JW1049;eco:b1062;ecoc:C3026_06455;`
- `GeneID:75203649;945787;`
- `GO:GO:0004151; GO:0005737; GO:0005829; GO:0006207; GO:0006221; GO:0008270; GO:0042803; GO:0044205`
- `EC:3.5.2.3`

## Notes

Dihydroorotase (DHOase) (EC 3.5.2.3)

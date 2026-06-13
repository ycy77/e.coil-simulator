---
entity_id: "protein.P0AF03"
entity_type: "protein"
name: "mog"
source_database: "UniProt"
source_id: "P0AF03"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mog chlG mogA yaaG b0009 JW0008"
---

# mog

`protein.P0AF03`

## Static

- Type: `protein`
- Source: `UniProt:P0AF03`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the adenylation of molybdopterin as part of the biosynthesis of the molybdenum-cofactor. {ECO:0000269|PubMed:15632135}.

## Biological Role

Component of molybdopterin adenylyltransferase (complex.ecocyc.CPLX0-8163).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Catalyzes the adenylation of molybdopterin as part of the biosynthesis of the molybdenum-cofactor. {ECO:0000269|PubMed:15632135}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8163|complex.ecocyc.CPLX0-8163]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0009|gene.b0009]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF03`
- `KEGG:ecj:JW0008;eco:b0009;ecoc:C3026_00050;`
- `GeneID:75169908;944760;`
- `GO:GO:0005524; GO:0005829; GO:0006777; GO:0032324; GO:0042802; GO:0061598`
- `EC:2.7.7.75`

## Notes

Molybdopterin adenylyltransferase (MPT adenylyltransferase) (EC 2.7.7.75)

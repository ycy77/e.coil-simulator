---
entity_id: "protein.P06986"
entity_type: "protein"
name: "hisC"
source_database: "UniProt"
source_id: "P06986"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisC b2021 JW2003"
---

# hisC

`protein.P06986`

## Static

- Type: `protein`
- Source: `UniProt:P06986`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (HPAT) (HspAT)

## Biological Role

Catalyzes L-phenylalanine:2-oxoglutarate aminotransferase (reaction.R00694), L-tyrosine:2-oxoglutarate aminotransferase (reaction.R00734). Component of histidinol-phosphate aminotransferase (complex.ecocyc.HISTPHOSTRANS-CPLX).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (HPAT) (HspAT)

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00694|reaction.R00694]] `KEGG` `database` - via EC:2.6.1.9
- `catalyzes` --> [[reaction.R00734|reaction.R00734]] `KEGG` `database` - via EC:2.6.1.9
- `is_component_of` --> [[complex.ecocyc.HISTPHOSTRANS-CPLX|complex.ecocyc.HISTPHOSTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2021|gene.b2021]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06986`
- `KEGG:ecj:JW2003;eco:b2021;ecoc:C3026_11395;`
- `GeneID:946551;`
- `GO:GO:0000105; GO:0004400; GO:0005829; GO:0030170; GO:0042802`
- `EC:2.6.1.9`

## Notes

Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (HPAT) (HspAT)

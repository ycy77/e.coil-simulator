---
entity_id: "protein.P45425"
entity_type: "protein"
name: "nanK"
source_database: "UniProt"
source_id: "P45425"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanK yhcI b3222 JW5538"
---

# nanK

`protein.P45425`

## Static

- Type: `protein`
- Source: `UniProt:P45425`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of N-acetylmannosamine (ManNAc) to ManNAc-6-P. Also has low level glucokinase activity in vitro. {ECO:0000269|PubMed:15157072, ECO:0000269|PubMed:17979299}.

## Biological Role

Component of N-acetylmannosamine kinase (complex.ecocyc.CPLX0-8588).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of N-acetylmannosamine (ManNAc) to ManNAc-6-P. Also has low level glucokinase activity in vitro. {ECO:0000269|PubMed:15157072, ECO:0000269|PubMed:17979299}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8588|complex.ecocyc.CPLX0-8588]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3222|gene.b3222]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45425`
- `KEGG:ecj:JW5538;eco:b3222;ecoc:C3026_17530;`
- `GeneID:947757;`
- `GO:GO:0005524; GO:0006974; GO:0008270; GO:0009384; GO:0019262`
- `EC:2.7.1.60`

## Notes

N-acetylmannosamine kinase (EC 2.7.1.60) (ManNAc kinase) (N-acetyl-D-mannosamine kinase)

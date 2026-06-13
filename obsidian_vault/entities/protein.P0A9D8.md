---
entity_id: "protein.P0A9D8"
entity_type: "protein"
name: "dapD"
source_database: "UniProt"
source_id: "P0A9D8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dapD b0166 JW0161"
---

# dapD

`protein.P0A9D8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9D8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the formation of N-succinyl-2-amino-6-oxo-L-pimelate from succinyl-CoA and tetrahydrodipicolinate, a key step in lysine biosynthesis via diaminopimelate pathway. {ECO:0000269|PubMed:6365916}. Tetrahydrodipicolinate succinylase (DapD) catalyzes the formation of N-succinyl-2-amino-6-ketopimelate from succinyl-CoA and tetrahydrodipicolinate, and is a key enzyme in the E. coli lysine biosynthetic pathway . A crystal structure of DapD from E. coli O157:H7 has been solved . Expression of dapD is repressed by lysine via ArgP . DapD: "diaminopimelate biosynthesis D"

## Biological Role

Component of tetrahydrodipicolinate succinylase (complex.ecocyc.CPLX0-3181).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of N-succinyl-2-amino-6-oxo-L-pimelate from succinyl-CoA and tetrahydrodipicolinate, a key step in lysine biosynthesis via diaminopimelate pathway. {ECO:0000269|PubMed:6365916}.

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3181|complex.ecocyc.CPLX0-3181]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0166|gene.b0166]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9D8`
- `KEGG:ecj:JW0161;eco:b0166;ecoc:C3026_00755;`
- `GeneID:93777259;944862;`
- `GO:GO:0005829; GO:0008666; GO:0009085; GO:0009089; GO:0016779; GO:0019877`
- `EC:2.3.1.117`

## Notes

2,3,4,5-tetrahydropyridine-2,6-dicarboxylate N-succinyltransferase (EC 2.3.1.117) (Succinyl-CoA: tetrahydrodipicolinate N-succinyltransferase) (Tetrahydrodipicolinate N-succinyltransferase) (THDP succinyltransferase) (THP succinyltransferase) (Tetrahydropicolinate succinylase)

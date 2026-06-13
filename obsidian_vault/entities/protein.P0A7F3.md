---
entity_id: "protein.P0A7F3"
entity_type: "protein"
name: "pyrI"
source_database: "UniProt"
source_id: "P0A7F3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrI b4244 JW4203"
---

# pyrI

`protein.P0A7F3`

## Static

- Type: `protein`
- Source: `UniProt:P0A7F3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in allosteric regulation of aspartate carbamoyltransferase.

## Biological Role

Component of aspartate carbamoyltransferase, regulatory subunit (complex.ecocyc.ASPCARBREG-DIMER), aspartate carbamoyltransferase (complex.ecocyc.ASPCARBTRANS-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in allosteric regulation of aspartate carbamoyltransferase.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ASPCARBREG-DIMER|complex.ecocyc.ASPCARBREG-DIMER]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.ASPCARBTRANS-CPLX|complex.ecocyc.ASPCARBTRANS-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4244|gene.b4244]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7F3`
- `KEGG:ecj:JW4203;eco:b4244;ecoc:C3026_22905;`
- `GeneID:86861356;93777580;948763;`
- `GO:GO:0005737; GO:0006207; GO:0006221; GO:0008270; GO:0009347`

## Notes

Aspartate carbamoyltransferase regulatory chain

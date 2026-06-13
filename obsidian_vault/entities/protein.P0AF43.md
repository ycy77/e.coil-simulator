---
entity_id: "protein.P0AF43"
entity_type: "protein"
name: "yjbB"
source_database: "UniProt"
source_id: "P0AF43"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjbB b4020 JW3980"
---

# yjbB

`protein.P0AF43`

## Static

- Type: `protein`
- Source: `UniProt:P0AF43`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Might be involved in phosphate export (PubMed:21488939). Overproduction of YjbB reduces the elevated levels of polyphosphate (polyP) in a phoU mutant that accumulates 1000-fold higher levels of polyP than the wild type, suggesting that YjbB exports excess intracellular phosphate (Pi) in the phoU mutant and thus reduces the levels of polyP (PubMed:21488939). {ECO:0000269|PubMed:21488939}. YjbB is a putative inorganic phosphate (Pi) export protein. Overproduction of YjbB reduces the increased levels of polyphosphate that accumulate in a phoU mutant . Overproduction of YjbB increases the rate of Pi export when a phoA, yjbB, pitA, pitB, phnC, pstSCAB-phoU mutant strain is grown on glycerol-3-phosphate as the sole carbon source . YjbB contains an N-terminal Na+/Pi cotransporter domain .

## Biological Role

Catalyzes TRANS-RXN0-470 (reaction.ecocyc.TRANS-RXN0-470).

## Annotation

FUNCTION: Might be involved in phosphate export (PubMed:21488939). Overproduction of YjbB reduces the elevated levels of polyphosphate (polyP) in a phoU mutant that accumulates 1000-fold higher levels of polyP than the wild type, suggesting that YjbB exports excess intracellular phosphate (Pi) in the phoU mutant and thus reduces the levels of polyP (PubMed:21488939). {ECO:0000269|PubMed:21488939}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-470|reaction.ecocyc.TRANS-RXN0-470]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4020|gene.b4020]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF43`
- `KEGG:ecj:JW3980;eco:b4020;ecoc:C3026_21715;`
- `GeneID:93777875;948521;`
- `GO:GO:0005315; GO:0005436; GO:0005886; GO:0035435; GO:0044341`

## Notes

Putative inorganic phosphate export protein YjbB

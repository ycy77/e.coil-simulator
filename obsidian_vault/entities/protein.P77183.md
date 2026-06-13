---
entity_id: "protein.P77183"
entity_type: "protein"
name: "paoD"
source_database: "UniProt"
source_id: "P77183"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paoD yagQ b0283 JW0277"
---

# paoD

`protein.P77183`

## Static

- Type: `protein`
- Source: `UniProt:P77183`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Chaperone required for the production of an active PaoABC aldehyde oxidoreductase. Stabilizes the PaoC subunit and is required for the insertion of the molybdenum cofactor into this subunit (PubMed:19368556, PubMed:21081498). Binds molybdenum cofactor. Binds the molybdopterin cytosine dinucleotide (MCD) form of the cofactor after its formation by the molybdenum cofactor cytidylyltransferase MocA (PubMed:24498065). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:21081498, ECO:0000269|PubMed:24498065}.

## Biological Role

Component of molybdenum cofactor insertion chaperone PaoD (complex.ecocyc.CPLX0-8110).

## Annotation

FUNCTION: Chaperone required for the production of an active PaoABC aldehyde oxidoreductase. Stabilizes the PaoC subunit and is required for the insertion of the molybdenum cofactor into this subunit (PubMed:19368556, PubMed:21081498). Binds molybdenum cofactor. Binds the molybdopterin cytosine dinucleotide (MCD) form of the cofactor after its formation by the molybdenum cofactor cytidylyltransferase MocA (PubMed:24498065). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:21081498, ECO:0000269|PubMed:24498065}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8110|complex.ecocyc.CPLX0-8110]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0283|gene.b0283]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77183`
- `KEGG:ecj:JW0277;eco:b0283;ecoc:C3026_01380;ecoc:C3026_24015;`
- `GeneID:945010;`
- `GO:GO:0042803; GO:0043546`

## Notes

Molybdenum cofactor insertion chaperone PaoD

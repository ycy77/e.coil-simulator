---
entity_id: "protein.P07654"
entity_type: "protein"
name: "pstA"
source_database: "UniProt"
source_id: "P07654"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pstA phoT b3726 JW3704"
---

# pstA

`protein.P07654`

## Static

- Type: `protein`
- Source: `UniProt:P07654`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for phosphate; probably responsible for the translocation of the substrate across the membrane. PstA is one of two inner membrane subunits of an ATP-dependent high affinity phosphate uptake system. Protein topology in the inner membrane has been determined .

## Biological Role

Component of phosphate ABC transporter (complex.ecocyc.ABC-27-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for phosphate; probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-27-CPLX|complex.ecocyc.ABC-27-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3726|gene.b3726]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07654`
- `KEGG:ecj:JW3704;eco:b3726;ecoc:C3026_20195;`
- `GeneID:948239;`
- `GO:GO:0005315; GO:0006817; GO:0006974; GO:0016020; GO:0035435; GO:0055052`

## Notes

Phosphate transport system permease protein PstA

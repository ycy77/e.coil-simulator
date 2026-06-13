---
entity_id: "protein.P0AFR9"
entity_type: "protein"
name: "ydcV"
source_database: "UniProt"
source_id: "P0AFR9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydcV b1443 JW1438"
---

# ydcV

`protein.P0AFR9`

## Static

- Type: `protein`
- Source: `UniProt:P0AFR9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in natural transformation (PubMed:26826386). Probably part of the ABC transporter complex YdcSTUV. Probably responsible for the translocation of the substrate across the membrane. During natural transformation, may serve as the channel for dsDNA uptake (Probable). {ECO:0000269|PubMed:26826386, ECO:0000305|PubMed:26826386}. YdcV is the predicted inner membrane component of an uncharacterized ABC transporter . YdcV is implicated in double strand (ds) DNA transport across the inner membrane during natural transformation; a ydcV deletion mutant has significantly decreased rates of natural transformation compared to wild type .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-51-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Involved in natural transformation (PubMed:26826386). Probably part of the ABC transporter complex YdcSTUV. Probably responsible for the translocation of the substrate across the membrane. During natural transformation, may serve as the channel for dsDNA uptake (Probable). {ECO:0000269|PubMed:26826386, ECO:0000305|PubMed:26826386}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-51-CPLX|complex.ecocyc.ABC-51-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1443|gene.b1443]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFR9`
- `KEGG:ecj:JW1438;eco:b1443;ecoc:C3026_08395;`
- `GeneID:75171524;945903;`
- `GO:GO:0005886; GO:0009290; GO:0016020; GO:0055052; GO:0055085`

## Notes

Inner membrane ABC transporter permease protein YdcV

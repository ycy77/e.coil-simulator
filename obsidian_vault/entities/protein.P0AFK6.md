---
entity_id: "protein.P0AFK6"
entity_type: "protein"
name: "potC"
source_database: "UniProt"
source_id: "P0AFK6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potC b1124 JW1110"
---

# potC

`protein.P0AFK6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFK6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine. potC encodes one of two integral membrane subunits of an ATP-dependent spermidine uptake system; PotC is predicted to contain 6 transmembrane regions

## Biological Role

Component of spermidine preferential ABC transporter (complex.ecocyc.ABC-24-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-24-CPLX|complex.ecocyc.ABC-24-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1124|gene.b1124]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFK6`
- `KEGG:ecj:JW1110;eco:b1124;ecoc:C3026_06765;`
- `GeneID:86863623;93776286;945691;`
- `GO:GO:0005886; GO:0015417; GO:0015847; GO:0016020; GO:0043190; GO:1903711`

## Notes

Spermidine/putrescine transport system permease protein PotC

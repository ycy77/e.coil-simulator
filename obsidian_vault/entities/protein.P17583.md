---
entity_id: "protein.P17583"
entity_type: "protein"
name: "cynX"
source_database: "UniProt"
source_id: "P17583"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cynX b0341 JW0332"
---

# cynX

`protein.P17583`

## Static

- Type: `protein`
- Source: `UniProt:P17583`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: This protein is part of an active transport system that transports exogenous cyanate into E.coli cells. CynX is a putative cyanate transporter. CynX is a member of the major facilitator superfamily (MFS) of transporters , and the cynX gene has been shown to be part of a cyanate-induced operon with cynS and cynT, encoding cyanase and carbonic anhydrase, respectively . However, no phenotype has been observed for a knockout mutation in cynX . Overexpression of cynX confers resistance to bromoacetate .

## Biological Role

Catalyzes TRANS-RXN-14 (reaction.ecocyc.TRANS-RXN-14).

## Annotation

FUNCTION: This protein is part of an active transport system that transports exogenous cyanate into E.coli cells.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-14|reaction.ecocyc.TRANS-RXN-14]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0341|gene.b0341]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17583`
- `KEGG:ecj:JW0332;eco:b0341;`
- `GeneID:946770;`
- `GO:GO:0005886; GO:0009440; GO:0022857`

## Notes

Cyanate transport protein CynX

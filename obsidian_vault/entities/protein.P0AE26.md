---
entity_id: "protein.P0AE26"
entity_type: "protein"
name: "araH"
source_database: "UniProt"
source_id: "P0AE26"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "araH b4460 JW1887"
---

# araH

`protein.P0AE26`

## Static

- Type: `protein`
- Source: `UniProt:P0AE26`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for L-arabinose. Probably responsible for the translocation of the substrate across the membrane. araH is predicted to encode a hydrophobic protein

## Biological Role

Component of arabinose ABC transporter (complex.ecocyc.ABC-2-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for L-arabinose. Probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-2-CPLX|complex.ecocyc.ABC-2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4460|gene.b4460]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE26`
- `KEGG:ecj:JW1887;eco:b4460;ecoc:C3026_10780;`
- `GeneID:948923;`
- `GO:GO:0005886; GO:0015147; GO:0015751; GO:0016020; GO:0042882; GO:0055052`

## Notes

L-arabinose transport system permease protein AraH

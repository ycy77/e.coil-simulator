---
entity_id: "protein.P0AFB1"
entity_type: "protein"
name: "nlpI"
source_database: "UniProt"
source_id: "P0AFB1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Lipid-anchor."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nlpI yhbM b3163 JW3132"
---

# nlpI

`protein.P0AFB1`

## Static

- Type: `protein`
- Source: `UniProt:P0AFB1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Lipid-anchor.

## Enriched Summary

FUNCTION: May be involved in cell division. May play a role in bacterial septation or regulation of cell wall degradation during cell division. Negatively controls the production of extracellular DNA (eDNA). {ECO:0000269|PubMed:10400590, ECO:0000269|PubMed:20833130}.

## Biological Role

Component of lipoprotein NlpI (complex.ecocyc.CPLX0-8198).

## Annotation

FUNCTION: May be involved in cell division. May play a role in bacterial septation or regulation of cell wall degradation during cell division. Negatively controls the production of extracellular DNA (eDNA). {ECO:0000269|PubMed:10400590, ECO:0000269|PubMed:20833130}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8198|complex.ecocyc.CPLX0-8198]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3163|gene.b3163]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFB1`
- `KEGG:ecj:JW3132;eco:b3163;ecoc:C3026_17230;`
- `GeneID:86948028;93778820;947673;`
- `GO:GO:0000270; GO:0005886; GO:0030674; GO:0042803; GO:0051301`

## Notes

Lipoprotein NlpI

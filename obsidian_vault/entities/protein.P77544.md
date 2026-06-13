---
entity_id: "protein.P77544"
entity_type: "protein"
name: "yfcF"
source_database: "UniProt"
source_id: "P77544"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfcF b2301 JW2298"
---

# yfcF

`protein.P77544`

## Static

- Type: `protein`
- Source: `UniProt:P77544`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Exhibits glutathione (GSH) S-transferase activity toward 1-chloro-2,4-dinitrobenzene (CDNB); however this activity is as low as 1% of that of GstA. Also displays a GSH-dependent peroxidase activity toward cumene hydroperoxide. Is involved in defense against oxidative stress, probably via its peroxidase activity. {ECO:0000269|PubMed:17018556}.

## Biological Role

Component of glutathione S-transferase YfcF (complex.ecocyc.CPLX0-8573).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Exhibits glutathione (GSH) S-transferase activity toward 1-chloro-2,4-dinitrobenzene (CDNB); however this activity is as low as 1% of that of GstA. Also displays a GSH-dependent peroxidase activity toward cumene hydroperoxide. Is involved in defense against oxidative stress, probably via its peroxidase activity. {ECO:0000269|PubMed:17018556}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8573|complex.ecocyc.CPLX0-8573]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2301|gene.b2301]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77544`
- `KEGG:ecj:JW2298;eco:b2301;ecoc:C3026_12835;`
- `GeneID:75205653;946749;`
- `GO:GO:0004364; GO:0004601; GO:0006559; GO:0006749; GO:0016034; GO:0042542`
- `EC:2.5.1.18`

## Notes

Glutathione S-transferase YfcF (EC 2.5.1.18)

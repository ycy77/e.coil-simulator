---
entity_id: "protein.P60061"
entity_type: "protein"
name: "adiC"
source_database: "UniProt"
source_id: "P60061"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:12867448}; Multi-pass membrane protein {ECO:0000269|PubMed:21368142}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "adiC aniC yjdD yjdE b4115 JW4076"
---

# adiC

`protein.P60061`

## Static

- Type: `protein`
- Source: `UniProt:P60061`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:12867448}; Multi-pass membrane protein {ECO:0000269|PubMed:21368142}.

## Enriched Summary

FUNCTION: Major component of the acid-resistance (AR) system allowing enteric pathogens to survive the acidic environment in the stomach (Probable). Exchanges extracellular arginine for its intracellular decarboxylation product agmatine (Agm) thereby expelling intracellular protons (PubMed:12867448, PubMed:14594828, PubMed:19578361, PubMed:21368142). Probably undergoes several conformational states in order to translocate the substrate across the membrane; keeps the substrate accessible to only 1 side of the membrane at a time by opening and closing 3 membrane-internal gates (Probable). {ECO:0000269|PubMed:12867448, ECO:0000269|PubMed:14594828, ECO:0000269|PubMed:19578361, ECO:0000269|PubMed:21368142, ECO:0000305|PubMed:14594828, ECO:0000305|PubMed:21368142}.

## Biological Role

Component of arginine:agmatine antiporter (complex.ecocyc.CPLX0-7535).

## Annotation

FUNCTION: Major component of the acid-resistance (AR) system allowing enteric pathogens to survive the acidic environment in the stomach (Probable). Exchanges extracellular arginine for its intracellular decarboxylation product agmatine (Agm) thereby expelling intracellular protons (PubMed:12867448, PubMed:14594828, PubMed:19578361, PubMed:21368142). Probably undergoes several conformational states in order to translocate the substrate across the membrane; keeps the substrate accessible to only 1 side of the membrane at a time by opening and closing 3 membrane-internal gates (Probable). {ECO:0000269|PubMed:12867448, ECO:0000269|PubMed:14594828, ECO:0000269|PubMed:19578361, ECO:0000269|PubMed:21368142, ECO:0000305|PubMed:14594828, ECO:0000305|PubMed:21368142}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7535|complex.ecocyc.CPLX0-7535]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4115|gene.b4115]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60061`
- `KEGG:ecj:JW4076;eco:b4115;ecoc:C3026_22235;`
- `GeneID:93777720;948628;`
- `GO:GO:0005886; GO:0043862; GO:1990451`

## Notes

Arginine/agmatine antiporter

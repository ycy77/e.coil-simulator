---
entity_id: "protein.P32136"
entity_type: "protein"
name: "yihO"
source_database: "UniProt"
source_id: "P32136"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihO b3876 JW5852"
---

# yihO

`protein.P32136`

## Static

- Type: `protein`
- Source: `UniProt:P32136`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Could be involved in sulfoquinovose import. {ECO:0000269|PubMed:24463506}. An E. coli K-12 ΔyihO strain does not grow when sulfoquinovose is supplied as the sole carbon source. yihO is part of a 10-gene cluster which is conserved across E. coli species and has been implicated in sulfoquinovose catabolism . The YihO protein is a member of the glycoside-pentoside-hexuronide (GPH) cation symporter family of transporters but its transport mechanism has not been experimentally characterised.

## Biological Role

Catalyzes TRANS-RXN0-580 (reaction.ecocyc.TRANS-RXN0-580).

## Annotation

FUNCTION: Could be involved in sulfoquinovose import. {ECO:0000269|PubMed:24463506}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-580|reaction.ecocyc.TRANS-RXN0-580]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3876|gene.b3876]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32136`
- `KEGG:ecj:JW5852;eco:b3876;ecoc:C3026_20955;`
- `GeneID:948377;`
- `GO:GO:0005886; GO:0006814; GO:0008643; GO:0015293; GO:0055085; GO:0072348; GO:1901682`

## Notes

Putative sulfoquinovose importer

---
entity_id: "protein.P0DUM3"
entity_type: "protein"
name: "timP"
source_database: "UniProt"
source_id: "P0DUM3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P0DUM2}; Single-pass membrane protein {ECO:0000250|UniProtKB:P0DUM2}. Note=The signal sequence is not cleaved and anchors the protein in the cell inner membrane. {ECO:0000250|UniProtKB:P0DUM2}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "timP ECK4669 ryfA b4812"
---

# timP

`protein.P0DUM3`

## Static

- Type: `protein`
- Source: `UniProt:P0DUM3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P0DUM2}; Single-pass membrane protein {ECO:0000250|UniProtKB:P0DUM2}. Note=The signal sequence is not cleaved and anchors the protein in the cell inner membrane. {ECO:0000250|UniProtKB:P0DUM2}.

## Enriched Summary

FUNCTION: Putative toxic component of a potential type I toxin-antitoxin (TA) system. Neutralized by sRNA antitoxin TimR which binds to the 5' UTR of timP mRNA and inhibits translation. The antitoxin gene is encoded immediately upstream and transcribed divergently from the toxin gene; antitoxin RNA is less stable than timP mRNA. {ECO:0000250|UniProtKB:P0DUM2}. In Salmonella Typhimurium SL1344, the homologous protein TimP is a small toxic inner membrane protein within the G0-8879 whose translation is repressed by the small regulatory RNA TimR .

## Annotation

FUNCTION: Putative toxic component of a potential type I toxin-antitoxin (TA) system. Neutralized by sRNA antitoxin TimR which binds to the 5' UTR of timP mRNA and inhibits translation. The antitoxin gene is encoded immediately upstream and transcribed divergently from the toxin gene; antitoxin RNA is less stable than timP mRNA. {ECO:0000250|UniProtKB:P0DUM2}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4812|gene.b4812]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DUM3`
- `GO:GO:0005886`

## Notes

Putative toxic protein TimP

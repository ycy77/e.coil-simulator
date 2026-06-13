---
entity_id: "protein.P37009"
entity_type: "protein"
name: "fbpC"
source_database: "UniProt"
source_id: "P37009"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01706}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01706}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fbpC afuC yagC b0262 JW0254"
---

# fbpC

`protein.P37009`

## Static

- Type: `protein`
- Source: `UniProt:P37009`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01706}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01706}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FbpABC involved in Fe(3+) ions import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01706}. AfuC is the ATP-binding component of a predicted ABC superfamily ferric cation transporter . afuBC is a remnant operon in E. coli K-12; a complete afuABC gene cluster is present in a wide range of bacteria and encodes a binding protein-dependent transport system initially implicated in Fe3+ uptake (afu: Actinobacillus ferric uptake) , but now believed to transport sugar phosphates . E. coli K-12 does not contain an afuA ortholog.

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FbpABC involved in Fe(3+) ions import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01706}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0262|gene.b0262]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37009`
- `KEGG:ecj:JW0254;eco:b0262;ecoc:C3026_01265;`
- `GeneID:86977687;947676;`
- `GO:GO:0005524; GO:0005886; GO:0015408; GO:0015697; GO:0016887; GO:0022857; GO:0043190; GO:0055085`
- `EC:7.2.2.7`

## Notes

Fe(3+) ions import ATP-binding protein FbpC (EC 7.2.2.7)

---
entity_id: "protein.P25798"
entity_type: "protein"
name: "fliF"
source_database: "UniProt"
source_id: "P25798"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}. Bacterial flagellum basal body {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliF fla AII.1 fla BI b1938 JW1922"
---

# fliF

`protein.P25798`

## Static

- Type: `protein`
- Source: `UniProt:P25798`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}. Bacterial flagellum basal body {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: The M ring may be actively involved in energy transduction. fliF encodes a flagellar protein that polymerizes to form the MS (membrane/supramembrane) ring of the flagellar basal body; together with the C (cytoplasmic ring) consisting of FliG, FliM and FliN proteins, the MS-C ring complex functions as the reversible rotor of the flagella motor. FliF is widely studied in Salmonella typhimurium however the characterization is considered to apply to the homologous protein in E. coli.The two proteins are 85% identitical over their entire length . In Salmonella typhimurium, the MS ring is an inner membrane structure consisting of approximately 26 subunits of FliF; the MS ring is the base of the flagella structure and serves as the 'housing' for the protein export apparatus that is required for construction of the flagella; at its cytoplasmic face the MS ring interacts with the upper C ring protein FliG and this interface is an essential component of flagella motor function . An E...

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: The M ring may be actively involved in energy transduction.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1938|gene.b1938]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25798`
- `KEGG:ecj:JW1922;eco:b1938;ecoc:C3026_10980;`
- `GeneID:946448;`
- `GO:GO:0003774; GO:0005829; GO:0005886; GO:0009431; GO:0030288; GO:0071973`

## Notes

Flagellar M-ring protein

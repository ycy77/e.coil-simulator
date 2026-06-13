---
entity_id: "protein.P0AEG6"
entity_type: "protein"
name: "dsbC"
source_database: "UniProt"
source_id: "P0AEG6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8168498}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsbC xprA b2893 JW2861"
---

# dsbC

`protein.P0AEG6`

## Static

- Type: `protein`
- Source: `UniProt:P0AEG6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8168498}.

## Enriched Summary

FUNCTION: Acts as a disulfide isomerase, interacting with incorrectly folded proteins to correct non-native disulfide bonds. DsbG and DsbC are part of a periplasmic reducing system that controls the level of cysteine sulfenylation, and provides reducing equivalents to rescue oxidatively damaged secreted proteins. Acts by transferring its disulfide bond to other proteins and is reduced in the process. DsbC is reoxidized by DsbD. {ECO:0000269|PubMed:19965429}.

## Biological Role

Component of protein disulfide isomerase DsbC (complex.ecocyc.DSBC-CPLX).

## Annotation

FUNCTION: Acts as a disulfide isomerase, interacting with incorrectly folded proteins to correct non-native disulfide bonds. DsbG and DsbC are part of a periplasmic reducing system that controls the level of cysteine sulfenylation, and provides reducing equivalents to rescue oxidatively damaged secreted proteins. Acts by transferring its disulfide bond to other proteins and is reduced in the process. DsbC is reoxidized by DsbD. {ECO:0000269|PubMed:19965429}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DSBC-CPLX|complex.ecocyc.DSBC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2893|gene.b2893]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEG6`
- `KEGG:ecj:JW2861;eco:b2893;ecoc:C3026_15865;`
- `GeneID:75205270;947363;`
- `GO:GO:0003756; GO:0006457; GO:0015035; GO:0030288; GO:0042597; GO:0042803; GO:0046688`

## Notes

Thiol:disulfide interchange protein DsbC

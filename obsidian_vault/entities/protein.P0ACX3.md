---
entity_id: "protein.P0ACX3"
entity_type: "protein"
name: "ydhR"
source_database: "UniProt"
source_id: "P0ACX3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydhR b1667 JW1657"
---

# ydhR

`protein.P0ACX3`

## Static

- Type: `protein`
- Source: `UniProt:P0ACX3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May function as monooxygenase and play a role in the metabolism of aromatic compounds. {ECO:0000305}. A solution structure of YdhR has been determined; the protein belongs to the α/β barrel superfamily of proteins. Bioinformatic analysis suggests that it might function as a mono-oxygenase involved in the oxygenation of polyaromatic ring compounds . YdhR accumulates in response to exposure to uranium .

## Biological Role

Component of putative monooxygenase YdhR (complex.ecocyc.CPLX0-3923).

## Annotation

FUNCTION: May function as monooxygenase and play a role in the metabolism of aromatic compounds. {ECO:0000305}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3923|complex.ecocyc.CPLX0-3923]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1667|gene.b1667]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACX3`
- `KEGG:ecj:JW1657;eco:b1667;ecoc:C3026_09560;`
- `GeneID:93775822;946177;`
- `GO:GO:0005829; GO:0016491; GO:0042803`
- `EC:1.-.-.-`

## Notes

Putative monooxygenase YdhR (EC 1.-.-.-)

---
entity_id: "protein.P0AD83"
entity_type: "protein"
name: "pyrL"
source_database: "UniProt"
source_id: "P0AD83"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrL b4246 JW4205"
---

# pyrL

`protein.P0AD83`

## Static

- Type: `protein`
- Source: `UniProt:P0AD83`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

pyr operon leader peptide (pyrBI operon attenuator) The PyrL leader peptide is involved in the control by attenuation of the expression of the pyrLBI operon . Within the pyrL sequence there is a poly-T tract that leads to polymerase pausing when UTP is not available. This pausing lets the ribosome that is translating the leader peptide sequence catch up to the polymerase, preventing formation of a terminator that blocks transcription of the rest of the operon. When UTP is abundant, the polymerase moves through the pause site and outpaces the ribosome, leading to premature termination. . For more information on this means of regulation, look at the entry for TU00484. Although pyrimidine levels have little effect on translation of PyrL, translation of the leader peptide is required for proper regulation by attenuation. Mutations that block translation of PyrL disrupt attenuation at pyrLBI .

## Annotation

pyr operon leader peptide (pyrBI operon attenuator)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4246|gene.b4246]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD83`
- `KEGG:ecj:JW4205;eco:b4246;ecoc:C3026_22915;`
- `GeneID:86861354;93777578;948768;`
- `GO:GO:0006221; GO:0019856; GO:0031555`

## Notes

pyr operon leader peptide (pyrBI operon attenuator)

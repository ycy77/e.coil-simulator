---
entity_id: "protein.P0AE30"
entity_type: "protein"
name: "artM"
source_database: "UniProt"
source_id: "P0AE30"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "artM b0861 JW0845"
---

# artM

`protein.P0AE30`

## Static

- Type: `protein`
- Source: `UniProt:P0AE30`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:8801422}. Sequence analysis indicates that ArtM has similarity to the HisM membrane component of the histine/LAO (ltsine/arginine/ornithine) ABC transporter system in Salmonella typhimurium. ArtM is predicted to be a hydrophobic protein containing 3 transmembrane regions .

## Biological Role

Component of L-arginine ABC transporter (complex.ecocyc.ABC-4-CPLX), putative ABC transporter ArtPQMI (complex.ecocyc.CPLX0-8120).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:8801422}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-4-CPLX|complex.ecocyc.ABC-4-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8120|complex.ecocyc.CPLX0-8120]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0861|gene.b0861]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE30`
- `KEGG:ecj:JW0845;eco:b0861;ecoc:C3026_05365;`
- `GeneID:75170934;75202487;949066;`
- `GO:GO:0005886; GO:0006865; GO:0016020; GO:0022857; GO:0055052; GO:0097638`

## Notes

Arginine ABC transporter permease protein ArtM

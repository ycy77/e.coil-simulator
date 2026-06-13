---
entity_id: "protein.P0AFH6"
entity_type: "protein"
name: "oppC"
source_database: "UniProt"
source_id: "P0AFH6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "oppC b1245 JW1237"
---

# oppC

`protein.P0AFH6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFH6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides and of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Probably responsible for the translocation of the substrate across the membrane (Probable). Plays an important nutritional role and is involved in the recycling of cell wall peptides (PubMed:9495761). {ECO:0000269|PubMed:9495761, ECO:0000305}. OppC is one of two predicted integral membrane subunits of an ATP-dependent uptake system for oligopeptides (with preference for tripeptides - including murein tripeptides* - and tetrapeptides) . * uptake of murein tripeptide requires the periplasmic murein tripeptide binding protein, MppA

## Biological Role

Component of oligopeptide ABC transporter (complex.ecocyc.ABC-22-CPLX), murein tripeptide ABC transporter (complex.ecocyc.CPLX0-3970).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides and of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Probably responsible for the translocation of the substrate across the membrane (Probable). Plays an important nutritional role and is involved in the recycling of cell wall peptides (PubMed:9495761). {ECO:0000269|PubMed:9495761, ECO:0000305}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-22-CPLX|complex.ecocyc.ABC-22-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3970|complex.ecocyc.CPLX0-3970]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1245|gene.b1245]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFH6`
- `KEGG:ecj:JW1237;eco:b1245;ecoc:C3026_07315;`
- `GeneID:93775310;945810;`
- `GO:GO:0005886; GO:0015031; GO:0015640; GO:0015834; GO:0016020; GO:0055052; GO:0140205; GO:0140207`

## Notes

Oligopeptide transport system permease protein OppC

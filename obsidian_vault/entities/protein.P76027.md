---
entity_id: "protein.P76027"
entity_type: "protein"
name: "oppD"
source_database: "UniProt"
source_id: "P76027"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P04285}; Peripheral membrane protein {ECO:0000250|UniProtKB:P04285}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "oppD b1246 JW1238"
---

# oppD

`protein.P76027`

## Static

- Type: `protein`
- Source: `UniProt:P76027`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P04285}; Peripheral membrane protein {ECO:0000250|UniProtKB:P04285}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides and of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Probably responsible for energy coupling to the transport system (Probable). Plays an important nutritional role and is involved in the recycling of cell wall peptides (PubMed:9495761). {ECO:0000269|PubMed:9495761, ECO:0000305}. OppD is one of two predicted ATP-binding subunits of a high affinity uptake system for oligopeptides (with preference for tripeptides - including murein tripeptides* - and tetrapeptides); OppD contains signature motifs conserved in ATP-binding cassette (ABC) domains . * uptake of murein tripeptide requires the periplasmic murein tripeptide binding protein, MppA

## Biological Role

Component of oligopeptide ABC transporter (complex.ecocyc.ABC-22-CPLX), murein tripeptide ABC transporter (complex.ecocyc.CPLX0-3970).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides and of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Probably responsible for energy coupling to the transport system (Probable). Plays an important nutritional role and is involved in the recycling of cell wall peptides (PubMed:9495761). {ECO:0000269|PubMed:9495761, ECO:0000305}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-22-CPLX|complex.ecocyc.ABC-22-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3970|complex.ecocyc.CPLX0-3970]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1246|gene.b1246]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76027`
- `KEGG:ecj:JW1238;eco:b1246;ecoc:C3026_07320;`
- `GeneID:945802;`
- `GO:GO:0005524; GO:0015031; GO:0015421; GO:0015640; GO:0015834; GO:0016020; GO:0016887; GO:0055052; GO:0140205; GO:0140207`
- `EC:7.4.2.6`

## Notes

Oligopeptide transport ATP-binding protein OppD (EC 7.4.2.6)

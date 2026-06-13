---
entity_id: "protein.P0A9U1"
entity_type: "protein"
name: "ybhF"
source_database: "UniProt"
source_id: "P0A9U1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybhF b0794 JW5104"
---

# ybhF

`protein.P0A9U1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9U1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YbhFSR that could be involved in efflux of cefoperazone. Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:27112147}. ybhF encodes the ATP binding subunit of a putative ABC exporter. ybhF is part of the cecR-ybhGFSR operon which cntains genes encoding a putative ABC exporter (ybhFSR), a putative membrane fusion protein (ybhG) and a transcriptional regulator (cecR) . YbhFSR is implicated in the efflux of of the third generation cephalosporin - cefoperazone , tetracycline drugs and the cationic compounds ethidium bromide and Hoechst33342 . YbhFSR may also function as a Na+ / (Li+):proton antiporter . Transcription of cecR-ybhGFSR is negatively regulated by EG12406-MONOMER "CecR" . In the Transporter Classification Database YbhGFSR is annotated as a 4-component system within the ATP-binding Cassette (ABC) superfamily . ΔybhF mutants show reduced growth in the presence of cephalosporin . Recombinant, purified YbhF has ATPase activity .

## Biological Role

Component of ABC exporter YbhFSR (complex.ecocyc.ABC-57-CPLX).

## Annotation

FUNCTION: Part of the ABC transporter complex YbhFSR that could be involved in efflux of cefoperazone. Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:27112147}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-57-CPLX|complex.ecocyc.ABC-57-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0794|gene.b0794]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9U1`
- `KEGG:ecj:JW5104;eco:b0794;ecoc:C3026_05020;`
- `GeneID:945413;`
- `GO:GO:0005524; GO:0005886; GO:0006855; GO:0015562; GO:0015904; GO:0016887; GO:0035725; GO:0055052; GO:0090452; GO:1990961`

## Notes

Probable multidrug ABC transporter ATP-binding protein YbhF

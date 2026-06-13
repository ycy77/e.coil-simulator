---
entity_id: "protein.P0AFQ2"
entity_type: "protein"
name: "ybhS"
source_database: "UniProt"
source_id: "P0AFQ2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybhS b0793 JW0777"
---

# ybhS

`protein.P0AFQ2`

## Static

- Type: `protein`
- Source: `UniProt:P0AFQ2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YbhFSR that could be involved in efflux of cefoperazone. Probably involved in the translocation of the substrate across the membrane. {ECO:0000305|PubMed:27112147}. ybhS encodes one of two the integral membrane subunits of a putative ABC exporter. ybhS is part of the cecR-ybhGFSR operon which contains genes encoding a putative ABC exporter (ybhFSR), a putative membrane fusion protein (ybhG) and a transcriptional regulator (cecR) . YbhFSR is implicated in the efflux of of the third generation cephalosporin - cefoperazone , tetracycline drugs and the cationic compounds ethidium bromide and Hoechst33342 . YbhFSR may also function as a Na+ / (Li+):proton antiporter . Transcription of cecR-ybhGFSR is negatively regulated by EG12406-MONOMER "CecR" . In the Transporter Classification Database YbhGFSR is annotated as a 4-component system within the ATP-binding Cassette (ABC) superfamily .

## Biological Role

Component of ABC exporter YbhFSR (complex.ecocyc.ABC-57-CPLX).

## Annotation

FUNCTION: Part of the ABC transporter complex YbhFSR that could be involved in efflux of cefoperazone. Probably involved in the translocation of the substrate across the membrane. {ECO:0000305|PubMed:27112147}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-57-CPLX|complex.ecocyc.ABC-57-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0793|gene.b0793]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFQ2`
- `KEGG:ecj:JW0777;eco:b0793;ecoc:C3026_05015;`
- `GeneID:75170858;945411;`
- `GO:GO:0005886; GO:0006855; GO:0015562; GO:0015904; GO:0035725; GO:0055052; GO:0090452; GO:0140359; GO:1990961`

## Notes

Probable multidrug ABC transporter permease YbhS

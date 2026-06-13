---
entity_id: "protein.P0A9I5"
entity_type: "protein"
name: "napD"
source_database: "UniProt"
source_id: "P0A9I5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02200, ECO:0000269|PubMed:17901208}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "napD yojF b2207 JW2195"
---

# napD

`protein.P0A9I5`

## Static

- Type: `protein`
- Source: `UniProt:P0A9I5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02200, ECO:0000269|PubMed:17901208}.

## Enriched Summary

FUNCTION: Chaperone for NapA, the catalytic subunit of the periplasmic nitrate reductase. It binds directly and specifically to the twin-arginine signal peptide of NapA, preventing premature interaction with the Tat translocase and premature export (PubMed:17901208, PubMed:22329966). May have a role in the insertion of the NapA molybdenum cofactor (PubMed:24314029). {ECO:0000269|PubMed:17901208, ECO:0000269|PubMed:22329966, ECO:0000269|PubMed:24314029}. NapD is a dedicated chaperone for EG12067 NapA, the molybdoprotein subunit of the periplasmic nitrate reductase. It binds specifically to the twin-arginine signal peptide of NapA, preventing premature export. In the absence of NapD, NapA is unstable and degraded . NapD defines a second family of twin-arginine signal peptide binding proteins (see also the EG12195-MONOMER "TorD" chaperone). The solution structure of NapD has been solved, showing a ferredoxin-like fold . A NapD binding epitope is located towards the N-terminus of the NapA signal peptide and partially overlaps with the twin arginine motif . An NMR structure of the NapD-NapA signal peptide complex has been reported . NapA lacking its signal peptide does not form a NapD-NapA complex . NapD: "nitrate reductase in the periplasm" Review:

## Annotation

FUNCTION: Chaperone for NapA, the catalytic subunit of the periplasmic nitrate reductase. It binds directly and specifically to the twin-arginine signal peptide of NapA, preventing premature interaction with the Tat translocase and premature export (PubMed:17901208, PubMed:22329966). May have a role in the insertion of the NapA molybdenum cofactor (PubMed:24314029). {ECO:0000269|PubMed:17901208, ECO:0000269|PubMed:22329966, ECO:0000269|PubMed:24314029}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2207|gene.b2207]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9I5`
- `KEGG:ecj:JW2195;eco:b2207;ecoc:C3026_12330;`
- `GeneID:93774971;945187;`
- `GO:GO:0005048; GO:0005737; GO:0051224`

## Notes

Chaperone NapD (NapA signal peptide-binding chaperone NapD)

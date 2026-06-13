---
entity_id: "protein.P0AFY8"
entity_type: "protein"
name: "seqA"
source_database: "UniProt"
source_id: "P0AFY8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00908, ECO:0000269|PubMed:9660922}. Note=Localization is cell cycle-dependent. Localizes at midcell in newborn cells, then migrates in opposite directions toward cell quarter sites and remains tethered there until the cell divides."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "seqA b0687 JW0674"
---

# seqA

`protein.P0AFY8`

## Static

- Type: `protein`
- Source: `UniProt:P0AFY8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00908, ECO:0000269|PubMed:9660922}. Note=Localization is cell cycle-dependent. Localizes at midcell in newborn cells, then migrates in opposite directions toward cell quarter sites and remains tethered there until the cell divides.

## Enriched Summary

FUNCTION: Negative regulator of replication initiation, which contributes to regulation of DNA replication and ensures that replication initiation occurs exactly once per chromosome per cell cycle. Binds to pairs of hemimethylated GATC sequences in the oriC region, thus preventing assembly of replication proteins and re-initiation at newly replicated origins. Repression is relieved when the region becomes fully methylated. Can also bind to hemimethylated GATC sequences outside of oriC region. Binds, with less affinity, to fully methylated GATC sites and affects timing of replication. May play a role in chromosome organization and gene regulation. {ECO:0000255|HAMAP-Rule:MF_00908, ECO:0000269|PubMed:10931282, ECO:0000269|PubMed:11080170, ECO:0000269|PubMed:20689753, ECO:0000269|PubMed:7553853, ECO:0000269|PubMed:7891562, ECO:0000269|PubMed:8011018}. The SeqA protein is a negative modulator of the initiation of chromosome replication and is involved in sequestration of G0-10506 oriC, ensuring a single round of chromosome replication per cell cycle . SeqA binds hemimethylated GATC sequences in the wake of the advancing replication fork and inhibits open complex formation , delaying reinitiation at the hemimethylated oriC until it is fully methylated by EG10204-MONOMER Dam . Regulation of replication by SeqA is important for survival of replication fork damage...

## Annotation

FUNCTION: Negative regulator of replication initiation, which contributes to regulation of DNA replication and ensures that replication initiation occurs exactly once per chromosome per cell cycle. Binds to pairs of hemimethylated GATC sequences in the oriC region, thus preventing assembly of replication proteins and re-initiation at newly replicated origins. Repression is relieved when the region becomes fully methylated. Can also bind to hemimethylated GATC sequences outside of oriC region. Binds, with less affinity, to fully methylated GATC sites and affects timing of replication. May play a role in chromosome organization and gene regulation. {ECO:0000255|HAMAP-Rule:MF_00908, ECO:0000269|PubMed:10931282, ECO:0000269|PubMed:11080170, ECO:0000269|PubMed:20689753, ECO:0000269|PubMed:7553853, ECO:0000269|PubMed:7891562, ECO:0000269|PubMed:8011018}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0687|gene.b0687]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFY8`
- `KEGG:ecj:JW0674;eco:b0687;ecoc:C3026_03425;`
- `GeneID:93776797;945272;`
- `GO:GO:0003688; GO:0005829; GO:0006355; GO:0007062; GO:0009314; GO:0010385; GO:0032297; GO:0032991; GO:0042802; GO:0042803; GO:0044729; GO:1990097`

## Notes

Negative modulator of initiation of replication

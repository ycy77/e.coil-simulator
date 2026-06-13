---
entity_id: "protein.P42596"
entity_type: "protein"
name: "rlmG"
source_database: "UniProt"
source_id: "P42596"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmG ygjO b3084 JW5513"
---

# rlmG

`protein.P42596`

## Static

- Type: `protein`
- Source: `UniProt:P42596`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the guanine in position 1835 (m2G1835) of 23S rRNA. {ECO:0000269|PubMed:17010380}. RlmG is the methyltransferase responsible for methylation of 23S rRNA at the N2 position of the G1835 nucleotide. In vitro, recombinant RlmG is able to methylate naked 23S rRNA, but not 23S rRNA assembled into the 50S ribosomal subunit . Methylation of G1835 occurs during the early stages of ribosome assembly and enhances association of the ribosomal subunits . Phylogenomic analysis revealed sequence similarities and conserved architecture of the predicted active sites; at that time, RlmG was thought to be a candidate for the RsmD 16S rRNA methyltransferase . Crystal and solution structures of RlmG in complex with S-adenosylmethionine have been determined, allowing modeling of the catalytic mechanism of the enzyme . The N-terminal domain of RlmG was shown to be able to bind RNA independently . An rlmG null mutation leads to loss of methylation at G1835 of the 23S rRNA. A strain lacking rlmG shows reduced fitness in growth competition assays, especially under sub-optimal growth conditions . RlmG: "rRNA large subunit methyltransferase G" Review:

## Biological Role

Catalyzes RXN-11635 (reaction.ecocyc.RXN-11635).

## Annotation

FUNCTION: Specifically methylates the guanine in position 1835 (m2G1835) of 23S rRNA. {ECO:0000269|PubMed:17010380}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11635|reaction.ecocyc.RXN-11635]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3084|gene.b3084]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42596`
- `KEGG:ecj:JW5513;eco:b3084;ecoc:C3026_16845;`
- `GeneID:947589;`
- `GO:GO:0003676; GO:0005737; GO:0008990; GO:0052916; GO:0070475`
- `EC:2.1.1.174`

## Notes

Ribosomal RNA large subunit methyltransferase G (EC 2.1.1.174) (23S rRNA m2G1835 methyltransferase) (rRNA (guanine-N(2)-)-methyltransferase RlmG)

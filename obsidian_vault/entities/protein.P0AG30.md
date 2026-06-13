---
entity_id: "protein.P0AG30"
entity_type: "protein"
name: "rho"
source_database: "UniProt"
source_id: "P0AG30"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rho nitA psuA rnsC sbaA tsu b3783 JW3756"
---

# rho

`protein.P0AG30`

## Static

- Type: `protein`
- Source: `UniProt:P0AG30`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Facilitates transcription termination by a mechanism that involves Rho binding to the nascent RNA, activation of Rho's RNA-dependent ATPase activity, and release of the mRNA from the DNA template. RNA-dependent NTPase which utilizes all four ribonucleoside triphosphates as substrates. {ECO:0000269|PubMed:1716628, ECO:0000269|PubMed:2461932}.

## Biological Role

Component of transcription termination factor Rho (complex.ecocyc.CPLX0-2441).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Facilitates transcription termination by a mechanism that involves Rho binding to the nascent RNA, activation of Rho's RNA-dependent ATPase activity, and release of the mRNA from the DNA template. RNA-dependent NTPase which utilizes all four ribonucleoside triphosphates as substrates. {ECO:0000269|PubMed:1716628, ECO:0000269|PubMed:2461932}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2441|complex.ecocyc.CPLX0-2441]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3783|gene.b3783]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG30`
- `KEGG:ecj:JW3756;eco:b3783;ecoc:C3026_20480;`
- `GeneID:89518679;93778161;948297;`
- `GO:GO:0003723; GO:0004386; GO:0005524; GO:0005829; GO:0006353; GO:0008186; GO:0016020; GO:0016787; GO:0042802`
- `EC:3.6.4.-`

## Notes

Transcription termination factor Rho (EC 3.6.4.-) (ATP-dependent helicase Rho)

---
entity_id: "protein.P30859"
entity_type: "protein"
name: "artI"
source_database: "UniProt"
source_id: "P30859"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8801422}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "artI b0863 JW0847"
---

# artI

`protein.P30859`

## Static

- Type: `protein`
- Source: `UniProt:P30859`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8801422}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. {ECO:0000269|PubMed:8801422}. Sequence analysis indicates that ArtI has similarity to the histidine-binding periplasmic protein (HisJ) and lysine/arginine/ornithine binding periplasmic protein (ArgT), both from Salmonella typhimurium. ArtI is also similar to the ArtJ arginine binding periplasmic protein of E. coli. Purified ArtI does not bind any of 20 common amino acids nor does it bind labelled arginine nor putrescine . artI is part of the artMQIP operon which is regulated by the CPLX0-228 "ArgR" repressor in response to arginine . It is assumed to form an ABC transporter of unknown specificity with the ArtMQP membrane components . states that ArtI is the nearest match (followed by ArtJ and HisJ) to a low-affinity arginine-ornithine protein (AbpS) characterized and mapped to min 63 on the E. coli map; artI, artJ and hisJ are located at min 19.4, 19.4, and 52.3 respectively; no gene near min 63 matches the AbpS sequence published; it is possible that MG1655 does not contain abpS .

## Biological Role

Component of putative ABC transporter ArtPQMI (complex.ecocyc.CPLX0-8120).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. {ECO:0000269|PubMed:8801422}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8120|complex.ecocyc.CPLX0-8120]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0863|gene.b0863]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30859`
- `KEGG:ecj:JW0847;eco:b0863;ecoc:C3026_05375;`
- `GeneID:93776559;948988;`
- `GO:GO:0015276; GO:0016020; GO:0016597; GO:0030288; GO:0042597; GO:0055052; GO:0097638`

## Notes

Putative ABC transporter arginine-binding protein 2

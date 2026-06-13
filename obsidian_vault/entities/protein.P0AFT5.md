---
entity_id: "protein.P0AFT5"
entity_type: "protein"
name: "btsR"
source_database: "UniProt"
source_id: "P0AFT5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btsR yehT b2125 JW5352"
---

# btsR

`protein.P0AFT5`

## Static

- Type: `protein`
- Source: `UniProt:P0AFT5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Member of the two-component regulatory system BtsS/BtsR, which is part of a nutrient-sensing regulatory network composed of BtsS/BtsR, the low-affinity pyruvate signaling system YpdA/YpdB and their respective target proteins, BtsT and YhjX. Responds to depletion of nutrients, specifically serine, and the concomitant presence of extracellular pyruvate. BtsR regulates expression of btsT by binding to its promoter region. Activation of the BtsS/BtsR signaling cascade also suppresses YpdA/YpdB-mediated yhjX induction. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22685278, ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:28469239}. BtsR, formerly YehT, belongs to the LytTR response regulator (RR) of the two-component system that is involved in the stationary-phase control network . An exhaustive search of the Escherichia coli genome found a single motif for the BtsR transcriptional regulator, located upstream of the G7942 gene; therefore, it seems to be the only target regulated by the EG12007/EG12006 system . On the other hand, genome-wide BtsR binding sites were determined in vivo by chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium, and two binding-targets were found EG12624 and EG11179, but G7942 was not identified...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system BtsS/BtsR, which is part of a nutrient-sensing regulatory network composed of BtsS/BtsR, the low-affinity pyruvate signaling system YpdA/YpdB and their respective target proteins, BtsT and YhjX. Responds to depletion of nutrients, specifically serine, and the concomitant presence of extracellular pyruvate. BtsR regulates expression of btsT by binding to its promoter region. Activation of the BtsS/BtsR signaling cascade also suppresses YpdA/YpdB-mediated yhjX induction. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22685278, ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:28469239}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (15)

- `activates` --> [[gene.b4354|gene.b4354]] `RegulonDB` `C` - regulator=BtsR; target=btsT; function=+
- `represses` --> [[gene.b0113|gene.b0113]] `RegulonDB` `S` - regulator=BtsR; target=pdhR; function=-
- `represses` --> [[gene.b0114|gene.b0114]] `RegulonDB` `S` - regulator=BtsR; target=aceE; function=-
- `represses` --> [[gene.b0115|gene.b0115]] `RegulonDB` `S` - regulator=BtsR; target=aceF; function=-
- `represses` --> [[gene.b0116|gene.b0116]] `RegulonDB` `S` - regulator=BtsR; target=lpd; function=-
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=BtsR; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=BtsR; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=BtsR; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=BtsR; target=csgD; function=-
- `represses` --> [[gene.b1041|gene.b1041]] `RegulonDB` `S` - regulator=BtsR; target=csgB; function=-
- `represses` --> [[gene.b1042|gene.b1042]] `RegulonDB` `S` - regulator=BtsR; target=csgA; function=-
- `represses` --> [[gene.b1043|gene.b1043]] `RegulonDB` `S` - regulator=BtsR; target=csgC; function=-
- `represses` --> [[gene.b1823|gene.b1823]] `RegulonDB` `S` - regulator=BtsR; target=cspC; function=-
- `represses` --> [[gene.b1824|gene.b1824]] `RegulonDB` `S` - regulator=BtsR; target=yobF; function=-
- `represses` --> [[gene.b3236|gene.b3236]] `RegulonDB` `S` - regulator=BtsR; target=mdh; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2125|gene.b2125]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFT5`
- `KEGG:ecj:JW5352;eco:b2125;ecoc:C3026_11915;`
- `GeneID:86860293;93775070;949024;`
- `GO:GO:0000156; GO:0000160; GO:0000976; GO:0005829; GO:0006355; GO:0032993`

## Notes

Transcriptional regulatory protein BtsR

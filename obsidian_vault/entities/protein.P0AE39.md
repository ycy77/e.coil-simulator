---
entity_id: "protein.P0AE39"
entity_type: "protein"
name: "ypdB"
source_database: "UniProt"
source_id: "P0AE39"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ypdB b2381 JW2378"
---

# ypdB

`protein.P0AE39`

## Static

- Type: `protein`
- Source: `UniProt:P0AE39`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system YpdA/YpdB, which is part of a nutrient-sensing regulatory network composed of YpdA/YpdB, the high-affinity pyruvate signaling system BtsS/BtsR and their respective target proteins, YhjX and BtsT. YpdB regulates expression of yhjX by binding to its promoter region. Activation of the YpdA/YpdB signaling cascade also promotes BtsS/BtsR-mediated btsT expression. {ECO:0000269|PubMed:23222720, ECO:0000269|PubMed:24659770}. Based on genomic SELEX (gSELEX) screening, gel shift assay, and reporter assay, it was determined that PyrR is a dual regulator that acts as an activator for yhjX and yhcC and as a repressor for six other targets (pbpC, yfjD, gltBC, yghW, astCADBE, and xthA) . There is unique cross-talk between low-affinity PyrSR and high-affinity BtsSR, which control the same exometabolite (pyruvate) but different sets of targets for pyruvate uptake and reutilization . A mutant with deletion of both ypdA and ypdB does not show a significant phenotype when measured by phenotype microarray . While wild-type E. coli shows significantly decreased swarming motility upon exposure to volatile organic compounds (VOCs) produced by Bacillus subtilis, a ypdB null mutant showed no significant difference in swarming motility upon VOC treatment...

## Biological Role

Component of PyrR-pyruvate (complex.ecocyc.CPLX0-8309).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system YpdA/YpdB, which is part of a nutrient-sensing regulatory network composed of YpdA/YpdB, the high-affinity pyruvate signaling system BtsS/BtsR and their respective target proteins, YhjX and BtsT. YpdB regulates expression of yhjX by binding to its promoter region. Activation of the YpdA/YpdB signaling cascade also promotes BtsS/BtsR-mediated btsT expression. {ECO:0000269|PubMed:23222720, ECO:0000269|PubMed:24659770}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `activates` --> [[gene.b3547|gene.b3547]] `RegulonDB` `C` - regulator=PyrR; target=yhjX; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8309|complex.ecocyc.CPLX0-8309]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2381|gene.b2381]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE39`
- `KEGG:ecj:JW2378;eco:b2381;ecoc:C3026_13240;`
- `GeneID:93774747;947395;`
- `GO:GO:0000156; GO:0000976; GO:0005829; GO:0006355; GO:0032993; GO:0046677; GO:0048870; GO:1900192`

## Notes

Transcriptional regulatory protein YpdB

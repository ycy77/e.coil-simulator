---
entity_id: "protein.P0AFU4"
entity_type: "protein"
name: "glrR"
source_database: "UniProt"
source_id: "P0AFU4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glrR yfhA b2554 JW2538"
---

# glrR

`protein.P0AFU4`

## Static

- Type: `protein`
- Source: `UniProt:P0AFU4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system GlrR/GlrK that up-regulates transcription of the glmY sRNA when cells enter the stationary growth phase. Regulates glmY transcription by binding to three conserved sites in the purL-glmY intergenic region. {ECO:0000269|PubMed:19843219}. GlrR is the response regulator of the two-component GlrKR signal transduction system, and it has extensive homology to the NtrC family of activators . GlrR contains a σ54 interaction domain which binds to a DNA region located more than 100bp upstream of glmY. Transcription of a glmY-lacZ fusion from the σ54 promoter is abolished in a GlrR null strain. In an indirect way, GlrR negatively regulates genes involved in the synthesis of inorganic polyphosphate (polyP) . Inhibition of glrR expression by CRISPRi reduced cellular fitness under treatment with the antibiotic carbonyl cyanide 3-chlorophenylhydrazone (CCCP) . Purified GlrR can be phosphorylated in vitro by the cognate histidine kinase GlrK as well as by the non-cognate histidine kinases UhpB, RstB, and BaeS . GlrR: "glmY-regulating response regulator"

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system GlrR/GlrK that up-regulates transcription of the glmY sRNA when cells enter the stationary growth phase. Regulates glmY transcription by binding to three conserved sites in the purL-glmY intergenic region. {ECO:0000269|PubMed:19843219}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (6)

- `activates` --> [[gene.b2570|gene.b2570]] `RegulonDB` `S` - regulator=GlrR; target=rseC; function=+
- `activates` --> [[gene.b2571|gene.b2571]] `RegulonDB` `S` - regulator=GlrR; target=rseB; function=+
- `activates` --> [[gene.b2572|gene.b2572]] `RegulonDB` `S` - regulator=GlrR; target=rseA; function=+
- `activates` --> [[gene.b2573|gene.b2573]] `RegulonDB` `S` - regulator=GlrR; target=rpoE; function=+
- `activates` --> [[gene.b4441|gene.b4441]] `RegulonDB` `C` - regulator=GlrR; target=glmY; function=+
- `activates` --> [[gene.b4725|gene.b4725]] `RegulonDB` `S` - regulator=GlrR; target=rseD; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2554|gene.b2554]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFU4`
- `KEGG:ecj:JW2538;eco:b2554;ecoc:C3026_14140;`
- `GeneID:93774581;947042;`
- `GO:GO:0000156; GO:0000160; GO:0000987; GO:0001216; GO:0003700; GO:0005524; GO:0005737; GO:0006351; GO:0032993; GO:0045893`

## Notes

Transcriptional regulatory protein GlrR

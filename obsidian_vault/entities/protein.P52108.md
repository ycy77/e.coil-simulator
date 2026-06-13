---
entity_id: "protein.P52108"
entity_type: "protein"
name: "rstA"
source_database: "UniProt"
source_id: "P52108"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rstA urpT b1608 JW1600"
---

# rstA

`protein.P52108`

## Static

- Type: `protein`
- Source: `UniProt:P52108`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system RstB/RstA. RstA appears to control genes involved in different biological processes, such as acid tolerance, curli fimbria formation, and anaerobic respiration, among others . Some phenotypes caused by RstA have been identified by mutational analysis. For example, RstA is a suppressor of a lesion in yjeE, a gene essential for cell growth and whose cellular function is unknown . RstA overproduction causes drug resistance . RstA belongs to the two-component system RstA/RstB . Both genes, rstA, encoding the response regulator, and rstB, encoding the sensor kinase, are transcribed together in an operon that is induced under low-Mg2+ growth conditions through the PhoP/PhoQ two-component system . rstA expression is reduced in a phoP phoQ double mutant and in phoP phoQ pmrA and phoP phoQ pmrB triple mutants . The autophosphorylation of RstB appears to be stimulated by low pH . Subsequently, the phosphate group is transferred from RstB to RstA to activate it . A 14-bp DNA sequence that contains the TACA direct repeat has been identified as the RstA DNA-binding site and is called the RstA box . RstA interacts with TopA weakly in vivo and increases its activity related to relaxing the negative supercoiled plasmid carrying the rstA gene in the study . RstA is not an essential protein...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system RstB/RstA.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (5)

- `activates` --> [[gene.b1597|gene.b1597]] `RegulonDB` `S` - regulator=RstA; target=asr; function=+
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=RstA; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=RstA; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=RstA; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=RstA; target=csgD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1608|gene.b1608]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52108`
- `KEGG:ecj:JW1600;eco:b1608;ecoc:C3026_09255;`
- `GeneID:93775756;946199;`
- `GO:GO:0000156; GO:0000976; GO:0005829; GO:0006355; GO:0032993`

## Notes

Transcriptional regulatory protein RstA

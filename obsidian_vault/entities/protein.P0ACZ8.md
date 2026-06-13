---
entity_id: "protein.P0ACZ8"
entity_type: "protein"
name: "cusR"
source_database: "UniProt"
source_id: "P0ACZ8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cusR ylcA b0571 JW0560"
---

# cusR

`protein.P0ACZ8`

## Static

- Type: `protein`
- Source: `UniProt:P0ACZ8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system CusS/CusR involved in response to copper and silver. Activates the expression of cusCFBA, hiuH and plasmid pRJ1004 gene pcoE in response to increasing levels of copper or silver ions. Can also increase the basal-level expression of copper resistance gene operon pcoABCD. {ECO:0000269|PubMed:11004187, ECO:0000269|PubMed:11283292, ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}. CusR, "Cu-sensing regulator", regulates genes related to the copper and silver efflux systems under anaerobic growth and under extreme copper stress in aerobic growth . CusR belongs to the two-component system CusS/CusR, which responds to increases in the copper concentration. Both cusR, encoding the response regulator, and cusS, encoding the sensor kinase, are organized in an operon that is located next to and in the opposite direction to an operon whose expression is activated by CusR . CusR is able to bind to the cusRS-cusCFBA intergenic region in both its phosphorylated and unphosphorylated forms, but in its unphosphorylated form it binds to many other targets in the genome . The sensor proteins YedW, UhpB, and YedV, which also belong to two-component systems, can activate CusR via signal cross talk...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system CusS/CusR involved in response to copper and silver. Activates the expression of cusCFBA, hiuH and plasmid pRJ1004 gene pcoE in response to increasing levels of copper or silver ions. Can also increase the basal-level expression of copper resistance gene operon pcoABCD. {ECO:0000269|PubMed:11004187, ECO:0000269|PubMed:11283292, ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (9)

- `activates` --> [[gene.b0570|gene.b0570]] `RegulonDB` `C` - regulator=CusR; target=cusS; function=+
- `activates` --> [[gene.b0571|gene.b0571]] `RegulonDB` `C` - regulator=CusR; target=cusR; function=+
- `activates` --> [[gene.b0572|gene.b0572]] `RegulonDB` `C` - regulator=CusR; target=cusC; function=+
- `activates` --> [[gene.b0573|gene.b0573]] `RegulonDB` `C` - regulator=CusR; target=cusF; function=+
- `activates` --> [[gene.b0574|gene.b0574]] `RegulonDB` `C` - regulator=CusR; target=cusB; function=+
- `activates` --> [[gene.b0575|gene.b0575]] `RegulonDB` `C` - regulator=CusR; target=cusA; function=+
- `activates` --> [[gene.b1970|gene.b1970]] `RegulonDB` `S` - regulator=CusR; target=hiuH; function=+
- `activates` --> [[gene.b1971|gene.b1971]] `RegulonDB` `S` - regulator=CusR; target=msrP; function=+
- `activates` --> [[gene.b1972|gene.b1972]] `RegulonDB` `S` - regulator=CusR; target=msrQ; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b0571|gene.b0571]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACZ8`
- `KEGG:ecj:JW0560;eco:b0571;ecoc:C3026_02835;`
- `GeneID:93776917;945003;`
- `GO:GO:0000156; GO:0000976; GO:0003677; GO:0005829; GO:0006355; GO:0032993; GO:0042802; GO:0046688`

## Notes

Transcriptional regulatory protein CusR

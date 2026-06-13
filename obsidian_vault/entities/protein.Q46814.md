---
entity_id: "protein.Q46814"
entity_type: "protein"
name: "xdhD"
source_database: "UniProt"
source_id: "Q46814"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xdhD ygfN b2881 JW2849"
---

# xdhD

`protein.Q46814`

## Static

- Type: `protein`
- Source: `UniProt:Q46814`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably has no xanthine dehydrogenase activity; however deletion results in increased adenine sensitivity, suggesting that this protein contributes to the conversion of adenine to guanine nucleotides during purine salvage. {ECO:0000269|PubMed:10986234}. XdhD has similarity to molybdenum cofactor-containing xanthine oxidases, including Drosophila melanogaster xanthine dehydrogenase and Desulfovibrio gigas aldehyde oxidoreductase and is predicted to catalyze oxidation of xanthine (with electron transfer to O2, rather than dehydrogenase activity with electron transfer to NAD or NADP) . An xdhD mutant exhibits sensitivity to adenine, which is indicative of a defect in purine salvage, but it does not exhibit a defect in an indirect assay of xanthine dehydrogenase activity . Deletion of xdhD does not confer N-hydroxylaminopurine sensitivity . An xdhD null mutant is able to reduce selenate to elemental red selenium .

## Biological Role

Component of predicted xanthine dehydrogenase (complex.ecocyc.CPLX0-1841).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

FUNCTION: Probably has no xanthine dehydrogenase activity; however deletion results in increased adenine sensitivity, suggesting that this protein contributes to the conversion of adenine to guanine nucleotides during purine salvage. {ECO:0000269|PubMed:10986234}.

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1841|complex.ecocyc.CPLX0-1841]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2881|gene.b2881]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46814`
- `KEGG:ecj:JW2849;eco:b2881;ecoc:C3026_15800;`
- `GeneID:75172981;949079;`
- `GO:GO:0005506; GO:0006144; GO:0006166; GO:0016491; GO:0051537`
- `EC:1.-.-.-`

## Notes

Probable hypoxanthine oxidase XdhD (EC 1.-.-.-)

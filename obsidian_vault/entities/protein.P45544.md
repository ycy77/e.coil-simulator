---
entity_id: "protein.P45544"
entity_type: "protein"
name: "frlR"
source_database: "UniProt"
source_id: "P45544"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frlR yhfR b3375 JW5698"
---

# frlR

`protein.P45544`

## Static

- Type: `protein`
- Source: `UniProt:P45544`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May regulate the transcription of the frlABCDR operon, involved in the utilization of fructoselysine and psicoselysine. {ECO:0000305|PubMed:12147680}.

## Biological Role

Component of DNA-binding transcriptional repressor FrlR (complex.ecocyc.CPLX0-8576).

## Annotation

FUNCTION: May regulate the transcription of the frlABCDR operon, involved in the utilization of fructoselysine and psicoselysine. {ECO:0000305|PubMed:12147680}.

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8576|complex.ecocyc.CPLX0-8576]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b3370|gene.b3370]] `RegulonDB` `C` - regulator=FrlR; target=frlA; function=-
- `represses` --> [[gene.b3371|gene.b3371]] `RegulonDB` `C` - regulator=FrlR; target=frlB; function=-
- `represses` --> [[gene.b3374|gene.b3374]] `RegulonDB` `C` - regulator=FrlR; target=frlD; function=-
- `represses` --> [[gene.b3375|gene.b3375]] `RegulonDB` `C` - regulator=FrlR; target=frlR; function=-
- `represses` --> [[gene.b4474|gene.b4474]] `RegulonDB` `C` - regulator=FrlR; target=frlC; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3375|gene.b3375]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45544`
- `KEGG:ecj:JW5698;eco:b3375;ecoc:C3026_18320;`
- `GeneID:93778623;947885;`
- `GO:GO:0003677; GO:0003700; GO:0045892`

## Notes

Probable fructoselysine utilization operon transcriptional repressor (HTH-type transcriptional regulator FrlR)

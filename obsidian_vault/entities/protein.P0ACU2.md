---
entity_id: "protein.P0ACU2"
entity_type: "protein"
name: "rutR"
source_database: "UniProt"
source_id: "P0ACU2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rutR ycdC b1013 JW0998"
---

# rutR

`protein.P0ACU2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACU2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Master transcription regulator which represses the degradation of pyrimidines (rutABCDEFG) and purines (gcl operon) for maintenance of metabolic balance between pyrimidines and purines. It also regulates the synthesis of pyrimidine nucleotides and arginine from glutamine (carAB) and the supply of glutamate (gadABWX). {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:17919280}.

## Biological Role

Component of DNA-binding transcriptional dual regulator RutR (complex.ecocyc.CPLX0-11745), RutR-uracil (complex.ecocyc.CPLX0-7651), RutR-thymine (complex.ecocyc.CPLX0-8058).

## Annotation

FUNCTION: Master transcription regulator which represses the degradation of pyrimidines (rutABCDEFG) and purines (gcl operon) for maintenance of metabolic balance between pyrimidines and purines. It also regulates the synthesis of pyrimidine nucleotides and arginine from glutamine (carAB) and the supply of glutamate (gadABWX). {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:17919280}.

## Outgoing Edges (19)

- `activates` --> [[gene.b0032|gene.b0032]] `RegulonDB` `C` - regulator=RutR; target=carA; function=+
- `activates` --> [[gene.b0033|gene.b0033]] `RegulonDB` `C` - regulator=RutR; target=carB; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-11745|complex.ecocyc.CPLX0-11745]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7651|complex.ecocyc.CPLX0-7651]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8058|complex.ecocyc.CPLX0-8058]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0592|gene.b0592]] `RegulonDB` `S` - regulator=RutR; target=fepB; function=-
- `represses` --> [[gene.b1006|gene.b1006]] `RegulonDB` `C` - regulator=RutR; target=rutG; function=-
- `represses` --> [[gene.b1007|gene.b1007]] `RegulonDB` `C` - regulator=RutR; target=rutF; function=-
- `represses` --> [[gene.b1008|gene.b1008]] `RegulonDB` `C` - regulator=RutR; target=rutE; function=-
- `represses` --> [[gene.b1009|gene.b1009]] `RegulonDB` `C` - regulator=RutR; target=rutD; function=-
- `represses` --> [[gene.b1010|gene.b1010]] `RegulonDB` `C` - regulator=RutR; target=rutC; function=-
- `represses` --> [[gene.b1011|gene.b1011]] `RegulonDB` `C` - regulator=RutR; target=rutB; function=-
- `represses` --> [[gene.b1012|gene.b1012]] `RegulonDB` `C` - regulator=RutR; target=rutA; function=-
- `represses` --> [[gene.b1013|gene.b1013]] `RegulonDB` `C` - regulator=RutR; target=rutR; function=-
- `represses` --> [[gene.b1649|gene.b1649]] `RegulonDB` `S` - regulator=RutR; target=nemR; function=-
- `represses` --> [[gene.b1650|gene.b1650]] `RegulonDB` `S` - regulator=RutR; target=nemA; function=-
- `represses` --> [[gene.b1651|gene.b1651]] `RegulonDB` `S` - regulator=RutR; target=gloA; function=-
- `represses` --> [[gene.b3515|gene.b3515]] `RegulonDB` `S` - regulator=RutR; target=gadW; function=-
- `represses` --> [[gene.b3516|gene.b3516]] `RegulonDB` `S` - regulator=RutR; target=gadX; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1013|gene.b1013]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACU2`
- `KEGG:ecj:JW0998;eco:b1013;ecoc:C3026_06160;`
- `GeneID:75171089;945075;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0045892; GO:0045893`

## Notes

HTH-type transcriptional regulator RutR (Rut operon repressor)

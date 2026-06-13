---
entity_id: "protein.P21514"
entity_type: "protein"
name: "pdeL"
source_database: "UniProt"
source_id: "P21514"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeL yahA b0315 JW0307"
---

# pdeL

`protein.P21514`

## Static

- Type: `protein`
- Source: `UniProt:P21514`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts both as an enzyme and as a c-di-GMP sensor to couple transcriptional activity to the c-di-GMP status of the cell (PubMed:26553851). Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (PubMed:15995192, PubMed:24451384, PubMed:26553851). Also acts as a transcription factor to control its own expression (PubMed:26553851). {ECO:0000269|PubMed:15995192, ECO:0000269|PubMed:24451384, ECO:0000269|PubMed:26553851}.

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991). Component of DNA-binding transcriptional dual regulator/c-di-GMP phosphodiesterase PdeL (complex.ecocyc.CPLX0-8109).

## Annotation

FUNCTION: Acts both as an enzyme and as a c-di-GMP sensor to couple transcriptional activity to the c-di-GMP status of the cell (PubMed:26553851). Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (PubMed:15995192, PubMed:24451384, PubMed:26553851). Also acts as a transcription factor to control its own expression (PubMed:26553851). {ECO:0000269|PubMed:15995192, ECO:0000269|PubMed:24451384, ECO:0000269|PubMed:26553851}.

## Outgoing Edges (11)

- `activates` --> [[gene.b0315|gene.b0315]] `RegulonDB` `C` - regulator=PdeL; target=pdeL; function=+
- `activates` --> [[gene.b4466|gene.b4466]] `RegulonDB` `S` - regulator=PdeL; target=yghJ; function=+
- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52
- `is_component_of` --> [[complex.ecocyc.CPLX0-8109|complex.ecocyc.CPLX0-8109]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b1938|gene.b1938]] `RegulonDB` `S` - regulator=PdeL; target=fliF; function=-
- `represses` --> [[gene.b1939|gene.b1939]] `RegulonDB` `S` - regulator=PdeL; target=fliG; function=-
- `represses` --> [[gene.b1940|gene.b1940]] `RegulonDB` `S` - regulator=PdeL; target=fliH; function=-
- `represses` --> [[gene.b1941|gene.b1941]] `RegulonDB` `S` - regulator=PdeL; target=fliI; function=-
- `represses` --> [[gene.b1942|gene.b1942]] `RegulonDB` `S` - regulator=PdeL; target=fliJ; function=-
- `represses` --> [[gene.b1943|gene.b1943]] `RegulonDB` `S` - regulator=PdeL; target=fliK; function=-
- `represses` --> [[gene.b3784|gene.b3784]] `RegulonDB` `S` - regulator=PdeL; target=wecA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0315|gene.b0315]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21514`
- `KEGG:ecj:JW0307;eco:b0315;ecoc:C3026_01545;ecoc:C3026_24715;`
- `GeneID:947459;`
- `GO:GO:0000976; GO:0005886; GO:0042803; GO:0045893; GO:0046872; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Cyclic di-GMP phosphodiesterase PdeL (EC 3.1.4.52)

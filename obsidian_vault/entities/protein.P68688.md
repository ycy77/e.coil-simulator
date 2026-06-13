---
entity_id: "protein.P68688"
entity_type: "protein"
name: "grxA"
source_database: "UniProt"
source_id: "P68688"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "grxA grx b0849 JW0833"
---

# grxA

`protein.P68688`

## Static

- Type: `protein`
- Source: `UniProt:P68688`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The disulfide bond functions as an electron carrier in the glutathione-dependent synthesis of deoxyribonucleotides by the enzyme ribonucleotide reductase. In addition, it is also involved in reducing some disulfide bonds in a coupled system with glutathione reductase. The oxidized form of Grx1 appears to be in a weak monomer-dimer equilibrium . For an extensive summary on Grx1, please see RED-GLUTAREDOXIN. Reviews: General InformationGlutaredoxins are ubiquitous proteins that catalyze the reduction of disulfides. Glutaredoxins are similar to thioredoxins; both are usually small (9-12 kDa), and both are capable of catalyzing thiol-disulfide exchange reactions. Representatives of at least one of these two protein families have been found in all organisms studied, indicating that proteins of this type are essential for cellular functions. A main difference between the two is the mechanism for their reduction. Glutaredoxins are generally reduced by the compound GLUTATHIONE (GSH), while thioredoxins are reduced by the specific flavoenzyme THIOREDOXIN-REDUCT-NADPH-CPLX. While thioredoxins are found to be general reductants of protein disulfides, glutaredoxins are better at reducing mixed disulfides between proteins (or low molecular weight thiol-containing compounds) and GSH...

## Biological Role

Catalyzes PRODISULFREDUCT-RXN (reaction.ecocyc.PRODISULFREDUCT-RXN), RXN-19629 (reaction.ecocyc.RXN-19629).

## Annotation

FUNCTION: The disulfide bond functions as an electron carrier in the glutathione-dependent synthesis of deoxyribonucleotides by the enzyme ribonucleotide reductase. In addition, it is also involved in reducing some disulfide bonds in a coupled system with glutathione reductase.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PRODISULFREDUCT-RXN|reaction.ecocyc.PRODISULFREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19629|reaction.ecocyc.RXN-19629]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0849|gene.b0849]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68688`
- `KEGG:ecj:JW0833;eco:b0849;ecoc:C3026_05300;`
- `GeneID:93776573;945479;`
- `GO:GO:0000166; GO:0005737; GO:0009055; GO:0009263; GO:0010134; GO:0015035; GO:0015036; GO:0015038; GO:0019153; GO:0019345; GO:0034599; GO:0045454`

## Notes

Glutaredoxin 1 (Grx1)

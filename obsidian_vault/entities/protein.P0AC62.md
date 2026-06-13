---
entity_id: "protein.P0AC62"
entity_type: "protein"
name: "grxC"
source_database: "UniProt"
source_id: "P0AC62"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "grxC yibM b3610 JW3585"
---

# grxC

`protein.P0AC62`

## Static

- Type: `protein`
- Source: `UniProt:P0AC62`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The disulfide bond functions as an electron carrier in the glutathione-dependent synthesis of deoxyribonucleotides by the enzyme ribonucleotide reductase. In addition, it is also involved in reducing some disulfide bonds in a coupled system with glutathione reductase. General InformationGlutaredoxins are ubiquitous proteins that catalyze the reduction of disulfides. Glutaredoxins are similar to thioredoxins; both are usually small (9-12 kDa), and both are capable of catalyzing thiol-disulfide exchange reactions. Representatives of at least one of these two protein families have been found in all organisms studied, indicating that proteins of this type are essential for cellular functions. A main difference between the two is the mechanism for their reduction. Glutaredoxins are generally reduced by the compound GLUTATHIONE (GSH), while thioredoxins are reduced by the specific flavoenzyme THIOREDOXIN-REDUCT-NADPH-CPLX. While thioredoxins are found to be general reductants of protein disulfides, glutaredoxins are better at reducing mixed disulfides between proteins (or low molecular weight thiol-containing compounds) and GSH. The substrate specificities of glutaredoxins and thioredoxins appear to depend on geometric and electrostatic complementarity and long-distance electrostatic interactions between the redoxin and its target...

## Biological Role

Catalyzes PRODISULFREDUCT-RXN (reaction.ecocyc.PRODISULFREDUCT-RXN).

## Annotation

FUNCTION: The disulfide bond functions as an electron carrier in the glutathione-dependent synthesis of deoxyribonucleotides by the enzyme ribonucleotide reductase. In addition, it is also involved in reducing some disulfide bonds in a coupled system with glutathione reductase.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PRODISULFREDUCT-RXN|reaction.ecocyc.PRODISULFREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3610|gene.b3610]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC62`
- `KEGG:ecj:JW3585;eco:b3610;ecoc:C3026_19575;`
- `GeneID:86861729;93778324;948132;`
- `GO:GO:0005737; GO:0005829; GO:0009263; GO:0015035; GO:0015038; GO:0034599; GO:0043295; GO:0045454`

## Notes

Glutaredoxin 3 (Grx3)

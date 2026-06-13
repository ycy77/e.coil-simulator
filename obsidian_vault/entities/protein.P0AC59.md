---
entity_id: "protein.P0AC59"
entity_type: "protein"
name: "grxB"
source_database: "UniProt"
source_id: "P0AC59"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "grxB b1064 JW1051"
---

# grxB

`protein.P0AC59`

## Static

- Type: `protein`
- Source: `UniProt:P0AC59`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in reducing some disulfide bonds in a coupled system with glutathione reductase. Does not act as hydrogen donor for ribonucleotide reductase. Glutaredoxins are ubiquitous proteins that catalyze the reduction of disulfides via reduced glutathione (GSH). Escherichia coli has three glutaredoxins (Grx1, Grx2, and Grx3) containing the classic dithiol active site CPYC, and a fourth one which contains a monothiol (CGFS) potential active site . The glutaredoxins do not act as enzymes, but rather as a cofactor, enabling intracellular redox reactions through a disulfide/dithiol enzymatic mechanism involving the active site cysteines. There is almost no similarity between the amino acid sequence of Grx2 (an approximately 27 kDa protein) and Grx1 or Grx3 (both 9-kDa proteins), with the exception of the active site which is identical in all three glutaredoxins. In contrast to glutaredoxin 1 and 3, Grx 2 is not a hydrogen donor for ribonucleotide reductase. On the other hand, Grx2 is the primary hydrogen donor to ArsC-catalyzed arsenate reduction (RXN-982) . It is also the most abundant glutaredoxin in the cell, with an intracellular concentration of 5 µM, compared with 0.2 µM and 2.4 µM for Grx1 and 3, respectively . General InformationGlutaredoxins are ubiquitous proteins that catalyze the reduction of disulfides...

## Biological Role

Catalyzes PRODISULFREDUCT-RXN (reaction.ecocyc.PRODISULFREDUCT-RXN).

## Annotation

FUNCTION: Involved in reducing some disulfide bonds in a coupled system with glutathione reductase. Does not act as hydrogen donor for ribonucleotide reductase.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PRODISULFREDUCT-RXN|reaction.ecocyc.PRODISULFREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1064|gene.b1064]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC59`
- `KEGG:ecj:JW1051;eco:b1064;`
- `GeneID:93776343;946926;`
- `GO:GO:0005829; GO:0015038`

## Notes

Glutaredoxin 2 (Grx2)

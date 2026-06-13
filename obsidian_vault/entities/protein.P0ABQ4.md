---
entity_id: "protein.P0ABQ4"
entity_type: "protein"
name: "folA"
source_database: "UniProt"
source_id: "P0ABQ4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folA tmrA b0048 JW0047"
---

# folA

`protein.P0ABQ4`

## Static

- Type: `protein`
- Source: `UniProt:P0ABQ4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Key enzyme in folate metabolism. Catalyzes an essential reaction for de novo glycine and purine synthesis, and for DNA precursor synthesis. The enzyme encoded by folA, dihydrofolate reductase (DHFR) provides the major dihydrofolate reductase activity in the tetrahydrofolate biosynthetic pathway. It catalyzes the reduction of dihydrofolate to tetrahydrofolate via hydride transfer from NADPH to C6 of the pteridine ring. Tetrahydrofolate is an important intermediate in the biosynthesis of proteins and nucleic acids (see pathway PWY-6614). Because dihydrofolate reductase is essential for cell division and growth, it is a target for drug development. It is susceptible to inhibition by several agents which have antitumor, antibacterial and antimalarial properties including the well known drugs methotrexate and trimethoprim . The folA gene has been characterized and the enzyme has been purified and characterized . E. coli dihydrofolate reductase has been used as a model enzyme for research on the relationship between enzyme structure, dynamics and function. Early kinetic studies of wild-type and mutant enzymes showed that the apoenzyme exists in at least two different conformational states, one of which is not catalytically competent . Subsequent kinetic studies of site-directed mutant enzymes contributed to a mechanistic model of catalysis...

## Biological Role

Catalyzes DIHYDROFOLATEREDUCT-RXN (reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

FUNCTION: Key enzyme in folate metabolism. Catalyzes an essential reaction for de novo glycine and purine synthesis, and for DNA precursor synthesis.

## Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0048|gene.b0048]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABQ4`
- `KEGG:ecj:JW0047;eco:b0048;ecoc:C3026_00250;`
- `GeneID:86862560;93777387;944790;`
- `GO:GO:0004146; GO:0005542; GO:0005829; GO:0006730; GO:0009257; GO:0009410; GO:0031427; GO:0046452; GO:0046654; GO:0046655; GO:0046656; GO:0046677; GO:0050661; GO:0051870; GO:0051871; GO:0070401; GO:0070402`
- `EC:1.5.1.3`

## Notes

Dihydrofolate reductase (EC 1.5.1.3)

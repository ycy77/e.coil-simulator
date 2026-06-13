---
entity_id: "protein.P32154"
entity_type: "protein"
name: "frvB"
source_database: "UniProt"
source_id: "P32154"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000305|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frvB yiiJ b3899 JW5562"
---

# frvB

`protein.P32154`

## Static

- Type: `protein`
- Source: `UniProt:P32154`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000305|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrvAB PTS system is involved in fructose transport. {ECO:0000305|PubMed:8019415}. Sequence analysis indicates that the frvB protein consists of a hydrophilic N-terminal domain linked to a hydrophobic C-terminal domain. The predicted protein is most similar to proteins of the fructose PTS. frvB contains a conserved cysteine residue (Cys13)

## Biological Role

Component of putative PTS enzyme II FrvAB (complex.ecocyc.CPLX-159).

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrvAB PTS system is involved in fructose transport. {ECO:0000305|PubMed:8019415}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-159|complex.ecocyc.CPLX-159]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3899|gene.b3899]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32154`
- `KEGG:ecj:JW5562;eco:b3899;ecoc:C3026_21080;`
- `GeneID:75174139;948390;`
- `GO:GO:0005351; GO:0005886; GO:0009401; GO:0016301; GO:0022877; GO:0090563; GO:1902495; GO:1990539`
- `EC:2.7.1.202`

## Notes

Fructose-like PTS system EIIBC component [Includes: PTS system fructose-like EIIB component (EC 2.7.1.202) (Fructose-like phosphotransferase enzyme IIB component); PTS system fructose-like EIIC component (Fructose-like permease IIC component)]

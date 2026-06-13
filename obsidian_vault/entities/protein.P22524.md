---
entity_id: "protein.P22524"
entity_type: "protein"
name: "mukE"
source_database: "UniProt"
source_id: "P22524"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid. Note=Restricted to the nucleoid region."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mukE kicA ycbA b0923 JW0906"
---

# mukE

`protein.P22524`

## Static

- Type: `protein`
- Source: `UniProt:P22524`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid. Note=Restricted to the nucleoid region.

## Enriched Summary

FUNCTION: Involved in chromosome condensation, segregation and cell cycle progression. May participate in facilitating chromosome segregation by condensation DNA from both sides of a centrally located replisome during cell division. Probably acts via its interaction with MukB and MukF. {ECO:0000269|PubMed:8602138}. MukE plays a role in chromosome partitioning during cell division . The effect of MukE on chromosome partitioning may be due to a role in DNA topology or condensation . MukF (the kleisin) and MukE (the kleisin-interacting winged-helix tandem element, "KITE") are proposed to be a toxin-antitoxin pair, respectively . Published reports disagree about whether or not the MukE protein is essential for viability. A mukE mutant is reported to exhibit heat sensitivity and formation of anucleate products of cell division . A mukE mutant also exhibits increased sensitivity to novobiocin, compared to wild type . A mukE mutant exhibits a defect in wild-type localization of MukB to nucleoid-associated foci . A mukF mutation suppresses the observed inviability of a mukE mutant . The heat sensitivity and division defects of a mukE mutant are suppressed by a topA10 or topA66 mutation, and this suppression is DNA gyrase dependent . The heat sensitivity of a mukE mutant is partly suppressed by a dam or seqA mutation, whereas the novobiocin and anucleate cell phenotypes are not...

## Biological Role

Component of bacterial condensin MukBEF (complex.ecocyc.CPLX0-2561), MukEF complex (complex.ecocyc.CPLX0-7697).

## Annotation

FUNCTION: Involved in chromosome condensation, segregation and cell cycle progression. May participate in facilitating chromosome segregation by condensation DNA from both sides of a centrally located replisome during cell division. Probably acts via its interaction with MukB and MukF. {ECO:0000269|PubMed:8602138}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2561|complex.ecocyc.CPLX0-2561]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.CPLX0-7697|complex.ecocyc.CPLX0-7697]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0923|gene.b0923]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22524`
- `KEGG:ecj:JW0906;eco:b0923;ecoc:C3026_05675;`
- `GeneID:75170997;75205325;945550;`
- `GO:GO:0000796; GO:0005737; GO:0006260; GO:0007059; GO:0009295; GO:0030261; GO:0051301`

## Notes

Chromosome partition protein MukE (Protein KicA)

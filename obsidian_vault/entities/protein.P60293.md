---
entity_id: "protein.P60293"
entity_type: "protein"
name: "mukF"
source_database: "UniProt"
source_id: "P60293"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid. Note=Restricted to the nucleoid region."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mukF kicB b0922 JW0905"
---

# mukF

`protein.P60293`

## Static

- Type: `protein`
- Source: `UniProt:P60293`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid. Note=Restricted to the nucleoid region.

## Enriched Summary

FUNCTION: Involved in chromosome condensation, segregation and cell cycle progression. May participate in facilitating chromosome segregation by condensation DNA from both sides of a centrally located replisome during cell division. Not required for mini-F plasmid partitioning. Probably acts via its interaction with MukB and MukE. Overexpression results in anucleate cells. It has a calcium binding activity. {ECO:0000269|PubMed:8602138}. MukF plays a role in chromosome partitioning during cell division, DNA topology and chromosome condensation as part of the CPLX0-2561. MukF is the kleisin subunit (from the Greek word kleisimo for "closure" ) within MukBEF, consistent with the N- and C-termini sharing homology to kleisin domains ; unlike other kleisins, MukF is present as a dimer . MukF and MukE initially were proposed to be a toxin-antitoxin pair, respectively . MukF has a leucine zipper region and an acidic region; both regions are functionally important . MukF bound to MukE is required for binding to MukB, whereas MukF can bind to MukB without being bound to MukE . MukBEF complex which is stimulated by Ca2+ or Mg2+; MukF was found to bind to Ca2+ . A crystal structure of a 33 kDa N-terminal fragment of MukF (nucleotides 1-287) was purified to 2.9Å resolution in presence of Ca2+, however no divalent metals were observed within the crystal structure...

## Biological Role

Component of bacterial condensin MukBEF (complex.ecocyc.CPLX0-2561), MukEF complex (complex.ecocyc.CPLX0-7697), MukF dimer (complex.ecocyc.CPLX0-7698).

## Annotation

FUNCTION: Involved in chromosome condensation, segregation and cell cycle progression. May participate in facilitating chromosome segregation by condensation DNA from both sides of a centrally located replisome during cell division. Not required for mini-F plasmid partitioning. Probably acts via its interaction with MukB and MukE. Overexpression results in anucleate cells. It has a calcium binding activity. {ECO:0000269|PubMed:8602138}.

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2561|complex.ecocyc.CPLX0-2561]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7697|complex.ecocyc.CPLX0-7697]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7698|complex.ecocyc.CPLX0-7698]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0922|gene.b0922]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60293`
- `KEGG:ecj:JW0905;eco:b0922;ecoc:C3026_05670;`
- `GeneID:93776493;945548;`
- `GO:GO:0000796; GO:0005509; GO:0005737; GO:0006260; GO:0007059; GO:0009295; GO:0030261; GO:0051301`

## Notes

Chromosome partition protein MukF (Protein KicB)

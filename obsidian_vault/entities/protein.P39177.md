---
entity_id: "protein.P39177"
entity_type: "protein"
name: "uspG"
source_database: "UniProt"
source_id: "P39177"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uspG ybdQ yzzU b0607 JW0600"
---

# uspG

`protein.P39177`

## Static

- Type: `protein`
- Source: `UniProt:P39177`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Has intrinsic autoadenylation and autophosphorylation activities, probably on Ser or Thr residues. {ECO:0000269|PubMed:16460009}. UspG belongs to the class II (UspF/G) subfamily of universal stress proteins . Abundance of UspG is increased in response to nitrosative stress . UspG possesses intrinsic autophosphorylation and autoadenylation activity; the C-terminal domain of UspG is important for these activities and required for dimerization . UspG binds to GroEL . A ΔuspG mutant exhibits a defect in resumption of growth after reaching stationary phase and exhibits increased sensitivity to carbonyl cyanide m-chlorophenyl hydrazone (CCCP, a respiratory chain uncoupler), compared to wild type . Single deletions of uspF or uspG have a negative effect on fimbria-dependent adhesion and show enhanced motility. However, the uspFG double mutant shows no adhesion phenotype. A uspF uspG double mutant is more sensitive to oxidative stress and to the antibiotic streptonigrin . UspG abundance is increased in response to stresses including heat, stationary phase, carbon or phosphate starvation, and CCCP treatment . UP12: "unknown protein 12" Reviews:

## Biological Role

Component of universal stress protein G (complex.ecocyc.CPLX0-3939).

## Annotation

FUNCTION: Has intrinsic autoadenylation and autophosphorylation activities, probably on Ser or Thr residues. {ECO:0000269|PubMed:16460009}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3939|complex.ecocyc.CPLX0-3939]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0607|gene.b0607]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39177`
- `KEGG:ecj:JW0600;eco:b0607;ecoc:C3026_03035;`
- `GeneID:945229;`
- `GO:GO:0004017; GO:0004672; GO:0005737; GO:0006950; GO:0042803; GO:0070733; GO:1902021`

## Notes

Universal stress protein UP12 (Universal stress protein G)

---
entity_id: "protein.Q46897"
entity_type: "protein"
name: "casE"
source_database: "UniProt"
source_id: "Q46897"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "casE cas6e ygcH b2756 JW2726"
---

# casE

`protein.Q46897`

## Static

- Type: `protein`
- Source: `UniProt:Q46897`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: CasE is required to process the pre-crRNA into single repeat-spacer units, with an 8-nt 5'-repeat DNA tag that may help other proteins recognize the crRNA. This subunit alone will cleave pre-crRNA, as will CasCDE or CasCE; cleavage does not require divalent metals or ATP. CasCDE alone is also able to form R-loops. Partially inhibits the cleavage of Holliday junctions by YgbT (Cas1). Yields a 5'-hydroxy group and a 2',3'-cyclic phosphate terminus.; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization...

## Biological Role

Component of CRISPR-associated complex for antiviral defense (complex.ecocyc.CPLX0-7725).

## Annotation

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: CasE is required to process the pre-crRNA into single repeat-spacer units, with an 8-nt 5'-repeat DNA tag that may help other proteins recognize the crRNA. This subunit alone will cleave pre-crRNA, as will CasCDE or CasCE; cleavage does not require divalent metals or ATP. CasCDE alone is also able to form R-loops. Partially inhibits the cleavage of Holliday junctions by YgbT (Cas1). Yields a 5'-hydroxy group and a 2',3'-cyclic phosphate terminus.; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7725|complex.ecocyc.CPLX0-7725]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2756|gene.b2756]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46897`
- `KEGG:ecj:JW2726;eco:b2756;ecoc:C3026_15150;`
- `GeneID:947226;`
- `GO:GO:0003723; GO:0004521; GO:0006396; GO:0016787; GO:0032991; GO:0051607; GO:0099048`
- `EC:3.1.-.-`

## Notes

CRISPR system Cascade subunit CasE (EC 3.1.-.-) (CasE endoRNase) (crRNA endonuclease)

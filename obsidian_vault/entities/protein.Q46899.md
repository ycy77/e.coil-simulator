---
entity_id: "protein.Q46899"
entity_type: "protein"
name: "casC"
source_database: "UniProt"
source_id: "Q46899"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "casC cas4 cse4 ygcJ b2758 JW2728"
---

# casC

`protein.Q46899`

## Static

- Type: `protein`
- Source: `UniProt:Q46899`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasCDE alone is also able to form R-loops. The 6 CasC (Cas7.1 - Cas7.6) subunits of the Cascade complex form a helical structure that binds crRNA and presents it for target DNA binding. Bound crRNA presents as 6 segments with a kink occurring at every 6th ribonucleotide. Mutating the target DNA residues that are complementary to the 'kink' residues does not affect target binding whereas mutating target residues located either side of the kink residues results in serious defects in target binding...

## Biological Role

Component of CRISPR-associated complex for antiviral defense (complex.ecocyc.CPLX0-7725).

## Annotation

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasCDE alone is also able to form R-loops.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7725|complex.ecocyc.CPLX0-7725]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2758|gene.b2758]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46899`
- `KEGG:ecj:JW2728;eco:b2758;ecoc:C3026_15160;`
- `GeneID:947224;`
- `GO:GO:0003723; GO:0032991; GO:0051607; GO:0071667; GO:0099048`

## Notes

CRISPR system Cascade subunit CasC

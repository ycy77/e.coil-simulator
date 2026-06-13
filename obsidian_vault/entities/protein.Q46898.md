---
entity_id: "protein.Q46898"
entity_type: "protein"
name: "casD"
source_database: "UniProt"
source_id: "Q46898"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "casD cas5 ygcI b2757 JW5844"
---

# casD

`protein.Q46898`

## Static

- Type: `protein`
- Source: `UniProt:Q46898`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasCDE alone is also able to form R-loops. CasD interacts with one CasC subunit (Cas7.6) and with CasA to form the tail of the Cascade complex. CasD also contributes to crRNA binding . Residues in the L1-helix and the β-hairpin of CasD are required for dsDNA binding of Cascade . CasA is required for the double-stranded target DNA binding activity of Cascade...

## Biological Role

Component of CRISPR-associated complex for antiviral defense (complex.ecocyc.CPLX0-7725).

## Annotation

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasCDE alone is also able to form R-loops.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7725|complex.ecocyc.CPLX0-7725]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2757|gene.b2757]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46898`
- `KEGG:ecj:JW5844;eco:b2757;ecoc:C3026_15155;`
- `GeneID:947225;`
- `GO:GO:0003723; GO:0032991; GO:0043571; GO:0051607; GO:0071667; GO:0099048`

## Notes

CRISPR system Cascade subunit CasD

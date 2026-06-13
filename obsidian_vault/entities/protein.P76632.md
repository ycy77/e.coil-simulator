---
entity_id: "protein.P76632"
entity_type: "protein"
name: "casB"
source_database: "UniProt"
source_id: "P76632"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "casB cse2 ygcK b2759 JW2729"
---

# casB

`protein.P76632`

## Static

- Type: `protein`
- Source: `UniProt:P76632`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. The two CasB subunits (Cse2.1 and Cse2.2) form a head to tail dimer that contacts the CasC helical backbone of the Cascade complex; the CasB subunits do not contact crRNA but may function to stabilise bound target DNA . An insertion mutant in casB/ygcK shows lower transposition of IS903 . Deletions of each Cas subunit (CasA, B, C, D, E) were made but only CasB was found to be dispensible for gene silencing and plasmid interference . CasB: "CRISPR-associated"

## Biological Role

Component of CRISPR-associated complex for antiviral defense (complex.ecocyc.CPLX0-7725).

## Annotation

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7725|complex.ecocyc.CPLX0-7725]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2759|gene.b2759]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76632`
- `KEGG:ecj:JW2729;eco:b2759;ecoc:C3026_15165;`
- `GeneID:947223;`
- `GO:GO:0003676; GO:0003677; GO:0003723; GO:0032991; GO:0051607; GO:0099048`

## Notes

CRISPR system Cascade subunit CasB

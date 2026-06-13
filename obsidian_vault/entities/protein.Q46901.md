---
entity_id: "protein.Q46901"
entity_type: "protein"
name: "casA"
source_database: "UniProt"
source_id: "Q46901"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "casA cse1 ygcL b2760 JW2730"
---

# casA

`protein.Q46901`

## Static

- Type: `protein`
- Source: `UniProt:Q46901`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, probably via interactions with CasA, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasA is not required for formation of Cascade, but probably enhances binding to and subsequent recognition of both target dsDNA and ssDNA. CasA interacts with CasB and with CasD in the Cascade complex. In the purified, crystallised Cascade complex CasA contains a zinc ion coordinated by 4 cysteine residues. CasA also contributes to crRNA binding . CasA is required for the double-stranded target DNA binding activity of Cascade...

## Biological Role

Component of CRISPR-associated complex for antiviral defense (complex.ecocyc.CPLX0-7725).

## Annotation

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA).; FUNCTION: A component of Cascade, which participates in CRISPR interference, the third stage of CRISPR immunity. Cascade binds both crRNA and in a sequence-specific manner negatively supercoiled dsDNA target. This leads to the formation of an R-loop in which the crRNA binds the target DNA, displacing the noncomplementary strand. Cas3 is recruited to Cascade, probably via interactions with CasA, nicks target DNA and then unwinds and cleaves the target, leading to DNA degradation and invader neutralization. CasA is not required for formation of Cascade, but probably enhances binding to and subsequent recognition of both target dsDNA and ssDNA.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7725|complex.ecocyc.CPLX0-7725]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2760|gene.b2760]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46901`
- `KEGG:ecj:JW2730;eco:b2760;ecoc:C3026_15170;`
- `GeneID:947222;`
- `GO:GO:0003677; GO:0003723; GO:0008270; GO:0032991; GO:0051607; GO:0099048`

## Notes

CRISPR system Cascade subunit CasA (CRISPR type I-E/Ecoli-associated protein CasA/Cse1) (CRISPR-associated protein CasA/Cse1)

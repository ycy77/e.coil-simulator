---
entity_id: "complex.ecocyc.CPLX0-8103"
entity_type: "complex"
name: "methyl-accepting chemotaxis protein - serine-sensing"
source_database: "EcoCyc"
source_id: "CPLX0-8103"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methyl-accepting chemotaxis protein - serine-sensing

`complex.ecocyc.CPLX0-8103`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8103`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P02942|protein.P02942]]

## Enriched Summary

The tsr gene product is one of four methyl-accepting chemotaxis proteins (MCPs) in E. coli K-12 (EG11034 Tsr, EG10988 Tar, EG11018 Trg, and EG10987 Tap). Tsr, also known as MCP-I, is the receptor for the attractant L-serine and related amino acids such as cysteine, L-alanine and glycine. It also responds to a variety of repellents such as acetate, benzoate, indole and L-leucine and is thermosensitive . Tsr and Tar mediate the chemotactic response to pH . Tsr mediates the chemotactic response to the quorum-sensing molecule AI-2; Tsr is thought to interact with LsrB-bound AI-2 to mediate chemotaxis towards AI-2 . Chemotaxis to AI-2 mediates the aggregating phenotype seen in E. coli strain W3110 (RpoS+) grown at 37°C to mid-exponential phase . E. coli MCPs form ternary complexes with the histidine autokinase CHEA-CPLX "CheA" and the coupling protein CHEW-MONOMER "CheW" . Tsr and CPLX0-8102 "Tar" are considered to be high-abundance receptors while CPLX0-8104 "Tap" and CPLX0-8105 "Trg" are low-abundance . Tsr forms homodimers which are further organised into trimers of dimers . The MCP homodimers are composed of a periplasmic ligand binding domain, a transmembrane domain and a cytoplasmic signaling domain (reviews: ). The cytoplasmic domains of the four E. coli MCPs have a high degree of sequence similarity...

## Biological Role

Component of chemotaxis signaling complex core unit - serine sensing (complex.ecocyc.TSR-CPLX).

## Annotation

The tsr gene product is one of four methyl-accepting chemotaxis proteins (MCPs) in E. coli K-12 (EG11034 Tsr, EG10988 Tar, EG11018 Trg, and EG10987 Tap). Tsr, also known as MCP-I, is the receptor for the attractant L-serine and related amino acids such as cysteine, L-alanine and glycine. It also responds to a variety of repellents such as acetate, benzoate, indole and L-leucine and is thermosensitive . Tsr and Tar mediate the chemotactic response to pH . Tsr mediates the chemotactic response to the quorum-sensing molecule AI-2; Tsr is thought to interact with LsrB-bound AI-2 to mediate chemotaxis towards AI-2 . Chemotaxis to AI-2 mediates the aggregating phenotype seen in E. coli strain W3110 (RpoS+) grown at 37°C to mid-exponential phase . E. coli MCPs form ternary complexes with the histidine autokinase CHEA-CPLX "CheA" and the coupling protein CHEW-MONOMER "CheW" . Tsr and CPLX0-8102 "Tar" are considered to be high-abundance receptors while CPLX0-8104 "Tap" and CPLX0-8105 "Trg" are low-abundance . Tsr forms homodimers which are further organised into trimers of dimers . The MCP homodimers are composed of a periplasmic ligand binding domain, a transmembrane domain and a cytoplasmic signaling domain (reviews: ). The cytoplasmic domains of the four E. coli MCPs have a high degree of sequence similarity . The cytoplasmic domain of a monomeric Tsr receptor protein consists of 2 antiparallel α-helices connected by a "U-turn" linker. In the dimeric Tsr protein the 4 α-helices pack against each other to form a super-coiled helical bundle . The distal region of the cytoplasmic domain (known as the hairpin tip) is the site of interaction with CheA and CheW and also contains the contact sites for trimer formation. The hairpin tip of dimeric Tsr (residues 383-397) is highly dyna

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TSR-CPLX|complex.ecocyc.TSR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P02942|protein.P02942]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8103`
- `QSPROTEOME:QS00049393`

## Notes

2*protein.P02942

---
entity_id: "complex.ecocyc.CPLX0-7725"
entity_type: "complex"
name: "CRISPR-associated complex for antiviral defense"
source_database: "EcoCyc"
source_id: "CPLX0-7725"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Cascade"
---

# CRISPR-associated complex for antiviral defense

`complex.ecocyc.CPLX0-7725`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7725`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46901|protein.Q46901]], [[protein.P76632|protein.P76632]], [[protein.Q46899|protein.Q46899]], [[protein.Q46898|protein.Q46898]], [[protein.Q46897|protein.Q46897]]

## Enriched Summary

CRISPR (clusters of regularly interspersed short palindromic repeats) loci are associated with a defense system against foreign DNA, such as bacteriophage, providing an adaptable genetic record of past infections. These systems occur widely in bacteria and archaea . The first reports of a CRISPR-like region in E. coli were by , who didn't know the biological function but noted the unusual nature of repeat sequences interspersed by non-repetitive regions of 32 nt between EG10488 and EG12845; this region is now referred to as the CRISPR array containing both the leader sequence, repeats and spacers. The CRISPR locus of E. coli K-12 (TU0-13725 plus the CRISPR array) belongs to the type I-E class of CRISPR/Cas loci . The CRISPR locus is transcribed into a large pre-crRNA. CasE alone or within the Cascade complex is required for processing of pre-crRNA into mature crRNA. Processed crRNAs of approximately 57 nt copurify with Cascade. In the presence of EG12634-MONOMER "Cas3", this complex gives rise to resistance against phages whose genomes have regions of complementarity to elements in the CRISPR repeats ; this process is also known as "interference". The activation of the CRISPR-Cas system, mediated by an hns mutation, negatively affects the lysogenic infection of the Stx2 phage lysogen in E. coli...

## Biological Role

Catalyzes RXN0-5435 (reaction.ecocyc.RXN0-5435).

## Annotation

CRISPR (clusters of regularly interspersed short palindromic repeats) loci are associated with a defense system against foreign DNA, such as bacteriophage, providing an adaptable genetic record of past infections. These systems occur widely in bacteria and archaea . The first reports of a CRISPR-like region in E. coli were by , who didn't know the biological function but noted the unusual nature of repeat sequences interspersed by non-repetitive regions of 32 nt between EG10488 and EG12845; this region is now referred to as the CRISPR array containing both the leader sequence, repeats and spacers. The CRISPR locus of E. coli K-12 (TU0-13725 plus the CRISPR array) belongs to the type I-E class of CRISPR/Cas loci . The CRISPR locus is transcribed into a large pre-crRNA. CasE alone or within the Cascade complex is required for processing of pre-crRNA into mature crRNA. Processed crRNAs of approximately 57 nt copurify with Cascade. In the presence of EG12634-MONOMER "Cas3", this complex gives rise to resistance against phages whose genomes have regions of complementarity to elements in the CRISPR repeats ; this process is also known as "interference". The activation of the CRISPR-Cas system, mediated by an hns mutation, negatively affects the lysogenic infection of the Stx2 phage lysogen in E. coli . CRISPR-mediated degradation of plasmid DNA has been reconstituted in vitro with purified Cascade and Cas3 . Cascade can also be loaded with synthetic crRNA in vitro . The Cascade complex locates target sequences within negatively supercoiled DNA that are flanked by a protospacer-adjacent motif (PAM). The PAM sequence is crucial for discrimination between self and non-self DNA. The crRNA invades the foreign dsDNA and forms hybrid molecules of RNA base-paired into duplex DNA, als

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5435|reaction.ecocyc.RXN0-5435]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P76632|protein.P76632]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.Q46897|protein.Q46897]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.Q46898|protein.Q46898]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.Q46899|protein.Q46899]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.Q46901|protein.Q46901]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-7725`
- `PDB:4U7U`
- `PDB:4QYZ`
- `PDB:4TVX`
- `PDB:5H9F`
- `PDB:5H9E`
- `PDB:5CD4`
- `PDB:4QYZ`
- `PDB:1VY8`
- `QSPROTEOME:QS00195751`

## Notes

1*protein.Q46901|2*protein.P76632|6*protein.Q46899|1*protein.Q46898|1*protein.Q46897

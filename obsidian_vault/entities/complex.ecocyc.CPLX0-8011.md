---
entity_id: "complex.ecocyc.CPLX0-8011"
entity_type: "complex"
name: "UDP-N-acetylglucosamine—undecaprenyl-phosphate N-acetylglucosaminephosphotransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8011"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UDP-N-acetylglucosamine—undecaprenyl-phosphate N-acetylglucosaminephosphotransferase

`complex.ecocyc.CPLX0-8011`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8011`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC78|protein.P0AC78]]

## Enriched Summary

Undecaprenyl-phosphate α-N-acetylglucosaminyl transferase (WecA, formerly Rfe) initiates the biosynthesis of enterobacterial common antigen (ECA) and O-antigen PS by catalyzing the transfer of N-acetylglucosamine (GlcNAc)-1-phosphate onto undecaprenyl phosphate to form Und-P-P-GlcNAc . This reaction requires a divalent cation . Rfe can function well with either Mg2+ or Mn2+, although the enzymatic reaction in vitro is more effective with Mn2+ . WecA is an integral membrane protein and studies have determined its membrane topology . Fluorescence microscopy studies showed that Rfe localizes to discrete regions in the bacterial plasma membrane . The N-terminal region is necessary for function, but not membrane localization . The nucleotide sequence of wecA has been determined and the protein has been expressed . However, overproduction and purification of WecA in E. coli has proven to be challenging . Mutants of rfe are unable to synthesize ECA and lipopolysaccharide 08-side chains . Site directed mutagenesis experiments identified conserved residues which were essential for catalysis . The enzyme activity of WecA is inhibited by the antibiotic Tunicamycin . Tunicamycin is an antibiotic that specifically prevents the transfer of GlcNAc-1-phosphate from UDP-GlcNAc to polyprenyl monophosphate acceptors...

## Biological Role

Catalyzes GLCNACPTRANS-RXN (reaction.ecocyc.GLCNACPTRANS-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Undecaprenyl-phosphate α-N-acetylglucosaminyl transferase (WecA, formerly Rfe) initiates the biosynthesis of enterobacterial common antigen (ECA) and O-antigen PS by catalyzing the transfer of N-acetylglucosamine (GlcNAc)-1-phosphate onto undecaprenyl phosphate to form Und-P-P-GlcNAc . This reaction requires a divalent cation . Rfe can function well with either Mg2+ or Mn2+, although the enzymatic reaction in vitro is more effective with Mn2+ . WecA is an integral membrane protein and studies have determined its membrane topology . Fluorescence microscopy studies showed that Rfe localizes to discrete regions in the bacterial plasma membrane . The N-terminal region is necessary for function, but not membrane localization . The nucleotide sequence of wecA has been determined and the protein has been expressed . However, overproduction and purification of WecA in E. coli has proven to be challenging . Mutants of rfe are unable to synthesize ECA and lipopolysaccharide 08-side chains . Site directed mutagenesis experiments identified conserved residues which were essential for catalysis . The enzyme activity of WecA is inhibited by the antibiotic Tunicamycin . Tunicamycin is an antibiotic that specifically prevents the transfer of GlcNAc-1-phosphate from UDP-GlcNAc to polyprenyl monophosphate acceptors . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLCNACPTRANS-RXN|reaction.ecocyc.GLCNACPTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AC78|protein.P0AC78]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8011`
- `QSPROTEOME:QS00196463`

## Notes

2*protein.P0AC78

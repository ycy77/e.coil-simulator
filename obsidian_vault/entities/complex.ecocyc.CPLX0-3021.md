---
entity_id: "complex.ecocyc.CPLX0-3021"
entity_type: "complex"
name: "isoaspartyl dipeptidase"
source_database: "EcoCyc"
source_id: "CPLX0-3021"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# isoaspartyl dipeptidase

`complex.ecocyc.CPLX0-3021`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3021`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39377|protein.P39377]]

## Enriched Summary

Isoaspartyl dipeptidase is an enzyme that breaks down β linkages, the peptide bonds that can form spontaneously between the side chain of an aspartate residue and another amino acid . Crystal structures of the enzyme have been solved . Isoaspartyl dipeptidase is a binuclear metalloenzyme that forms an octamer comprised of a tetramer of dimers. The reaction mechanism was investigated utilizing a number of site-directed mutants in the active site and has been modeled using quantum chemical methods . Mutations in solvent-exposed residues that increase hydrophobicity can trigger supramolecular self-assembly into extended fiber structures . An iadA mutant has no apparent growth defect; however, it still contains ~30% of wild type isoaspartyl dipeptidase activity . This may be due to a second enzyme, CPLX0-263 "IaaA". IadA: "isoaspartyl dipeptidase A" Isoaspartyl dipeptidase is an enzyme that breaks down β linkages, the peptide bonds that can form spontaneously between the side chain of an aspartate residue and another amino acid . Crystal structures of the enzyme have been solved . Isoaspartyl dipeptidase is a binuclear metalloenzyme that forms an octamer comprised of a tetramer of dimers. The reaction mechanism was investigated utilizing a number of site-directed mutants in the active site and has been modeled using quantum chemical methods...

## Biological Role

Catalyzes RXN0-3241 (reaction.ecocyc.RXN0-3241). Bound by Zinc cation (molecule.C00038).

## Annotation

Isoaspartyl dipeptidase is an enzyme that breaks down β linkages, the peptide bonds that can form spontaneously between the side chain of an aspartate residue and another amino acid . Crystal structures of the enzyme have been solved . Isoaspartyl dipeptidase is a binuclear metalloenzyme that forms an octamer comprised of a tetramer of dimers. The reaction mechanism was investigated utilizing a number of site-directed mutants in the active site and has been modeled using quantum chemical methods . Mutations in solvent-exposed residues that increase hydrophobicity can trigger supramolecular self-assembly into extended fiber structures . An iadA mutant has no apparent growth defect; however, it still contains ~30% of wild type isoaspartyl dipeptidase activity . This may be due to a second enzyme, CPLX0-263 "IaaA". IadA: "isoaspartyl dipeptidase A"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3241|reaction.ecocyc.RXN0-3241]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P39377|protein.P39377]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:CPLX0-3021`
- `QSPROTEOME:QS00191659`

## Notes

8*protein.P39377

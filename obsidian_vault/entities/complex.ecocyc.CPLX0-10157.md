---
entity_id: "complex.ecocyc.CPLX0-10157"
entity_type: "complex"
name: "peptidyl-prolyl cis-trans isomerase/OMP chaperone FkpA"
source_database: "EcoCyc"
source_id: "CPLX0-10157"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# peptidyl-prolyl cis-trans isomerase/OMP chaperone FkpA

`complex.ecocyc.CPLX0-10157`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-10157`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P45523|protein.P45523]]

## Enriched Summary

Early studies implicated FkpA as a periplasmic peptidyl-prolyl cis/trans isomerase (PPIase) with independent chaperone activity . FkpA is part of a periplasmic chaperone network that maintains outer membrane proteins (OMPs) in an unfolded state prior to membrane insertion . FkpA prevents the aggregation of a defective-folding variant of the maltose-binding protein; FkpA consists of two domains - an N-terminal domain of unknown function and the C-terminal FK506-binding domain; the purified protein has PPIase activity that is inhibited by FK506 . Purified FkpA forms a homodimer; FK506-complexed and ligand-free structures have been reported (see also ). A mutant strain lacking the 4 periplasmic PPIases (EG10757-MONOMER PpiA, FkpA, EG10985-MONOMER SurA and G6242-MONOMER PpiD) is viable but has diminished growth and is significantly more sensitive to selected antibiotics . FkpA function is important for OMP biogenesis under heat shock conditions . Purified FkpA binds unfolded OMP clients (OmpA171, OmpX, and BamA) and exhibits chaperone activity; FkpA improves uOMP folding yields but does not behave as a folding catalyst; FkpA outcompetes SurA, but not Skp, for OmpA171 binding; FkpA binds OMP clients using an extensive interface that spans the inner surfaces of both its domains; both domains are required for tight client binding and chaperone function...

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN).

## Annotation

Early studies implicated FkpA as a periplasmic peptidyl-prolyl cis/trans isomerase (PPIase) with independent chaperone activity . FkpA is part of a periplasmic chaperone network that maintains outer membrane proteins (OMPs) in an unfolded state prior to membrane insertion . FkpA prevents the aggregation of a defective-folding variant of the maltose-binding protein; FkpA consists of two domains - an N-terminal domain of unknown function and the C-terminal FK506-binding domain; the purified protein has PPIase activity that is inhibited by FK506 . Purified FkpA forms a homodimer; FK506-complexed and ligand-free structures have been reported (see also ). A mutant strain lacking the 4 periplasmic PPIases (EG10757-MONOMER PpiA, FkpA, EG10985-MONOMER SurA and G6242-MONOMER PpiD) is viable but has diminished growth and is significantly more sensitive to selected antibiotics . FkpA function is important for OMP biogenesis under heat shock conditions . Purified FkpA binds unfolded OMP clients (OmpA171, OmpX, and BamA) and exhibits chaperone activity; FkpA improves uOMP folding yields but does not behave as a folding catalyst; FkpA outcompetes SurA, but not Skp, for OmpA171 binding; FkpA binds OMP clients using an extensive interface that spans the inner surfaces of both its domains; both domains are required for tight client binding and chaperone function . FkpA chaperone function is required for bacteriophage HK97 infection and for imported colicin M lytic activity . fkpA is a member of the RPOE-MONOMER Sigma E regulon . FkpA improves yields of E. coli based antibody production systems (and see ). fkpA: CPD-10016 FK-506 binding protein . Related review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P45523|protein.P45523]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-10157`
- `QSPROTEOME:QS00188929`

## Notes

2*protein.P45523

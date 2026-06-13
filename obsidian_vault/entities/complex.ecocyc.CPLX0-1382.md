---
entity_id: "complex.ecocyc.CPLX0-1382"
entity_type: "complex"
name: "RNase P"
source_database: "EcoCyc"
source_id: "CPLX0-1382"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ribonuclease P"
---

# RNase P

`complex.ecocyc.CPLX0-1382`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1382`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7Y8|protein.P0A7Y8]]

## Enriched Summary

Ribonuclease P (RNase P) is an RNA-containing protein that catalyzes the nucleolytic cleavage of the 5' end of pre-tRNAs during their processing to mature uncharged tRNAs . For the leuX-tRNA, the enzyme can cleave the 3' Rho-independent terminator, though not very efficiently in PWY0-1614 . See PWY0-1628 and PWY0-1625 as well as individual tRNA processing pathways. It also cleaves the precursor to 4.5 S stable RNA . In E. coli and other bacteria the RNase P holoenzyme is comprised of a catalytic RNA subunit (a ribozyme), and a non-catalytic protein subunit that stabilizes the RNA subunit . The bacterial RNA subunits are classified into A-type (ancestral-type) found in E. coli, and B-type (Bacillus-type). RNase P is also found in archaea and eukaryotes. The RNA subunits have homologs across the three kingdoms, but the bacterial protein subunits have no structural homologs with those of archaea and eukaryotes . The 1989 Nobel Prize in chemistry was awarded to Sidney Altman and Thomas Cech for the discovery of catalytic RNAs. Altman's work focused on the characterization of E. coli RnpB RNA . Much of the work on E. coli RNase P has been done in strain MRE600, a non-K-12 strain that lacks RNase I activity . Please see the summaries for RnpA and RnpB for information on these subunits and additional information on the holoenzyme...

## Biological Role

Catalyzes 3.1.26.5-RXN (reaction.ecocyc.3.1.26.5-RXN), endoribonuclease (reaction.ecocyc.RXN-24138), RXN0-6480 (reaction.ecocyc.RXN0-6480), RXN0-7478 (reaction.ecocyc.RXN0-7478), RXN0-7480 (reaction.ecocyc.RXN0-7480), RXN0-7481 (reaction.ecocyc.RXN0-7481). Bound by Magnesium cation (molecule.C00305).

## Annotation

Ribonuclease P (RNase P) is an RNA-containing protein that catalyzes the nucleolytic cleavage of the 5' end of pre-tRNAs during their processing to mature uncharged tRNAs . For the leuX-tRNA, the enzyme can cleave the 3' Rho-independent terminator, though not very efficiently in PWY0-1614 . See PWY0-1628 and PWY0-1625 as well as individual tRNA processing pathways. It also cleaves the precursor to 4.5 S stable RNA . In E. coli and other bacteria the RNase P holoenzyme is comprised of a catalytic RNA subunit (a ribozyme), and a non-catalytic protein subunit that stabilizes the RNA subunit . The bacterial RNA subunits are classified into A-type (ancestral-type) found in E. coli, and B-type (Bacillus-type). RNase P is also found in archaea and eukaryotes. The RNA subunits have homologs across the three kingdoms, but the bacterial protein subunits have no structural homologs with those of archaea and eukaryotes . The 1989 Nobel Prize in chemistry was awarded to Sidney Altman and Thomas Cech for the discovery of catalytic RNAs. Altman's work focused on the characterization of E. coli RnpB RNA . Much of the work on E. coli RNase P has been done in strain MRE600, a non-K-12 strain that lacks RNase I activity . Please see the summaries for RnpA and RnpB for information on these subunits and additional information on the holoenzyme. Reviews:

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.3.1.26.5-RXN|reaction.ecocyc.3.1.26.5-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24138|reaction.ecocyc.RXN-24138]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6480|reaction.ecocyc.RXN0-6480]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7478|reaction.ecocyc.RXN0-7478]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7480|reaction.ecocyc.RXN0-7480]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7481|reaction.ecocyc.RXN0-7481]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7Y8|protein.P0A7Y8]] `EcoCyc` `database` - EcoCyc component coefficient=1

## External IDs

- `EcoCyc:CPLX0-1382`

## Notes

1*protein.P0A7Y8

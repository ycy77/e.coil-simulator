---
entity_id: "complex.ecocyc.DSBC-CPLX"
entity_type: "complex"
name: "protein disulfide isomerase DsbC"
source_database: "EcoCyc"
source_id: "DSBC-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "DsbC"
  - "disulfide oxidoreductase 2"
  - "thiol:disulfide oxidoreductase DsbC"
  - "protein disulfide oxidoreductase DsbC"
---

# protein disulfide isomerase DsbC

`complex.ecocyc.DSBC-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DSBC-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PERI-BAC-GN
- Complex type: `structural`
- Components: [[protein.P0AEG6|protein.P0AEG6]]

## Enriched Summary

DsbC is a periplasmic disulfide oxidoreductase which is thought to be the main catalyst of protein disulfide bond rearrangement in the periplasm although there is also evidence for a role in de novo disulphide bond formation. DsbC, DsbD and thioredoxin are the components of a pathway for protein disulfide bond isomerization in E. coli K-12 . As an isomerase DsbC is active in the reduced state; reducing potential is passed from cytoplasmic thioredoxin, through the DsbD membrane protein to periplasmic DsbC (see also ). dsbC null mutants have phenotypes (eg. reduced alkaline phosphatase activity; hypersensitivity to penicillin) that are associated with defects in the efficient folding of envelope proteins containing disulfide bonds; overexpression of dsbC can substitute for the loss of dsbA in vivo; purified DsbC accelerates the reduction of insulin in the presence of dithiothreitol . DsbC activity impacts proteins containing multiple disulfide bonds: inactivation of dsbC impacts (very slightly) the maturation of alkaline phosphatase but does not affect OmpA maturation; inactivation of dsbC has a significant impact on the maturation of heterologously expressed mouse urokinase (containing 12 disulfide bonds) . DsbC has a greater protein disulfide isomerizing activity than DsbA . DsbC substrates include RNase I, MepA , AppA , LptD and RcsF...

## Biological Role

Catalyzes 5.3.4.1-RXN (reaction.ecocyc.5.3.4.1-RXN).

## Annotation

DsbC is a periplasmic disulfide oxidoreductase which is thought to be the main catalyst of protein disulfide bond rearrangement in the periplasm although there is also evidence for a role in de novo disulphide bond formation. DsbC, DsbD and thioredoxin are the components of a pathway for protein disulfide bond isomerization in E. coli K-12 . As an isomerase DsbC is active in the reduced state; reducing potential is passed from cytoplasmic thioredoxin, through the DsbD membrane protein to periplasmic DsbC (see also ). dsbC null mutants have phenotypes (eg. reduced alkaline phosphatase activity; hypersensitivity to penicillin) that are associated with defects in the efficient folding of envelope proteins containing disulfide bonds; overexpression of dsbC can substitute for the loss of dsbA in vivo; purified DsbC accelerates the reduction of insulin in the presence of dithiothreitol . DsbC activity impacts proteins containing multiple disulfide bonds: inactivation of dsbC impacts (very slightly) the maturation of alkaline phosphatase but does not affect OmpA maturation; inactivation of dsbC has a significant impact on the maturation of heterologously expressed mouse urokinase (containing 12 disulfide bonds) . DsbC has a greater protein disulfide isomerizing activity than DsbA . DsbC substrates include RNase I, MepA , AppA , LptD and RcsF . DsbC is able to reduce the disulfide linked dimer of arabinose binding protein (AraF) which forms under oxidative stress conditions . DsbC may act to reduce misoxidized disulfide bonds (which then become substrates for DsbA) or it may act as a true isomerase which shuffles misoxidized disulfide bonds into the correct position (see ); heterologous expression of a dedicated thiol reductase in an E. coli dsbC null mutant restores activity t

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.5.3.4.1-RXN|reaction.ecocyc.5.3.4.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEG6|protein.P0AEG6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DSBC-CPLX`
- `QSPROTEOME:QS00203723`

## Notes

2*protein.P0AEG6

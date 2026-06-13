---
entity_id: "complex.ecocyc.CPLX0-2941"
entity_type: "complex"
name: "protease IV, a signal peptide peptidase"
source_database: "EcoCyc"
source_id: "CPLX0-2941"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# protease IV, a signal peptide peptidase

`complex.ecocyc.CPLX0-2941`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2941`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P08395|protein.P08395]]

## Enriched Summary

Protease IV is an endopeptidase that degrades cleaved lipoprotein signal peptide . It may not be the only protease carrying out this function, as signal peptide is still degraded, albeit slowly, in its absence . Protease IV functions as a tetramer with a novel bowl shaped architecture . Analysis of the peptide fragments generated from cleavage of prolipoprotein signal peptide by purified SppA suggests that it cleaves predominantly in the hydrophobic segment of the signal peptide . SppA has one transmembrane segment (spanning residues 29-45) and the carboxy-terminal domain is located in the periplasm . Deletion of sppA did not affect degradation of the signal peptides of fusion proteins in vivo . Protease IV is an endopeptidase that degrades cleaved lipoprotein signal peptide . It may not be the only protease carrying out this function, as signal peptide is still degraded, albeit slowly, in its absence . Protease IV functions as a tetramer with a novel bowl shaped architecture . Analysis of the peptide fragments generated from cleavage of prolipoprotein signal peptide by purified SppA suggests that it cleaves predominantly in the hydrophobic segment of the signal peptide . SppA has one transmembrane segment (spanning residues 29-45) and the carboxy-terminal domain is located in the periplasm...

## Biological Role

Catalyzes RXN0-3201 (reaction.ecocyc.RXN0-3201).

## Annotation

Protease IV is an endopeptidase that degrades cleaved lipoprotein signal peptide . It may not be the only protease carrying out this function, as signal peptide is still degraded, albeit slowly, in its absence . Protease IV functions as a tetramer with a novel bowl shaped architecture . Analysis of the peptide fragments generated from cleavage of prolipoprotein signal peptide by purified SppA suggests that it cleaves predominantly in the hydrophobic segment of the signal peptide . SppA has one transmembrane segment (spanning residues 29-45) and the carboxy-terminal domain is located in the periplasm . Deletion of sppA did not affect degradation of the signal peptides of fusion proteins in vivo .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3201|reaction.ecocyc.RXN0-3201]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08395|protein.P08395]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-2941`
- `QSPROTEOME:QS00188493`

## Notes

4*protein.P08395

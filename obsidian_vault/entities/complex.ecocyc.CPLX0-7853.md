---
entity_id: "complex.ecocyc.CPLX0-7853"
entity_type: "complex"
name: "Der GTPase-activating protein YihI"
source_database: "EcoCyc"
source_id: "CPLX0-7853"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GAP-like protein that activates GTPase activity of Der"
---

# Der GTPase-activating protein YihI

`complex.ecocyc.CPLX0-7853`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7853`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8H6|protein.P0A8H6]]

## Enriched Summary

YihI activates the GTPase activity of G7319-MONOMER Der and can thus be considered a GAP (GTPase activating)-like protein. The stimulation is specific to Der; YihI does not stimulate the GTPase activity of Era or ObgE . YihI is an unusual, highly hydrophilic protein with an uneven distribution of charged residues, resulting in an N-terminal region with high pI and a C-terminal region with low pI. The interaction of YihI with Der requires only the C-terminal 78 amino acids of YihI . YihI was identified in a phylogenetic screen that found proteins containing domains that only occur in organisms that also contain a EG10204-MONOMER Dam methyltransferase . A yihI deletion mutant is viable and shows a shorter lag period, but the same post-lag growth rate as a wild-type strain. yihI is expressed during the lag period. Overexpression of yihI inhibits cell growth and biogenesis of the 50S ribosomal subunit . Moderate overexpression of yihI can partially complement the colony and liquid culture growth defects of the derT57I mutant, but does not restore the GTPase activity of Der . YihI activates the GTPase activity of G7319-MONOMER Der and can thus be considered a GAP (GTPase activating)-like protein. The stimulation is specific to Der; YihI does not stimulate the GTPase activity of Era or ObgE...

## Biological Role

Catalyzes RXN-21992 (reaction.ecocyc.RXN-21992).

## Annotation

YihI activates the GTPase activity of G7319-MONOMER Der and can thus be considered a GAP (GTPase activating)-like protein. The stimulation is specific to Der; YihI does not stimulate the GTPase activity of Era or ObgE . YihI is an unusual, highly hydrophilic protein with an uneven distribution of charged residues, resulting in an N-terminal region with high pI and a C-terminal region with low pI. The interaction of YihI with Der requires only the C-terminal 78 amino acids of YihI . YihI was identified in a phylogenetic screen that found proteins containing domains that only occur in organisms that also contain a EG10204-MONOMER Dam methyltransferase . A yihI deletion mutant is viable and shows a shorter lag period, but the same post-lag growth rate as a wild-type strain. yihI is expressed during the lag period. Overexpression of yihI inhibits cell growth and biogenesis of the 50S ribosomal subunit . Moderate overexpression of yihI can partially complement the colony and liquid culture growth defects of the derT57I mutant, but does not restore the GTPase activity of Der .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21992|reaction.ecocyc.RXN-21992]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8H6|protein.P0A8H6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7853`
- `QSPROTEOME:QS00049447`

## Notes

2*protein.P0A8H6

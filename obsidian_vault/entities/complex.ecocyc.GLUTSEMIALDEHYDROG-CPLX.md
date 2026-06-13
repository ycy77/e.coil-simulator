---
entity_id: "complex.ecocyc.GLUTSEMIALDEHYDROG-CPLX"
entity_type: "complex"
name: "glutamate-5-semialdehyde dehydrogenase"
source_database: "EcoCyc"
source_id: "GLUTSEMIALDEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "&gamma"
  - "-glutamyl phosphate reductase"
  - "GPR"
---

# glutamate-5-semialdehyde dehydrogenase

`complex.ecocyc.GLUTSEMIALDEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTSEMIALDEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07004|protein.P07004]]

## Enriched Summary

Glutamate-5-semialdehyde dehydrogenase (ProA) catalyzes the the reduction of γ-glutamyl phosphate to glutamate 5-semialdehyde, the second reaction in the PROSYN-PWY pathway . Although GLUTKIN-CPLX (G5K) activity produces the unstable intermediate L-GLUTAMATE-5-P (GP), suggesting channeling of this compound to ProA, a stable complex between G5K and ProA could not be isolated . The channeling of GP has subsequently been challenged by evidence that a protein-protein interaction is not required between G5K and ProA for proline synthesis, and the measured half-life of GP is long enough to reach ProA . proAB is part of a genomic region that is commonly deleted in E. coli clones isolated from long-term stab cultures . Overexpression of EG10088 asd can complement a proA mutant . Increased expression of a ProA E383A mutant, which has N-acetyl-L-glutamate 5-semialdehyde dehydrogenase activity, allows a ΔEG10065 argC mutant to grow on glucose without arginine supplementation . Suppressor mutations that allow a ΔEG10418 gshA strain to grow in the presence of arsenate map to proA and proB, enabling synthesis of γ-glutamyl cysteine, which is converted to glutathione by GshB. The suppressor alleles of ProB reduce its Km for glutamate and relieve proline-mediated feedback inhibition in the presence of a proA null allele...

## Biological Role

Catalyzes GLUTSEMIALDEHYDROG-RXN (reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN).

## Annotation

Glutamate-5-semialdehyde dehydrogenase (ProA) catalyzes the the reduction of γ-glutamyl phosphate to glutamate 5-semialdehyde, the second reaction in the PROSYN-PWY pathway . Although GLUTKIN-CPLX (G5K) activity produces the unstable intermediate L-GLUTAMATE-5-P (GP), suggesting channeling of this compound to ProA, a stable complex between G5K and ProA could not be isolated . The channeling of GP has subsequently been challenged by evidence that a protein-protein interaction is not required between G5K and ProA for proline synthesis, and the measured half-life of GP is long enough to reach ProA . proAB is part of a genomic region that is commonly deleted in E. coli clones isolated from long-term stab cultures . Overexpression of EG10088 asd can complement a proA mutant . Increased expression of a ProA E383A mutant, which has N-acetyl-L-glutamate 5-semialdehyde dehydrogenase activity, allows a ΔEG10065 argC mutant to grow on glucose without arginine supplementation . Suppressor mutations that allow a ΔEG10418 gshA strain to grow in the presence of arsenate map to proA and proB, enabling synthesis of γ-glutamyl cysteine, which is converted to glutathione by GshB. The suppressor alleles of ProB reduce its Km for glutamate and relieve proline-mediated feedback inhibition in the presence of a proA null allele . Evolution and recruitment of promiscuous enzymes have been studied using ProA and its ability to replace ArgC . The effects of segmental amplification was studied from a K-12 derived mutant that had the proBA operon moved convergent to rpoS gene, which found that protein expression doesn't scale well with gene copy number and mRNA expression . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN|reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07004|protein.P07004]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GLUTSEMIALDEHYDROG-CPLX`
- `QSPROTEOME:QS00181769`

## Notes

4*protein.P07004

---
entity_id: "molecule.ecocyc.Methionine-synthase-cob-I-alamins"
entity_type: "small_molecule"
name: "cob(I)alamin-[methionine synthase]"
source_database: "EcoCyc"
source_id: "Methionine-synthase-cob-I-alamins"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# cob(I)alamin-[methionine synthase]

`molecule.ecocyc.Methionine-synthase-cob-I-alamins`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Methionine-synthase-cob-I-alamins`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EC-2.1.1.13 is a vitamin B12-dependent zinc metalloenzyme that catalyzes the transfer of a methyl group from 5-METHYL-THF-GLU-N to homocysteine. Methionine synthase is one of two eukaryotic enzymes that require a cobalamin prosthetic group for activity. Unlike the other enzyme (EC-5.4.99.2), which requires adenosylcobalamin, the cobalamin cofactor of methionine synthase needs to be methylated. Upon the initial transfer of a cob(II)alamin cofactor from a CPD-20918, it is methylated to the active methylcob(III)alamin form by EC-1.16.1.8, which uses S-ADENOSYLMETHIONINE as the methyl donor. The methyl group is subsequently transferred to homocysteine to form methionine, leaving the cofactor briefly in a cob(I)alamin form, which is regenerated to the active methylcob(III)alamin form by a transfer of a methyl group from 5-METHYL-THF-GLU-N "5-methyltetrahydrofolate" . The enzyme becomes inactivated occasionally during its cycle by oxidation of Co(I) to Co(II). Reactivation by reductive methylation is catalysed by the enzyme itself, with S-adenosyl-L-methionine as the methyl donor and a reducing system. For the mammalian enzyme, the reducing system involves NADPH and EC-1.16.1.8. In bacteria, the reducing agent is flavodoxin, and no further catalyst is needed (the flavodoxin is kept in the reduced state by NADPH and EC-1.18.1.2)...

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

EC-2.1.1.13 is a vitamin B12-dependent zinc metalloenzyme that catalyzes the transfer of a methyl group from 5-METHYL-THF-GLU-N to homocysteine. Methionine synthase is one of two eukaryotic enzymes that require a cobalamin prosthetic group for activity. Unlike the other enzyme (EC-5.4.99.2), which requires adenosylcobalamin, the cobalamin cofactor of methionine synthase needs to be methylated. Upon the initial transfer of a cob(II)alamin cofactor from a CPD-20918, it is methylated to the active methylcob(III)alamin form by EC-1.16.1.8, which uses S-ADENOSYLMETHIONINE as the methyl donor. The methyl group is subsequently transferred to homocysteine to form methionine, leaving the cofactor briefly in a cob(I)alamin form, which is regenerated to the active methylcob(III)alamin form by a transfer of a methyl group from 5-METHYL-THF-GLU-N "5-methyltetrahydrofolate" . The enzyme becomes inactivated occasionally during its cycle by oxidation of Co(I) to Co(II). Reactivation by reductive methylation is catalysed by the enzyme itself, with S-adenosyl-L-methionine as the methyl donor and a reducing system. For the mammalian enzyme, the reducing system involves NADPH and EC-1.16.1.8. In bacteria, the reducing agent is flavodoxin, and no further catalyst is needed (the flavodoxin is kept in the reduced state by NADPH and EC-1.18.1.2). A histidine residue embedded in the canonical B12-binding DxHxxG motif in methionine synthase serves as the lower axial ligand to the cobalt, which is bound in the "base-off/His-on" state .

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN-21538|reaction.ecocyc.RXN-21538]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21539|reaction.ecocyc.RXN-21539]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Methionine-synthase-cob-I-alamins`

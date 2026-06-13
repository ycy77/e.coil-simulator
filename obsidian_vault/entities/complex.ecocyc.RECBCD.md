---
entity_id: "complex.ecocyc.RECBCD"
entity_type: "complex"
name: "exodeoxyribonuclease V"
source_database: "EcoCyc"
source_id: "RECBCD"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Exonuclease V"
  - "RecBCD"
---

# exodeoxyribonuclease V

`complex.ecocyc.RECBCD`

## Static

- Type: `complex`
- Source: `EcoCyc:RECBCD`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P04993|protein.P04993]], [[protein.P07648|protein.P07648]], [[protein.P08394|protein.P08394]]

## Enriched Summary

RecB, RecC, and RecD make up an ATP-dependent helicase/nuclease complex that promotes homologous recombination in the repair of double-strand DNA breaks and during bacterial conjugation; RecBCD's DNA-degradative properties also serve to protect E. coli from phages (reviewed in ). RecBCD function is central to the accurate completion of DNA replication (and see ). Early studies identified recB and recC mutations which have reduced efficiency for genetic recombination and increased sensitivity to DNA damaging agents that cause double-strand breaks (DSBs); the products of these loci were associated with various ATP-dependent deoxyribonuclease and helicase activities . The enzyme was named Exonuclease V; later work showed that it contained three subunits - RecB, RecC and RecD . RecBCD is a rapid, highly processive DNA helicase which in vitro can unwind DNA at a rate of nearly 1,000 bp/sec (see also ). The unwinding rate of DNA by individual RecBCD molecules is heterogeneous . RecBCD is a bipolar DNA helicase with two ssDNA translocating motors: RecB with a 3' → 5' directed motion and RecD with a 5' → 3' directed motion; RecBCD can initiate unwinding from blunt DNA ends . RecBC has both 3' → 5' and 5' → 3' ssDNA translocase activity . RecBCD is a potent nuclease; the C-terminal domain of RecB is responsible for the nuclease activities associated with RecBCD...

## Biological Role

Catalyzes RXN-19004 (reaction.ecocyc.RXN-19004), RXN0-2605 (reaction.ecocyc.RXN0-2605).

## Annotation

RecB, RecC, and RecD make up an ATP-dependent helicase/nuclease complex that promotes homologous recombination in the repair of double-strand DNA breaks and during bacterial conjugation; RecBCD's DNA-degradative properties also serve to protect E. coli from phages (reviewed in ). RecBCD function is central to the accurate completion of DNA replication (and see ). Early studies identified recB and recC mutations which have reduced efficiency for genetic recombination and increased sensitivity to DNA damaging agents that cause double-strand breaks (DSBs); the products of these loci were associated with various ATP-dependent deoxyribonuclease and helicase activities . The enzyme was named Exonuclease V; later work showed that it contained three subunits - RecB, RecC and RecD . RecBCD is a rapid, highly processive DNA helicase which in vitro can unwind DNA at a rate of nearly 1,000 bp/sec (see also ). The unwinding rate of DNA by individual RecBCD molecules is heterogeneous . RecBCD is a bipolar DNA helicase with two ssDNA translocating motors: RecB with a 3' → 5' directed motion and RecD with a 5' → 3' directed motion; RecBCD can initiate unwinding from blunt DNA ends . RecBC has both 3' → 5' and 5' → 3' ssDNA translocase activity . RecBCD is a potent nuclease; the C-terminal domain of RecB is responsible for the nuclease activities associated with RecBCD . The activity of RecBCD is regulated by interaction with a specific cis-acting DNA sequence (5' GCTGGTGG 3') called 'Chi" for cross-over hotspot instigator . The effect of Chi on RecBCD activity in vitro is dependent on reaction conditions, and more specifically, on the ratio of Mg2+ to ATP . Interaction with Chi causes RecBC(D) to nick the Chi-containing strand 3' to the Chi site DNA . Interaction with Chi causes RecBCD

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-19004|reaction.ecocyc.RXN-19004]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2605|reaction.ecocyc.RXN0-2605]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P04993|protein.P04993]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P07648|protein.P07648]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P08394|protein.P08394]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:RECBCD`
- `PDB:1W36`
- `PDB:3K70`
- `PDB:5LD2`
- `PDB:5MBV`
- `PDB:6T2V`
- `PDB:6T2U`
- `PDB:6SJG`
- `PDB:6SJF`
- `QSPROTEOME:QS00185231`

## Notes

1*protein.P04993|1*protein.P07648|1*protein.P08394

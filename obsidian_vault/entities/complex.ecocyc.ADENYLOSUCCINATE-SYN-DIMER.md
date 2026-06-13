---
entity_id: "complex.ecocyc.ADENYLOSUCCINATE-SYN-DIMER"
entity_type: "complex"
name: "adenylosuccinate synthetase"
source_database: "EcoCyc"
source_id: "ADENYLOSUCCINATE-SYN-DIMER"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# adenylosuccinate synthetase

`complex.ecocyc.ADENYLOSUCCINATE-SYN-DIMER`

## Static

- Type: `complex`
- Source: `EcoCyc:ADENYLOSUCCINATE-SYN-DIMER`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A7D4|protein.P0A7D4]]

## Enriched Summary

Adenylosuccinate synthetase catalyzes the first committed step toward the de novo synthesis of AMP. The alarmone ppGpp is a regulator of adenylosuccinate synthetase . The cyclic nucleotide guanosine 5'-diphosphate 2':3'-cyclic monophosphate binds more tightly to the active site than ppGpp . Extensive kinetic studies of wild-type and mutant enzymes have defined the substrate binding sites and residues involved in catalysis. This work is reviewed in . The Asp333 residue appears to be the determinant for GTP specificity . Intersubunit complementation experiments suggested that the enzyme contains two shared active sites at the dimer interface. The Kd for dimer dissociation is 1 µM, and the presence of IMP stabilizes the dimeric form . The interaction of IMP with the enzyme drives the conformational transition of the active site . Crystal structures of the enzyme have been determined , and a catalytic mechanism has been proposed based on these studies. purA is essential for growth on glycerol minimal medium . PurA Function required for ATP sufficiency. Deletion of purA or purB was shown to result in a decrease in acid resistance, apparently due to the effects of decreased ATP biosynthesis on processes that require ATP for survival under acidic conditions . Enhanced transcription of purA in response to an adenylate drain...

## Biological Role

Catalyzes ADENYLOSUCCINATE-SYNTHASE-RXN (reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Adenylosuccinate synthetase catalyzes the first committed step toward the de novo synthesis of AMP. The alarmone ppGpp is a regulator of adenylosuccinate synthetase . The cyclic nucleotide guanosine 5'-diphosphate 2':3'-cyclic monophosphate binds more tightly to the active site than ppGpp . Extensive kinetic studies of wild-type and mutant enzymes have defined the substrate binding sites and residues involved in catalysis. This work is reviewed in . The Asp333 residue appears to be the determinant for GTP specificity . Intersubunit complementation experiments suggested that the enzyme contains two shared active sites at the dimer interface. The Kd for dimer dissociation is 1 µM, and the presence of IMP stabilizes the dimeric form . The interaction of IMP with the enzyme drives the conformational transition of the active site . Crystal structures of the enzyme have been determined , and a catalytic mechanism has been proposed based on these studies. purA is essential for growth on glycerol minimal medium . PurA Function required for ATP sufficiency. Deletion of purA or purB was shown to result in a decrease in acid resistance, apparently due to the effects of decreased ATP biosynthesis on processes that require ATP for survival under acidic conditions . Enhanced transcription of purA in response to an adenylate drain. Interaction between the purA and histidine biosynthesis has been demonstrated in E. coli and Salmonella . It is related to the consumption of adenylate during histidine biosynthesis with the release of the byproduct AICAR subsequently in the histidine pathway; AICAR is a later intermediate (but 2 reactions removed) in the biosynthesis of the purine nucleotide biosynthesis branch point compound IMP. When this histidine synthetic pathway is constricted at the

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN|reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7D4|protein.P0A7D4]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ADENYLOSUCCINATE-SYN-DIMER`
- `QSPROTEOME:QS00167603`

## Notes

2*protein.P0A7D4

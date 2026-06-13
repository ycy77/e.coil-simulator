---
entity_id: "complex.ecocyc.E3-CPLX"
entity_type: "complex"
name: "lipoamide dehydrogenase"
source_database: "EcoCyc"
source_id: "E3-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# lipoamide dehydrogenase

`complex.ecocyc.E3-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:E3-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9P0|protein.P0A9P0]]

## Enriched Summary

Lipoamide dehydrogenase is the E3 component of three multicomponent enzyme complexes: PYRUVATEDEH-CPLX, 2OXOGLUTARATEDEH-CPLX, and the GCVMULTI-CPLX . It catalyzes the transfer of electrons to the ultimate acceptor, NAD. Kinetics of the reaction have been studied and suggest a modified ping-pong mechanism . Site-directed mutagenesis was used to identify and characterize the redox-active disulfide and a charged residue influencing the redox potential of the FAD cofactor . The insertion of the FAD cofactor is essential for dimerization and full activity . An lpd null mutant produces more pyruvate and L-glutamate under aerobic conditions. Metabolic flux analysis shows that the ENTNER-DOUDOROFF-PWY and the glyoxylate shunt are activated . Another dihydrolipoate dehydrogenase activity has been detected in E. coli lpd mutants; thus, an isozyme may exist . A mutation in the lpd gene in E. coli causes the pyruvate dehydrogenase complex to be less sensitive to NADH inhibition and active during anaerobic growth . Amino acid substitutions at Glu354 that lowered the sensitivity of the enzyme to NADH inhibition were proposed to act by restricting the movement of NADH . Suppressor mutations in lpd have been shown to restore growth to a redox-defective mutant that lacks both the thioredoxin and glutathione/glutaredoxin reduction pathways...

## Biological Role

Catalyzes 1.8.1.4-RXN (reaction.ecocyc.1.8.1.4-RXN), RXN-15119 (reaction.ecocyc.RXN-15119), RXN-7716 (reaction.ecocyc.RXN-7716), RXN-8629 (reaction.ecocyc.RXN-8629), RXN0-1132 (reaction.ecocyc.RXN0-1132). Component of 2-oxoglutarate dehydrogenase complex (complex.ecocyc.2OXOGLUTARATEDEH-CPLX), glycine cleavage system (complex.ecocyc.GCVMULTI-CPLX), pyruvate dehydrogenase (complex.ecocyc.PYRUVATEDEH-CPLX). Bound by FAD (molecule.C00016).

## Annotation

Lipoamide dehydrogenase is the E3 component of three multicomponent enzyme complexes: PYRUVATEDEH-CPLX, 2OXOGLUTARATEDEH-CPLX, and the GCVMULTI-CPLX . It catalyzes the transfer of electrons to the ultimate acceptor, NAD. Kinetics of the reaction have been studied and suggest a modified ping-pong mechanism . Site-directed mutagenesis was used to identify and characterize the redox-active disulfide and a charged residue influencing the redox potential of the FAD cofactor . The insertion of the FAD cofactor is essential for dimerization and full activity . An lpd null mutant produces more pyruvate and L-glutamate under aerobic conditions. Metabolic flux analysis shows that the ENTNER-DOUDOROFF-PWY and the glyoxylate shunt are activated . Another dihydrolipoate dehydrogenase activity has been detected in E. coli lpd mutants; thus, an isozyme may exist . A mutation in the lpd gene in E. coli causes the pyruvate dehydrogenase complex to be less sensitive to NADH inhibition and active during anaerobic growth . Amino acid substitutions at Glu354 that lowered the sensitivity of the enzyme to NADH inhibition were proposed to act by restricting the movement of NADH . Suppressor mutations in lpd have been shown to restore growth to a redox-defective mutant that lacks both the thioredoxin and glutathione/glutaredoxin reduction pathways. The suppressor mutations reduced Lpd activity resulting in dihydrolipoamide accumulation, which could then serve as an electron donor via reduction of glutaredoxins. The reoxidation of Lpd restored TCA cycle function . Lipoamide dehydrogenase exhibits low, but measurable tellurite reductase activity . lpd shows differential codon adaptation, resulting in differential translation efficiency signatures, in aerotolerant compared to obligate anaerobic mi

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.1.8.1.4-RXN|reaction.ecocyc.1.8.1.4-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15119|reaction.ecocyc.RXN-15119]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-7716|reaction.ecocyc.RXN-7716]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8629|reaction.ecocyc.RXN-8629]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1132|reaction.ecocyc.RXN0-1132]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.2OXOGLUTARATEDEH-CPLX|complex.ecocyc.2OXOGLUTARATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.GCVMULTI-CPLX|complex.ecocyc.GCVMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.PYRUVATEDEH-CPLX|complex.ecocyc.PYRUVATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9P0|protein.P0A9P0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:E3-CPLX`
- `QSPROTEOME:QS00161937`

## Notes

2*protein.P0A9P0

---
entity_id: "complex.ecocyc.MONOMER0-46"
entity_type: "complex"
name: "NhaR-Na+ DNA-binding transcriptional activator"
source_database: "EcoCyc"
source_id: "MONOMER0-46"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "YaaB"
  - "AntO"
  - "B0020"
  - "NhaR"
  - "NhaR-Na<SUP>+</SUP>"
---

# NhaR-Na+ DNA-binding transcriptional activator

`complex.ecocyc.MONOMER0-46`

## Static

- Type: `complex`
- Source: `EcoCyc:MONOMER0-46`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9G2|protein.P0A9G2]], [[molecule.C01330|molecule.C01330]]

## Enriched Summary

The transcription factor NhaR, for "Na+/H+ antiporter Regulator," is dependent on Na+ and controls the transcription of genes involved in adaptation to Na+ and alkaline pH , biofilm formation , and response to adverse conditions , like salt stress . At 20°C and in the absence of the protein EG11837-MONOMER BipA, NhaR regulates genes involved in ribosome biogenesis, capsule production, lipopolysaccharide synthesis, and motility . This regulator belongs to the LysR family. NhaR is composed of two domains: the amino-terminal domain, which contains the DNA-binding region, and the carboxy-terminal domain, which is possibly responsible for inducer binding . In systematic studies of oligomerization, it was shown that some members of the LysR family, like NhaR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The binding targets for NhaR are 17 nucleotides long. Each dimer binds to one of these conserved sequences. The lengths of the degenerate binding sites of NhaR were defined according to the matrix shown for this regulator in the database RegPrecise, which contains matrices generated from alignments of orthologous regions . The deletion of nhaR increased the viability of Escherichia coli in soil (~10-fold at 42 days)...

## Annotation

The transcription factor NhaR, for "Na+/H+ antiporter Regulator," is dependent on Na+ and controls the transcription of genes involved in adaptation to Na+ and alkaline pH , biofilm formation , and response to adverse conditions , like salt stress . At 20°C and in the absence of the protein EG11837-MONOMER BipA, NhaR regulates genes involved in ribosome biogenesis, capsule production, lipopolysaccharide synthesis, and motility . This regulator belongs to the LysR family. NhaR is composed of two domains: the amino-terminal domain, which contains the DNA-binding region, and the carboxy-terminal domain, which is possibly responsible for inducer binding . In systematic studies of oligomerization, it was shown that some members of the LysR family, like NhaR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The binding targets for NhaR are 17 nucleotides long. Each dimer binds to one of these conserved sequences. The lengths of the degenerate binding sites of NhaR were defined according to the matrix shown for this regulator in the database RegPrecise, which contains matrices generated from alignments of orthologous regions . The deletion of nhaR increased the viability of Escherichia coli in soil (~10-fold at 42 days) . This indicates that NhaR may induce unnecessary or costly stress responses in the context of soil, negatively affecting energy efficiency or growth in this environment. The NhaR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding ener

## Outgoing Edges (2)

- `represses` --> [[gene.b0953|gene.b0953]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3995|gene.b3995]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (2)

- `is_component_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A9G2|protein.P0A9G2]] `EcoCyc` `database` - EcoCyc component coefficient=

## External IDs

- `EcoCyc:MONOMER0-46`

## Notes

protein.P0A9G2|molecule.C01330

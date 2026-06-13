---
entity_id: "complex.ecocyc.GLUTATHIONE-SYN-CPLX"
entity_type: "complex"
name: "glutathione synthetase"
source_database: "EcoCyc"
source_id: "GLUTATHIONE-SYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutathione synthetase

`complex.ecocyc.GLUTATHIONE-SYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTATHIONE-SYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P04425|protein.P04425]]

## Enriched Summary

Glutathione synthetase catalyzes the second, final step in the pathway for the biosynthesis of GLUTATHIONE, also referred to as GSH for its γ-Glu-Cys-Gly tripeptide structure . Crystal structures of the enzyme have been solved . Site-directed mutagenesis identified the R233 residue and the importance of flexibility of the I226-G242 loop for catalytic activity. The loop is thought to enhance the recognition of glycine and stabilize the reaction intermediate . In the crystal structure of the quarternary complex with ADP, glutathione and sulfate, the flexible loops are fixed, allowing better understanding of the active site and the mechanism of substrate recognition . Further site-directed mutagenesis was used to probe the γ-glutamyl cysteine binding site . A strain overexpressing GshA and GshB is more resistant to radiation than wild type . In cells lacking metal efflux systems, glutathione biosynthesis is required for resistance to Cd2+, Zn2+ and Cu2+ . A gshB trxB double mutant exhibits a growth defect which can be suppressed by growth in rich medium containing DTT or by gain-of-function mutations in ahpC . Transcription of gshB increases with increased cadmium concentration. A microarray analysis measuring the transcriptional response of wild-type and gshB mutant strains to cadmium stress has been performed . Persistant, sublethally injured E...

## Biological Role

Catalyzes GLUTATHIONE-SYN-RXN (reaction.ecocyc.GLUTATHIONE-SYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Glutathione synthetase catalyzes the second, final step in the pathway for the biosynthesis of GLUTATHIONE, also referred to as GSH for its γ-Glu-Cys-Gly tripeptide structure . Crystal structures of the enzyme have been solved . Site-directed mutagenesis identified the R233 residue and the importance of flexibility of the I226-G242 loop for catalytic activity. The loop is thought to enhance the recognition of glycine and stabilize the reaction intermediate . In the crystal structure of the quarternary complex with ADP, glutathione and sulfate, the flexible loops are fixed, allowing better understanding of the active site and the mechanism of substrate recognition . Further site-directed mutagenesis was used to probe the γ-glutamyl cysteine binding site . A strain overexpressing GshA and GshB is more resistant to radiation than wild type . In cells lacking metal efflux systems, glutathione biosynthesis is required for resistance to Cd2+, Zn2+ and Cu2+ . A gshB trxB double mutant exhibits a growth defect which can be suppressed by growth in rich medium containing DTT or by gain-of-function mutations in ahpC . Transcription of gshB increases with increased cadmium concentration. A microarray analysis measuring the transcriptional response of wild-type and gshB mutant strains to cadmium stress has been performed . Persistant, sublethally injured E. coli induced by lactic acid stress exhibited slower resuscitation rates in ΔsodB, ΔgshA and ΔgshB mutants, and even more slowly in a ΔsodA mutant, relative to wild-type . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTATHIONE-SYN-RXN|reaction.ecocyc.GLUTATHIONE-SYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P04425|protein.P04425]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GLUTATHIONE-SYN-CPLX`
- `QSPROTEOME:QS00181727`

## Notes

4*protein.P04425

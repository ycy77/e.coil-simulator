---
entity_id: "complex.ecocyc.CPLX0-10342"
entity_type: "complex"
name: "Hda-β-clamp complex"
source_database: "EcoCyc"
source_id: "CPLX0-10342"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Hda-β-clamp complex

`complex.ecocyc.CPLX0-10342`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-10342`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69931|protein.P69931]], [[complex.ecocyc.CPLX0-3761|complex.ecocyc.CPLX0-3761]]

## Enriched Summary

G7313-MONOMER Hda has been shown to interact with the β subunit of DNA polymerase III (known as the CPLX0-3761) in vitro; the interaction is mediated by a hexapeptide sequence located in the amino terminus of Hda . Apo-Hda is homodimeric in solution ; however, the active protein is monomeric and bound to ADP . Two molecules of Hda associate with a β-clamp dimer . The Arg168 residue within the AAA+ Box VII motif is involved in DnaA-ATP hydrolysis . The complex inhibits the reinitiation of DNA replication in a process termed RIDA (regulatory inactivation of DnaA) . Hda and the sliding clamp stimulate ATP hydrolysis within the MONOMER0-160 DnaA-ATP complex, which renders it inactive for the initiation of DNA replication . The RIDA mechanism was reported to be the most important factor that controls the replication initiation frequency, which maintains the chromosome-to-cell size ratio within a narrow range . G7313-MONOMER Hda has been shown to interact with the β subunit of DNA polymerase III (known as the CPLX0-3761) in vitro; the interaction is mediated by a hexapeptide sequence located in the amino terminus of Hda . Apo-Hda is homodimeric in solution ; however, the active protein is monomeric and bound to ADP . Two molecules of Hda associate with a β-clamp dimer . The Arg168 residue within the AAA+ Box VII motif is involved in DnaA-ATP hydrolysis...

## Biological Role

Catalyzes RXN0-7444 (reaction.ecocyc.RXN0-7444).

## Annotation

G7313-MONOMER Hda has been shown to interact with the β subunit of DNA polymerase III (known as the CPLX0-3761) in vitro; the interaction is mediated by a hexapeptide sequence located in the amino terminus of Hda . Apo-Hda is homodimeric in solution ; however, the active protein is monomeric and bound to ADP . Two molecules of Hda associate with a β-clamp dimer . The Arg168 residue within the AAA+ Box VII motif is involved in DnaA-ATP hydrolysis . The complex inhibits the reinitiation of DNA replication in a process termed RIDA (regulatory inactivation of DnaA) . Hda and the sliding clamp stimulate ATP hydrolysis within the MONOMER0-160 DnaA-ATP complex, which renders it inactive for the initiation of DNA replication . The RIDA mechanism was reported to be the most important factor that controls the replication initiation frequency, which maintains the chromosome-to-cell size ratio within a narrow range .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7444|reaction.ecocyc.RXN0-7444]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-3761|complex.ecocyc.CPLX0-3761]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A988|protein.P0A988]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P69931|protein.P69931]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-10342`

## Notes

2*protein.P69931|1*complex.ecocyc.CPLX0-3761

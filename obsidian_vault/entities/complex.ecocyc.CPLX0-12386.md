---
entity_id: "complex.ecocyc.CPLX0-12386"
entity_type: "complex"
name: "malonyl-ACP decarboxylase"
source_database: "EcoCyc"
source_id: "CPLX0-12386"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# malonyl-ACP decarboxylase

`complex.ecocyc.CPLX0-12386`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-12386`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ADQ2|protein.P0ADQ2]]

## Enriched Summary

This gene encodes a malonyl-ACP decarboxylase (renamed MadA) that enables FabH-independent fatty acid synthesis initiation . FabY consists of an N-terminal acetyltransferase domain and a C-terminal thioesterase domain. Based on genetic interactions with fabH, it is therefore possible that FabY has an enzymatic activity that contributes to the initiation of fatty acid biosynthesis . Further structural characterization studies verified the two distinct domains; the N-terminal domain (MadAN) belongs to the Acetyltransf_1 protein family and the C-terminal domain (MadAC) belongs to the thioesterase hot dog superfamily. MadA forms a dimer with the two domains folding independently and not interacting; the C-domain has two ACP-binding sites and is necessary and sufficient for enzymatic activity . A ΔfabH ΔfabY double mutant shows synthetic lethality. Overexpression of FabY rescues the growth defect of a ppGpp0 ΔfabH mutant and largely alleviates the altered fatty acid composition of a fabH mutant . Overexpression of FabY from a plasmid increases resistance to xanthorrhizol . MadA and MadAC can complement a ΔfabH mutant strain, restoring cell size and growth rates to wild-type levels . Transcription of fabY appears to be regulated by (p)ppGpp and DksA...

## Biological Role

Catalyzes MALONYL-ACPDECARBOX-RXN (reaction.ecocyc.MALONYL-ACPDECARBOX-RXN).

## Annotation

This gene encodes a malonyl-ACP decarboxylase (renamed MadA) that enables FabH-independent fatty acid synthesis initiation . FabY consists of an N-terminal acetyltransferase domain and a C-terminal thioesterase domain. Based on genetic interactions with fabH, it is therefore possible that FabY has an enzymatic activity that contributes to the initiation of fatty acid biosynthesis . Further structural characterization studies verified the two distinct domains; the N-terminal domain (MadAN) belongs to the Acetyltransf_1 protein family and the C-terminal domain (MadAC) belongs to the thioesterase hot dog superfamily. MadA forms a dimer with the two domains folding independently and not interacting; the C-domain has two ACP-binding sites and is necessary and sufficient for enzymatic activity . A ΔfabH ΔfabY double mutant shows synthetic lethality. Overexpression of FabY rescues the growth defect of a ppGpp0 ΔfabH mutant and largely alleviates the altered fatty acid composition of a fabH mutant . Overexpression of FabY from a plasmid increases resistance to xanthorrhizol . MadA and MadAC can complement a ΔfabH mutant strain, restoring cell size and growth rates to wild-type levels . Transcription of fabY appears to be regulated by (p)ppGpp and DksA . This enzyme was found to interact with the GAPDH-A-MONOMER enzyme in glycolysis in a large assessment of protein-protein interactions (PPIs) . FabY: "fatty acid biosynthesis Y"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.MALONYL-ACPDECARBOX-RXN|reaction.ecocyc.MALONYL-ACPDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ADQ2|protein.P0ADQ2]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-12386`
- `QSPROTEOME:QS00199561`

## Notes

2*protein.P0ADQ2

---
entity_id: "complex.ecocyc.CPLX0-7754"
entity_type: "complex"
name: "DNA-binding transcriptional activator UhpA-phosphorylated"
source_database: "EcoCyc"
source_id: "CPLX0-7754"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "UhpA response regulator - phosphorylated"
  - "UhpA-P<sup>asp54</sup>"
---

# DNA-binding transcriptional activator UhpA-phosphorylated

`complex.ecocyc.CPLX0-7754`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7754`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `regulatory`
- Components: [[protein.P0AGA6|protein.P0AGA6]]

## Enriched Summary

The regulatory protein for "uptake of hexose phosphates," UhpA , activates the transcription of a gene that codes for UhpT, a protein that transports many phosphorylated sugars into the cell . Inhibition of uhpA expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic pyocyanin . UhpA is the response regulator in the unusual two-component regulatory system comprised of three proteins, UhpA/UhpB/UhpC, and is a member of the NarL subfamily of response regulators. The signal that triggers this signaling pathway is glucose 6-phosphate external. This sugar is sensed by UhpC, which interacts with UhpB to stimulate its autophosphorylation. Then, phosphorylated UhpB transfers the phosphate group to UhpA in Asp-54 to activate it . UhpB unphosphorylated is able to dephosphorylate to UhpA . UhpA has two modules: the receiver module, which contains the putative site of phosphorylation in the N-terminal domain , and the activation module, which contains a helix-turn-helix motif for DNA binding in the C-terminal domain. UhpA shows 30% identity with DctD . The RNA polymerase RpoA and RpoD subunits are necessary for the transcriptional activation by UhpA , which induces open complex formation, but the stabilization of this complex is CRP dependent . These two regulatory proteins appear to stimulate the DNA binding of each other to the uhpT promoter...

## Annotation

The regulatory protein for "uptake of hexose phosphates," UhpA , activates the transcription of a gene that codes for UhpT, a protein that transports many phosphorylated sugars into the cell . Inhibition of uhpA expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic pyocyanin . UhpA is the response regulator in the unusual two-component regulatory system comprised of three proteins, UhpA/UhpB/UhpC, and is a member of the NarL subfamily of response regulators. The signal that triggers this signaling pathway is glucose 6-phosphate external. This sugar is sensed by UhpC, which interacts with UhpB to stimulate its autophosphorylation. Then, phosphorylated UhpB transfers the phosphate group to UhpA in Asp-54 to activate it . UhpB unphosphorylated is able to dephosphorylate to UhpA . UhpA has two modules: the receiver module, which contains the putative site of phosphorylation in the N-terminal domain , and the activation module, which contains a helix-turn-helix motif for DNA binding in the C-terminal domain. UhpA shows 30% identity with DctD . The RNA polymerase RpoA and RpoD subunits are necessary for the transcriptional activation by UhpA , which induces open complex formation, but the stabilization of this complex is CRP dependent . These two regulatory proteins appear to stimulate the DNA binding of each other to the uhpT promoter . Two UhpA dimers bind to two sites with different affinities upstream of uhpT. The weak site is essential for activation, and its occupancy is dependent on the occupancy of the strong site. This site contains inverted repeats with the consensus CCTGA/GA/G separated by 6 bp . The uhpT, uhpC, uhpB, and uhpA genes are located in tandem in the same locus in the genome, and while uhpT is transcribed alone , it has been

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AGA6|protein.P0AGA6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7754`
- `QSPROTEOME:QS00049656`

## Notes

2*protein.P0AGA6

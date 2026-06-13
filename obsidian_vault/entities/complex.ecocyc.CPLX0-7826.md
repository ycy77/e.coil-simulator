---
entity_id: "complex.ecocyc.CPLX0-7826"
entity_type: "complex"
name: "dITP/XTP pyrophosphatase"
source_database: "EcoCyc"
source_id: "CPLX0-7826"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dITP/XTP pyrophosphatase

`complex.ecocyc.CPLX0-7826`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7826`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P52061|protein.P52061]]

## Enriched Summary

RdgB is a nucleoside triphosphate pyrophosphatase which hydrolyses deoxyinosine triphosphate (dITP) and xanthosine triphosphate (XTP), mutagenic products of purine nucleotide deamination. RdgB may therefore act to reduce the abundance of noncanonical purines that can be misincorporated during DNA replication, serving as quality control in the metabolism of DNA precursors . A suppressor screen identified inosine as the main source of noncanonical nucleotides that are removed by RdgB . RdgB does not exhibit strong activity towards dATP, dCTP, or dTTP; the range of hydrolyzed substrates suggests that the O6 atom of the nucleotide substrate is critical for RdgB activity . Crystal structures of free RdgB and in complexes with the ITP substrate or IMP product have been solved. Substrate binding induces closure of the active site and positioning of conserved amino acid residues for catalysis. Site-directed mutagenesis allowed identification of residues that are essential for catalytic activity, and a mechanism for catalysis and substrate specificity was proposed . rdgB was first identified due to its genetic interaction with the recA200 allele . The major consequence of loss of rdgB appears to be chromosomal fragmentation . An rdgB mutation leads to increased intrachromosomal recombination, compared to wild type, and causes SOS induction...

## Biological Role

Catalyzes RXN0-1602 (reaction.ecocyc.RXN0-1602), RXN0-1603 (reaction.ecocyc.RXN0-1603), RXN0-6382 (reaction.ecocyc.RXN0-6382). Bound by Magnesium cation (molecule.C00305).

## Annotation

RdgB is a nucleoside triphosphate pyrophosphatase which hydrolyses deoxyinosine triphosphate (dITP) and xanthosine triphosphate (XTP), mutagenic products of purine nucleotide deamination. RdgB may therefore act to reduce the abundance of noncanonical purines that can be misincorporated during DNA replication, serving as quality control in the metabolism of DNA precursors . A suppressor screen identified inosine as the main source of noncanonical nucleotides that are removed by RdgB . RdgB does not exhibit strong activity towards dATP, dCTP, or dTTP; the range of hydrolyzed substrates suggests that the O6 atom of the nucleotide substrate is critical for RdgB activity . Crystal structures of free RdgB and in complexes with the ITP substrate or IMP product have been solved. Substrate binding induces closure of the active site and positioning of conserved amino acid residues for catalysis. Site-directed mutagenesis allowed identification of residues that are essential for catalytic activity, and a mechanism for catalysis and substrate specificity was proposed . rdgB was first identified due to its genetic interaction with the recA200 allele . The major consequence of loss of rdgB appears to be chromosomal fragmentation . An rdgB mutation leads to increased intrachromosomal recombination, compared to wild type, and causes SOS induction . Both phenotypes are suppressed by purA expression . A recA200 rdgB double mutant is inviable at elevated temperatures that are nonpermissive for the recA200 allele; under nonpermissive conditions the double mutant exhibits DNA degradation and a defect in DNA replication, but no defect in protein translation . A moa rdgB double mutant exhibits hypersensitivity to N-6-hydroxylaminopurine (HAP) that is suppressed by an nfi (endonuclease V) muta

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1602|reaction.ecocyc.RXN0-1602]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1603|reaction.ecocyc.RXN0-1603]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6382|reaction.ecocyc.RXN0-6382]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P52061|protein.P52061]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7826`
- `QSPROTEOME:QS00183037`

## Notes

2*protein.P52061

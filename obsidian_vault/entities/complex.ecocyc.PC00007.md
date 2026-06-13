---
entity_id: "complex.ecocyc.PC00007"
entity_type: "complex"
name: "DNA-binding transcriptional repressor TrpR"
source_database: "EcoCyc"
source_id: "PC00007"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "TrpR"
---

# DNA-binding transcriptional repressor TrpR

`complex.ecocyc.PC00007`

## Static

- Type: `complex`
- Source: `EcoCyc:PC00007`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A881|protein.P0A881]]

## Enriched Summary

TrpR, "tryptophan (trp) transcriptional repressor," negatively regulates expression of the trp regulon in response to intracellular levels of tryptophan . The TrpR regulon is involved in tryptophan biosynthesis, transport, and regulation. This regulon partially overlaps with the TyrR regulon, since expression of several genes is regulated by TrpR and TyrR, the transcriptional regulator of the TyrR regulon . TrpR represses transcription by interfering with the ability of RNA polymerase to interact with the promoter . The aporepressor is activated as a DNA-binding protein by noncooperative binding of two L-tryptophan molecules to the homodimer . The consensus sequence for TrpR is described as two symmetrically arranged half-sites with the sequence GNACT separated by a spacer of 8 bp . Nonspecific sequences appear to assist TrpR binding to the specific site, because it was observed, by footprinting assay, that the affinity of the specific site increased when the length of sequence used in the experiment was longer . X-ray crystallography of the aporepressor , the holorepressor , and repressor bound to the operator oligonucleotide as well as NMR studies of the repressor and aporepressor in solution and bound to an operator oligonucleotide reveal that the small 25-kDa protein belongs to the helix-turn-helix (HTH) family...

## Biological Role

Component of DNA-binding transcriptional repressor TrpR-L-tryptophan (complex.ecocyc.CPLX-125).

## Annotation

TrpR, "tryptophan (trp) transcriptional repressor," negatively regulates expression of the trp regulon in response to intracellular levels of tryptophan . The TrpR regulon is involved in tryptophan biosynthesis, transport, and regulation. This regulon partially overlaps with the TyrR regulon, since expression of several genes is regulated by TrpR and TyrR, the transcriptional regulator of the TyrR regulon . TrpR represses transcription by interfering with the ability of RNA polymerase to interact with the promoter . The aporepressor is activated as a DNA-binding protein by noncooperative binding of two L-tryptophan molecules to the homodimer . The consensus sequence for TrpR is described as two symmetrically arranged half-sites with the sequence GNACT separated by a spacer of 8 bp . Nonspecific sequences appear to assist TrpR binding to the specific site, because it was observed, by footprinting assay, that the affinity of the specific site increased when the length of sequence used in the experiment was longer . X-ray crystallography of the aporepressor , the holorepressor , and repressor bound to the operator oligonucleotide as well as NMR studies of the repressor and aporepressor in solution and bound to an operator oligonucleotide reveal that the small 25-kDa protein belongs to the helix-turn-helix (HTH) family. The dimer is composed of two identical six-helical subunits, where four of the helices intertwine with the corresponding helices from the other subunit. Binding of tryptophan stabilizes the HTH and alters the orientation of the HTH such that the repressor fits into the major grooves . The crystal structure of the repressor-operator complex reveals that specific binding is mostly mediated by contacts to the phosphate backbone and water-mediated hydrogen bonds

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-125|complex.ecocyc.CPLX-125]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A881|protein.P0A881]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PC00007`
- `QSPROTEOME:QS00200429`

## Notes

2*protein.P0A881

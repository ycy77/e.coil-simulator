---
entity_id: "complex.ecocyc.CPLX0-3281"
entity_type: "complex"
name: "RNase III"
source_database: "EcoCyc"
source_id: "CPLX0-3281"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ribonuclease III"
  - "ribonuclease 3"
---

# RNase III

`complex.ecocyc.CPLX0-3281`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3281`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A7Y0|protein.P0A7Y0]]

## Enriched Summary

RNase III (ribonuclease III) is an endonuclease that cleaves double-stranded RNA (dsRNA) to yield 5'-phosphates and 3'-hydroxyls . It is required for processing of ribosomal RNA (rRNA), some tRNA precursors and phage mRNA, for the regulation of a number of genes and for proper function of regulatory antisense RNAs, usually cleaving dsRNA created by the formation of stem structures within single-stranded RNA. RNase III is a key enzyme in rRNA processing, cleaving 30S precursor rRNA to yield 23S, 17S and 5S rRNA, though it has been suggested based on degradation experiments that the 30S RNA is not actually a precursor to these rRNAs . The 23S rRNA sequence is flanked by RNase III cleavage sites and is cleaved at multiple points at its 5' end and one at its 3' end . Some of the 5' cleavage of 23S rRNA occurs even in the absence of RNase III . Regions flanking the 16S rRNA are predicted to form a 26-bp double helical stem at the base of a loop containing the 16S rRNA. RNase III cleaves at both sites that combine to form the stem . Electron microscopy confirms that both the 16S and 23S rRNA sequences form loops with stems made from flanking regions that coincide with RNase III cleavage sites . 5S rRNA is separated from the 30S precursor as a 7S fragment, which is then cleaved at its 3' end by RNase III and finally by RNase E to yield the final 5S rRNA...

## Biological Role

Catalyzes 3.1.26.3-RXN (reaction.ecocyc.3.1.26.3-RXN), endoribonuclease (reaction.ecocyc.RXN0-6478), RXN0-7461 (reaction.ecocyc.RXN0-7461), RXN0-7476 (reaction.ecocyc.RXN0-7476). Bound by Magnesium cation (molecule.C00305).

## Annotation

RNase III (ribonuclease III) is an endonuclease that cleaves double-stranded RNA (dsRNA) to yield 5'-phosphates and 3'-hydroxyls . It is required for processing of ribosomal RNA (rRNA), some tRNA precursors and phage mRNA, for the regulation of a number of genes and for proper function of regulatory antisense RNAs, usually cleaving dsRNA created by the formation of stem structures within single-stranded RNA. RNase III is a key enzyme in rRNA processing, cleaving 30S precursor rRNA to yield 23S, 17S and 5S rRNA, though it has been suggested based on degradation experiments that the 30S RNA is not actually a precursor to these rRNAs . The 23S rRNA sequence is flanked by RNase III cleavage sites and is cleaved at multiple points at its 5' end and one at its 3' end . Some of the 5' cleavage of 23S rRNA occurs even in the absence of RNase III . Regions flanking the 16S rRNA are predicted to form a 26-bp double helical stem at the base of a loop containing the 16S rRNA. RNase III cleaves at both sites that combine to form the stem . Electron microscopy confirms that both the 16S and 23S rRNA sequences form loops with stems made from flanking regions that coincide with RNase III cleavage sites . 5S rRNA is separated from the 30S precursor as a 7S fragment, which is then cleaved at its 3' end by RNase III and finally by RNase E to yield the final 5S rRNA . In the absence of RNase III activity, mature 16S rRNA can still be found, but no mature 23S rRNA is detectable and unprocessed 23S rRNA with extraneous sequence is incorporated in 50S ribosomes . This unprocessed 30S rRNA can contribute elements to multiple ribosomes, resulting in pairs or occasionally trios of 50S ribosomes linked together by unprocessed rRNA . tRNA processing starting with cleavage by RNase III rather than

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.3.1.26.3-RXN|reaction.ecocyc.3.1.26.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6478|reaction.ecocyc.RXN0-6478]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7461|reaction.ecocyc.RXN0-7461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7476|reaction.ecocyc.RXN0-7476]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7Y0|protein.P0A7Y0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3281`
- `QSPROTEOME:QS00049523`

## Notes

2*protein.P0A7Y0

---
entity_id: "complex.ecocyc.GDPMANDEHYDRA-CPLX"
entity_type: "complex"
name: "GDP-mannose 4,6-dehydratase"
source_database: "EcoCyc"
source_id: "GDPMANDEHYDRA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# GDP-mannose 4,6-dehydratase

`complex.ecocyc.GDPMANDEHYDRA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GDPMANDEHYDRA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC88|protein.P0AC88]]

## Enriched Summary

GDP-mannose 4,6-dehydratase catalyzes the first step in the pathway that converts GDP-D-mannose to GDP-L-fucose. GDP-L-fucose is one of the precursors of colanic acid (M antigen), an extracellular polysaccharide . Recombinant enzyme was expressed and purified as a GST fusion protein and characterized both with and without the GST tag. These studies suggested that the active form of the enzyme is a homohexamer, containing one mole of tightly bound NADP per monomer . However, later work showed the enzyme to be a homodimer . The crystal structure of the enzyme has been determined at 2.3 Å resolution. It is a member of the short-chain dehydrogenase/reductase (SDR) family. Each monomer was shown to be composed of a larger N-terminal domain that binds the NADP or NADPH cofactor, and a C-terminal domain with the sugar-nucleotide binding site . This enzyme as also been used in metabolic engineering studies to produce GDP-L-fucose for the synthesis of fucosylated oligosaccharides . Review: GDP-mannose 4,6-dehydratase catalyzes the first step in the pathway that converts GDP-D-mannose to GDP-L-fucose. GDP-L-fucose is one of the precursors of colanic acid (M antigen), an extracellular polysaccharide . Recombinant enzyme was expressed and purified as a GST fusion protein and characterized both with and without the GST tag...

## Biological Role

Catalyzes GDPMANDEHYDRA-RXN (reaction.ecocyc.GDPMANDEHYDRA-RXN). Bound by NADP+ (molecule.C00006).

## Annotation

GDP-mannose 4,6-dehydratase catalyzes the first step in the pathway that converts GDP-D-mannose to GDP-L-fucose. GDP-L-fucose is one of the precursors of colanic acid (M antigen), an extracellular polysaccharide . Recombinant enzyme was expressed and purified as a GST fusion protein and characterized both with and without the GST tag. These studies suggested that the active form of the enzyme is a homohexamer, containing one mole of tightly bound NADP per monomer . However, later work showed the enzyme to be a homodimer . The crystal structure of the enzyme has been determined at 2.3 Å resolution. It is a member of the short-chain dehydrogenase/reductase (SDR) family. Each monomer was shown to be composed of a larger N-terminal domain that binds the NADP or NADPH cofactor, and a C-terminal domain with the sugar-nucleotide binding site . This enzyme as also been used in metabolic engineering studies to produce GDP-L-fucose for the synthesis of fucosylated oligosaccharides . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GDPMANDEHYDRA-RXN|reaction.ecocyc.GDPMANDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AC88|protein.P0AC88]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GDPMANDEHYDRA-CPLX`
- `QSPROTEOME:QS00200435`

## Notes

2*protein.P0AC88

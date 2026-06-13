---
entity_id: "complex.ecocyc.CPLX0-3881"
entity_type: "complex"
name: "GDP-L-fucose synthase"
source_database: "EcoCyc"
source_id: "CPLX0-3881"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# GDP-L-fucose synthase

`complex.ecocyc.CPLX0-3881`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3881`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32055|protein.P32055]]

## Enriched Summary

GDP-fucose synthase is a bifunctional enzyme that catalyzes the two-step synthesis of GDP-fucose from GDP-4-dehydro-6-deoxy-D-mannose via a GDP-4-dehydro-6-L-deoxygalactose intermediate . The presence of the GDP-4-dehydro-6-L-deoxygalactose intermediate was initially postulated, but not shown . The epimerase reaction can occur in the absence of the NADPH cofactor . The enzyme belongs to the short-chain dehydrogenase/reductase (SDR) family and the reductase-epimerase-dehydrogenase (RED) superfamily . Its N-terminal domain contains a six-stranded NADP+ binding Rossmann fold domain . Crystal structure data suggests that there is a single active site . The reaction follows a random bi-bi mechanism . Mutants in proposed active site residues have been isolated and characterized . The enzyme is a homodimer . The enzymatic reaction has been shown to involve epimerization first at C-3'' and then at C-5'' of the mannose ring, followed by an NADPH-dependent reduction of the carbonyl at C-4''. The epimerization reactions involve the participation of acid/base residues at the active site . The enzyme has also been used in metabolic engineering studies to produce GDP-L-fucose for the synthesis of fucosylated oligosaccharides...

## Biological Role

Catalyzes 1.1.1.271-RXN (reaction.ecocyc.1.1.1.271-RXN).

## Annotation

GDP-fucose synthase is a bifunctional enzyme that catalyzes the two-step synthesis of GDP-fucose from GDP-4-dehydro-6-deoxy-D-mannose via a GDP-4-dehydro-6-L-deoxygalactose intermediate . The presence of the GDP-4-dehydro-6-L-deoxygalactose intermediate was initially postulated, but not shown . The epimerase reaction can occur in the absence of the NADPH cofactor . The enzyme belongs to the short-chain dehydrogenase/reductase (SDR) family and the reductase-epimerase-dehydrogenase (RED) superfamily . Its N-terminal domain contains a six-stranded NADP+ binding Rossmann fold domain . Crystal structure data suggests that there is a single active site . The reaction follows a random bi-bi mechanism . Mutants in proposed active site residues have been isolated and characterized . The enzyme is a homodimer . The enzymatic reaction has been shown to involve epimerization first at C-3'' and then at C-5'' of the mannose ring, followed by an NADPH-dependent reduction of the carbonyl at C-4''. The epimerization reactions involve the participation of acid/base residues at the active site . The enzyme has also been used in metabolic engineering studies to produce GDP-L-fucose for the synthesis of fucosylated oligosaccharides . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.1.1.1.271-RXN|reaction.ecocyc.1.1.1.271-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P32055|protein.P32055]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3881`
- `QSPROTEOME:QS00182733`

## Notes

2*protein.P32055

---
entity_id: "complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX"
entity_type: "complex"
name: "fused aspartate kinase/homoserine dehydrogenase 2"
source_database: "EcoCyc"
source_id: "ASPKINIIHOMOSERDEHYDROGII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "aspartate kinase II"
  - "aspartokinase II"
  - "homoserine dehydrogenase II"
---

# fused aspartate kinase/homoserine dehydrogenase 2

`complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPKINIIHOMOSERDEHYDROGII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00562|protein.P00562]]

## Enriched Summary

Aspartate kinase II / homoserine dehydrogenase II (MetL) is a bifunctional enzyme that catalyzes the first step in the biosynthesis of lysine and homoserine, and indirectly methionine and threonine, as well as catalyzing the final step in homoserine biosynthesis. MetL catalyzes both the conversion of L-aspartate into L-aspartyl-4-phosphate and the conversion of L-aspartate semialdehyde into homoserine . The aspartate kinase / homoserine dehydrogenase protein comprises a dimer of MetL monomers . The protein's enzymatic activity depends on this dimerization . Each MetL monomer consists of three domains. The amino-terminal domain houses the aspartate kinase activity, the carboxy-terminal domain houses the homoserine dehydrogenase activity, and a middle domain links the two . Both the amino- and carboxy-terminal domains are involved in dimerization to form the active enzyme . metL expression is inhibited by PD04032 and by S-adenosylmethionine . MetL protein abundance is also negatively regulated by high methionine levels . Aspartate kinase II / homoserine dehydrogenase II (MetL) is a bifunctional enzyme that catalyzes the first step in the biosynthesis of lysine and homoserine, and indirectly methionine and threonine, as well as catalyzing the final step in homoserine biosynthesis...

## Biological Role

Catalyzes ASPARTATEKIN-RXN (reaction.ecocyc.ASPARTATEKIN-RXN), HOMOSERDEHYDROG-RXN (reaction.ecocyc.HOMOSERDEHYDROG-RXN).

## Annotation

Aspartate kinase II / homoserine dehydrogenase II (MetL) is a bifunctional enzyme that catalyzes the first step in the biosynthesis of lysine and homoserine, and indirectly methionine and threonine, as well as catalyzing the final step in homoserine biosynthesis. MetL catalyzes both the conversion of L-aspartate into L-aspartyl-4-phosphate and the conversion of L-aspartate semialdehyde into homoserine . The aspartate kinase / homoserine dehydrogenase protein comprises a dimer of MetL monomers . The protein's enzymatic activity depends on this dimerization . Each MetL monomer consists of three domains. The amino-terminal domain houses the aspartate kinase activity, the carboxy-terminal domain houses the homoserine dehydrogenase activity, and a middle domain links the two . Both the amino- and carboxy-terminal domains are involved in dimerization to form the active enzyme . metL expression is inhibited by PD04032 and by S-adenosylmethionine . MetL protein abundance is also negatively regulated by high methionine levels .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ASPARTATEKIN-RXN|reaction.ecocyc.ASPARTATEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.HOMOSERDEHYDROG-RXN|reaction.ecocyc.HOMOSERDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P00562|protein.P00562]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASPKINIIHOMOSERDEHYDROGII-CPLX`
- `QSPROTEOME:QS00181559`

## Notes

2*protein.P00562

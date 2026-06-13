---
entity_id: "complex.ecocyc.ASPKINIHOMOSERDEHYDROGI-CPLX"
entity_type: "complex"
name: "fused aspartate kinase/homoserine dehydrogenase 1"
source_database: "EcoCyc"
source_id: "ASPKINIHOMOSERDEHYDROGI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "aspartate kinase I"
  - "aspartokinase I"
  - "homoserine dehydrogenase I"
---

# fused aspartate kinase/homoserine dehydrogenase 1

`complex.ecocyc.ASPKINIHOMOSERDEHYDROGI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPKINIHOMOSERDEHYDROGI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00561|protein.P00561]]

## Enriched Summary

Aspartate kinase I / homoserine dehydrogenase I (ThrA) is a bifunctional enzyme that catalyzes the first step in the biosynthesis of lysine and homoserine, and indirectly methionine and threonine, as well as catalyzing the final step in homoserine biosynthesis. It is strongly regulated by one of its downstream products, threonine. ThrA catalyzes both the ATP-dependent conversion of L-aspartate to L-aspartyl-4-phosphate and the NAD(P)H-dependent reduction of L-aspartate-semialdehyde to form homoserine . Aspartate kinase I / homoserine dehydrogenase I comprises a dimer of ThrA dimers . Although the dimeric form is catalytically active, the binding equilibrium dramatically favors the tetrameric form . The aspartate kinase and homoserine dehydrogenase activities of each ThrA monomer are catalyzed by independent domains connected by a linker region . The competitive inhibitor threonine binds ThrA at two sites per monomer, one high affinity, the other low affinity. Binding at both sites is cooperative . The low-affinity threonine binding site is actually the kinase active site, and bound threonine actually overlaps with the binding site of aspartate . Threonine acts as an allosteric inhibitor at the high-affinity site, inducing a conformational change in the protein that increases the distance between the kinase and dehydrogenase active sites...

## Biological Role

Catalyzes ASPARTATEKIN-RXN (reaction.ecocyc.ASPARTATEKIN-RXN), HOMOSERDEHYDROG-RXN (reaction.ecocyc.HOMOSERDEHYDROG-RXN).

## Annotation

Aspartate kinase I / homoserine dehydrogenase I (ThrA) is a bifunctional enzyme that catalyzes the first step in the biosynthesis of lysine and homoserine, and indirectly methionine and threonine, as well as catalyzing the final step in homoserine biosynthesis. It is strongly regulated by one of its downstream products, threonine. ThrA catalyzes both the ATP-dependent conversion of L-aspartate to L-aspartyl-4-phosphate and the NAD(P)H-dependent reduction of L-aspartate-semialdehyde to form homoserine . Aspartate kinase I / homoserine dehydrogenase I comprises a dimer of ThrA dimers . Although the dimeric form is catalytically active, the binding equilibrium dramatically favors the tetrameric form . The aspartate kinase and homoserine dehydrogenase activities of each ThrA monomer are catalyzed by independent domains connected by a linker region . The competitive inhibitor threonine binds ThrA at two sites per monomer, one high affinity, the other low affinity. Binding at both sites is cooperative . The low-affinity threonine binding site is actually the kinase active site, and bound threonine actually overlaps with the binding site of aspartate . Threonine acts as an allosteric inhibitor at the high-affinity site, inducing a conformational change in the protein that increases the distance between the kinase and dehydrogenase active sites . This transition has been studied via fluorescence analysis . The homoserine dehydrogenase activity of ThrA is inhibited by direct binding of substrates for the kinase activity within the dehydrogenase domain . There are some inhibitors that shut down both the kinase and dehydrogenase activities of ThrA. L-serine is a competitive inhibitor of both activities, as well as inducing a conformational shift that renders threonine binding nonc

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ASPARTATEKIN-RXN|reaction.ecocyc.ASPARTATEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.HOMOSERDEHYDROG-RXN|reaction.ecocyc.HOMOSERDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P00561|protein.P00561]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ASPKINIHOMOSERDEHYDROGI-CPLX`
- `QSPROTEOME:QS00183259`

## Notes

4*protein.P00561

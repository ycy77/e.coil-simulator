---
entity_id: "complex.ecocyc.MALATE-DEHASE"
entity_type: "complex"
name: "malate dehydrogenase"
source_database: "EcoCyc"
source_id: "MALATE-DEHASE"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# malate dehydrogenase

`complex.ecocyc.MALATE-DEHASE`

## Static

- Type: `complex`
- Source: `EcoCyc:MALATE-DEHASE`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P61889|protein.P61889]]

## Enriched Summary

Malate dehydrogenase (Mdh) catalyzes the reversible oxidation of malate to generate oxaloacetate, using NAD+ as an electron acceptor . Mdh carries out the oxidation reaction as part of the TCA cycle, the glyoxylate cycle, and gluconeogenesis. It reduces oxaloacetate to generate malate as part of anaerobic respiration and mixed-acid fermentation. Malate dehydrogenase comprises a dimer of Mdh monomers . A crystal structure of this dimer shows that Arg-81, Arg-153 and His-177 may all be involved in substrate interaction . Although Mdh does not interact directly with the oxaloacetate-utilizing enzyme ASPAMINOTRANS-DIMER, it does appear to directly transfer NADH to NADH-DHI-CPLX . Mdh activity is depressed during anaerobic conditions . There is a 2-fold difference between expression of Mdh under aerobic versus anaerobic conditions. In addition, Mdh expression increases during growth on pyruvate, is low during growth on glucose, and is increased 5-fold by heme limitation during anaerobic growth . mdh belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . Review: Malate dehydrogenase (Mdh) catalyzes the reversible oxidation of malate to generate oxaloacetate, using NAD+ as an electron acceptor . Mdh carries out the oxidation reaction as part of the TCA cycle, the glyoxylate cycle, and gluconeogenesis...

## Biological Role

Catalyzes MALATE-DEH-RXN (reaction.ecocyc.MALATE-DEH-RXN).

## Annotation

Malate dehydrogenase (Mdh) catalyzes the reversible oxidation of malate to generate oxaloacetate, using NAD+ as an electron acceptor . Mdh carries out the oxidation reaction as part of the TCA cycle, the glyoxylate cycle, and gluconeogenesis. It reduces oxaloacetate to generate malate as part of anaerobic respiration and mixed-acid fermentation. Malate dehydrogenase comprises a dimer of Mdh monomers . A crystal structure of this dimer shows that Arg-81, Arg-153 and His-177 may all be involved in substrate interaction . Although Mdh does not interact directly with the oxaloacetate-utilizing enzyme ASPAMINOTRANS-DIMER, it does appear to directly transfer NADH to NADH-DHI-CPLX . Mdh activity is depressed during anaerobic conditions . There is a 2-fold difference between expression of Mdh under aerobic versus anaerobic conditions. In addition, Mdh expression increases during growth on pyruvate, is low during growth on glucose, and is increased 5-fold by heme limitation during anaerobic growth . mdh belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.MALATE-DEH-RXN|reaction.ecocyc.MALATE-DEH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P61889|protein.P61889]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:MALATE-DEHASE`
- `QSPROTEOME:QS00154219`

## Notes

2*protein.P61889

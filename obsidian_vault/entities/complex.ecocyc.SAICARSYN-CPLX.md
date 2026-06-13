---
entity_id: "complex.ecocyc.SAICARSYN-CPLX"
entity_type: "complex"
name: "phosphoribosylaminoimidazole-succinocarboxamide synthase"
source_database: "EcoCyc"
source_id: "SAICARSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphoribosylaminoimidazole-succinocarboxamide synthase

`complex.ecocyc.SAICARSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SAICARSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7D7|protein.P0A7D7]]

## Enriched Summary

PurC catalyzes the ligation of the carboxylate group of 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylate (CAIR) to the amino group of aspartate . This is one of two reactions in purine metabolism that utilize aspartate and a ribonucleoside triphosphate, the other being ADENYLOSUCCINATE-SYN-DIMER (PurA). Their kinetic mechanisms are similar although they show only 16% amino acid sequence identity. For E. coli PurC a rapid equilibrium random ter-ter kinetic mechanism has been demonstrated . The overproduction and purification of native and hexahistidine-tagged recombinant PurC have been reported. A crystal structure of PurC in complex with ADP or ADP-CAIR has been determined . Review: PurC catalyzes the ligation of the carboxylate group of 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylate (CAIR) to the amino group of aspartate . This is one of two reactions in purine metabolism that utilize aspartate and a ribonucleoside triphosphate, the other being ADENYLOSUCCINATE-SYN-DIMER (PurA). Their kinetic mechanisms are similar although they show only 16% amino acid sequence identity. For E. coli PurC a rapid equilibrium random ter-ter kinetic mechanism has been demonstrated . The overproduction and purification of native and hexahistidine-tagged recombinant PurC have been reported. A crystal structure of PurC in complex with ADP or ADP-CAIR has been determined . Review:

## Biological Role

Catalyzes SAICARSYN-RXN (reaction.ecocyc.SAICARSYN-RXN).

## Annotation

PurC catalyzes the ligation of the carboxylate group of 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylate (CAIR) to the amino group of aspartate . This is one of two reactions in purine metabolism that utilize aspartate and a ribonucleoside triphosphate, the other being ADENYLOSUCCINATE-SYN-DIMER (PurA). Their kinetic mechanisms are similar although they show only 16% amino acid sequence identity. For E. coli PurC a rapid equilibrium random ter-ter kinetic mechanism has been demonstrated . The overproduction and purification of native and hexahistidine-tagged recombinant PurC have been reported. A crystal structure of PurC in complex with ADP or ADP-CAIR has been determined . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SAICARSYN-RXN|reaction.ecocyc.SAICARSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A7D7|protein.P0A7D7]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:SAICARSYN-CPLX`
- `QSPROTEOME:QS00049524`

## Notes

3*protein.P0A7D7

---
entity_id: "complex.ecocyc.CPLX0-8615"
entity_type: "complex"
name: "maltodextrin glucosidase"
source_database: "EcoCyc"
source_id: "CPLX0-8615"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# maltodextrin glucosidase

`complex.ecocyc.CPLX0-8615`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8615`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P21517|protein.P21517]]

## Enriched Summary

Maltodextrin glucosidase (MalZ) catalyzes the hydrolysis of short malto-oligosaccharides ranging from maltotriose to maltoheptaose, liberating glucose from the reducing end. Final products of the reaction are glucose and maltose . To a small extent, the enzyme can directly release maltose from maltodextrins longer than maltotriose . Maltodextrin glucosidase also hydrolyzes γ-cyclodextrin, which contains eight glucosyl residues; however, γ-cyclodextrin is not transported by E. coli and is thus not a physiological substrate . The enzyme can also act as a transglycosylase . MalZ may play a role in regulating the intracellular level of maltotriose, the inducer of the mal regulon: overexpression of malZ results in decreased expression of the other mal genes . GroEL-GroES- and chemical chaperone-assisted folding and irreversible thermal denaturation of MalZ have been studied . A crystal structure of the enzyme has been solved at 3.7 Å resolution; while the N-terminal region appears to be flexible or unstructured, it is required for formation of the functional enzyme . A more recent crystal structure shows the enzyme in a homodimeric conformation, with the N-terminal domain of one subunit located close to and gating the active site of the second subunit . A malZ mutant is able to grow well on short malto-oligosaccharides and is able to degrade dextrins to maltotriose...

## Biological Role

Catalyzes MALTODEXGLUCOSID-RXN (reaction.ecocyc.MALTODEXGLUCOSID-RXN), RXN-14281 (reaction.ecocyc.RXN-14281), RXN-14282 (reaction.ecocyc.RXN-14282), RXN-14283 (reaction.ecocyc.RXN-14283), RXN0-5183 (reaction.ecocyc.RXN0-5183).

## Annotation

Maltodextrin glucosidase (MalZ) catalyzes the hydrolysis of short malto-oligosaccharides ranging from maltotriose to maltoheptaose, liberating glucose from the reducing end. Final products of the reaction are glucose and maltose . To a small extent, the enzyme can directly release maltose from maltodextrins longer than maltotriose . Maltodextrin glucosidase also hydrolyzes γ-cyclodextrin, which contains eight glucosyl residues; however, γ-cyclodextrin is not transported by E. coli and is thus not a physiological substrate . The enzyme can also act as a transglycosylase . MalZ may play a role in regulating the intracellular level of maltotriose, the inducer of the mal regulon: overexpression of malZ results in decreased expression of the other mal genes . GroEL-GroES- and chemical chaperone-assisted folding and irreversible thermal denaturation of MalZ have been studied . A crystal structure of the enzyme has been solved at 3.7 Å resolution; while the N-terminal region appears to be flexible or unstructured, it is required for formation of the functional enzyme . A more recent crystal structure shows the enzyme in a homodimeric conformation, with the N-terminal domain of one subunit located close to and gating the active site of the second subunit . A malZ mutant is able to grow well on short malto-oligosaccharides and is able to degrade dextrins to maltotriose . The malZ292 allele supresses the Mal- defect of a malQ mutant by acquiring dextrinyl transferase activity, but not the ability to hydrolyze maltose . A malZ mutant contains increased levels of glycogen when grown on maltose or maltodextrin, and overexpression of MalZ in a ΔmalP glgA mutant decreses the amount of glycogen when grown on maltose . Expression of malZ is dependent on the MalT regulator , but is also

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.MALTODEXGLUCOSID-RXN|reaction.ecocyc.MALTODEXGLUCOSID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14281|reaction.ecocyc.RXN-14281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14282|reaction.ecocyc.RXN-14282]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14283|reaction.ecocyc.RXN-14283]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5183|reaction.ecocyc.RXN0-5183]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P21517|protein.P21517]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8615`
- `QSPROTEOME:QS00181909`

## Notes

2*protein.P21517

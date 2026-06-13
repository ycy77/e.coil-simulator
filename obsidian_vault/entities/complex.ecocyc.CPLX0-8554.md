---
entity_id: "complex.ecocyc.CPLX0-8554"
entity_type: "complex"
name: "3-dehydro-D-guloside 4-epimerase"
source_database: "EcoCyc"
source_id: "CPLX0-8554"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-dehydro-D-guloside 4-epimerase

`complex.ecocyc.CPLX0-8554`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8554`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76044|protein.P76044]]

## Enriched Summary

Purified YcjR has 3-dehydro-D-guloside 4-epimerase activity . A crystal structure of YcjR has been solved at 1.86Å resolution; the enzyme is homodimeric in the crystal structure, but elutes as a homotetramer by gel filtration. Site-directed mutagenesis of conserved Glu residues within the predicted active site and assaying the catalytic activities of the mutant enzymes indicates that Glu146 is responsible for the proton abstraction at the C4 position of the 3-keto-D-glucoside substrate, forming the cis-enediolate intermediate that is then reprotonated on the opposite face by Glu240 to generate the corresponding 3-keto-D-guloside . YcjR has sequence similarity to D-tagatose-3-epimerase isolated from Pseudomonas cichorii and was overexpressed and purified . Purified YcjR has 3-dehydro-D-guloside 4-epimerase activity . A crystal structure of YcjR has been solved at 1.86Å resolution; the enzyme is homodimeric in the crystal structure, but elutes as a homotetramer by gel filtration...

## Biological Role

Catalyzes RXN-20681 (reaction.ecocyc.RXN-20681). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

Purified YcjR has 3-dehydro-D-guloside 4-epimerase activity . A crystal structure of YcjR has been solved at 1.86Å resolution; the enzyme is homodimeric in the crystal structure, but elutes as a homotetramer by gel filtration. Site-directed mutagenesis of conserved Glu residues within the predicted active site and assaying the catalytic activities of the mutant enzymes indicates that Glu146 is responsible for the proton abstraction at the C4 position of the 3-keto-D-glucoside substrate, forming the cis-enediolate intermediate that is then reprotonated on the opposite face by Glu240 to generate the corresponding 3-keto-D-guloside . YcjR has sequence similarity to D-tagatose-3-epimerase isolated from Pseudomonas cichorii and was overexpressed and purified .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-20681|reaction.ecocyc.RXN-20681]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76044|protein.P76044]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8554`
- `QSPROTEOME:QS00196197`

## Notes

4*protein.P76044

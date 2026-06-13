---
entity_id: "complex.ecocyc.ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX"
entity_type: "complex"
name: "aspartate-semialdehyde dehydrogenase"
source_database: "EcoCyc"
source_id: "ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aspartate-semialdehyde dehydrogenase

`complex.ecocyc.ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9Q9|protein.P0A9Q9]]

## Enriched Summary

Aspartate semialdehyde dehydrogenase (Asd) carries out the middle step in the pathway of homoserine biosynthesis, generating L-aspartate-semialdehyde. Asd catalyzes the NADPH-dependent conversion of L-aspartyl-4-phosphate to L-aspartate-semialdehyde . As Asd transfers the pro-S hydrogen from NADPH, it is a class B hydrogenase . Aspartate semialdehyde dehydrogenase comprises a dimer of Asd monomers . A number of crystal structures have been solved for Asd, in both active and inactive forms . A crystal structure to 2.5 Å resolution shows that each Asd monomer has an amino-terminal NADPH-binding domain and a separate dimerization domain, with the active site existing in a cleft between the two domains . The active site contains a cysteine, Cys-135, that is required for activity, but reportedly not for substrate binding . A crystal structure with a substrate analog, however, shows that it binds to this cysteine . As observed in extract, the activity of Asd appears to undergo short-term repression by lysine, methionine, and threonine . Translation of Asd is repressed by the small RNA SgrS; overexpression of Aid exacerbates the effects of glucose-phosphate stress in a ppsA mutant . Aspartate semialdehyde dehydrogenase (Asd) carries out the middle step in the pathway of homoserine biosynthesis, generating L-aspartate-semialdehyde...

## Biological Role

Catalyzes ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN (reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN).

## Annotation

Aspartate semialdehyde dehydrogenase (Asd) carries out the middle step in the pathway of homoserine biosynthesis, generating L-aspartate-semialdehyde. Asd catalyzes the NADPH-dependent conversion of L-aspartyl-4-phosphate to L-aspartate-semialdehyde . As Asd transfers the pro-S hydrogen from NADPH, it is a class B hydrogenase . Aspartate semialdehyde dehydrogenase comprises a dimer of Asd monomers . A number of crystal structures have been solved for Asd, in both active and inactive forms . A crystal structure to 2.5 Å resolution shows that each Asd monomer has an amino-terminal NADPH-binding domain and a separate dimerization domain, with the active site existing in a cleft between the two domains . The active site contains a cysteine, Cys-135, that is required for activity, but reportedly not for substrate binding . A crystal structure with a substrate analog, however, shows that it binds to this cysteine . As observed in extract, the activity of Asd appears to undergo short-term repression by lysine, methionine, and threonine . Translation of Asd is repressed by the small RNA SgrS; overexpression of Aid exacerbates the effects of glucose-phosphate stress in a ppsA mutant .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9Q9|protein.P0A9Q9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX`
- `QSPROTEOME:QS00196589`

## Notes

2*protein.P0A9Q9

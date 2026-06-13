---
entity_id: "complex.ecocyc.DALADEHYDROG-CPLX"
entity_type: "complex"
name: "D-amino acid dehydrogenase"
source_database: "EcoCyc"
source_id: "DALADEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-amino acid dehydrogenase

`complex.ecocyc.DALADEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DALADEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A6J5|protein.P0A6J5]]

## Enriched Summary

E. coli can utilize L- and D-alanine as the sole source of carbon, nitrogen and energy . D-amino acid dehydrogenase is the second enzyme of the ALADEG-PWY pathway. The enzyme has broad substrate specificity; it catalyzes the oxidative deamination of many D-amino acids, although D-alanine is the best substrate . The enzyme is membrane-associated and linked to the respiratory chain . The purine nucleoside phosphoramidase activity of EG12172-MONOMER HinT is required for the activity of D-amino acid dehydrogenase . In the final step of a partial purification of the enzyme from E. coli K-12, the enzyme eluted in a single peak of ~100 kDa . Purification of D-amino acid dehydrogenase from E. coli B showed two subunits of apparently different sizes, a 45 kDa subunit that may be encoded by dadA, and a 55 kDa subunit for which no gene had been identified . As this is the only report of two non-identical subunits, and the enzyme was purified from E. coli B, D-amino acid dehydrogenase is here represented as a dimer of identical DadA subunits. DadA is a substrate for the membrane-anchored endoprotease EG11506-MONOMER FtsH . Regulatory mutations (dadR) increasing expression of DadA (and thus, likely the expression of the dadAX operon, which also encodes D-alanine racemase) lead to the ability to utilize D-isomers of several amino acids...

## Biological Role

Catalyzes D-alanine dehydrogenase (reaction.ecocyc.DALADEHYDROG-RXN), RXN-11193 (reaction.ecocyc.RXN-11193). Bound by FAD (molecule.C00016).

## Annotation

E. coli can utilize L- and D-alanine as the sole source of carbon, nitrogen and energy . D-amino acid dehydrogenase is the second enzyme of the ALADEG-PWY pathway. The enzyme has broad substrate specificity; it catalyzes the oxidative deamination of many D-amino acids, although D-alanine is the best substrate . The enzyme is membrane-associated and linked to the respiratory chain . The purine nucleoside phosphoramidase activity of EG12172-MONOMER HinT is required for the activity of D-amino acid dehydrogenase . In the final step of a partial purification of the enzyme from E. coli K-12, the enzyme eluted in a single peak of ~100 kDa . Purification of D-amino acid dehydrogenase from E. coli B showed two subunits of apparently different sizes, a 45 kDa subunit that may be encoded by dadA, and a 55 kDa subunit for which no gene had been identified . As this is the only report of two non-identical subunits, and the enzyme was purified from E. coli B, D-amino acid dehydrogenase is here represented as a dimer of identical DadA subunits. DadA is a substrate for the membrane-anchored endoprotease EG11506-MONOMER FtsH . Regulatory mutations (dadR) increasing expression of DadA (and thus, likely the expression of the dadAX operon, which also encodes D-alanine racemase) lead to the ability to utilize D-isomers of several amino acids . Both L-alanine and D-alanine are able to induce the expression of dadA, and expression is catabolite-repressible . However, L-alanine may be the actual inducer of dadAX expression . dadX and dadA are expressed and show a mutant phenotype within the oxic nutrient-deprived region at mid-height of spatially structured biofilms, where they enable utilization of alanine as a carbon and nitrogen source . dadA mutants lack the ability to utilize either L-al

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.DALADEHYDROG-RXN|reaction.ecocyc.DALADEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11193|reaction.ecocyc.RXN-11193]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6J5|protein.P0A6J5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DALADEHYDROG-CPLX`
- `QSPROTEOME:QS00049482`

## Notes

2*protein.P0A6J5

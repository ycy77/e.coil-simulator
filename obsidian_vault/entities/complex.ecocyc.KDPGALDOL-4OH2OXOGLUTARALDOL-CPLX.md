---
entity_id: "complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX"
entity_type: "complex"
name: "KHG/KDPG aldolase"
source_database: "EcoCyc"
source_id: "KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "multifunctional 2-keto-3-deoxygluconate 6-phosphate aldolase and 2-keto-4-hydroxyglutarate aldolase and oxaloacetate decarboxylase"
  - "2-keto-3-deoxygluconate 6-phosphate/2-keto-4-hydroxyglutarate aldolase"
---

# KHG/KDPG aldolase

`complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A955|protein.P0A955]]

## Enriched Summary

The eda gene encodes a trimeric multifunctional enzyme. One activity, 2-keto-3-deoxygluconate 6-phosphate aldolase (KDPG aldolase), catalyzes an aldol cleavage of KDPG to D-glyceraldehyde 3-phosphate and pyruvate. KDPG is a key intermediate in the Entner-Doudoroff pathway which constitutes the primary route of gluconate metabolism in E. coli . The other activity, 2-keto-4-hydroxyglutarate aldolase (KHG aldolase), cleaves KHG to glyoxylate and pyruvate and participates in the regulation of intracellular levels of glyoxylate. The enzyme also has oxaloacetate decarboxylase activity and participates in the dissimilation of glyoxylate to pyruvate . A summary of these activities is presented in . KHG/KDPG aldolase is a Schiff-base mechanism, Class I, lysine-type aldolase . The E. coli KHG aldolase activity is stereoselective for the L-isomer (S-enantiomer) of 2-keto-4-hydroxyglutarate and is defined by EC 4.1.3.42. This is in contrast to EC 4.1.3.16 which defines an enzyme found in mammals that can efficiently utilize both enantiomers of 4-hydroxy-2-oxoglutarate . The native E. coli enzyme purified from cell extracts has been kinetically characterized and has a homotrimeric subunit structure . Recombinantly produced enzyme has been purified and characterized . The native enzyme can undergo reversible acid inactivation...

## Biological Role

Catalyzes KDPGALDOL-RXN (reaction.ecocyc.KDPGALDOL-RXN), OXALODECARB-RXN (reaction.ecocyc.OXALODECARB-RXN), L-4-hydroxy-2-oxoglutarate aldolase (reaction.ecocyc.RXN-13990).

## Annotation

The eda gene encodes a trimeric multifunctional enzyme. One activity, 2-keto-3-deoxygluconate 6-phosphate aldolase (KDPG aldolase), catalyzes an aldol cleavage of KDPG to D-glyceraldehyde 3-phosphate and pyruvate. KDPG is a key intermediate in the Entner-Doudoroff pathway which constitutes the primary route of gluconate metabolism in E. coli . The other activity, 2-keto-4-hydroxyglutarate aldolase (KHG aldolase), cleaves KHG to glyoxylate and pyruvate and participates in the regulation of intracellular levels of glyoxylate. The enzyme also has oxaloacetate decarboxylase activity and participates in the dissimilation of glyoxylate to pyruvate . A summary of these activities is presented in . KHG/KDPG aldolase is a Schiff-base mechanism, Class I, lysine-type aldolase . The E. coli KHG aldolase activity is stereoselective for the L-isomer (S-enantiomer) of 2-keto-4-hydroxyglutarate and is defined by EC 4.1.3.42. This is in contrast to EC 4.1.3.16 which defines an enzyme found in mammals that can efficiently utilize both enantiomers of 4-hydroxy-2-oxoglutarate . The native E. coli enzyme purified from cell extracts has been kinetically characterized and has a homotrimeric subunit structure . Recombinantly produced enzyme has been purified and characterized . The native enzyme can undergo reversible acid inactivation . Chemical modification studies show that active site Arg, Lys and Glu residues in each subunit are required for KHG aldolase activity . Manual peptide sequencing established that the three subunits are identical . Pyruvate analogs designed as mechanistic inhibitors of KDPG aldolase resulted in either competitive, or slow-binding inhibition . Crystal structures of recombinant wild-type and mutant enzymes have been solved including a wild-type structure containin

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.KDPGALDOL-RXN|reaction.ecocyc.KDPGALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.OXALODECARB-RXN|reaction.ecocyc.OXALODECARB-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-13990|reaction.ecocyc.RXN-13990]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A955|protein.P0A955]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX`
- `QSPROTEOME:QS00199581`

## Notes

3*protein.P0A955

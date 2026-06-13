---
entity_id: "complex.ecocyc.LYSDECARBOX-CPLX"
entity_type: "complex"
name: "lysine decarboxylase 1"
source_database: "EcoCyc"
source_id: "LYSDECARBOX-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "LdcI"
  - "LDC1"
---

# lysine decarboxylase 1

`complex.ecocyc.LYSDECARBOX-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LYSDECARBOX-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9H3|protein.P0A9H3]]

## Enriched Summary

There are two lysine decarboxylases in E. coli, encoded by the cadA and ldcC genes. The cadA gene product, lysine decarboxylase 1 (CadA), is an inducible enzyme that has been studied since the 1940's (e.g. ). CadA is more active, more thermostable, and has a lower pH optimum than the constitutively expressed ldcC-encoded enzyme . CadA is part of the lysine-dependent acid resistance system 4 (AR4, LDAR) which confers resistance to weak organic acids produced during carbohydrate fermentation under conditions of anaerobiosis and phosphate starvation . Lysine decarboxylase is induced under acidic growth conditions and plays a role in maintaining pH homeostasis or extending the growth period by detoxification of the extracellular medium. It consumes a proton during production of the polyamine cadaverine, which is secreted by the lysine/cadaverine antiporter CadB. A lysine decarboxylase-negative phenotype is not only a hallmark of many pathogenic E. coli strains, but is in fact pathoadaptive (reviewed in ). Crystal structures of CadA has been solved, showing a pentameric ring consisting of CadA dimers . The lysine decarboxylase activity of CadA is inhibited by the alarmone ppGpp . pH-dependent activation of the enzyme involves structural rearrangements in the active site . CadA interacts with and stimulates the ATPase activity of EG11731-MONOMER RavA...

## Biological Role

Catalyzes LYSDECARBOX-RXN (reaction.ecocyc.LYSDECARBOX-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

There are two lysine decarboxylases in E. coli, encoded by the cadA and ldcC genes. The cadA gene product, lysine decarboxylase 1 (CadA), is an inducible enzyme that has been studied since the 1940's (e.g. ). CadA is more active, more thermostable, and has a lower pH optimum than the constitutively expressed ldcC-encoded enzyme . CadA is part of the lysine-dependent acid resistance system 4 (AR4, LDAR) which confers resistance to weak organic acids produced during carbohydrate fermentation under conditions of anaerobiosis and phosphate starvation . Lysine decarboxylase is induced under acidic growth conditions and plays a role in maintaining pH homeostasis or extending the growth period by detoxification of the extracellular medium. It consumes a proton during production of the polyamine cadaverine, which is secreted by the lysine/cadaverine antiporter CadB. A lysine decarboxylase-negative phenotype is not only a hallmark of many pathogenic E. coli strains, but is in fact pathoadaptive (reviewed in ). Crystal structures of CadA has been solved, showing a pentameric ring consisting of CadA dimers . The lysine decarboxylase activity of CadA is inhibited by the alarmone ppGpp . pH-dependent activation of the enzyme involves structural rearrangements in the active site . CadA interacts with and stimulates the ATPase activity of EG11731-MONOMER RavA . Interaction with RavA reduces the inhibitory effect of ppGpp on CadA activity . A cryo-EM map of the RavA-CadA complex reveals that the LARA domain of RavA re-arranges itself to match the five-fold symmetry of CadA . A 3D cryo-EM reconstruction of CadA has been compared to that of LdcC; the C-terminal β-sheet provides a sequence signature that allows classification of enzymes into CadA-like vs. LdcC-like and explains why only C

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LYSDECARBOX-RXN|reaction.ecocyc.LYSDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9H3|protein.P0A9H3]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:LYSDECARBOX-CPLX`

## Notes

10*protein.P0A9H3

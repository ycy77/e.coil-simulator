---
entity_id: "complex.ecocyc.GLYCOPHOSPHORYL-CPLX"
entity_type: "complex"
name: "glycogen phosphorylase"
source_database: "EcoCyc"
source_id: "GLYCOPHOSPHORYL-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glycogen phosphorylase

`complex.ecocyc.GLYCOPHOSPHORYL-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYCOPHOSPHORYL-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC86|protein.P0AC86]]

## Enriched Summary

Glycogen phosphorylase (GlgP) is one of two distinct α-glucan phosphorylases in E. coli, the second being MALDEXPHOSPHORYL-CPLX, which is encoded by the malP gene. The two isozymes are more closely related to each other than to phosphorylases from other organisms . GlgP catalyzes a step in the breakdown of glycogen, removing glucose units from the polysaccharide outer chains . Glycogen phosphorylase shows a marked preference for the larger polymer Glycogens glycogen over the smaller Maltodextrins maltodextrins as the polyglucose substrate, although its affinity even for glycogen is low. It is believed that glycogen phosphorylase plays a role in the slow degradation of endogenous glycogen during long stationary conditions . The PTSH-MONOMER component of the PEP:sugar phosphotransferase system (PTS) binds to glycogen phosphorylase and allosterically regulates the oligomeric state of the enzyme. Binding of HPr to GlgP decreases the Km of GlgP for glycogen 5-fold. Phosphorylated HPr has 4-fold higher affinity for GlgP than the unphosphorylated form, although it does not appear to stimulate the activity of GlgP . His806 of GlgP was found to be phosphorylated . Glycogens Glycogen occurs in E. coli in two forms - smaller β particles, and larger α particles, which are aggregates of β particles...

## Biological Role

Catalyzes GLYCOPHOSPHORYL-RXN (reaction.ecocyc.GLYCOPHOSPHORYL-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Glycogen phosphorylase (GlgP) is one of two distinct α-glucan phosphorylases in E. coli, the second being MALDEXPHOSPHORYL-CPLX, which is encoded by the malP gene. The two isozymes are more closely related to each other than to phosphorylases from other organisms . GlgP catalyzes a step in the breakdown of glycogen, removing glucose units from the polysaccharide outer chains . Glycogen phosphorylase shows a marked preference for the larger polymer Glycogens glycogen over the smaller Maltodextrins maltodextrins as the polyglucose substrate, although its affinity even for glycogen is low. It is believed that glycogen phosphorylase plays a role in the slow degradation of endogenous glycogen during long stationary conditions . The PTSH-MONOMER component of the PEP:sugar phosphotransferase system (PTS) binds to glycogen phosphorylase and allosterically regulates the oligomeric state of the enzyme. Binding of HPr to GlgP decreases the Km of GlgP for glycogen 5-fold. Phosphorylated HPr has 4-fold higher affinity for GlgP than the unphosphorylated form, although it does not appear to stimulate the activity of GlgP . His806 of GlgP was found to be phosphorylated . Glycogens Glycogen occurs in E. coli in two forms - smaller β particles, and larger α particles, which are aggregates of β particles . Mutation of the glgP gene results in larger, fragile α particles, which are composed of larger β particles with higher average chain length . ΔglgP mutants display a glycogen-excess phenotype . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AC86|protein.P0AC86]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLYCOPHOSPHORYL-CPLX`
- `QSPROTEOME:QS00199671`

## Notes

2*protein.P0AC86

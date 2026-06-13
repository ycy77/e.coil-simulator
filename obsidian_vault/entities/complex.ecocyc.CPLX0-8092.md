---
entity_id: "complex.ecocyc.CPLX0-8092"
entity_type: "complex"
name: "negative regulator of MalT activity/cystathionine β-lyase"
source_database: "EcoCyc"
source_id: "CPLX0-8092"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# negative regulator of MalT activity/cystathionine β-lyase

`complex.ecocyc.CPLX0-8092`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8092`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P23256|protein.P23256]]

## Enriched Summary

MalY is a bifunctional protein with a regulatory as well as an enzymatic function . MalY acts as a negative regulator of the maltose regulon by forming a complex with the transcriptional activator PD00237 MalT in the absence of the inducer maltotriose, thus competing with maltotriose binding to MalT . Mutations that reduce MalY's repressor activity map to regions away from the enzyme active site . Mutations in MalT affects its sensitivity to MalY inhibition . MalY forms a dimer with the ADP-bound resting form of MalT . CryoEM analysis found that MalY binds to one oligomerization surface of MalT to form a dimer which then forms a heterotetramer (2:2 complex) that prevents MalT from forming its various multimeric forms . MalY belongs to a family of aminotransferases and catalyzes the carbon-sulfur bond cleavage (β C-S lyase) of cystathionine . The cystathionase activity of MalY is not required for its regulatory function . The physiological substrate is unknown . An in-gel staining assay showed that MalY also has cysteine desulfhydrase activity; a quintuple ΔmetC tnaA cysK cysM malY mutant contains significantly reduces that activity . In addition, MalY has low alanine racemase activity . Crystal structures of the wild-type and a mutant enzyme have been solved. The PYRIDOXAL_PHOSPHATE (PLP) cofactor is bound to Lys233 . PLP binding increases the stability of the dimeric enzyme...

## Biological Role

Catalyzes ALARACECAT-RXN (reaction.ecocyc.ALARACECAT-RXN), CYSTATHIONINE-BETA-LYASE-RXN (reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN), LCYSDESULF-RXN (reaction.ecocyc.LCYSDESULF-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

MalY is a bifunctional protein with a regulatory as well as an enzymatic function . MalY acts as a negative regulator of the maltose regulon by forming a complex with the transcriptional activator PD00237 MalT in the absence of the inducer maltotriose, thus competing with maltotriose binding to MalT . Mutations that reduce MalY's repressor activity map to regions away from the enzyme active site . Mutations in MalT affects its sensitivity to MalY inhibition . MalY forms a dimer with the ADP-bound resting form of MalT . CryoEM analysis found that MalY binds to one oligomerization surface of MalT to form a dimer which then forms a heterotetramer (2:2 complex) that prevents MalT from forming its various multimeric forms . MalY belongs to a family of aminotransferases and catalyzes the carbon-sulfur bond cleavage (β C-S lyase) of cystathionine . The cystathionase activity of MalY is not required for its regulatory function . The physiological substrate is unknown . An in-gel staining assay showed that MalY also has cysteine desulfhydrase activity; a quintuple ΔmetC tnaA cysK cysM malY mutant contains significantly reduces that activity . In addition, MalY has low alanine racemase activity . Crystal structures of the wild-type and a mutant enzyme have been solved. The PYRIDOXAL_PHOSPHATE (PLP) cofactor is bound to Lys233 . PLP binding increases the stability of the dimeric enzyme . Overexpression of malY in an otherwise wild-type strain interferes with growth on maltose . Overexpression in a metC mutant complements the methionine requirement of the mutant . Reviews:

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ALARACECAT-RXN|reaction.ecocyc.ALARACECAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN|reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P23256|protein.P23256]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8092`
- `QSPROTEOME:QS00181855`

## Notes

2*protein.P23256

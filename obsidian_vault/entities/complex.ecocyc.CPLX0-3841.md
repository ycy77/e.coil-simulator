---
entity_id: "complex.ecocyc.CPLX0-3841"
entity_type: "complex"
name: "4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol kinase"
source_database: "EcoCyc"
source_id: "CPLX0-3841"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol kinase

`complex.ecocyc.CPLX0-3841`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3841`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P62615|protein.P62615]]

## Enriched Summary

4-diphosphocytidyl-2-C-methylerythritol kinase (IspE) is involved in the fourth step of the methylerythritol phosphate pathway. IspE catalyzes the ATP-dependent phosphorylation of 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol to yield 2-phospho-4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol . A crystal structure of IspE has been solved to 2 Å resolution, revealing the structural basis for substrate specificity and catalysis. The enzyme is a homodimer with a solvent-filled channel . A triclinic crystal structure of IspE-ADP complex was determined at 2 Å resolution . Several residues that are critical for the enzymatic activity of IspE have been identified . IspE is a member of the GHMP kinase (galactokinase, homoserine kinase, mevalonate kinase, and phosphomevalonate kinase) family . ispE is an essential gene . Since the enzymes of the methylerythritol pathway are not found in humans, these enzymes have attracted interest for its potential as anti-infective drug targets. Inhibitors of IspE have been investigated . Both computational and high-throughput experimental methods have been used to attempt to identify inhibitors of IspE |CITS [21903402][22563402]|. 4-diphosphocytidyl-2-C-methylerythritol kinase (IspE) is involved in the fourth step of the methylerythritol phosphate pathway...

## Biological Role

Catalyzes 2.7.1.148-RXN (reaction.ecocyc.2.7.1.148-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

4-diphosphocytidyl-2-C-methylerythritol kinase (IspE) is involved in the fourth step of the methylerythritol phosphate pathway. IspE catalyzes the ATP-dependent phosphorylation of 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol to yield 2-phospho-4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol . A crystal structure of IspE has been solved to 2 Å resolution, revealing the structural basis for substrate specificity and catalysis. The enzyme is a homodimer with a solvent-filled channel . A triclinic crystal structure of IspE-ADP complex was determined at 2 Å resolution . Several residues that are critical for the enzymatic activity of IspE have been identified . IspE is a member of the GHMP kinase (galactokinase, homoserine kinase, mevalonate kinase, and phosphomevalonate kinase) family . ispE is an essential gene . Since the enzymes of the methylerythritol pathway are not found in humans, these enzymes have attracted interest for its potential as anti-infective drug targets. Inhibitors of IspE have been investigated . Both computational and high-throughput experimental methods have been used to attempt to identify inhibitors of IspE |CITS [21903402][22563402]|.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.1.148-RXN|reaction.ecocyc.2.7.1.148-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P62615|protein.P62615]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3841`
- `QSPROTEOME:QS00181767`

## Notes

2*protein.P62615

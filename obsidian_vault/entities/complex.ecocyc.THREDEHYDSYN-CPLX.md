---
entity_id: "complex.ecocyc.THREDEHYDSYN-CPLX"
entity_type: "complex"
name: "threonine deaminase"
source_database: "EcoCyc"
source_id: "THREDEHYDSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "threonine dehydratase"
---

# threonine deaminase

`complex.ecocyc.THREDEHYDSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:THREDEHYDSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P04968|protein.P04968]]

## Enriched Summary

Threonine deaminase (IlvA) carries out the first step in the synthesis of isoleucine. IlvA catalyzes the breakdown of L-threonine to generate 2-oxobutanoate and ammonia . Although the conversion of threonine into oxobutanoate is also the first step in the pathway of threonine degradation, IlvA is not thought to play a role in that pathway. This expectation is bolstered by the presence of an oxygen-responsive promoter for ilvA and the anaerobic nature of the degradation pathway. Threonine deaminase is a tetramer . It has been alternately reported that either two or four pyridoxal phosphate molecules bind per tetramer . In the complete absence of pyridoxal phosphate, the enzyme dissociates into nonfunctional 102 kD dimers . It has also been suggested that IlvA has several active multimeric forms, rather than being solely active as a tetramer . The regulatory small molecules valine and isoleucine both bind threonine deaminase at four molecules per tetramer, the former cooperatively . Isoleucine binds only twice per tetramer . Crystal structures of threonine deaminase to 2.8 and 2.9 Å resolution reveal that it is a dimer of dimers, consisting of a set of carboxy-terminal regulatory domains projecting outward from a core of pyridoxal-containing amino-termini . The regulatory domains possessed two effector-binding sites...

## Biological Role

Catalyzes THREDEHYD-RXN (reaction.ecocyc.THREDEHYD-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Threonine deaminase (IlvA) carries out the first step in the synthesis of isoleucine. IlvA catalyzes the breakdown of L-threonine to generate 2-oxobutanoate and ammonia . Although the conversion of threonine into oxobutanoate is also the first step in the pathway of threonine degradation, IlvA is not thought to play a role in that pathway. This expectation is bolstered by the presence of an oxygen-responsive promoter for ilvA and the anaerobic nature of the degradation pathway. Threonine deaminase is a tetramer . It has been alternately reported that either two or four pyridoxal phosphate molecules bind per tetramer . In the complete absence of pyridoxal phosphate, the enzyme dissociates into nonfunctional 102 kD dimers . It has also been suggested that IlvA has several active multimeric forms, rather than being solely active as a tetramer . The regulatory small molecules valine and isoleucine both bind threonine deaminase at four molecules per tetramer, the former cooperatively . Isoleucine binds only twice per tetramer . Crystal structures of threonine deaminase to 2.8 and 2.9 Å resolution reveal that it is a dimer of dimers, consisting of a set of carboxy-terminal regulatory domains projecting outward from a core of pyridoxal-containing amino-termini . The regulatory domains possessed two effector-binding sites . Valine and isoleucine work to promote states with high and low affinity, respectively, for threonine. Isoleucine also appears to directly impact catalysis . IlvA is cotranslated with IlvD . In addition to this contranslation, ilvA can also be transcribed and translated separately from its own oxygen-sensitive promoter . IlvA abundance increases following treatment of cells with glycyl-leucine . Mutations in ilvA code for enzymes with significantly reduced th

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P04968|protein.P04968]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:THREDEHYDSYN-CPLX`
- `QSPROTEOME:QS00197015`

## Notes

4*protein.P04968

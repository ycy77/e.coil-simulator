---
entity_id: "complex.ecocyc.CPLX0-7808"
entity_type: "complex"
name: "coproporphyrinogen III oxidase"
source_database: "EcoCyc"
source_id: "CPLX0-7808"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# coproporphyrinogen III oxidase

`complex.ecocyc.CPLX0-7808`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7808`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P36553|protein.P36553]]

## Enriched Summary

Oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX is catalyzed by two enzymes in E. coli. Under anaerobic conditions, the EG11836 hemN gene product is active . Under aerobic conditions, HemF catalyzes the coproporphyrinogen III oxidase reaction. HemF is a strictly aerobic enzyme, requiring molecular oxygen as the electron acceptor and producing hydrogen peroxide . During hydrogen peroxide stress, the HemF activity becomes critical, replacing HemN . His and Trp residues essential for catalytic activity were identified by kinetic analysis of mutant enzymes . Overexpression of hemF can suppress the growth defect of a hemG mutant; thus, HemF was hypothesized to be able to oxidize protoporphyrinogen IX as well . However, no such activity was found in vitro . HemF synthesis is induced by OxyR in response to low chronic oxidative stress. A ΔhemF mutant is extremely sensitive to externally added hydrogen peroxide . Oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX is catalyzed by two enzymes in E. coli. Under anaerobic conditions, the EG11836 hemN gene product is active . Under aerobic conditions, HemF catalyzes the coproporphyrinogen III oxidase reaction. HemF is a strictly aerobic enzyme, requiring molecular oxygen as the electron acceptor and producing hydrogen peroxide...

## Biological Role

Catalyzes RXN0-1461 (reaction.ecocyc.RXN0-1461). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

Oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX is catalyzed by two enzymes in E. coli. Under anaerobic conditions, the EG11836 hemN gene product is active . Under aerobic conditions, HemF catalyzes the coproporphyrinogen III oxidase reaction. HemF is a strictly aerobic enzyme, requiring molecular oxygen as the electron acceptor and producing hydrogen peroxide . During hydrogen peroxide stress, the HemF activity becomes critical, replacing HemN . His and Trp residues essential for catalytic activity were identified by kinetic analysis of mutant enzymes . Overexpression of hemF can suppress the growth defect of a hemG mutant; thus, HemF was hypothesized to be able to oxidize protoporphyrinogen IX as well . However, no such activity was found in vitro . HemF synthesis is induced by OxyR in response to low chronic oxidative stress. A ΔhemF mutant is extremely sensitive to externally added hydrogen peroxide .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1461|reaction.ecocyc.RXN0-1461]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P36553|protein.P36553]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7808`
- `QSPROTEOME:QS00049666`

## Notes

2*protein.P36553

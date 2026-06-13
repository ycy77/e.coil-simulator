---
entity_id: "complex.ecocyc.CPLX-8331"
entity_type: "complex"
name: "cyclic pyranopterin monophosphate synthase"
source_database: "EcoCyc"
source_id: "CPLX-8331"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cyclic pyranopterin monophosphate synthase

`complex.ecocyc.CPLX-8331`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-8331`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A738|protein.P0A738]]

## Enriched Summary

MoaC participates in the PWY-6823 pathway, catalyzing the formation of the cyclic pyranopterin monophosphate intermediate . Crystal structures of wild-type and mutant MoaC and an inactive MoaC mutant in complex with 3',8-cH2GTP have been solved. The enzyme is organized into a tightly packed hexamer that is arranged in a trimer-of-dimers form. The monomer consists of an antiparallel, four-stranded beta sheet packed against two long alpha helices, and its fold belongs to the ferredoxin-like family. The active site is located at the interface of two monomers in a pocket that contains several strictly conserved residues . Genes encoding T117P and D128A substitutions did not complement a moaC mutant . Additional residues critical for activity have been identified by site-directed mutagenesis. Based on studies of trapped reaction intermediates within active site mutants, a reaction mechanism was proposed . Further mechanistic characterization using an uncleavable substrate analogue indicated that during the last step of catalysis, formation of the cyclic phosphate is coupled to pterin ring formation and likely provides the thermodynamic driving force for formation of the tetracyclic pyranopterin . Using an E. coli strain overproducing MoaA and MoaC, precursor Z was produced, purified, and chemically characterized...

## Biological Role

Catalyzes RXN-17809 (reaction.ecocyc.RXN-17809).

## Annotation

MoaC participates in the PWY-6823 pathway, catalyzing the formation of the cyclic pyranopterin monophosphate intermediate . Crystal structures of wild-type and mutant MoaC and an inactive MoaC mutant in complex with 3',8-cH2GTP have been solved. The enzyme is organized into a tightly packed hexamer that is arranged in a trimer-of-dimers form. The monomer consists of an antiparallel, four-stranded beta sheet packed against two long alpha helices, and its fold belongs to the ferredoxin-like family. The active site is located at the interface of two monomers in a pocket that contains several strictly conserved residues . Genes encoding T117P and D128A substitutions did not complement a moaC mutant . Additional residues critical for activity have been identified by site-directed mutagenesis. Based on studies of trapped reaction intermediates within active site mutants, a reaction mechanism was proposed . Further mechanistic characterization using an uncleavable substrate analogue indicated that during the last step of catalysis, formation of the cyclic phosphate is coupled to pterin ring formation and likely provides the thermodynamic driving force for formation of the tetracyclic pyranopterin . Using an E. coli strain overproducing MoaA and MoaC, precursor Z was produced, purified, and chemically characterized . In earlier work, expression of genes moaABC in a moeA mutant resulted in the production of "compound Z", an oxidized product of precursor Z . Mutants in molybdenum cofactor (MoCo) biosynthesis genes were initially identified by their chlorate resistance and hence named "chl"; the mutant phenotype is due to the lack of several enzymes that require MoCo for activity, such as nitrate reductase (see e.g. ). chlA3: "chlorate resistance A" MoaC: "molybdenum cofactor bios

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-17809|reaction.ecocyc.RXN-17809]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A738|protein.P0A738]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX-8331`
- `QSPROTEOME:QS00181781`

## Notes

6*protein.P0A738

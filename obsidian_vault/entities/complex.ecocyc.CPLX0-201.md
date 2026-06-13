---
entity_id: "complex.ecocyc.CPLX0-201"
entity_type: "complex"
name: "fructose-6-phosphate aldolase 1"
source_database: "EcoCyc"
source_id: "CPLX0-201"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FSA 1"
---

# fructose-6-phosphate aldolase 1

`complex.ecocyc.CPLX0-201`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-201`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P78055|protein.P78055]]

## Enriched Summary

Fructose 6-phosphate aldolase (FSA, FsaA) is a class I aldolase whose physiological role is not yet known . Flux-balance analysis suggests that high flux through the fructose 6-phosphate aldolase reaction is unlikely in vivo . Class I aldolases catalyze an aldol addition between a ketone donor and an aldose acceptor. Catalysis involves formation of a Schiff base intermediate between the catalytic lysine residue (Lys85) and the donor substrate. Crystal structures of the wild type enzyme and several point mutants have been solved . Two pentameric rings of FsaA monomers combine to form a decameric complex . A detailed catalytic mechanism was proposed, involving Tyr131 as a general acid/base residue . The application of this enzyme and certain mutants for stereoselective synthesis of deoxysugars has been investigated, e.g. , and FsaA has been exploited in metabolic engineering applications, e.g. . The substrate range of the enzyme was broadened by structure-guided mutagenesis of noncatalytic residues within the active site . During growth on dihydroxyacetone (DHA) as the sole source of carbon in a ΔdhaKLM mutant, expression of fsaA (which could provide an alternative pathway for DHA utilization) is not upregulated; however, the growth rate of a ΔfsaA mutant on DHA is somewhat reduced compared to wild-type...

## Biological Role

Catalyzes RXN0-313 (reaction.ecocyc.RXN0-313).

## Annotation

Fructose 6-phosphate aldolase (FSA, FsaA) is a class I aldolase whose physiological role is not yet known . Flux-balance analysis suggests that high flux through the fructose 6-phosphate aldolase reaction is unlikely in vivo . Class I aldolases catalyze an aldol addition between a ketone donor and an aldose acceptor. Catalysis involves formation of a Schiff base intermediate between the catalytic lysine residue (Lys85) and the donor substrate. Crystal structures of the wild type enzyme and several point mutants have been solved . Two pentameric rings of FsaA monomers combine to form a decameric complex . A detailed catalytic mechanism was proposed, involving Tyr131 as a general acid/base residue . The application of this enzyme and certain mutants for stereoselective synthesis of deoxysugars has been investigated, e.g. , and FsaA has been exploited in metabolic engineering applications, e.g. . The substrate range of the enzyme was broadened by structure-guided mutagenesis of noncatalytic residues within the active site . During growth on dihydroxyacetone (DHA) as the sole source of carbon in a ΔdhaKLM mutant, expression of fsaA (which could provide an alternative pathway for DHA utilization) is not upregulated; however, the growth rate of a ΔfsaA mutant on DHA is somewhat reduced compared to wild-type . Expression of wild-type fsaA does not rescue growth of a pfkA pfkB zwf mutant on glucose; however, expression of an FsaA A129S mutant does . FsaA: "fructose-six-phosphate aldolase A" Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-313|reaction.ecocyc.RXN0-313]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P78055|protein.P78055]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:CPLX0-201`
- `QSPROTEOME:QS00181693`

## Notes

10*protein.P78055

---
entity_id: "complex.ecocyc.CPLX0-7927"
entity_type: "complex"
name: "NADPH-dependent curcumin/dihydrocurcumin reductase"
source_database: "EcoCyc"
source_id: "CPLX0-7927"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NADPH-dependent curcumin/dihydrocurcumin reductase

`complex.ecocyc.CPLX0-7927`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7927`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76113|protein.P76113]]

## Enriched Summary

The purified product of Escherichia coli gene curA was shown to catalyze the NADPH-dependent, sequential reduction of curcumin first to the stable intermediate dihydrocurcumin, and then to the final end product tetrahydrocurcumin. Curcumin is a plant secondary metabolite and curcumin metabolizing microorganisms were found in samples of human feces. The organism with the highest curcumin converting activity was isolated, cultured and identified as Escherichia coli. High curcumin converting activity was also identified in Escherichia coli K-12 substr. DH10B whose genome sequence has been determined. The curcumin metabolizing enzyme was purified from extracts of this organism and used to identify its encoding gene. Following gene cloning and overexpression, the recombinant enzyme was purified and characterized. The results showed that E. coli gene yncB encoded the curcumin-converting enzyme and it was renamed curA . CurA protein showed amino acid sequence similarity with some members of the medium-chain dehydrogenase/reductase (MDR) superfamily. Due to its non-requirement for Zn2+ the enzyme is a member of a zinc-independent family of the MDR superfamily. Creation of a C247A mutant in a putative NADPH binding site by site-directed mutagenesis and purification and assay of the resulting enzyme showed an approximately 50% reduction in activity in this mutant...

## Biological Role

Catalyzes RXN0-6676 (reaction.ecocyc.RXN0-6676), RXN0-6677 (reaction.ecocyc.RXN0-6677).

## Annotation

The purified product of Escherichia coli gene curA was shown to catalyze the NADPH-dependent, sequential reduction of curcumin first to the stable intermediate dihydrocurcumin, and then to the final end product tetrahydrocurcumin. Curcumin is a plant secondary metabolite and curcumin metabolizing microorganisms were found in samples of human feces. The organism with the highest curcumin converting activity was isolated, cultured and identified as Escherichia coli. High curcumin converting activity was also identified in Escherichia coli K-12 substr. DH10B whose genome sequence has been determined. The curcumin metabolizing enzyme was purified from extracts of this organism and used to identify its encoding gene. Following gene cloning and overexpression, the recombinant enzyme was purified and characterized. The results showed that E. coli gene yncB encoded the curcumin-converting enzyme and it was renamed curA . CurA protein showed amino acid sequence similarity with some members of the medium-chain dehydrogenase/reductase (MDR) superfamily. Due to its non-requirement for Zn2+ the enzyme is a member of a zinc-independent family of the MDR superfamily. Creation of a C247A mutant in a putative NADPH binding site by site-directed mutagenesis and purification and assay of the resulting enzyme showed an approximately 50% reduction in activity in this mutant . The apparent molecular mass of the complex was determined by gel filtration chromatography and the apparent molecular mass of the subunit was determined by SDS-PAGE. The absorption spectrum of the enzyme suggested that the enzyme contained no bound cofactor. Qualitative and quantitative analysis for a variety of metals showed no metal content. The enzyme secondary structure showed a surprisingly wide range of pH stabil

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6676|reaction.ecocyc.RXN0-6676]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6677|reaction.ecocyc.RXN0-6677]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76113|protein.P76113]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7927`
- `QSPROTEOME:QS00049677`

## Notes

2*protein.P76113

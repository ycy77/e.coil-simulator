---
entity_id: "complex.ecocyc.GAPDH-A-CPLX"
entity_type: "complex"
name: "glyceraldehyde-3-phosphate dehydrogenase"
source_database: "EcoCyc"
source_id: "GAPDH-A-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GAPDH-A"
---

# glyceraldehyde-3-phosphate dehydrogenase

`complex.ecocyc.GAPDH-A-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GAPDH-A-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P0A9B2|protein.P0A9B2]]

## Enriched Summary

Glyceraldehyde 3-phosphate dehydrogenase A catalyzes the reversible oxidative phosphorylation of D-glyceraldehyde-3-phosphate to 1,3-bisphospho-D-glycerate in the presence of NAD+ and phosphate during glycolysis and gluconeogenesis in E. coli. The enzyme is also found in many other organisms and its properties have been extensively studied (see ). E. coli is unusual in having two glyceraldehyde-3-phosphate dehydrogenase (GAPDH) activities encoded by gapA and EG10368 (gapB). However, the gapA encoded enzyme has a highly efficient phosphorylating glyceraldehyde-3-phosphate dehydrogenase activity and a low phosphorylating erythrose-4-phosphate dehydrogenase activity, whereas the epd encoded enzyme has an efficient non-phosphorylating erythrose-4-phosphate dehydrogenase activity and a very low phosphorylating glyceraldehyde-3-phosphate dehydrogenase activity . The GapA protein has a sequence that is more similar to eukaryotic sequences than to the thermophilic bacterial enzymes, and to prokaryotic enzymes in general . The gapA product is required for glycolysis, while the epd product is not . Both enzymes may be involved in production of pyridoxal 5'-phosphate (PLP) . Early studies of gapA mutants from E. coli K-10 implicated its role in glycolysis and demonstrated some of its catalytic properties...

## Biological Role

Catalyzes GAPOXNPHOSPHN-RXN (reaction.ecocyc.GAPOXNPHOSPHN-RXN).

## Annotation

Glyceraldehyde 3-phosphate dehydrogenase A catalyzes the reversible oxidative phosphorylation of D-glyceraldehyde-3-phosphate to 1,3-bisphospho-D-glycerate in the presence of NAD+ and phosphate during glycolysis and gluconeogenesis in E. coli. The enzyme is also found in many other organisms and its properties have been extensively studied (see ). E. coli is unusual in having two glyceraldehyde-3-phosphate dehydrogenase (GAPDH) activities encoded by gapA and EG10368 (gapB). However, the gapA encoded enzyme has a highly efficient phosphorylating glyceraldehyde-3-phosphate dehydrogenase activity and a low phosphorylating erythrose-4-phosphate dehydrogenase activity, whereas the epd encoded enzyme has an efficient non-phosphorylating erythrose-4-phosphate dehydrogenase activity and a very low phosphorylating glyceraldehyde-3-phosphate dehydrogenase activity . The GapA protein has a sequence that is more similar to eukaryotic sequences than to the thermophilic bacterial enzymes, and to prokaryotic enzymes in general . The gapA product is required for glycolysis, while the epd product is not . Both enzymes may be involved in production of pyridoxal 5'-phosphate (PLP) . Early studies of gapA mutants from E. coli K-10 implicated its role in glycolysis and demonstrated some of its catalytic properties . A gapA mutant exhibits a growth defect and also exhibits increased aggregation and lysis phenotypes that are rescued by high-salt media . Regulation of gapA gene expression has been studied . The regulation of the fkpA, gapA, and hslT genes is affected by evolution under conditions of chronic heat stress . The E.coli sequence contains several amino acids that are conserved in all GAPDHs and are postulated to be involved NAD+ binding, or the catalytic mechanism . The crystal stru

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GAPOXNPHOSPHN-RXN|reaction.ecocyc.GAPOXNPHOSPHN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9B2|protein.P0A9B2]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GAPDH-A-CPLX`
- `QSPROTEOME:QS00188853`

## Notes

4*protein.P0A9B2

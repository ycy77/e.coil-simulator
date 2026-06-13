---
entity_id: "complex.ecocyc.ISOCIT-LYASE"
entity_type: "complex"
name: "isocitrate lyase"
source_database: "EcoCyc"
source_id: "ISOCIT-LYASE"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# isocitrate lyase

`complex.ecocyc.ISOCIT-LYASE`

## Static

- Type: `complex`
- Source: `EcoCyc:ISOCIT-LYASE`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9G6|protein.P0A9G6]]

## Enriched Summary

Isocitrate lyase catalyzes the reversible conversion of THREO-DS-ISO-CITRATE to SUC and GLYOX. The formation of glyoxylate is a key reaction in the GLYOXYLATE-BYPASS. The glyoxylate cycle is similar to the TCA cycle (see TCA) but it bypasses the TCA cycle reactions that lead to a loss of CARBON-DIOXIDE, thus providing TCA cycle intermediates for cell carbon biosynthesis (see TCA-GLYOX-BYPASS). The glyoxylate cycle has been extensively studied in connection with growth on acetate which is used in the synthesis of these biosynthetic precursors. Isocitrate lyase has been characterized from E. coli K-12 strains ML308 and D5H3G7 (the strain origins can be found in , respectively). Its encoding gene aceA has been characterized as part of the aceBAK operon which is transcriptionally regulated by iclR and fadR and inducible by growth on acetate and is repressed on most other carbon sources . The enzyme purified from cell extracts was characterized as a homotetramer . Its crystal structure determined at 2.1 Å resolution showed a tetramer in the asymmetric unit . Recombinant, N-terminally His-tagged enzyme has also been overexpressed, purified and characterized . The enzyme was shown to be phosphorylated in vivo and in vitro, probably at histidine residues, and that the phosphorylated form is the catalytically active form . Biochemical characterization of isocitrate lyase from E...

## Biological Role

Catalyzes ISOCIT-CLEAV-RXN (reaction.ecocyc.ISOCIT-CLEAV-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Isocitrate lyase catalyzes the reversible conversion of THREO-DS-ISO-CITRATE to SUC and GLYOX. The formation of glyoxylate is a key reaction in the GLYOXYLATE-BYPASS. The glyoxylate cycle is similar to the TCA cycle (see TCA) but it bypasses the TCA cycle reactions that lead to a loss of CARBON-DIOXIDE, thus providing TCA cycle intermediates for cell carbon biosynthesis (see TCA-GLYOX-BYPASS). The glyoxylate cycle has been extensively studied in connection with growth on acetate which is used in the synthesis of these biosynthetic precursors. Isocitrate lyase has been characterized from E. coli K-12 strains ML308 and D5H3G7 (the strain origins can be found in , respectively). Its encoding gene aceA has been characterized as part of the aceBAK operon which is transcriptionally regulated by iclR and fadR and inducible by growth on acetate and is repressed on most other carbon sources . The enzyme purified from cell extracts was characterized as a homotetramer . Its crystal structure determined at 2.1 Å resolution showed a tetramer in the asymmetric unit . Recombinant, N-terminally His-tagged enzyme has also been overexpressed, purified and characterized . The enzyme was shown to be phosphorylated in vivo and in vitro, probably at histidine residues, and that the phosphorylated form is the catalytically active form . Biochemical characterization of isocitrate lyase from E. coli K-12 cells grown on acetate or glycolate suggested that only one form of the enzyme exists, with no isoforms . Cysteine sites in peptides of this AceA protein were significantly oxidized in a redox proteomics study in a ΔCPLX0-245 Ahp mutant . Site-directed mutagenesis and modification studies identified Cys195 as important to activity . Site-directed mutagenesis also identified residues Lys193, Lys

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9G6|protein.P0A9G6]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ISOCIT-LYASE`
- `QSPROTEOME:QS00195657`

## Notes

4*protein.P0A9G6

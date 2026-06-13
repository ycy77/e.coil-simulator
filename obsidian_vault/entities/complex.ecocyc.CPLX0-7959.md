---
entity_id: "complex.ecocyc.CPLX0-7959"
entity_type: "complex"
name: "adenylosuccinate lyase"
source_database: "EcoCyc"
source_id: "CPLX0-7959"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# adenylosuccinate lyase

`complex.ecocyc.CPLX0-7959`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7959`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AB89|protein.P0AB89]]

## Enriched Summary

Adenylosuccinate lyase (ASL), the product of the gene purB in E. coli, catalyzes two reactions in de novo purine nucleotide biosynthesis. In addition to the removal of fumarate from 5'-phosphoribosyl-4-(N-succinocarboxamide)-5-aminoimidazole, the enzyme also converts adenylosuccinate to AMP . The enzyme was concluded to be a homotetramer, with a subunit apparent molecular mass of 49.5 kDa determined by SDS-PAGE and a mean native molecular mass of 211 kDa determined by non-denaturing PAGE . Crystal structures of the wild-type and mutant enzymes also indicated a homotetramer . Note that the PDB link 3GZH () states that the organism is E. coli O157H7, therefore it is shown here as an ortholog. PurB is a member of the aspartase/fumarase superfamily (β-elimination superfamily) . The role of His171 in catalysis has been identified . An E115K mutation in purB was shown to result in slower growth of E. coli strain DH5α in minimal medium. Replacement with the wild-type allele from E. coli K-12 resulted in an enhanced growth phenotype . Deletion of purB or purA was shown to result in a decrease in acid resistance, apparently due to the effects of decreased ATP biosynthesis on processes that require ATP for survival under acidic conditions . Review: Adenylosuccinate lyase (ASL), the product of the gene purB in E. coli, catalyzes two reactions in de novo purine nucleotide biosynthesis...

## Biological Role

Catalyzes AICARSYN-RXN (reaction.ecocyc.AICARSYN-RXN), AMPSYN-RXN (reaction.ecocyc.AMPSYN-RXN).

## Annotation

Adenylosuccinate lyase (ASL), the product of the gene purB in E. coli, catalyzes two reactions in de novo purine nucleotide biosynthesis. In addition to the removal of fumarate from 5'-phosphoribosyl-4-(N-succinocarboxamide)-5-aminoimidazole, the enzyme also converts adenylosuccinate to AMP . The enzyme was concluded to be a homotetramer, with a subunit apparent molecular mass of 49.5 kDa determined by SDS-PAGE and a mean native molecular mass of 211 kDa determined by non-denaturing PAGE . Crystal structures of the wild-type and mutant enzymes also indicated a homotetramer . Note that the PDB link 3GZH () states that the organism is E. coli O157H7, therefore it is shown here as an ortholog. PurB is a member of the aspartase/fumarase superfamily (β-elimination superfamily) . The role of His171 in catalysis has been identified . An E115K mutation in purB was shown to result in slower growth of E. coli strain DH5α in minimal medium. Replacement with the wild-type allele from E. coli K-12 resulted in an enhanced growth phenotype . Deletion of purB or purA was shown to result in a decrease in acid resistance, apparently due to the effects of decreased ATP biosynthesis on processes that require ATP for survival under acidic conditions . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.AICARSYN-RXN|reaction.ecocyc.AICARSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.AMPSYN-RXN|reaction.ecocyc.AMPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AB89|protein.P0AB89]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7959`
- `QSPROTEOME:QS00181577`

## Notes

4*protein.P0AB89

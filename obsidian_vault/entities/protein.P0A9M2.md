---
entity_id: "protein.P0A9M2"
entity_type: "protein"
name: "hpt"
source_database: "UniProt"
source_id: "P0A9M2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hpt b0125 JW5009"
---

# hpt

`protein.P0A9M2`

## Static

- Type: `protein`
- Source: `UniProt:P0A9M2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Purine salvage pathway enzyme which catalyzes the transfer of the ribosyl-5-phosphate group from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to the N9 position of hypoxanthine to yield IMP (inosine 5'-monophosphate). To a lesser extent, can also act on guanine leading to GMP, but shows a highly less efficient activity with xanthine. {ECO:0000269|PubMed:12070315}.

## Biological Role

Catalyzes XMP:pyrophosphate phosphoribosyltransferase (reaction.R02142). Component of hypoxanthine phosphoribosyltransferase (complex.ecocyc.CPLX0-7685).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Purine salvage pathway enzyme which catalyzes the transfer of the ribosyl-5-phosphate group from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to the N9 position of hypoxanthine to yield IMP (inosine 5'-monophosphate). To a lesser extent, can also act on guanine leading to GMP, but shows a highly less efficient activity with xanthine. {ECO:0000269|PubMed:12070315}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02142|reaction.R02142]] `KEGG` `database` - via EC:2.4.2.8
- `is_component_of` --> [[complex.ecocyc.CPLX0-7685|complex.ecocyc.CPLX0-7685]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0125|gene.b0125]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9M2`
- `KEGG:ecj:JW5009;eco:b0125;ecoc:C3026_00530;`
- `GeneID:86862633;946624;`
- `GO:GO:0000287; GO:0004422; GO:0005829; GO:0006166; GO:0006178; GO:0032263; GO:0032264; GO:0032991; GO:0042802; GO:0046100; GO:0051289; GO:0052657; GO:0097216`
- `EC:2.4.2.8`

## Notes

Hypoxanthine phosphoribosyltransferase (HPRT) (EC 2.4.2.8) (6-oxopurine phosphoribosyltransferase) (6-oxopurine PRTase)

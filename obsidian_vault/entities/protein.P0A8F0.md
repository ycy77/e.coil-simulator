---
entity_id: "protein.P0A8F0"
entity_type: "protein"
name: "upp"
source_database: "UniProt"
source_id: "P0A8F0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "upp uraP b2498 JW2483"
---

# upp

`protein.P0A8F0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8F0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of uracil and 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to UMP and diphosphate.

## Biological Role

Component of uracil phosphoribosyltransferase (complex.ecocyc.URACIL-PRIBOSYLTRANS-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of uracil and 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to UMP and diphosphate.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.URACIL-PRIBOSYLTRANS-CPLX|complex.ecocyc.URACIL-PRIBOSYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2498|gene.b2498]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8F0`
- `KEGG:ecj:JW2483;eco:b2498;ecoc:C3026_13855;`
- `GeneID:86860619;93774638;946979;`
- `GO:GO:0000287; GO:0004845; GO:0005525; GO:0005737; GO:0005829; GO:0006206; GO:0006223; GO:0016020; GO:0042802; GO:0044206; GO:0097216`
- `EC:2.4.2.9`

## Notes

Uracil phosphoribosyltransferase (EC 2.4.2.9) (UMP pyrophosphorylase) (UPRTase)

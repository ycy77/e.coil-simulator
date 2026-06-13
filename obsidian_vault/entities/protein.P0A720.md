---
entity_id: "protein.P0A720"
entity_type: "protein"
name: "tmk"
source_database: "UniProt"
source_id: "P0A720"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tmk ycfG b1098 JW1084"
---

# tmk

`protein.P0A720`

## Static

- Type: `protein`
- Source: `UniProt:P0A720`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible phosphorylation of deoxythymidine monophosphate (dTMP) to deoxythymidine diphosphate (dTDP), using ATP as its preferred phosphoryl donor (PubMed:8631667). Situated at the junction of both de novo and salvage pathways of deoxythymidine triphosphate (dTTP) synthesis, is essential for DNA synthesis and cellular growth. {ECO:0000269|PubMed:8631667}.

## Biological Role

Component of dTMP kinase (complex.ecocyc.CPLX0-8260).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible phosphorylation of deoxythymidine monophosphate (dTMP) to deoxythymidine diphosphate (dTDP), using ATP as its preferred phosphoryl donor (PubMed:8631667). Situated at the junction of both de novo and salvage pathways of deoxythymidine triphosphate (dTTP) synthesis, is essential for DNA synthesis and cellular growth. {ECO:0000269|PubMed:8631667}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8260|complex.ecocyc.CPLX0-8260]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1098|gene.b1098]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A720`
- `KEGG:ecj:JW1084;eco:b1098;ecoc:C3026_06635;`
- `GeneID:93776310;945663;`
- `GO:GO:0004798; GO:0005524; GO:0005737; GO:0005829; GO:0006227; GO:0006233; GO:0006235; GO:0015949; GO:0042803`
- `EC:2.7.4.9`

## Notes

Thymidylate kinase (EC 2.7.4.9) (Thymidine monophosphate kinase) (dTMP kinase) (TMPK)

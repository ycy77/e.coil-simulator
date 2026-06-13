---
entity_id: "protein.P00350"
entity_type: "protein"
name: "gnd"
source_database: "UniProt"
source_id: "P00350"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gnd b2029 JW2011"
---

# gnd

`protein.P00350`

## Static

- Type: `protein`
- Source: `UniProt:P00350`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidative decarboxylation of 6-phosphogluconate to ribulose 5-phosphate and CO(2), with concomitant reduction of NADP to NADPH. {ECO:0000269|PubMed:19686854}. 6-phosphogluconate dehydrogenase (6PGDH) is an enzyme of the oxidative branch of the pentose phosphate pathway. Three crystal structures of the enzyme in complex with substrate and cosubstrate compounds have been solved. Binding of NADP+ may induce a conformational change in the enzyme. A catalytic mechanism has been proposed . gnd is a highly polymorphic gene within E. coli populations, likely due to interstrain transfer and recombination. This may be a result of its proximity to the rfb region, which determines O antigen structure . Expression of 6PGDH is growth rate-regulated . Most of the growth rate-dependent increase in 6PGDH levels is due to increased transcription, leading to higher mRNA levels . Post-transcriptional regulation involves a secondary structure element between codons 67 and 78 of the gnd mRNA . This region may function by sequestration of the translation initiation region into an mRNA secondary structure, thus reducing the efficiency of translation initiation . However, the effector of this regulatory mechanism has apparently not yet been identified. truA (hisT) mutants reduce the growth rate-dependent increase of 6PGDH expression by post-transcriptional regulation...

## Biological Role

Catalyzes 6-phospho-D-gluconate:NADP+ 2-oxidoreductase (decarboxylating) (reaction.R01528), 6-phospho-D-gluconate:NAD+ 2-oxidoreductase (decarboxylating) (reaction.R10221). Component of 6-phosphogluconate dehydrogenase, decarboxylating (complex.ecocyc.6PGLUCONDEHYDROG-CPLX).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidative decarboxylation of 6-phosphogluconate to ribulose 5-phosphate and CO(2), with concomitant reduction of NADP to NADPH. {ECO:0000269|PubMed:19686854}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R01528|reaction.R01528]] `KEGG` `database` - via EC:1.1.1.44
- `catalyzes` --> [[reaction.R10221|reaction.R10221]] `KEGG` `database` - via EC:1.1.1.343
- `is_component_of` --> [[complex.ecocyc.6PGLUCONDEHYDROG-CPLX|complex.ecocyc.6PGLUCONDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2029|gene.b2029]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00350`
- `KEGG:ecj:JW2011;eco:b2029;ecoc:C3026_11435;`
- `GeneID:946554;`
- `GO:GO:0004616; GO:0005829; GO:0006098; GO:0009051; GO:0019521; GO:0042802; GO:0042803; GO:0050661; GO:0097216`
- `EC:1.1.1.44`

## Notes

6-phosphogluconate dehydrogenase, decarboxylating (EC 1.1.1.44)

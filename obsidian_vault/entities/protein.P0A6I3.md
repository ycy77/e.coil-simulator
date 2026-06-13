---
entity_id: "protein.P0A6I3"
entity_type: "protein"
name: "coaA"
source_database: "UniProt"
source_id: "P0A6I3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "coaA panK rts b3974 JW3942"
---

# coaA

`protein.P0A6I3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6I3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

Pantothenate kinase (EC 2.7.1.33) (Pantothenic acid kinase) (Rts protein) Pantothenate kinase catalyzes the first step in the biosynthesis of coenzyme A, an essential cofactor that is involved in many reactions. This reaction is also the most highly regulated step in the pathway . Pantothenate kinase is sensitive to feedback inhibition by the CoA pool . Mutants that are refractory to feedback inhibition, but retain catalytic activity, have been isolated; these mutants have a higher intracellular CoA content and secrete 4'-phosphopantetheine . The compounds CPD0-1152 and CPD0-1153 are competitive inhibitors of pantothenate kinase and can be utilized as substrates of the CoA biosynthesis pathway . The phosphopantothenimide moiety is transferred to ACP, rendering it incapable of supporting fatty acid biosynthesis. Thus, CPD0-1152 and CPD0-1153 are pro-antibiotics , explaining earlier results . Further inhibitors/substrates of pantothenate kinase have been designed and tested . Growth rescue of a EG10004 dfp null mutant by addition of pantethine requires the pantetheine kinase activity of CoaA . Utilization of two different translation start sites of coaA results in proteins that differ by eight amino acids at the N terminus...

## Biological Role

Component of pantothenate kinase / pantetheine kinase (complex.ecocyc.PANTOTHENATE-KIN-CPLX).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

Pantothenate kinase (EC 2.7.1.33) (Pantothenic acid kinase) (Rts protein)

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PANTOTHENATE-KIN-CPLX|complex.ecocyc.PANTOTHENATE-KIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3974|gene.b3974]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6I3`
- `KEGG:ecj:JW3942;eco:b3974;`
- `GeneID:93777919;948479;`
- `GO:GO:0004594; GO:0005524; GO:0005737; GO:0015937; GO:0042803; GO:0050165`
- `EC:2.7.1.33`

## Notes

Pantothenate kinase (EC 2.7.1.33) (Pantothenic acid kinase) (Rts protein)

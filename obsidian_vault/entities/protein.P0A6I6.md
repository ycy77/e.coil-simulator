---
entity_id: "protein.P0A6I6"
entity_type: "protein"
name: "coaD"
source_database: "UniProt"
source_id: "P0A6I6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00151}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "coaD kdtB yicA b3634 JW3609"
---

# coaD

`protein.P0A6I6`

## Static

- Type: `protein`
- Source: `UniProt:P0A6I6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00151}.

## Enriched Summary

FUNCTION: Reversibly transfers an adenylyl group from ATP to 4'-phosphopantetheine, yielding dephospho-CoA (dPCoA) and pyrophosphate (PubMed:10480925, PubMed:17873050). CoA is not a substrate for the enzyme (PubMed:10480925). {ECO:0000255|HAMAP-Rule:MF_00151, ECO:0000269|PubMed:10480925, ECO:0000269|PubMed:17873050}. Phosphopantetheine adenylyltransferase (PPAT) catalyzes the transfer of an adenyly group from ATP to 4'-phosphopantetheine . This is the penultimate reaction and a secondary rate-limiting step in CoA biosynthesis . Coenzyme A binds to the enzyme, but did not appear to influence catalytic activity of the reverse reaction . However, CoA is a competitive inhibitor of the forward reaction . The enzyme is homohexameric in solution, behaving as a dimer of trimers . Crystal and solution structures of PPAT have been solved, and the catalytic mechanism and substrate interactions have been characterized . The reverse reaction appears to proceed via a ternary complex mechanism ; product inhibition studies of the forward reaction are consistent with a random bi-bi kinetic mechanism . The functional landscape of PPAT was investigated by broad mutational scanning, a technique whereby homologs from hundreds of different organisms are evaluated for the ability to complement an E. coli mutant . coaD is essential for growth in complex media...

## Biological Role

Component of pantetheine-phosphate adenylyltransferase (complex.ecocyc.COADTRI-CPLX).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Reversibly transfers an adenylyl group from ATP to 4'-phosphopantetheine, yielding dephospho-CoA (dPCoA) and pyrophosphate (PubMed:10480925, PubMed:17873050). CoA is not a substrate for the enzyme (PubMed:10480925). {ECO:0000255|HAMAP-Rule:MF_00151, ECO:0000269|PubMed:10480925, ECO:0000269|PubMed:17873050}.

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.COADTRI-CPLX|complex.ecocyc.COADTRI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3634|gene.b3634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6I6`
- `KEGG:ecj:JW3609;eco:b3634;ecoc:C3026_19695;`
- `GeneID:75202203;947386;`
- `GO:GO:0004595; GO:0005524; GO:0005737; GO:0015937; GO:0042802`
- `EC:2.7.7.3`

## Notes

Phosphopantetheine adenylyltransferase (EC 2.7.7.3) (Dephospho-CoA pyrophosphorylase) (Pantetheine-phosphate adenylyltransferase) (PPAT)

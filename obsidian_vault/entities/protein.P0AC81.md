---
entity_id: "protein.P0AC81"
entity_type: "protein"
name: "gloA"
source_database: "UniProt"
source_id: "P0AC81"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gloA b1651 JW1643"
---

# gloA

`protein.P0AC81`

## Static

- Type: `protein`
- Source: `UniProt:P0AC81`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the isomerization of the hemithioacetal formed spontaneously from methylglyoxal and glutathione, to S-lactoylglutathione, which is then hydrolyzed by a type II glyoxalase (GloB or GloC). Is involved in methylglyoxal (MG) detoxification (Probable) (PubMed:10913283). Involved in resistance to hypochlorous acid (HOCl), which is the active component of household bleach and a powerful antimicrobial during the innate immune response (PubMed:23536188). {ECO:0000269|PubMed:10913283, ECO:0000269|PubMed:23536188, ECO:0000305|PubMed:25670698}. Glyoxalase I catalyzes the first of two sequential steps in the conversion of methylgloxal to D-lactate. The enzyme tightly binds one ion of nickel per enzyme dimer and is the first example of a nickel-containing glyoxalase . Glyoxalase I shows lower levels of activity with a number of other metal ion cofactors including Co2+, but not including Zn2+ . Crystal structures of glyoxalase I in the apo form and in complex with various metal ions have been determined . The nickel active site structure has been probed by X-ray absorption studies . The two active sites of the homodimer are initially asymmetric; only one site binds Ni2+...

## Biological Role

Component of lactoylglutathione lyase (complex.ecocyc.GLYOXI-CPLX).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization of the hemithioacetal formed spontaneously from methylglyoxal and glutathione, to S-lactoylglutathione, which is then hydrolyzed by a type II glyoxalase (GloB or GloC). Is involved in methylglyoxal (MG) detoxification (Probable) (PubMed:10913283). Involved in resistance to hypochlorous acid (HOCl), which is the active component of household bleach and a powerful antimicrobial during the innate immune response (PubMed:23536188). {ECO:0000269|PubMed:10913283, ECO:0000269|PubMed:23536188, ECO:0000305|PubMed:25670698}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GLYOXI-CPLX|complex.ecocyc.GLYOXI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1651|gene.b1651]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC81`
- `KEGG:ecj:JW1643;eco:b1651;ecoc:C3026_09475;`
- `GeneID:93775805;946161;`
- `GO:GO:0004462; GO:0005737; GO:0005829; GO:0016151; GO:0019243; GO:0042803`
- `EC:4.4.1.5`

## Notes

Lactoylglutathione lyase (EC 4.4.1.5) (Aldoketomutase) (Glyoxalase I) (Glx I) (Ketone-aldehyde mutase) (Methylglyoxalase) (S-D-lactoylglutathione methylglyoxal lyase)

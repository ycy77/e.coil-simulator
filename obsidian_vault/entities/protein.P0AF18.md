---
entity_id: "protein.P0AF18"
entity_type: "protein"
name: "nagA"
source_database: "UniProt"
source_id: "P0AF18"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nagA b0677 JW0663"
---

# nagA

`protein.P0AF18`

## Static

- Type: `protein`
- Source: `UniProt:P0AF18`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the first step in the biosynthesis of amino-sugar-nucleotides. Catalyzes the hydrolysis of the N-acetyl group of N-acetylglucosamine-6-phosphate (GlcNAc-6-P) to yield glucosamine 6-phosphate and acetate. In vitro, can also hydrolyze substrate analogs such as N-thioacetyl-D-glucosamine-6-phosphate, N-trifluoroacetyl-D-glucosamine-6-phosphate, N-acetyl-D-glucosamine-6-sulfate, N-acetyl-D-galactosamine-6-phosphate, and N-formyl-D-glucosamine-6-phosphate. {ECO:0000269|PubMed:16630633, ECO:0000269|PubMed:17567047, ECO:0000269|PubMed:17567048, ECO:0000269|PubMed:2190615, ECO:0000269|PubMed:4861885, ECO:0000269|PubMed:9143339}. N-acetylglucosamine-6-phosphate deacetylase catalyzes the first cytoplasmic reaction in the metabolism of N-acetyl-D-glucosamine. N-acetylglucosamine can serve as the sole source of carbon for E. coli and is transported into the cell via phosphotransferase transport systems. It thus reaches the cytoplasm in the phosphorylated form, N-acetylglucosamine-6-phosphate. A catalytic mechanism of NagA involving the formation of a tetrahedral intermediate has been proposed , and the function of amino acids and the Zn2+ within the active site has been modelled . The rate-limiting step is the cleavage of the amide bond . Crystal structures of the apoenzyme, the Zn2+-containing enzyme, and a mutant have been solved...

## Biological Role

Component of N-acetylglucosamine-6-phosphate deacetylase (complex.ecocyc.NAG6PDEACET-CPLX).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the first step in the biosynthesis of amino-sugar-nucleotides. Catalyzes the hydrolysis of the N-acetyl group of N-acetylglucosamine-6-phosphate (GlcNAc-6-P) to yield glucosamine 6-phosphate and acetate. In vitro, can also hydrolyze substrate analogs such as N-thioacetyl-D-glucosamine-6-phosphate, N-trifluoroacetyl-D-glucosamine-6-phosphate, N-acetyl-D-glucosamine-6-sulfate, N-acetyl-D-galactosamine-6-phosphate, and N-formyl-D-glucosamine-6-phosphate. {ECO:0000269|PubMed:16630633, ECO:0000269|PubMed:17567047, ECO:0000269|PubMed:17567048, ECO:0000269|PubMed:2190615, ECO:0000269|PubMed:4861885, ECO:0000269|PubMed:9143339}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.NAG6PDEACET-CPLX|complex.ecocyc.NAG6PDEACET-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0677|gene.b0677]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF18`
- `KEGG:ecj:JW0663;eco:b0677;ecoc:C3026_03365;`
- `GeneID:75170675;75204968;945289;`
- `GO:GO:0006046; GO:0008270; GO:0008448; GO:0019262; GO:0032991; GO:0042802; GO:0051289`
- `EC:3.5.1.25`

## Notes

N-acetylglucosamine-6-phosphate deacetylase (GlcNAc 6-P deacetylase) (EC 3.5.1.25)

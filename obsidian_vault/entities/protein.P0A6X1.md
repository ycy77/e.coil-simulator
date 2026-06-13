---
entity_id: "protein.P0A6X1"
entity_type: "protein"
name: "hemA"
source_database: "UniProt"
source_id: "P0A6X1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemA b1210 JW1201"
---

# hemA

`protein.P0A6X1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6X1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent reduction of glutamyl-tRNA(Glu) to glutamate 1-semialdehyde (GSA). In the absence of NADPH, exhibits substrate esterase activity, leading to the release of glutamate from tRNA. {ECO:0000269|PubMed:12370189, ECO:0000269|PubMed:1569081}. Glutamyl-tRNA reductase catalyzes the first step of porphyrin biosynthesis. The reaction appears to proceed via a thioester intermediate . Determinants for recognition of Glu-tRNA(Glu) by the enzyme have been studied . HemA can be isolated in multiple multimeric forms, but the dimer may represent the functional form of the enzyme . The HemA dimer forms a tight complex with glutamate-1-semialdehyde 2,1-aminomutase, the second enzyme in the pathway, suggesting metabolic channeling of the highly reactive intermediate glutamate-1-semialdehyde . Heme limitation leads to an increase in abundance of HemA protein , although only a 3-fold increase in hemA expression can be detected . In Salmonella typhimurium, HemA abundance appears to be increased by stabilization of the protein . Mutants of hemA are dependent on δ-aminolevulinic acid (ALA) for growth and can not produce ALA from either glutamate or glutamyl-tRNA . Mutations in hemA as well as other genes coding for respiratory gene cofactor and prosthetic groups led to increased resistance to the aminoglycoside antibiotic gentamicin .

## Biological Role

Component of glutamyl-tRNA reductase (complex.ecocyc.CPLX0-3741).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent reduction of glutamyl-tRNA(Glu) to glutamate 1-semialdehyde (GSA). In the absence of NADPH, exhibits substrate esterase activity, leading to the release of glutamate from tRNA. {ECO:0000269|PubMed:12370189, ECO:0000269|PubMed:1569081}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3741|complex.ecocyc.CPLX0-3741]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1210|gene.b1210]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6X1`
- `KEGG:ecj:JW1201;eco:b1210;ecoc:C3026_07110;`
- `GeneID:945777;`
- `GO:GO:0008883; GO:0019353; GO:0042802; GO:0050661`
- `EC:1.2.1.70`

## Notes

Glutamyl-tRNA reductase (GluTR) (EC 1.2.1.70)

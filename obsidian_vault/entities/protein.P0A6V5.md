---
entity_id: "protein.P0A6V5"
entity_type: "protein"
name: "glpE"
source_database: "UniProt"
source_id: "P0A6V5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10735872}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpE b3425 JW3388"
---

# glpE

`protein.P0A6V5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6V5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10735872}.

## Enriched Summary

FUNCTION: Transferase that catalyzes the transfer of sulfur from thiosulfate to thiophilic acceptors such as cyanide or dithiols (PubMed:10735872). May function in a CysM-independent thiosulfate assimilation pathway by catalyzing the conversion of thiosulfate to sulfite, which can then be used for L-cysteine biosynthesis (PubMed:28756590). The relatively low affinity of GlpE for both thiosulfate and cyanide suggests that these compounds may not be physiological substrates (PubMed:10735872). Thioredoxin 1 or related dithiol proteins could be the physiological sulfur acceptor (PubMed:10735872). {ECO:0000269|PubMed:10735872, ECO:0000269|PubMed:28756590}.

## Biological Role

Component of thiosulfate sulfurtransferase GlpE (complex.ecocyc.CPLX0-242).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Transferase that catalyzes the transfer of sulfur from thiosulfate to thiophilic acceptors such as cyanide or dithiols (PubMed:10735872). May function in a CysM-independent thiosulfate assimilation pathway by catalyzing the conversion of thiosulfate to sulfite, which can then be used for L-cysteine biosynthesis (PubMed:28756590). The relatively low affinity of GlpE for both thiosulfate and cyanide suggests that these compounds may not be physiological substrates (PubMed:10735872). Thioredoxin 1 or related dithiol proteins could be the physiological sulfur acceptor (PubMed:10735872). {ECO:0000269|PubMed:10735872, ECO:0000269|PubMed:28756590}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-242|complex.ecocyc.CPLX0-242]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3425|gene.b3425]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6V5`
- `KEGG:ecj:JW3388;eco:b3425;ecoc:C3026_18570;`
- `GeneID:93778571;947935;`
- `GO:GO:0004792; GO:0005737; GO:0006791; GO:0103041`
- `EC:2.8.1.1`

## Notes

Thiosulfate sulfurtransferase GlpE (EC 2.8.1.1) (Thiosulfate:cyanide sulfurtransferase)

---
entity_id: "protein.P0AGB0"
entity_type: "protein"
name: "serB"
source_database: "UniProt"
source_id: "P0AGB0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "serB b4388 JW4351"
---

# serB

`protein.P0AGB0`

## Static

- Type: `protein`
- Source: `UniProt:P0AGB0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of phosphoserine (P-Ser). Also catalyzes the hydrolysis of phosphothreonine (P-Thr). {ECO:0000269|PubMed:16990279}. Phosphoserine phosphatase catalyzes the last step in serine biosynthesis. The enzyme belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . Enzymatic studies were originally performed using partially purified enzyme from E. coli strain W ; assays of the purified enzyme were performed as part of an investigation of the HAD superfamily of enzymes . serB is essential for growth on glycerol minimal medium; the growth defect can be rescued by addition of serine . GPH-MONOMER Gph, IMIDHISTID-CPLX HisB and PGAM2-MONOMER YtjC were identified as multicopy suppressors of the conditional ΔserB phenotype . Directed evolution experiments identified mutations that increased fitness and enzymatic activity of these suppressors . Review:

## Biological Role

Catalyzes O-phospho-L-serine phosphohydrolase (reaction.R00582), D-O-phosphoserine phosphohydrolase (reaction.R02853), RXN0-5114 (reaction.ecocyc.RXN0-5114). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of phosphoserine (P-Ser). Also catalyzes the hydrolysis of phosphothreonine (P-Thr). {ECO:0000269|PubMed:16990279}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00582|reaction.R00582]] `KEGG` `database` - via EC:3.1.3.3
- `catalyzes` --> [[reaction.R02853|reaction.R02853]] `KEGG` `database` - via EC:3.1.3.3
- `catalyzes` --> [[reaction.ecocyc.RXN0-5114|reaction.ecocyc.RXN0-5114]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4388|gene.b4388]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGB0`
- `KEGG:ecj:JW4351;eco:b4388;ecoc:C3026_23710;`
- `GeneID:93777457;948913;`
- `GO:GO:0000287; GO:0005737; GO:0006564; GO:0008652; GO:0016791; GO:0036424`
- `EC:3.1.3.3`

## Notes

Phosphoserine phosphatase (PSP) (PSPase) (EC 3.1.3.3) (O-phosphoserine phosphohydrolase)

---
entity_id: "protein.P0A799"
entity_type: "protein"
name: "pgk"
source_database: "UniProt"
source_id: "P0A799"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgk b2926 JW2893"
---

# pgk

`protein.P0A799`

## Static

- Type: `protein`
- Source: `UniProt:P0A799`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Phosphoglycerate kinase (EC 2.7.2.3) Phosphoglycerate kinase encoded by gene pgk catalyzes the reversible phosphorylation of 3-phospho-D-glycerate to 1,3-bisphospho-D-glycerate during glycolysis and gluconeogenesis in E. coli. In the glycolytic reaction direction the enzyme catalyzes the transfer of a phosphoryl group from 1,3-bisphospho-D-glycerate to ADP, forming ATP and 3-phospho-D-glycerate. Pgk cDNAs from a variety of organisms have been isolated. Their protein products are all monomers of similar size, with similar tertiary structures . The amino acid sequence of the E. coli enzyme is highly homologous to that of eukaryotes . Part of gene pgk showed similarity to an ORF found in the enterobacterial fish pathogen Edwardsiella ictaluri . The gene order around pgk in the Enterobacteriaceae differs from that in most other bacteria and transcriptional regulation of the E. coli epd-pgk-fbaA region has been studied . In earlier work, phosphoglycerate kinase was purified to near homogeneity from cell extracts of E. coli K-12. When assayed in the reverse direction its activity was dependent upon the presence of ATP and 3-phospho-D-glycerate . A pgk mutant cannot grow on sugars or gluconeogenic substrates . A mapping study using transductional crosses determined a gene order in the pgk region...

## Biological Role

Catalyzes PHOSGLYPHOS-RXN (reaction.ecocyc.PHOSGLYPHOS-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Phosphoglycerate kinase (EC 2.7.2.3)

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PHOSGLYPHOS-RXN|reaction.ecocyc.PHOSGLYPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2926|gene.b2926]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A799`
- `KEGG:ecj:JW2893;eco:b2926;ecoc:C3026_16030;`
- `GeneID:86861010;89517738;947414;`
- `GO:GO:0004618; GO:0005524; GO:0005829; GO:0006094; GO:0006096; GO:0043531; GO:0097216`
- `EC:2.7.2.3`

## Notes

Phosphoglycerate kinase (EC 2.7.2.3)

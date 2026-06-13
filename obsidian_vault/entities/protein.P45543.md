---
entity_id: "protein.P45543"
entity_type: "protein"
name: "frlD"
source_database: "UniProt"
source_id: "P45543"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frlD yhfQ b3374 JW3337"
---

# frlD

`protein.P45543`

## Static

- Type: `protein`
- Source: `UniProt:P45543`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent phosphorylation of fructoselysine to fructoselysine 6-phosphate (PubMed:12147680). Functions in a fructoselysine degradation pathway that allows E.coli to grow on fructoselysine or psicoselysine (PubMed:12147680, PubMed:14641112). To a much lesser extenst, is also able to phosphorylate psicoselysine (PubMed:14641112). {ECO:0000269|PubMed:12147680, ECO:0000269|PubMed:14641112}. FrlD is a monomeric fructoselysine 6-kinase . FrlD is a member of the PfkB family of kinases and has similarity to the glucosamine-6-phosphate synthase isomerase domain . A structure model of FrlD was used to identify potential residues involved in substrate recognition, and site-directed mutants were tested for enzymatic activity. Most of the mutants showed significantly decreased activity. A Met220Leu mutant has decreased activity with fructoselysine, but increased activity with fructosevaline as the substrate . Fructoselysine 6-kinase activity is undetectable when cells are grown on glucose; stationary phase extracts of cells grown on fructoselysine or psicoselysine have a kinase activity of 100 nmol/min per mg of protein . Experiments in were done with proteins from E. coli BL21(DE3). FrlD: "fructoselysine"

## Biological Role

Catalyzes RXN0-962 (reaction.ecocyc.RXN0-962).

## Annotation

FUNCTION: Catalyzes the ATP-dependent phosphorylation of fructoselysine to fructoselysine 6-phosphate (PubMed:12147680). Functions in a fructoselysine degradation pathway that allows E.coli to grow on fructoselysine or psicoselysine (PubMed:12147680, PubMed:14641112). To a much lesser extenst, is also able to phosphorylate psicoselysine (PubMed:14641112). {ECO:0000269|PubMed:12147680, ECO:0000269|PubMed:14641112}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-962|reaction.ecocyc.RXN0-962]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3374|gene.b3374]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45543`
- `KEGG:ecj:JW3337;eco:b3374;`
- `GeneID:947886;`
- `GO:GO:0005524; GO:0019200`
- `EC:2.7.1.218`

## Notes

Fructoselysine 6-kinase (EC 2.7.1.218)

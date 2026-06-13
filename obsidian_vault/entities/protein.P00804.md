---
entity_id: "protein.P00804"
entity_type: "protein"
name: "lspA"
source_database: "UniProt"
source_id: "P00804"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00161, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:1894646, ECO:0000269|PubMed:6368552}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00161, ECO:0000269|PubMed:1894646, ECO:0000269|PubMed:6368552}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lspA lsp b0027 JW0025"
---

# lspA

`protein.P00804`

## Static

- Type: `protein`
- Source: `UniProt:P00804`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00161, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:1894646, ECO:0000269|PubMed:6368552}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00161, ECO:0000269|PubMed:1894646, ECO:0000269|PubMed:6368552}.

## Enriched Summary

FUNCTION: This protein specifically catalyzes the removal of signal peptides from prolipoproteins. {ECO:0000255|HAMAP-Rule:MF_00161, ECO:0000269|PubMed:6368552, ECO:0000269|PubMed:6374664, ECO:0000269|PubMed:6378662}. lspA encodes prolipoprotein signal peptidase (signal peptidase II) - an inner membrane endopeptidase that cleaves the signal peptide from glyceride modified prolipoproteins including EG10544-MONOMER . Signal peptidase II requires a glyceride modified cysteine residue at the cleavage site . The peptidic antibiotic, globomycin specifically inhibits signal peptidase II activity resulting in the accumulation of glyceride modified prolipoprotein in the inner membrane and cell death . LspA has four predicted membrane-spanning hydrophobic segments . LspA does not have an apparent signal peptide . LspA contains four transmembrane domains and both termini are located in the cytoplasm . lspA is part of a five gene operon (ribF-ileS-lspA-fkpB-ispH) . Reviews:

## Biological Role

Catalyzes RXN-17362 (reaction.ecocyc.RXN-17362).

## Enriched Pathways

- `eco03060` Protein export (KEGG)

## Annotation

FUNCTION: This protein specifically catalyzes the removal of signal peptides from prolipoproteins. {ECO:0000255|HAMAP-Rule:MF_00161, ECO:0000269|PubMed:6368552, ECO:0000269|PubMed:6374664, ECO:0000269|PubMed:6378662}.

## Pathways

- `eco03060` Protein export (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-17362|reaction.ecocyc.RXN-17362]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0027|gene.b0027]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00804`
- `KEGG:ecj:JW0025;eco:b0027;ecoc:C3026_00130;`
- `GeneID:93777409;944800;`
- `GO:GO:0004175; GO:0004190; GO:0005886; GO:0006465`
- `EC:3.4.23.36`

## Notes

Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein signal peptidase) (Signal peptidase II) (SPase II)

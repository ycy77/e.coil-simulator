---
entity_id: "protein.P07464"
entity_type: "protein"
name: "lacA"
source_database: "UniProt"
source_id: "P07464"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:3922433}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lacA b0342 JW0333"
---

# lacA

`protein.P07464`

## Static

- Type: `protein`
- Source: `UniProt:P07464`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:3922433}.

## Enriched Summary

FUNCTION: Catalyzes the CoA-dependent transfer of an acetyl group to the 6-O-methyl position of a range of galactosides, glucosides, and lactosides (PubMed:14009486, PubMed:4630409, PubMed:7592843). May assist cellular detoxification by acetylating non-metabolizable pyranosides, thereby preventing their reentry into the cell (Probable). {ECO:0000269|PubMed:14009486, ECO:0000269|PubMed:4630409, ECO:0000269|PubMed:7592843, ECO:0000305|PubMed:11937062}.

## Biological Role

Catalyzes acyl-CoA:beta-D-galactoside 6-acetyltransferase (reaction.R02616). Component of galactoside O-acetyltransferase (complex.ecocyc.GALACTOACETYLTRAN-CPLX).

## Annotation

FUNCTION: Catalyzes the CoA-dependent transfer of an acetyl group to the 6-O-methyl position of a range of galactosides, glucosides, and lactosides (PubMed:14009486, PubMed:4630409, PubMed:7592843). May assist cellular detoxification by acetylating non-metabolizable pyranosides, thereby preventing their reentry into the cell (Probable). {ECO:0000269|PubMed:14009486, ECO:0000269|PubMed:4630409, ECO:0000269|PubMed:7592843, ECO:0000305|PubMed:11937062}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02616|reaction.R02616]] `KEGG` `database` - via EC:2.3.1.18
- `is_component_of` --> [[complex.ecocyc.GALACTOACETYLTRAN-CPLX|complex.ecocyc.GALACTOACETYLTRAN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0342|gene.b0342]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07464`
- `KEGG:ecj:JW0333;eco:b0342;`
- `GeneID:945674;`
- `GO:GO:0005737; GO:0005989; GO:0008870; GO:0042802`
- `EC:2.3.1.18`

## Notes

Galactoside O-acetyltransferase (GAT) (EC 2.3.1.18) (Acetyl-CoA:galactoside 6-O-acetyltransferase) (Thiogalactoside acetyltransferase) (Thiogalactoside transacetylase)

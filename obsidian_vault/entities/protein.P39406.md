---
entity_id: "protein.P39406"
entity_type: "protein"
name: "rsmC"
source_database: "UniProt"
source_id: "P39406"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmC yjjT b4371 JW4333"
---

# rsmC

`protein.P39406`

## Static

- Type: `protein`
- Source: `UniProt:P39406`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the guanine in position 1207 of 16S rRNA in the 30S particle. {ECO:0000269|PubMed:9873033}. RsmC is the methyltransferase responsible for methylation of 16S rRNA at the N2 position of the G1207 nucleotide. In vitro, the enzyme can methylate 16S rRNA within the 30S ribosomal subunit, but not free 16S rRNA . RsmC appears to contribute to the correct duplex formation of helix 34 in 16S rRNA . The C-terminal domain of RsmC is conserved across many known and predicted N-methyltransferases. The N-terminal domain also has some similarity with this conserved domain, but is missing all the residues predicted to be required for methyltransferase activity . A crystal structure of RsmC has been solved at 2.1 Å resolution, confirming structural similarity of the N- and C-terminal domains, and thus domain duplication. The C-terminal domain may require presence of the N-terminal domain for proper folding . Point mutants in various predicted active site residues show reduced activity . Review:

## Biological Role

Catalyzes RXN-11576 (reaction.ecocyc.RXN-11576). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Specifically methylates the guanine in position 1207 of 16S rRNA in the 30S particle. {ECO:0000269|PubMed:9873033}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11576|reaction.ecocyc.RXN-11576]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4371|gene.b4371]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39406`
- `KEGG:ecj:JW4333;eco:b4371;ecoc:C3026_23615;`
- `GeneID:948892;`
- `GO:GO:0003676; GO:0005737; GO:0005829; GO:0008990; GO:0031167; GO:0034337; GO:0052914; GO:0070475; GO:0140691`
- `EC:2.1.1.172`

## Notes

Ribosomal RNA small subunit methyltransferase C (EC 2.1.1.172) (16S rRNA m2G1207 methyltransferase) (rRNA (guanine-N(2)-)-methyltransferase RsmC)

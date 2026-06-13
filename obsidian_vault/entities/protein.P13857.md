---
entity_id: "protein.P13857"
entity_type: "protein"
name: "rimL"
source_database: "UniProt"
source_id: "P13857"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rimL b1427 JW1423"
---

# rimL

`protein.P13857`

## Static

- Type: `protein`
- Source: `UniProt:P13857`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: This enzyme acetylates the N-terminal serine of ribosomal protein bL12, converting it into the acetylated form of bL12 known as bL7. {ECO:0000269|PubMed:2671655}. RimL is the acetyl transferase that acetylates the Nα-terminal serine residue of ribosomal protein L12, converting it into its modified form, L7 . Acetylation of L12 does not appear to be essential for its function . RimL can also acetylate a mutant ribosomal protein L12 which contains alanine instead of serine at the N-terminal position (after cleavage of the leading methionine); substitution of the adjacent amino acid with aspartate leads to lower catalytic efficiency . RimL is similar to the MccE acetyltransferase that acetylates and thereby provides resistance to processed microcin C (McC). RimL, but not RimI or RimJ, contributes to E. coli's basal level of resistance to McC and some of its analogs . A rimL mutant lacks ribosomal protein L7, the acetylated form of ribosomal protein L12 . RimL shows similarity to RimJ .

## Biological Role

Catalyzes RXN0-5231 (reaction.ecocyc.RXN0-5231).

## Annotation

FUNCTION: This enzyme acetylates the N-terminal serine of ribosomal protein bL12, converting it into the acetylated form of bL12 known as bL7. {ECO:0000269|PubMed:2671655}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5231|reaction.ecocyc.RXN0-5231]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1427|gene.b1427]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13857`
- `KEGG:ecj:JW1423;eco:b1427;ecoc:C3026_08305;`
- `GeneID:945998;`
- `GO:GO:0004596; GO:0005737; GO:0008080; GO:0008999; GO:1990189`
- `EC:2.3.1.-`

## Notes

Ribosomal-protein-serine acetyltransferase (EC 2.3.1.-) (Acetylating enzyme for N-terminus of ribosomal protein L7/L12)

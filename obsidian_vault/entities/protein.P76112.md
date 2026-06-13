---
entity_id: "protein.P76112"
entity_type: "protein"
name: "mnaT"
source_database: "UniProt"
source_id: "P76112"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mnaT yncA b1448 JW5233"
---

# mnaT

`protein.P76112`

## Static

- Type: `protein`
- Source: `UniProt:P76112`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acyltransferase that appears to be required for E.coli optimal growth rate and yield via the formation of N-acetylated amino acids. Catalyzes the acylation of L-methionine using acetyl-CoA or propanoyl-CoA as acyl donors, and the acetylation of L-phenylglycine (PubMed:27941785). Is also able to N-acylate other free L-amino acids and their derivatives using a CoA thioester as cosubstrate. Using acetyl-CoA as an acyl donor, substrate specificity is methionine sulfone > methionine sulfoximine > methionine sulfoxide > methionine. Asparagine, lysine, glutamine, aspartate and glutamate are very poor substrates. Using methionine as a substrate, acyl donor preference is propanoyl-CoA > acetyl-CoA >> butyryl-CoA (Ref.4). Likely plays a role in the resistance against the toxic effects of L-methionine sulfoximine (MSX), via its ability to catalyze its acetylation; MSX is a rare amino acid which inhibits glutamine synthetase (GlnA) (By similarity). {ECO:0000250|UniProtKB:Q8ZPD3, ECO:0000269|PubMed:27941785, ECO:0000269|Ref.4}.

## Biological Role

Component of L-amino acid N-acyltransferase (complex.ecocyc.CPLX0-7962).

## Annotation

FUNCTION: Acyltransferase that appears to be required for E.coli optimal growth rate and yield via the formation of N-acetylated amino acids. Catalyzes the acylation of L-methionine using acetyl-CoA or propanoyl-CoA as acyl donors, and the acetylation of L-phenylglycine (PubMed:27941785). Is also able to N-acylate other free L-amino acids and their derivatives using a CoA thioester as cosubstrate. Using acetyl-CoA as an acyl donor, substrate specificity is methionine sulfone > methionine sulfoximine > methionine sulfoxide > methionine. Asparagine, lysine, glutamine, aspartate and glutamate are very poor substrates. Using methionine as a substrate, acyl donor preference is propanoyl-CoA > acetyl-CoA >> butyryl-CoA (Ref.4). Likely plays a role in the resistance against the toxic effects of L-methionine sulfoximine (MSX), via its ability to catalyze its acetylation; MSX is a rare amino acid which inhibits glutamine synthetase (GlnA) (By similarity). {ECO:0000250|UniProtKB:Q8ZPD3, ECO:0000269|PubMed:27941785, ECO:0000269|Ref.4}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7962|complex.ecocyc.CPLX0-7962]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1448|gene.b1448]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76112`
- `KEGG:ecj:JW5233;eco:b1448;ecoc:C3026_08425;`
- `GeneID:946010;`
- `GO:GO:0016747; GO:0103045`
- `EC:2.3.1.-`

## Notes

L-amino acid N-acyltransferase MnaT (EC 2.3.1.-) (L-methionine N-acyltransferase) (L-methionine sulfoximine/L-methionine sulfone N-acetyltransferase) (L-phenylglycine N-acetyltransferase)

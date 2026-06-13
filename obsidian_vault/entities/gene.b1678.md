---
entity_id: "gene.b1678"
entity_type: "gene"
name: "ldtE"
source_database: "NCBI RefSeq"
source_id: "gene-b1678"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1678"
  - "ldtE"
---

# ldtE

`gene.b1678`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1678`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldtE (gene.b1678) is a gene entity. It encodes ynhG (protein.P76193). Encoded protein function: FUNCTION: Responsible, at least in part, for generating a meso-diaminopimelyl-3-a meso-diaminopimelyl-3 cross-link. {ECO:0000269|PubMed:18456808}. EcoCyc product frame: G6904-MONOMER. EcoCyc synonyms: ynhG. Genomic coordinates: 1757721-1758725. EcoCyc protein note: LdtE (formerly YnhG) is a membrane anchored, periplasmic L,D-transpeptidase that catalyses the formation of meso-diaminopimelate→meso-diaminopimelate cross links (also called DAP3→DAP3 or 3-3 cross-links) in peptidoglycan; LdtE cleaves the m-DAP3→D-ala4 peptide bond of an acyl donor stem tetrapeptide and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of m-DAP3 of an acceptor stem peptide. Muropeptides obtained from the peptidoglycan of a BW25113Δ(G7073 "ldtA" G6422 "ldtB" G6571 "ldtC" ldtE) quadruple mutant (BW25113Δ4) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein ; muropeptides obtained from the peptidoglycan of a BW25113Δ(ldtA ldtB ldtC EG11253 "ldtD" ldtE) quintuple mutant (BW25113Δ5) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein, nor do they contain meso-DAP3-meso-DAP3 cross-links, free tripeptide stems or tetrapeptide stems with Gly as the fourth amino acid...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76193|protein.P76193]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005605,ECOCYC:G6904,GeneID:946174`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1757721-1758725:-; feature_type=gene

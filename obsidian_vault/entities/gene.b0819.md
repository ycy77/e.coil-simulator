---
entity_id: "gene.b0819"
entity_type: "gene"
name: "ldtB"
source_database: "NCBI RefSeq"
source_id: "gene-b0819"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0819"
  - "ldtB"
---

# ldtB

`gene.b0819`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0819`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldtB (gene.b0819) is a gene entity. It encodes ybiS (protein.P0AAX8). Encoded protein function: FUNCTION: Responsible, at least in part, for anchoring of the major outer membrane lipoprotein (Lpp, also known as the Braun lipoprotein) to the peptidoglycan via a meso-diaminopimelyl-L-Lys- bond on the terminal residue of Lpp. Can be oxidized in vivo, its reduction depends preferentially on DsbG, although DsbC is able to partially replace DsbG. {ECO:0000269|PubMed:18456808}. EcoCyc product frame: G6422-MONOMER. EcoCyc synonyms: ybiS. Genomic coordinates: 854824-855744. EcoCyc protein note: LdtB is a periplasmic L,D-transpeptidase which cleaves the meso-diaminopimeloyl3→ D-alanine4 peptide bond in a peptidoglycan tetrapeptide stem and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of the lysine residue located at the C terminus of CPLX0-8279 "Braun lipoprotein" . This activity anchors Braun lipoprotein to the peptidoglycan and contributes to the stability of the cell envelope. Muropeptides obtained from the peptidoglycan of an E. coli BW25113 Δ(G7073 "ldtA" ldtB G6571 "ldtC" G6904 "ldtE") quadruple mutant (BW25113Δ4) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein (see also )...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAX8|protein.P0AAX8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002797,ECOCYC:G6422,GeneID:945441`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:854824-855744:-; feature_type=gene

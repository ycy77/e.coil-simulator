---
entity_id: "gene.b1990"
entity_type: "gene"
name: "ldtA"
source_database: "NCBI RefSeq"
source_id: "gene-b1990"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1990"
  - "ldtA"
---

# ldtA

`gene.b1990`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1990`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldtA (gene.b1990) is a gene entity. It encodes erfK (protein.P39176). Encoded protein function: FUNCTION: Responsible, at least in part, for anchoring of the major outer membrane lipoprotein (Lpp, also known as the Braun lipoprotein) to the peptidoglycan via a meso-diaminopimelyl-L-Lys- bond on the terminal residue of Lpp. {ECO:0000269|PubMed:18456808}. EcoCyc product frame: G7073-MONOMER. EcoCyc synonyms: yzzT, yeeG, erfK. Genomic coordinates: 2062391-2063323. EcoCyc protein note: LdtA is an L,D-transpeptidase which cleaves the meso-diaminopimeloyl3→ D-alanine4 peptide bond in a peptidoglycan tetrapeptide stem and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of the lysine residue located at the C terminus of CPLX0-8279 "Braun lipoprotein" . This activity anchors Braun lipoprotein to the peptidoglycan and contributes to the stability of the cell envelope. Muropeptides obtained from the peptidoglycan of an E. coli BW25113 Δ(ldtA G6422 "ldtB" G6571 "ldtC" G6904 "ldtE") quadruple mutant (BW25113Δ4) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein (see also ). Expression of ldtA in BW25113Δ4 restores the appearance of this muropeptide suggesting that LdtA catalyzes the covalent anchoring of Braun lipoprotein to the peptidoglycan . Complementation analysis suggests that E...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39176|protein.P39176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006607,ECOCYC:G7073,GeneID:945273`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2062391-2063323:-; feature_type=gene

---
entity_id: "gene.b1113"
entity_type: "gene"
name: "ldtC"
source_database: "NCBI RefSeq"
source_id: "gene-b1113"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1113"
  - "ldtC"
---

# ldtC

`gene.b1113`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1113`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldtC (gene.b1113) is a gene entity. It encodes ycfS (protein.P75954). Encoded protein function: FUNCTION: Responsible, at least in part, for anchoring of the major outer membrane lipoprotein (Lpp, also known as the Braun lipoprotein) to the peptidoglycan via a meso-diaminopimelyl-L-Lys- bond on the terminal residue of Lpp. {ECO:0000269|PubMed:18456808}. EcoCyc product frame: G6571-MONOMER. EcoCyc synonyms: ycfS. Genomic coordinates: 1169412-1170374. EcoCyc protein note: LdtC is an L,D-transpeptidase which cleaves the meso-diaminopimeloyl3→ D-alanine4 peptide bond in a peptidoglycan tetrapeptide stem and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of the lysine residue located at the C terminus of CPLX0-8279 "Braun lipoprotein" . This activity anchors Braun lipoprotein to the peptidoglycan and contributes to the stability of the cell envelope. Muropeptides obtained from the peptidoglycan of an E. coli BW25113 Δ(G7073 "ldtA" G6422 "ldtB" ldtC G6904 "ldtE") quadruple mutant (BW25113Δ4) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein (see also ). Expression of ldtC in BW25113Δ4 restores the appearance of this muropeptide suggesting that LdtC catalyzes the covalent anchoring of Braun lipoprotein to the peptidoglycan . Complementation analysis suggests that E...

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75954|protein.P75954]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ldtC; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=ldtC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003760,ECOCYC:G6571,GeneID:945666`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1169412-1170374:-; feature_type=gene

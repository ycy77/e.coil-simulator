---
entity_id: "gene.b3809"
entity_type: "gene"
name: "dapF"
source_database: "NCBI RefSeq"
source_id: "gene-b3809"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3809"
  - "dapF"
---

# dapF

`gene.b3809`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3809`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dapF (gene.b3809) is a gene entity. It encodes dapF (protein.P0A6K1). Encoded protein function: FUNCTION: Involved in the succinylase branch of the L-lysine biosynthesis and in the biosynthesis of the pentapeptide incorporated in the peptidoglycan moiety (PubMed:3283102). Catalyzes the stereoinversion of LL-2,6-diaminopimelate (L,L-DAP) to meso-diaminopimelate (meso-DAP) (PubMed:3031013, PubMed:3042781, PubMed:6378903). {ECO:0000269|PubMed:3031013, ECO:0000269|PubMed:3042781, ECO:0000269|PubMed:3283102, ECO:0000269|PubMed:6378903}. EcoCyc product frame: DIAMINOPIMEPIM-MONOMER. Genomic coordinates: 3994762-3995586.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6K1|protein.P0A6K1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dapF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012442,ECOCYC:EG10209,GeneID:948364`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3994762-3995586:+; feature_type=gene

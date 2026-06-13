---
entity_id: "gene.b3150"
entity_type: "gene"
name: "dolP"
source_database: "NCBI RefSeq"
source_id: "gene-b3150"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3150"
  - "dolP"
---

# dolP

`gene.b3150`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3150`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dolP (gene.b3150) is a gene entity. It encodes dolP (protein.P64596). Encoded protein function: FUNCTION: Plays an important role in maintaining outer membrane integrity (PubMed:33315009, PubMed:33847565). Supports proper folding and function of BamA under envelope stress conditions (PubMed:33847565). Binds specifically to anionic phospholipids via the BON 2 domain (PubMed:33315009). This interaction is essential for function and guides the protein to the cell division site (PubMed:33315009). It was reported that DolP is a potential upstream regulator of the amidase activator NlpD (PubMed:28708841). However, later studies suggest that DolP affects cell division and may impact daughter cell separation, but likely not as a regulator of NlpD (PubMed:35604759). {ECO:0000269|PubMed:28708841, ECO:0000269|PubMed:33315009, ECO:0000269|PubMed:33847565, ECO:0000269|PubMed:35604759}. EcoCyc product frame: G7644-MONOMER. EcoCyc synonyms: ecfH, yraP. Genomic coordinates: 3296409-3296984. EcoCyc protein note: DolP (formerly YraP) is an outer membrane lipoprotein; a DolP-mCherry fusion protein localizes to the septal ring division site...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64596|protein.P64596]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=dolP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010350,ECOCYC:G7644,GeneID:947659`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3296409-3296984:+; feature_type=gene

---
entity_id: "gene.b0378"
entity_type: "gene"
name: "yaiW"
source_database: "NCBI RefSeq"
source_id: "gene-b0378"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0378"
  - "yaiW"
---

# yaiW

`gene.b0378`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0378`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaiW (gene.b0378) is a gene entity. It encodes yaiW (protein.P77562). Encoded protein function: Uncharacterized protein YaiW EcoCyc product frame: G6227-MONOMER. Genomic coordinates: 397872-398966. EcoCyc protein note: YaiW possesses an N-terminal lipobox sequence which lacks the inner membrane retention signal; YaiW is surface exposed; the highly similar YaiW protein from Salmonella typhimurium is a surface exposed outer membrane lipoprotein . An E. coli ΔyaiW strain has moderately stronger growth in the presence of sublethal concentrations of two truncated species of the antimicrobial peptide Bac7 and a decreased internalisation of the peptide species. Deletion of yaiW does not affect sensitivity to other antimicrobial peptides species such as bleomycin sulfate and microcin B17 . A ΔyaiW strain shows enhanced secretion of the extracellular protein EG11807-MONOMER "YebF" and of YebF fusion proteins possibly due to defects in the outer membrane; a ΔyaiF strain shows signs of envelope instability . The yaiW gene is a member of the σE regulon . yaiW is cotranscribed with sbmA .

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77562|protein.P77562]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yaiW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001299,ECOCYC:G6227,GeneID:945038`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:397872-398966:+; feature_type=gene

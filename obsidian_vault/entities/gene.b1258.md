---
entity_id: "gene.b1258"
entity_type: "gene"
name: "yciF"
source_database: "NCBI RefSeq"
source_id: "gene-b1258"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1258"
  - "yciF"
---

# yciF

`gene.b1258`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1258`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciF (gene.b1258) is a gene entity. It encodes yciF (protein.P21362). Encoded protein function: Protein YciF EcoCyc product frame: EG11126-MONOMER. Genomic coordinates: 1315270-1315770. EcoCyc protein note: YciF is highly conserved across Enterobacteriaceae. Its expression is induced under osmotic stress imposed by NaCl in both aerobic and anaerobic conditions and repressed by H-NS . YciF is part of the σS regulon . The yciGFE locus is expressed poorly . The yciF gene of Salmonella enterica serovar Typhimurium is regulated by RpoS (σS) and by bile independent of RpoS . A crystal structure of YciF has been solved at 2 Å resolution; it was found to be a structural homolog of rubrerythrin, a protein with a diiron center. YciF forms a dimer both in the crystal structure and in solution .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by mcbR (protein.P76114).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21362|protein.P21362]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76114|protein.P76114]] `RegulonDB` `S` - regulator=McbR; target=yciF; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=yciF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004222,ECOCYC:EG11126,GeneID:947133`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1315270-1315770:-; feature_type=gene

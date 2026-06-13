---
entity_id: "gene.b0679"
entity_type: "gene"
name: "nagE"
source_database: "NCBI RefSeq"
source_id: "gene-b0679"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0679"
  - "nagE"
---

# nagE

`gene.b0679`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0679`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nagE (gene.b0679) is a gene entity. It encodes nagE (protein.P09323). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:4919472). This system is involved in N-acetylglucosamine transport (PubMed:4919472). It can also transport and phosphorylate the antibiotic streptozotocin (PubMed:161156). Could play a significant role in the recycling of peptidoglycan (PubMed:19617367). {ECO:0000269|PubMed:161156, ECO:0000269|PubMed:19617367, ECO:0000269|PubMed:4919472, ECO:0000305|PubMed:3056518}. EcoCyc product frame: NAGE-MONOMER. EcoCyc synonyms: pstN, ptsN. Genomic coordinates: 703944-705890.

## Biological Role

Repressed by crp (protein.P0ACJ8), nagC (protein.P0AF20). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09323|protein.P09323]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nagE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=nagE; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=nagE; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=nagE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002312,ECOCYC:EG10635,GeneID:945292`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:703944-705890:+; feature_type=gene

---
entity_id: "gene.b2114"
entity_type: "gene"
name: "metG"
source_database: "NCBI RefSeq"
source_id: "gene-b2114"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2114"
  - "metG"
---

# metG

`gene.b2114`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2114`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metG (gene.b2114) is a gene entity. It encodes metG (protein.P00959). Encoded protein function: FUNCTION: Catalyzes the attachment of L-methionine to tRNA(Met) (PubMed:216545, PubMed:367445, PubMed:4297674, PubMed:4581817, PubMed:7932711). Is required not only for elongation of protein synthesis but also for the initiation of all mRNA translation through initiator tRNA(fMet) aminoacylation (PubMed:216545, PubMed:4581817). MetRS can indeed attach methionine to tRNA(mMet), which supplies methionine for elongation of nascent peptides, and to tRNA(fMet), which supplies formylmethionine for initiation of peptide synthesis (PubMed:216545, PubMed:4581817). However, MetRS charges tRNA(fMet) with a greater efficiency than tRNA(mMet) in several strains of E.coli, suggesting a preference for initiation of new peptides (PubMed:216545). Cannot use D-methionine (PubMed:4297674). {ECO:0000269|PubMed:216545, ECO:0000269|PubMed:367445, ECO:0000269|PubMed:4297674, ECO:0000269|PubMed:4581817, ECO:0000269|PubMed:7932711}.; FUNCTION: In addition, MetRS can reject misactivated homocysteine by a tRNA-independent hydrolysis of the homocysteinyl-AMP intermediate, preventing incorporation of homocysteine into tRNA and proteins (PubMed:2191291, PubMed:7024910)...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00959|protein.P00959]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=metG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006991,ECOCYC:EG10586,GeneID:946643`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2194300-2196333:+; feature_type=gene

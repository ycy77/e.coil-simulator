---
entity_id: "gene.b3357"
entity_type: "gene"
name: "crp"
source_database: "NCBI RefSeq"
source_id: "gene-b3357"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3357"
  - "crp"
---

# crp

`gene.b3357`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3357`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

crp (gene.b3357) is a gene entity. It encodes crp (protein.P0ACJ8). Encoded protein function: FUNCTION: A global transcription regulator, which plays a major role in carbon catabolite repression (CCR) as well as other processes. Binds cyclic AMP (cAMP) which allosterically activates DNA binding (to consensus sequence 5'-AAATGTGATCTAGATCACATTT-3') to directly regulate the transcription of about 300 genes in about 200 operons and indirectly regulate the expression of about half the genome. There are 3 classes of CRP promoters; class I promoters have a single CRP-binding site upstream of the RNA polymerase (RNAP)-binding site, whereas in class II promoters the single CRP- and RNAP-binding site overlap, CRP making multiple contacts with RNAP. Class III promoters require multiple activator molecules, including at least one CRP dimer. CRP can act as an activator, repressor, coactivator or corepressor. Induces a severe bend in DNA (about 87 degrees), bringing upstream promoter elements into contact with RNAP. Acts as a negative regulator of its own synthesis as well as for adenylate cyclase (cyaA), which generates cAMP. High levels of active CRP are detrimental to growth (PubMed:16260780). In CCR it prevents expression of genes involved in catabolism of nonpreferred carbon sources when glucose is present...

## Biological Role

Repressed by fis (protein.P0A6R3), crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), cra (protein.P0ACP1).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACJ8|protein.P0ACJ8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=crp; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=crp; function=-+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=crp; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=crp; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=crp; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0010970,ECOCYC:EG10164,GeneID:947867`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3486120-3486752:+; feature_type=gene

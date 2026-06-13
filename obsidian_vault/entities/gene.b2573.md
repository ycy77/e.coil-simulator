---
entity_id: "gene.b2573"
entity_type: "gene"
name: "rpoE"
source_database: "NCBI RefSeq"
source_id: "gene-b2573"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2573"
  - "rpoE"
---

# rpoE

`gene.b2573`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2573`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoE (gene.b2573) is a gene entity. It encodes rpoE (protein.P0AGB6). Encoded protein function: FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase (RNAP) to specific initiation sites and are then released (PubMed:2691330, PubMed:7889935, PubMed:9159522, PubMed:9159523). Extracytoplasmic function (ECF) sigma-E controls the envelope stress response, responding to periplasmic protein stress, increased levels of periplasmic lipopolysaccharide (LPS) as well as heat shock (PubMed:7889935) and oxidative stress; it controls protein processing in the extracytoplasmic compartment. The 90 member regulon consists of the genes necessary for the synthesis and maintenance of both proteins and LPS of the outer membrane (PubMed:11274153, PubMed:16336047, PubMed:7889934). Indirectly activates transcription of csrB and csrC, 2 sRNAs that antagonize translational regulator CsrA, linking envelope stress, the stringent response and the catabolite repression systems (PubMed:28924029). {ECO:0000269|PubMed:11274153, ECO:0000269|PubMed:16336047, ECO:0000269|PubMed:2691330, ECO:0000269|PubMed:28924029, ECO:0000269|PubMed:7889934, ECO:0000269|PubMed:7889935, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}. EcoCyc product frame: RPOE-MONOMER. EcoCyc synonyms: sigE. Genomic coordinates: 2709437-2710012...

## Biological Role

Repressed by csrA (protein.P69913). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), glnG (protein.P0AFB8), glrR (protein.P0AFU4), rpoE (protein.P0AGB6), rcsB (protein.P0DMC7), rpoS (protein.P13445), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGB6|protein.P0AGB6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpoE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rpoE; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rpoE; function=+
- `activates` <-- [[protein.P0AFU4|protein.P0AFU4]] `RegulonDB` `S` - regulator=GlrR; target=rpoE; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rpoE; function=+
- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `C` - regulator=RcsB; target=rpoE; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rpoE; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=rpoE; function=+
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB|EcoCyc` `C` - regulator=CsrA; target=rpoE; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0008467,ECOCYC:EG11897,GeneID:947050`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2709437-2710012:-; feature_type=gene

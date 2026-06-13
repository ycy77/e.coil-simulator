---
entity_id: "gene.b0339"
entity_type: "gene"
name: "cynT"
source_database: "NCBI RefSeq"
source_id: "gene-b0339"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0339"
  - "cynT"
---

# cynT

`gene.b0339`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0339`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cynT (gene.b0339) is a gene entity. It encodes cynT (protein.P0ABE9). Encoded protein function: FUNCTION: Reversible hydration of carbon dioxide. Carbon dioxide formed in the bicarbonate-dependent decomposition of cyanate by cyanase (CynS) diffuses out of the cell faster than it would be hydrated to bicarbonate, so the apparent function of this enzyme is to catalyze the hydration of carbon dioxide and thus prevent depletion of cellular bicarbonate. {ECO:0000269|PubMed:1740425}. EcoCyc product frame: CARBODEHYDRAT-MONOMER. Genomic coordinates: 358799-359458. EcoCyc protein note: E. coli encodes two carbonic anhydrases, CynT (carbonic anhydrase 1) and Can (CPLX0-7521). The enzymes belong to Clade A and Clade B of the β class of carbonic anhydrases, respectively . cynT is encoded in an operon with EG10175, the gene encoding CYANLY-CPLX, and its expression is inducible by cyanate . The biological role of the CynT carbonic anhydrase is to prevent the depletion of endogenous bicarbonate due to rapid loss of CO2, the product of the cyanase-catalyzed reaction, by diffusion out of the cell . The enzyme behaves as an oligomer of two or four subunits, depending on the presence of bicarbonate . Inhibition of CynT activity by CPD0-1626 has been investigated...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), cynR (protein.P27111).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABE9|protein.P0ABE9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cynT; function=+
- `activates` <-- [[protein.P27111|protein.P27111]] `RegulonDB` `S` - regulator=CynR; target=cynT; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cynT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001171,ECOCYC:EG10176,GeneID:946548`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:358799-359458:+; feature_type=gene

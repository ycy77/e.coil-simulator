---
entity_id: "gene.b0039"
entity_type: "gene"
name: "caiA"
source_database: "NCBI RefSeq"
source_id: "gene-b0039"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0039"
  - "caiA"
---

# caiA

`gene.b0039`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0039`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

caiA (gene.b0039) is a gene entity. It encodes caiA (protein.P60584). Encoded protein function: FUNCTION: Catalyzes the reduction of crotonobetainyl-CoA to gamma-butyrobetainyl-CoA (PubMed:10209289, PubMed:10978161, PubMed:8060125). The electron donor could be the FixA/FixB complex (PubMed:12081978). {ECO:0000269|PubMed:10978161, ECO:0000269|PubMed:12081978, ECO:0000305|PubMed:10209289, ECO:0000305|PubMed:8060125}. EcoCyc product frame: CROBETREDUCT-MONOMER. EcoCyc synonyms: yaaO. Genomic coordinates: 39244-40386. EcoCyc protein note: Although E. coli K-12 does contain the cai genes, it can not utilize carnitine as a carbon or nitrogen source. However, under anaerobic conditions, carnitine can be metabolized to γ-butyrobetaine. The CaiA enzyme has been purified from the O44 K74 strain . In that strain, CaiA appears to be a homotetramer and forms a complex with CaiB, γ-butyrobetaine-CoA:carnitine CoA transferase . Expression of the cai operon is induced by carnitine and crotonobetaine under anaerobic conditions . demonstrated production of γ-butyrobetaine in an engineered L-carnitine-overproducing mutant of K-12 BW25113 and abolition of γ-butyrobetaine formation upon caiA deletion.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), caiF (protein.P0AE58).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60584|protein.P60584]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=caiA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=caiA; function=+
- `activates` <-- [[protein.P0AE58|protein.P0AE58]] `RegulonDB` `S` - regulator=CaiF; target=caiA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000139,ECOCYC:EG11560,GeneID:949064`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:39244-40386:-; feature_type=gene

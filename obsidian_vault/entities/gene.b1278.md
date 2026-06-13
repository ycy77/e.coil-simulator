---
entity_id: "gene.b1278"
entity_type: "gene"
name: "pgpB"
source_database: "NCBI RefSeq"
source_id: "gene-b1278"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1278"
  - "pgpB"
---

# pgpB

`gene.b1278`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1278`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgpB (gene.b1278) is a gene entity. It encodes pgpB (protein.P0A924). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of diacylglycerol diphosphate (DGPP) to phosphatidate (PA) and the subsequent dephosphorylation of PA to diacylglycerol (DAG). Also has undecaprenyl pyrophosphate phosphatase activity, required for the biosynthesis of the lipid carrier undecaprenyl phosphate. Can also use lysophosphatidic acid (LPA) and phosphatidylglycerophosphate as substrates. The pattern of activities varies according to subcellular location, PGP phosphatase activity is higher in the cytoplasmic membrane, whereas PA and LPA phosphatase activities are higher in the outer membrane. Activity is independent of a divalent cation ion and insensitive to inhibition by N-ethylmaleimide. {ECO:0000269|PubMed:15778224, ECO:0000269|PubMed:18411271, ECO:0000269|PubMed:21148555, ECO:0000269|PubMed:8940025}. EcoCyc product frame: PGPPHOSPHAB-MONOMER. Genomic coordinates: 1339330-1340094. EcoCyc protein note: E. coli contains three phosphatidylglycerophosphatases - EG10704 "PgpA", PgpB and EG11371 "PgpC" - which catalyse the dephosphorylation of phosphatidylglycerol phosphate (PGP) to phosphatidylglycerol (PG), an essential phospholipid of the inner and outer membrane in E. coli...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A924|protein.P0A924]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pgpB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004294,ECOCYC:EG10705,GeneID:945863`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1339330-1340094:+; feature_type=gene

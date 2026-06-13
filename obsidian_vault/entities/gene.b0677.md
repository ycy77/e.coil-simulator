---
entity_id: "gene.b0677"
entity_type: "gene"
name: "nagA"
source_database: "NCBI RefSeq"
source_id: "gene-b0677"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0677"
  - "nagA"
---

# nagA

`gene.b0677`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0677`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nagA (gene.b0677) is a gene entity. It encodes nagA (protein.P0AF18). Encoded protein function: FUNCTION: Involved in the first step in the biosynthesis of amino-sugar-nucleotides. Catalyzes the hydrolysis of the N-acetyl group of N-acetylglucosamine-6-phosphate (GlcNAc-6-P) to yield glucosamine 6-phosphate and acetate. In vitro, can also hydrolyze substrate analogs such as N-thioacetyl-D-glucosamine-6-phosphate, N-trifluoroacetyl-D-glucosamine-6-phosphate, N-acetyl-D-glucosamine-6-sulfate, N-acetyl-D-galactosamine-6-phosphate, and N-formyl-D-glucosamine-6-phosphate. {ECO:0000269|PubMed:16630633, ECO:0000269|PubMed:17567047, ECO:0000269|PubMed:17567048, ECO:0000269|PubMed:2190615, ECO:0000269|PubMed:4861885, ECO:0000269|PubMed:9143339}. EcoCyc product frame: NAG6PDEACET-MONOMER. Genomic coordinates: 701603-702751. EcoCyc protein note: N-acetylglucosamine-6-phosphate deacetylase catalyzes the first cytoplasmic reaction in the metabolism of N-acetyl-D-glucosamine. N-acetylglucosamine can serve as the sole source of carbon for E. coli and is transported into the cell via phosphotransferase transport systems. It thus reaches the cytoplasm in the phosphorylated form, N-acetylglucosamine-6-phosphate...

## Biological Role

Repressed by crp (protein.P0ACJ8), nagC (protein.P0AF20). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), phoP (protein.P23836).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF18|protein.P0AF18]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nagA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nagA; function=-+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=nagA; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nagA; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=nagA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002301,ECOCYC:EG10632,GeneID:945289`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:701603-702751:-; feature_type=gene

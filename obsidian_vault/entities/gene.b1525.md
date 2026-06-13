---
entity_id: "gene.b1525"
entity_type: "gene"
name: "sad"
source_database: "NCBI RefSeq"
source_id: "gene-b1525"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1525"
  - "sad"
---

# sad

`gene.b1525`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1525`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sad (gene.b1525) is a gene entity. It encodes sad (protein.P76149). Encoded protein function: FUNCTION: Catalyzes the NAD(+)-dependent oxidation of succinate semialdehyde to succinate. It acts preferentially with NAD as cosubstrate but can also use NADP. Prevents the toxic accumulation of succinate semialdehyde (SSA) and plays an important role when arginine and putrescine are used as the sole nitrogen or carbon sources. {ECO:0000269|PubMed:17873044, ECO:0000269|PubMed:20639325, ECO:0000269|PubMed:7009588, ECO:0000269|PubMed:7011797}. EcoCyc product frame: G6811-MONOMER. EcoCyc synonyms: yneI. Genomic coordinates: 1613315-1614703. EcoCyc protein note: E. coli K-12 encodes two succinate semialdehyde dehydrogenases, Sad and CPLX0-7688 "GabD", which differ in their ability to utilize NAD+ and NADP+. Sad is the smaller enzyme and preferentially utilizes NAD+ ; the gene encoding it was long unknown. Sad also functions as a glutarate semialdehyde dehydrogenase during degradation of L-lysine . YneI was found to be identical to the orphan enzymatic activity of NAD+-dependent succinate semialdehyde dehydrogenase (Sad). Its activity was first predicted using phylogenetic profiles and later confirmed biochemically . Sad has an important role during growth on arginine and is likely required for growth on putrescine as the sole source of nitrogen...

## Biological Role

Activated by lrp (protein.P0ACJ0), yneJ (protein.P77309).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76149|protein.P76149]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P77309|protein.P77309]] `RegulonDB` `S` - regulator=PtrR; target=sad; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005092,ECOCYC:G6811,GeneID:947440`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1613315-1614703:-; feature_type=gene

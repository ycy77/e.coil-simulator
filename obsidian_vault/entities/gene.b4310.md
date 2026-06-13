---
entity_id: "gene.b4310"
entity_type: "gene"
name: "nanM"
source_database: "NCBI RefSeq"
source_id: "gene-b4310"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4310"
  - "nanM"
---

# nanM

`gene.b4310`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4310`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanM (gene.b4310) is a gene entity. It encodes nanM (protein.P39371). Encoded protein function: FUNCTION: Converts alpha-N-acetylneuranimic acid (Neu5Ac) to the beta-anomer, accelerating the equilibrium between the alpha- and beta-anomers. Probably facilitates sialidase-negative bacteria to compete successfully for limited amounts of extracellular Neu5Ac, which is likely taken up in the beta-anomer. In addition, the rapid removal of sialic acid from solution might be advantageous to the bacterium to damp down host responses (PubMed:18063573). Forms linear aceneuramate during interconversion of Neu5Ac anomers (PubMed:33895133). {ECO:0000269|PubMed:18063573, ECO:0000269|PubMed:33895133}. EcoCyc product frame: G7920-MONOMER. EcoCyc synonyms: yjhT. Genomic coordinates: 4537659-4538765. EcoCyc protein note: The periplasmic N-acetylneuraminate mutarotase supports the efficient use of α-N-acetylneuraminate (α-NeuNAc) as the sole source of carbon. Sialoglycoconjugates present in vertebrates are linked exclusively by α-linkages; once released by sialidases, spontaneous mutarotation converts the α anomer to β-NeuNAc, which constitutes more than 90% of NeuNAc at equilibrium. However, the spontaneous rate of mutarotation is relatively slow. Thus, loss of N-acetylneuraminate mutarotase confers a small growth delay to cells grown on α-NeuNAc...

## Biological Role

Repressed by nanR (protein.P0A8W0), nagC (protein.P0AF20). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39371|protein.P39371]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nanM; function=+
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanM; function=-
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=nanM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014132,ECOCYC:G7920,GeneID:949106`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4537659-4538765:-; feature_type=gene

---
entity_id: "gene.b3115"
entity_type: "gene"
name: "tdcD"
source_database: "NCBI RefSeq"
source_id: "gene-b3115"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3115"
  - "tdcD"
---

# tdcD

`gene.b3115`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3115`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdcD (gene.b3115) is a gene entity. It encodes tdcD (protein.P11868). Encoded protein function: FUNCTION: Catalyzes the conversion of propionyl phosphate and ADP to propionate and ATP. It can also use acetyl phosphate as phosphate group acceptor. {ECO:0000255|HAMAP-Rule:MF_01881, ECO:0000269|PubMed:9484901}. EcoCyc product frame: PROPKIN-MONOMER. EcoCyc synonyms: yhaA. Genomic coordinates: 3262452-3263660. EcoCyc protein note: The tdcD gene encodes a protein with propionate and acetate kinase activity. Propionate kinase functions in the anaerobic degradation of threonine . Evidence suggests that TdcD also catalyzes the reverse reaction converting propionyl-phosphate and ADP to propionate and ATP, which is the last step in pathway PWY-5437. E. coli double null mutants deficient in TdcD and AckA activity, or Pta and AckA activity were unable to metabolize threonine to propionate. This suggested the occurrence of both this reaction and the preceding reaction that converts propanoyl-CoA and phosphate to propionyl-phosphate and coenzyme A in this pathway . Based on sequence similarity, TdcD was predicted to be an acetate kinase . Overexpression of tdcD partially rescues the anaerobic growth defect of an ackA mutant. A tdcD deletion mutant has no obvious phenotype . E. coli TdcD shows 42% identity and 62% overall similarity with TdcD from Salmonella enterica subsp...

## Biological Role

Activated by crp (protein.P0ACJ8), tdcA (protein.P0ACQ7), tdcR (protein.P11866).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11868|protein.P11868]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tdcD; function=+
- `activates` <-- [[protein.P0ACQ7|protein.P0ACQ7]] `RegulonDB` `S` - regulator=TdcA; target=tdcD; function=+
- `activates` <-- [[protein.P11866|protein.P11866]] `RegulonDB` `S` - regulator=TdcR; target=tdcD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010245,ECOCYC:EG11172,GeneID:947635`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3262452-3263660:-; feature_type=gene

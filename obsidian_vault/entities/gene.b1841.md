---
entity_id: "gene.b1841"
entity_type: "gene"
name: "yobA"
source_database: "NCBI RefSeq"
source_id: "gene-b1841"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1841"
  - "yobA"
---

# yobA

`gene.b1841`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1841`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yobA (gene.b1841) is a gene entity. It encodes yobA (protein.P0AA57). Encoded protein function: FUNCTION: Component of the AZY copper uptake system (PubMed:40108346). YobA positively regulates activity of the copper importer YebZ (PubMed:40108346). It binds a single Cu(2+) ion with high affinity, but cannot bind Cu(+) (PubMed:34822841). The AZY proteins link copper import to multiple antibiotic resistance (PubMed:40108346). They are necessary for the copper-dependent activation of the mar operon, thus leading to multidrug antibiotic resistance via the mar pathway (PubMed:40108346). The AZY proteins may also be involved in copper delivery to membrane proteins, but they are not involved in copper tolerance or antioxidant defense (PubMed:34822841). YobA is required for the activity of the copper-related NADH dehydrogenase II (NDH-2) (PubMed:34822841). {ECO:0000269|PubMed:34822841, ECO:0000269|PubMed:40108346}. EcoCyc product frame: G7014-MONOMER. Genomic coordinates: 1924595-1924969. EcoCyc protein note: YobA is a member of the CopC family of periplasmic copper-binding proteins; purified YobA binds a single Cu2+ ion with high affinity...

## Biological Role

Repressed by nac (protein.Q47005). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA57|protein.P0AA57]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yobA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yobA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0006123,ECOCYC:G7014,GeneID:948315`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1924595-1924969:-; feature_type=gene
